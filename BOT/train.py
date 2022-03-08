import numpy as np
import random
import json
#import classla

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

from nltk_utils import bagOfWords_BG, tokenize, stem

from bot_utils import StripOfChar, classla

from model import NeuralNet


# OPEN .JSON INTENTS FILE
with open('intentsBG.json', 'r', encoding="utf8") as f:
    intents = json.load(f)

print(intents)

# ESTABLISH PIPELINE AND RESOURCES LOCATION FOR APPROPRIATE LANGUAGE
pipeline = classla.Pipeline(dir="~/classla_resources", lang="bg", use_gpu=False)


# ESTABLISH GENERAL-PURPOSE LISTS
all_words = []
tags = []
xy = []

####################################################
# LOOP THROUGH ALL INTENTS FROM .JSON FILE
####################################################
for intent in intents['intents']:
    tag = intent['tag']
    # add to tag list
    tags.append(tag)
    for pattern in intent['patterns']:
        # tokenize each word in the sentence
        print(f"PATTERN {pattern}")
        patt = pipeline(pattern)
        lemmatizedWord = [f'{word.lemma}' for sent in patt.sentences for word in sent.words]
        print(f"TOKENIZED: {lemmatizedWord}")
        # add to our words list
        all_words.extend(lemmatizedWord)
        # add to xy pair
        xy.append((StripOfChar(lemmatizedWord), tag))

# REMOVE PUNCT FROM WORDS LIST
ignoreWords = ['?', '.', '!', '(', ')', '{', '}']
allWords = [w for w in all_words if w not in ignoreWords]


# STRIP OF UNNECESSARY CHARS AFTER LEMMA
StripOfChar(allWords)

print("\n", allWords, "\n")

# SORT, REMOVE DUPLICATES
allWords = sorted(set(allWords))
tags = sorted(set(tags))

print(len(xy), "patterns", xy)
print(len(tags), "tags:", tags)
print(len(allWords), "unique stemmed words:", allWords)
print("\n")


# CREATE TRAINING DATA
X_train = []
y_train = []


###########################
# CREATE BAG OF WORDS (BG)
###########################

for (pattern_sentence, tag) in xy:
    # X: bag of words for each pattern_sentence
    bag = bagOfWords_BG(pattern_sentence, allWords)
    X_train.append(bag)
    # y: PyTorch CrossEntropyLoss needs only class labels, not one-hot
    label = tags.index(tag)
    y_train.append(label)


X_train = np.array(X_train)
y_train = np.array(y_train)

print(X_train)
print(y_train)



# Hyper-parameters
num_epochs = 1500
batch_size = 8
learning_rate = 0.001
input_size = len(X_train[0])
hidden_size = 8
output_size = len(tags)
print(input_size, output_size)



#############################################
# CREATE PYTORCH DATASET FOR FURTHER TRAINING
#############################################
class ChatDataset(Dataset):

    def __init__(self):
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = y_train

    # support indexing such that dataset[i] can be used to get i-th sample
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    # we can call len(dataset) to return the size
    def __len__(self):
        return self.n_samples


dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset,
                          batch_size=batch_size,
                          shuffle=True,
                          num_workers=0)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = NeuralNet(input_size, hidden_size, output_size).to(device)

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# Train the model
for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(dtype=torch.long).to(device)

        # Forward pass
        outputs = model(words)
        # if y would be one-hot, we must apply
        # labels = torch.max(labels, 1)[1]
        loss = criterion(outputs, labels)

        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

print(f'final loss: {loss.item():.4f}')



data = {
    "model_state": model.state_dict(),
    "input_size": input_size,
    "hidden_size": hidden_size,
    "output_size": output_size,
    "all_words": allWords,
    "tags": tags
}

FILE = "dataBG.pth"
torch.save(data, FILE)

print(f'training complete. file saved to {FILE}') 

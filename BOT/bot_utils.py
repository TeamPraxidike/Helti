"""
import classla
#classla.download('bg')
nlp = classla.Pipeline('bg') # run classla.download('bg') beforehand if necessary
doc = nlp("Алеко Константинов е роден в Свищов.")
print(doc)

"""

"""
basic demo script
"""

import sys
import argparse
import os

import classla
from classla.resources.common import DEFAULT_MODEL_DIR
from classla.utils.conll import CoNLL



def StripOfChar(listOfLemmas):
    '''
    ~ Removes any unnecessary characters after lemmatization
    '''
    for x in listOfLemmas:
        if "-" not in x:
            continue
        else:
            for y in range(len(x)):
                if x[y] != "-":
                    continue
                else:
                    listOfLemmas[listOfLemmas.index(x)] = x.replace(x[y:len(x)],"")
                    break

    return listOfLemmas



if __name__ == '__main__':
    # get arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--models_dir', help='location of models files | default: ~/classla_resources',
                        default=DEFAULT_MODEL_DIR)
    parser.add_argument('-l', '--lang', help='Demo language',
                        default="bg")
    parser.add_argument('-c', '--cpu', action='store_true', help='Use cpu as the device.')
    args = parser.parse_args()

    example_sentences = {"bg": ["Алеко Константинов беше роден в Свищов, но аз съща съм се родил там.", "Имало едно време един голям карък"]}

    if args.lang not in example_sentences:
        print(f'Sorry, but we don\'t have a demo sentence for "{args.lang}" for the moment. Try one of these languages: {list(example_sentences.keys())}')
        sys.exit(1)

    # download the models
    classla.download(args.lang, args.models_dir)


    # set up a pipeline
    print('---')
    print('Building pipeline...')
    pipeline = classla.Pipeline(dir=args.models_dir, lang=args.lang, use_gpu=(not args.cpu))

    print((example_sentences[args.lang]))
    # process the document
    doc = pipeline(example_sentences[args.lang][0])


    # access nlp annotations
    print('')
    print('Input: {}'.format(example_sentences[args.lang]))
    print("The tokenizer split the input into {} sentences.".format(len(doc.sentences)))
    print('---')

    print('tokens of first sentence: ')
    strang = doc.sentences[0].tokens_string()
    print(strang)
    print('')
    print('---')

    print('dependency parse of first sentence: ')
    doc.sentences[0].print_dependencies()
    print('')
    print('---')

    """
    -> sent in doc.sentences returns a 2d list
    -> word in sent.words returns keys from dictionary saved in the first list
    -> the next operation returns the value from the said key
    ---> in this case the k:v pair is 'lemma':'value'
    """

    lemmas = [f'{word.lemma}' for sent in doc.sentences for word in sent.words]

    cleanLemmas = StripOfChar(lemmas)
    print(cleanLemmas)
    print('')
    print('---')

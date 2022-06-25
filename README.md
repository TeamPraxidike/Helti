
# Helti

[Документация на Български](./READMEBG.md)

>This is a project made for Hackathon October 2021 (hosted by Asen Zlatarov) & NOIT by eccy, joan, smensmen and thefallenking

>Won first place at Hackathon Burgas "Asen Zlatarov"

## Installation

Download using

```bash
git clone https://github.com/Zakrok09/Helti.git
```

Host the website on localhost using the **Live Server Extension** on Visual Studio Code or by using Chrome Dev Host.

## Usage

### Usage of website

After opening the website on a localhost make an account by following the instructions. After making an account return to the inital page and log in if necesarry. Depending on the type of account your are using a panel will open showing you tools for a patient's or a doctor's account.

### Usage of model

Download the repository and open the MODEL folder. Open a console and make sure you install the dependecies (You must have atleast python 3.8.8 and pip installed).

```bash
python -m pip install tensorflow
python -m pip install opencv-python
python -m pip install flask

OR

pip install tensorflow
pip install opencv-python
pip install opencv-python
```

After you have downloaded and installed the dependecies, either use python IDE or another compiler and run app.py.

## Used programming languages

This projects uses a variety of programming languages:

- Website - HTML5, SCSS, JavaScript ES6 ECMAScript 2018 (with some legacy elements)
- Machine learning models - Python
- Chat bot - Python

If you want to read the code documentation open [CODE.md](./CODE.md)

## Further Dependecies

This projects uses a variety of open-source packages

- Website - leaflet.js, CryptoJS
- Machine learning models - tensorflow, opencv-python, numpy, flask
- Chat bot - numpy, random, json, classla, nltk, torch, NeuralNet, nltk_utils, bagOfWords_BG, bot_utils, StripOfChar, chat, get_response, langdetect, detect, detect_langs, Flask, render_template, request, jsonify

## Back-end

This website uses Firebase for its back-end. Security wise, the database is accessible by certain requirements and can't be edited by non-admins. The section of code that connect the front-end to the back-end is obfuscated.

## Model

We have two AI models. The first one is a regression model for predicting heart diseases. The second one is a classification model which uses x-rays photos for input and predicts pneumonia.

## Chat bot

The current develpment stage revolves around 2 versions of the Bot:

- Bulgarian version with retrieval-based response methods with Classla (forked from Stanza lib)
- English version with retrieval-based response methods (Stanza lib)

## License

[MIT](https://choosealicense.com/licenses/mit/)

special thanks to gesha, alexander and pepi - moral support


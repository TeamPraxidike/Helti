[Documentation in English](./README.md)

# Helti

>Този проект е направен за НОИТ от eccy и thefallenking

## Инсталиране

Изтеглете чрез команда:

```bash
git clone https://github.com/Zakrok09/Helti.git
```

За да хостнете уебсайта използвайте **Live Server Extension** във Visual Studio Code.

## Използване

### Използване на уебсайта

След като отворите сайта си направете акаунт като следвате инструкциите. След като си направите акаунт се върнете на заглавната страница и ако трябва влезте в акаунта. В зависимост от вида на акаунта ви ще се отворят инстурменти соътветно за лекар или за пациент.

### Използване на модела

Изтеглете репозиторито и отворете папка MODEL. Отворете конзолата и проверете дали имате всички нужни библотеки изтеглени (Трябва да имате python 3.8.8 и pip инсталирани).

```bash
python -m pip install tensorflow
python -m pip install opencv-python
python -m pip install flask

ИЛИ

pip install tensorflow
pip install opencv-python
pip install opencv-python
```

След като сте изтеглили и инстарали библиотеките, използвайте python IDE или друг компилатор и въведете app.py.

## Използвани програмни езици

Този проект използва редици езици:

- Уебсайт - HTML5, SCSS, JavaScript ES6 ECMAScript 2018 (with some legacy elements)
- Модели на ИИ - Python
- Чат бот - Python

Ако искате да прочетете документацията на кода отворте [CODE.md](./CODE.md)

## Използванио библиотеки

Този проект използва open-source пакети и библиотеки

- Уебсайт - leaflet.js
- Модели на ИИ - tensorflow, opencv-python, numpy, flask
- Чат бот - numpy, random, json, classla, nltk, torch, NeuralNet, nltk_utils, bagOfWords_BG, bot_utils, StripOfChar, chat, get_response, langdetect, detect, detect_langs, Flask, render_template, request, jsonify

## Back-end

Този сайт използва Firebase за back-end. От страна на сигурност, базата данни е отворена само за администратори и не може да бъде редактирана. Частта от кода, която свързва front с back-end-а е обфускирана (криптирана).

## Модел

Имаме два AI модела. Първият е регресионен. Вторият е за класифициране и използва снимки от рентген за да разпознава пневмония.

## Чат бот

Ботът бива разработван в два вида:

- Българска версия с retrieval-based response методи с Classla (forked from Stanza lib)
- Английската версия с retrieval-based response methods (Stanza lib)

## Лиценз

[MIT](https://choosealicense.com/licenses/mit/)


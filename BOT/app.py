from flask import Flask, render_template, request, jsonify
from langdetect import detect, detect_langs
from chat import get_response
import classla

app = Flask(__name__)

classla.download('bg')

@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # TODO: check if text is valid
    if len(text) < 3 or text in ['?', '.', '!', '(', ')', '{', '}', '']:
        return jsonify({"answer": "Моля, въведете валидно съобщение."})
    if detect(text) != 'bg' and detect(text) != 'ru':
        print(text)
        print(len(text))
        print(detect(text))
        print(detect_langs(text))
        return jsonify({"answer": "Please, enter a valid message in Bulgarian or switch to the English version of the website."})
    print(text)
    print(len(text))
    print(detect(text))
    print(detect_langs(text))
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)
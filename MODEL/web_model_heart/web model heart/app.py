from flask import Flask, render_template, request
import heart_web

app = Flask(__name__, static_folder="images")

@app.route("/", methods = ['GET','POST'])
def hello():

    pd = []
    if request.method == "POST":
        data = request.form["data"]
        pred_data = heart_web.model_prediction(data)
        pd = str(round(pred_data[0]*100,3))+"%"

    return render_template("index.html", prediction = pd)

if __name__ == "__main__":
    app.run(debug=True)
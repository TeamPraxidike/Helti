from flask import Flask, render_template, request

import model

app = Flask(__name__, static_folder="images_site")

@app.route("/", methods = ['GET'])
def hello():

    return render_template("index.html")

@app.route("/", methods = ['POST'])
def predict():
    imagefile = request.files['imageFile']
    imagepath = "./images/" + imagefile.filename
    imagefile.save(imagepath)
       
    pred_val = model.model_prediction(imagepath)
    pd = pred_val[0]
    ch = str(round(pred_val[1]*100,3)) + "%"

    imgname = imagefile.filename
       
    return render_template("index.html", chance = ch, prediction = pd, name = imgname)
    
if __name__ == "__main__":
    app.run(debug=True)
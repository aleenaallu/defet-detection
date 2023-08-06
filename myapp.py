from flask import Flask, render_template,request
from tensorflow import keras
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

app = Flask(__name__)
model = keras.models.load_model('model.h5')
@app.route('/')
def index():
    return render_template("index.html", name="Tariq")


@app.route('/prediction', methods=["POST"])
def prediction():
    img = request.files['img']
    img.save('img.jpg')
    img = image.load_img("img.jpg", target_size=(110,110))
    x=image.img_to_array(img) / 255
    resized_img_np = np.expand_dims(x,axis=0)
    prediction = model.predict(resized_img_np) 
    output={'freshapple':0,'freshbanana':1,'freshorange':2,'rottenapple':3,'rottenbanana':4,'rottenorange':5} 
    value=np.argmax(prediction)
    # print(value)
    lb=list(output.keys())
    # print(lb)
    # print(lb[value])
    pre=lb[value]
    return render_template("prediction.html", data=pre)
    

if __name__ =="__main__":
    app.run(host='0.0.0.0',port=9000)
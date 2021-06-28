from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os, sys, glob, re


# import pandas as pd
# import streamlit as st
import pickle
import Sensor_values as sv

app = Flask(__name__)

model_path = "SoilNet_93_86.h5"

SoilNet = load_model(model_path)

classes = {0: "Alluvial Soil:-{ Rice,Wheat,Sugarcane,Maize,Cotton,Soyabean,Jute, Specially - Soyabean  }",
           1: "Black Soil:-{ Virginia, Wheat , Jowar,Millets,Linseed,Castor,Sunflower, Specially - Wheat } ",
           2: "Clay Soil:-{ Rice,Lettuce,Chard,Broccoli,Cabbage,Snap Beans, Specially - GroundNut}",
           3: "Red Soil:{ Cotton,Wheat,Pilses,Millets,OilSeeds,Potatoes, Specially - Cotton  }"}

pickel_in = open("classifier.pkl","rb")
rm = pickle.load(pickel_in)

# GET THE SENSOR VALUES INTO THE CODE
sensor_values = sv.get_readings()
user_location = sensor_values[0]
sensor_values = sensor_values[1]

Fertiliser_Input = np.array(sensor_values[0 : 11])
def predictions(pH, EC, OC, N, P, K, S, Zn, Fe, Cu, Mn, B):
    pred = rm.predict([[pH, EC, OC, N, P, K, S, Zn, Fe, Cu, Mn, B]])
    # print(pred)
    # cropPrediction = pred[0]
    return (pred[0])

# @app.route('/manual', methods=['GET', 'POST'])
# def plantPredictionManualData():
#     st.title("Crop Prediction From Soil Analysis")
#
#     st.write(""" ##### All the fields are compulsory(*)""")
#
#     f, l = st.beta_columns(2)
#     pH = f.text_input("pH(0 to 14)*")
#     EC = l.text_input("Electrical Conductivity EC (0.2 to 10 dSm/m)*")
#     f, l = st.beta_columns(2)
#     OC = f.text_input("Organic Carbon OC (0.2 to 2 %)*")
#     N = l.text_input("Nitrogen N(100 to 700 Kg/Ha)*")
#     f, l = st.beta_columns(2)
#     P = f.text_input("Phosphorus P (10 to 80 Kg/Ha)*")
#     K = l.text_input("Potassium K(150 to 800 Kg/Ha)*")
#     f, l = st.beta_columns(2)
#     S = f.text_input("Sulfur S(2 to 50 PPM)*")
#     Zn = l.text_input("Zinc Zn(0.2 to 5 PPM)*")
#     f, l = st.beta_columns(2)
#     Fe = f.text_input("Iron Fe(2 to 20 PPM)*")
#     Cu = l.text_input("Copper Cu(0.2 to 5 PPM)*")
#     f, l = st.beta_columns(2)
#     Mn = f.text_input("Manganese Mn(2 to 25 PPM)*")
#     B = l.text_input("Boron B(0.2 to 5 PPM)*")
#
#     result = ""
#     if st.button("Predict"):
#         result = predictions(pH, EC, OC, N, P, K, S, Zn, Fe, Cu, Mn, B)
#     st.success('Crop Predicated is : {}'.format(result))
#
#     st.write("""
#              #### Note:Enter Data Related to Only following Districts And Talukas of Maharashtra:
#        """)
#     st.write("""##### Shirala,Jamner,Dhule,Malegaon,Nashik,Junnar,Mulshi,Yavatmal,Washim,Wani,Nanded,Karvir
#                 """)
#     st.write("""
#              ##### Mukhed,Buldana,Khamgaon,Patan,Koregaon,Karad,Kagal,Nagpur(Rural),Bhusawal,Jalgaon,Akola.
#              """)
def plantPrediction():

    # physical parameters
    pH = sensor_values[0] #pH
    EC = sensor_values[1]
    OC = sensor_values[2] #organic carbon
    # the macro-nutrients
    N = sensor_values[3]
    P = sensor_values[4]
    K = sensor_values[5]
    # micro-nutrients
    S = sensor_values[6]
    Zn = sensor_values[7]
    Fe = sensor_values[8]
    Cu = sensor_values[9]
    Mn = sensor_values[10]
    B = sensor_values[11]

    result = ""
    # if st.button("Predict"):
    result = predictions(pH, EC, OC, N, P, K, S, Zn, Fe, Cu, Mn, B)
    # print('Crop Predicated is : {}'.format(result))
    return ('Best Plant Type  : {}'.format(result))
def model_predict(image_path, model):
    print("Predicted")
    image = load_img(image_path, target_size=(224, 224))
    image = img_to_array(image)
    image = image / 255
    image = np.expand_dims(image, axis=0)

    result = np.argmax(model.predict(image))
    prediction = classes[result]
    plantPredictionResult = plantPrediction()
    if result == 0:
        print("Alluvial.html")

        return "Alluvial", "Alluvial.html"
    elif result == 1:
        print("Black.html")

        return "Black", "Black.html"
    elif result == 2:
        print("Clay.html")

        return "Clay", "Clay.html"
    elif result == 3:
        print("Red.html")

        return "Red", "Red.html"


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    print("Entered")
    if request.method == 'POST':
        print("Entered here")
        file = request.files['image']  # fet input
        filename = file.filename
        print("@@ Input posted = ", filename)

        file_path = os.path.join('static/user uploaded', filename)
        file.save(file_path)

        print("@@ Predicting class......")
        pred, output_page = model_predict(file_path, SoilNet)

        return render_template(output_page, pred_output=pred, user_image=file_path, pred_crop = plantPrediction())




if __name__ == '__main__':
    app.run(debug=True, threaded=False)


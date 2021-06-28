import numpy as np
import pandas as pd
import streamlit as st
import pickle
import Sensor_values as sv

pickel_in = open("classifier.pkl","rb")
rm = pickle.load(pickel_in)

# GET THE SENSOR VALUES INTO THE CODE
sensor_values = sv.get_readings()
user_location = sensor_values[0]
sensor_values = sensor_values[1]

Fertiliser_Input = np.array(sensor_values[0 : 11])
def predictions(pH, EC, OC, N, P, K, S, Zn, Fe, Cu, Mn, B):
    pred = rm.predict([[pH, EC, OC, N, P, K, S, Zn, Fe, Cu, Mn, B]])
    print(pred)
    return (pred[0])


def main():

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
    print('Crop Predicated is : {}'.format(result))




if __name__ == '__main__':
    main()
    # print(sensor_values[0])



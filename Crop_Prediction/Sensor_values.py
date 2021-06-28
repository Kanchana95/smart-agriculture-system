
import random

def get_readings():    
    # import ipinfo

    
    # Using your IP Address to find out your location
    
    # ipinfo_api_key = (input('Enter the API Key : '))
    # handler = ipinfo.getHandler(ipinfo_api_key)
    # details = handler.getDetails()
    city = 'Kalutara'
    
    # Generation of random values for circuit simulation

    # pH = f.text_input("pH(0 to 14)*")
    # EC = l.text_input("Electrical Conductivity EC (0.2 to 10 dSm/m)*")
    # OC = f.text_input("Organic Carbon OC (0.2 to 2 %)*")
    # N = l.text_input("Nitrogen N(100 to 700 Kg/Ha)*")
    # P = f.text_input("Phosphorus P (10 to 80 Kg/Ha)*")
    # K = l.text_input("Potassium K(150 to 800 Kg/Ha)*")
    # S = f.text_input("Sulfur S(2 to 50 PPM)*")
    # Zn = l.text_input("Zinc Zn(0.2 to 5 PPM)*")
    # Fe = f.text_input("Iron Fe(2 to 20 PPM)*")
    # Cu = l.text_input("Copper Cu(0.2 to 5 PPM)*")
    # Mn = f.text_input("Manganese Mn(2 to 25 PPM)*")
    # B = l.text_input("Boron B(0.2 to 5 PPM)*")
    
    Artificial_pH = round(random.uniform(0,14), 2)
    Artificial_EC= round(random.uniform(0.2, 10), 1)

    Artificial_OC = round(random.uniform(0.2, 2), 1)
    Artificial_N = round(random.uniform(100, 700), 1)
    Artificial_P = round(random.uniform(10, 80), 1)
    Artificial_K = round(random.uniform(150, 800), 1)
    Artificial_S = round(random.uniform(2, 50), 1)
    Artificial_Zn = round(random.uniform(0.2, 5), 1)
    Artificial_Fe = round(random.uniform(2, 20), 1)
    Artificial_Cu = round(random.uniform(0.2, 5), 1)
    Artificial_Mn = round(random.uniform(2, 25), 1)
    Artificial_B = round(random.uniform(0.2, 5), 1)
    
    Artificial_Moisture = round(random.uniform(27,87), 1)
    Artificial_Pressure = round(random.uniform(98, 103), 1)
    
    Artificial_temp = round(random.uniform(25, 45), 1)
    Artificial_humidity = round(random.uniform(29, 90), 1)
    
    # Collating all random values in a list
    
    readings = [Artificial_pH, Artificial_EC, Artificial_OC, Artificial_N, Artificial_P, Artificial_K, Artificial_S,
                Artificial_Zn, Artificial_Fe, Artificial_Cu, Artificial_Mn, Artificial_B,
                Artificial_temp, Artificial_humidity, Artificial_Pressure, 
                Artificial_Moisture]
    
    # Printing the values to know the order    
    # print('pH : ', Artificial_pH)
    # print('OC : ', Artificial_OC)
    # print('N : ', Artificial_N)
    # print('P : ', Artificial_P)
    # print('K : ', Artificial_K)
    # print('S : ', Artificial_S)
    # print('Zn : ', Artificial_Zn)
    # print('Fe : ', Artificial_Fe)
    # print('Cu : ', Artificial_Cu)
    # print('Mn : ', Artificial_Mn)
    # print('B : ', Artificial_B)
    # print('Temperature : ', Artificial_temp)
    # print('Humidity : ', Artificial_humidity)
    # print('Pressure : ', Artificial_Pressure)
    # print('Moisture : ', Artificial_Moisture)

    return [city, readings]


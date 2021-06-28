import pandas as pd
import requests, json
import pickle
from datetime import datetime, timedelta
import time



rainlevels ={
    "thunderstorm with light rain":1,
    "thunderstorm with rain":3,
    "thunderstorm with heavy rain":6,
    "light thunderstorm":0.5,
    "thunderstorm":1,
    "heavy thunderstorm":10,
    "ragged thunderstorm":20,
    "thunderstorm with light drizzle":0.5,
    "thunderstorm with drizzle":1,
    "thunderstorm with heavy drizzle":8,
    "light intensity drizzle":0.2,
    "drizzle":0.5,
    "heavy intensity drizzle":1,
    "light intensity drizzle rain":2,
    "shower rain and drizzle":4,
    "heavy shower rain and drizzle":6,
    "shower drizzle":8,
    "light rain":1,
    "moderate rain":3,
    "heavy intensity rain":6,
    "very heavy rain":8,
    "extreme rain":10,
    "freezing rain":15,
    "light intensity shower rain":20,
    "shower rain":5,
    "heavy intensity shower rain":40,
    "ragged shower rain":50
}






def apicalling():
  coreURL = "http://api.openweathermap.org/data/2.5/forecast?"
  API_KEY = "44f8aebf4a313bff2845450b88be3213"


  lati= "6.9271"
  longi= "79.8612"

  #API calling q: appid:
  URL = coreURL + "lat=" + lati + "&lon=" + longi + "&appid=" + API_KEY
  #request
  response = requests.get(URL).json()
  return response

def respoToDF(response):
  preDf = pd.DataFrame()
  # Creating empty lists
  prediction_num = 0
  list_prediction_num = []
  date_time_prediction = []
  owm_city_id = []
  city_name = []
  latitude = []
  longitude = []
  country_name = []
  population = []
  timezone = [] # Shift in seconds from UTC
  sunrise = []
  sunset = []
  # Main
  temp_prediction = []
  temp_feels_like_prediction = []
  temp_min_prediction = []
  temp_max_prediction = []
  pressure_prediction = []
  sea_level_prediction = []
  grnd_level_prediction = []
  humidity_prediction = []
  temp_kf_prediction = []
  # Weather
  main_weather_prediction = []
  main_weather_description_prediction = []
  # Clouds
  clouds_prediction = []
  # Wind
  wind_speed_prediction = []
  wind_degree_prediction = []

  # Add data to list

  for num_forecasts in response["list"]:
      preDf['prediction_num'] = prediction_num
      list_prediction_num.append(prediction_num)
      date_time_prediction.append(response['list'][prediction_num]['dt_txt'])
      
      owm_city_id.append(response['city']['id'])
      city_name.append(response['city']['name'])
      latitude.append(response['city']['coord']['lat'])
      longitude.append(response['city']['coord']['lon'])
      country_name.append(response['city']['country'])
      population.append(response['city']['population'])
      
      if response['city']['timezone'] >0 :
          timezone.append("+" + str((response['city']['timezone'])/3600))
      else:
          timezone.append((response['city']['timezone'])/3600)
          
      sunrise.append(response['city']['sunrise'])
      sunset.append(response['city']['sunset'])
      
      # Main
      temp_prediction.append(response['list'][prediction_num]['main']['temp'])
      temp_feels_like_prediction.append(response['list'][prediction_num]['main']['feels_like'])
      temp_min_prediction.append(response['list'][prediction_num]['main']['temp_min'])
      temp_max_prediction.append(response['list'][prediction_num]['main']['temp_max'])
      pressure_prediction.append(response['list'][prediction_num]['main']['pressure'])
      sea_level_prediction.append(response['list'][prediction_num]['main']['sea_level'])
      grnd_level_prediction.append(response['list'][prediction_num]['main']['grnd_level'])
      humidity_prediction.append(response['list'][prediction_num]['main']['humidity'])
      temp_kf_prediction.append(response['list'][prediction_num]['main']['temp_kf'])
      # Weather
      main_weather_prediction.append(response['list'][prediction_num]['weather'][0]['main'])
      main_weather_description_prediction.append(response['list'][prediction_num]['weather'][0]['description'])
      # Clouds
      clouds_prediction.append(response['list'][prediction_num]['clouds']['all'])
      # Wind
      wind_speed_prediction.append(response['list'][prediction_num]['wind']['speed'])
      wind_degree_prediction.append(response['list'][prediction_num]['wind']['deg'])
      
      prediction_num += 1



  # Put data into a dataframe
  preDf['prediction_num'] = list_prediction_num
  preDf['date_time_prediction'] = date_time_prediction
  preDf['owm_city_id'] = owm_city_id
  preDf['city_name'] = city_name
  preDf['latitude'] = latitude
  preDf['longitude'] = longitude
  preDf['country_name'] = country_name
  preDf['population'] = population
  preDf['timezone'] = timezone
  preDf['sunrise'] = sunrise
  preDf['sunset'] = sunset
  # Main
  preDf['temp_prediction'] = temp_prediction
  preDf['temp_feels_like_prediction'] = temp_feels_like_prediction
  preDf['temp_min_prediction'] = temp_min_prediction
  preDf['temp_max_prediction'] = temp_max_prediction
  preDf['pressure_prediction'] = pressure_prediction
  preDf['sea_level_prediction'] = sea_level_prediction
  preDf['grnd_level_prediction'] = grnd_level_prediction
  preDf['humidity_prediction'] = humidity_prediction
  preDf['temp_kf_prediction'] = temp_kf_prediction
      # Weather
  preDf['main_weather_prediction'] = main_weather_prediction
  preDf['main_weather_description_prediction'] = main_weather_description_prediction
      # Clouds
  preDf['clouds_prediction'] = clouds_prediction
      # Wind
  preDf['wind_speed_prediction'] = wind_speed_prediction
  preDf['wind_degree_prediction'] = wind_degree_prediction
  return preDf



def readclusters():
  spratedf1=pd.read_csv("supplyclust.csv")
  return spratedf1



def load_model():
  loaded_model = pickle.load(open("kmmodel.sav", 'rb'))
  return load_model

def calrate(lmodel, spratedf, preDf, cropt, cropage, croparea,t1,t2,t3,t4,t5,m1,m2,m3,m4,m5):


  inarray=[[t1,t2,t3,t4,t5,m1,m2,m3,m4,m5]]
  #load model

  result = int (lmodel.predict(inarray))
  print("result"+str(result))
  tree_efficiencydf=spratedf[(spratedf["crop_type"]==cropt)& (spratedf["crop_age"]==cropage)]
  tarcol=result+2
  print("tarcol"+str(tarcol))
  t=3
  supplyrate(m1,m3,m4,m5,tree_efficiencydf,preDf,t,tarcol)

def supplyrate(m1,m3,m4,m5,tree_efficiencydf,preDf,t,tarcol):
  rtval=0
  A=True
  while(A==True):
      time.sleep(120)
      if ((m1<0.2) or (m5<0.2) or (m3<0.3) or (m4<0.3)):
          tree_efficiency=float(tree_efficiencydf.iloc[:,[tarcol]].values)*3600.0/10000.0
          grossws=9.5+tree_efficiency
          caldf=preDf.iloc[1:9]
          weatherlist=list(caldf.main_weather_description_prediction.unique())
          totalrainfall=0
          for i in weatherlist:
            if i in rainlevels.keys():
              totalrainfall=totalrainfall+rainlevels[i]*t
          netws=grossws-totalrainfall*t
          if ((netws<9.5) & (totalrainfall>5)):
            rtval=1
          elif ((netws<9.5) & (totalrainfall==5)):
            rtval=1
          elif ((netws<9.5) & (totalrainfall<5)):
            rtval=2
          elif ((netws==9.5) & (totalrainfall<5)):
            rtval=2
          elif ((netws>9.5) & (netws<11)):
            rtval=3
          elif (netws>11):
            rtval=4
          else:
            rtval=1
      else:
          rtval=0

           
def main():

  #get input crop type
  cropt="soyabeans"
  #get inut crop age
  cropage="reproduction"
  #get crop area
  croparea=1
  #get input temparature values


  Ab=1
  while(Ab==1):  
    tary=[1]
    nowtime = datetime.now()
    nexttime = nowtime+timedelta(hours = 24)
    response=apicalling()
    preDf1=respoToDF(response).copy()

    while(tary[0]==1):
      if nowtime<nexttime:
        t1,t2,t3,t4,t5=24,21,20,18,17
        #get input moisture values
        m1,m2,m3,m4,m5=0.0897,0.09548,0.11258,0.13596,0.16789
        spratedf=readclusters()
        lmodel=pickle.load(open("kmmodel.sav", 'rb'))
        outputval=calrate(lmodel, spratedf, preDf1, cropt, cropage, croparea,t1,t2,t3,t4,t5,m1,m2,m3,m4,m5)

      else:
        tary[0]=0




if __name__=="__main__":
  main()

  


                 
                    




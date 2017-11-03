from django.shortcuts import render
import requests
import json
from django.http import HttpResponseRedirect
from .forms import NameForm
from .weather import Weather
from datetime import datetime
from .forecast import Forecast
from .CityPic import Img
from .LocalTime import LocalTime

def DayOfWeek(wd):
    if wd == 1: return 'Monday'
    if wd == 2: return 'Tuesday'
    if wd == 3: return 'Wednesday'
    if wd == 4: return 'Thursday'
    if wd == 5: return 'Friday'
    if wd == 6: return 'Saturday'
    if wd == 7: return 'Sunday'

#Afficher les données météo à partir de l'id de la ville
def weather(request, city_id):

    weather1=Weather(city_id)
    weather1.retrieveWeathInfo()

    temp=weather1.dict['temp']
    max=weather1.dict['temp_max']
    min=weather1.dict['temp_min']
    city=weather1.dict['city']
    icon=weather1.dict['icon']
    description=weather1.dict['main']
    lon=int(weather1.dict['lon'])
    lat=int(weather1.dict['lat'])


    img=Img(lat,lon)
    img.retrieveImgRef()
    reference=img.reference
    width=int(img.width)


    fcst = Forecast(city_id)
    fcst.retrieve_forecast()

    wd1=datetime.strptime(fcst.day_1[0]['dt_txt'][:10],'%Y-%m-%d').isoweekday()
    day1=DayOfWeek(wd1)
    temp11, max11, min11, wind11, pressure11, humidity11, desc11, icon11 = fcst.day_1[0]['main']['temp'],fcst.day_1[0]['main']['temp_max'],fcst.day_1[0]['main']['temp_min'], fcst.day_1[0]['wind']['speed'],fcst.day_1[0]['main']['pressure'],fcst.day_1[0]['main']['humidity'],fcst.day_1[0]['weather'][0]['description'],fcst.day_1[0]['weather'][0]['icon']
    temp12, max12, min12, wind12, pressure12, humidity12, desc12, icon12 = fcst.day_1[1]['main']['temp'],fcst.day_1[1]['main']['temp_max'],fcst.day_1[1]['main']['temp_min'], fcst.day_1[1]['wind']['speed'],fcst.day_1[1]['main']['pressure'],fcst.day_1[1]['main']['humidity'],fcst.day_1[1]['weather'][0]['description'],fcst.day_1[1]['weather'][0]['icon']
    temp13, max13, min13, wind13, pressure13, humidity13, desc13, icon13 = fcst.day_1[2]['main']['temp'],fcst.day_1[2]['main']['temp_max'],fcst.day_1[2]['main']['temp_min'], fcst.day_1[2]['wind']['speed'],fcst.day_1[2]['main']['pressure'],fcst.day_1[2]['main']['humidity'],fcst.day_1[2]['weather'][0]['description'],fcst.day_1[2]['weather'][0]['icon']
    temp14, max14, min14, wind14, pressure14, humidity14, desc14, icon14 = fcst.day_1[3]['main']['temp'],fcst.day_1[3]['main']['temp_max'],fcst.day_1[3]['main']['temp_min'], fcst.day_1[3]['wind']['speed'],fcst.day_1[3]['main']['pressure'],fcst.day_1[3]['main']['humidity'],fcst.day_1[3]['weather'][0]['description'],fcst.day_1[3]['weather'][0]['icon']
    temp15, max15, min15, wind15, pressure15, humidity15, desc15, icon15 = fcst.day_1[4]['main']['temp'],fcst.day_1[4]['main']['temp_max'],fcst.day_1[4]['main']['temp_min'], fcst.day_1[4]['wind']['speed'],fcst.day_1[4]['main']['pressure'],fcst.day_1[4]['main']['humidity'],fcst.day_1[4]['weather'][0]['description'],fcst.day_1[4]['weather'][0]['icon']
    temp16, max16, min16, wind16, pressure16, humidity16, desc16, icon16 = fcst.day_1[5]['main']['temp'],fcst.day_1[5]['main']['temp_max'],fcst.day_1[5]['main']['temp_min'], fcst.day_1[5]['wind']['speed'],fcst.day_1[5]['main']['pressure'],fcst.day_1[5]['main']['humidity'],fcst.day_1[5]['weather'][0]['description'],fcst.day_1[5]['weather'][0]['icon']
    temp17, max17, min17, wind17, pressure17, humidity17, desc17, icon17 = fcst.day_1[6]['main']['temp'],fcst.day_1[6]['main']['temp_max'],fcst.day_1[6]['main']['temp_min'], fcst.day_1[6]['wind']['speed'],fcst.day_1[6]['main']['pressure'],fcst.day_1[6]['main']['humidity'],fcst.day_1[6]['weather'][0]['description'],fcst.day_1[6]['weather'][0]['icon']
    temp18, max18, min18, wind18, pressure18, humidity18, desc18, icon18 = fcst.day_1[7]['main']['temp'],fcst.day_1[7]['main']['temp_max'],fcst.day_1[7]['main']['temp_min'], fcst.day_1[7]['wind']['speed'],fcst.day_1[7]['main']['pressure'],fcst.day_1[7]['main']['humidity'],fcst.day_1[7]['weather'][0]['description'],fcst.day_1[7]['weather'][0]['icon']

    wd2 = datetime.strptime(fcst.day_2[0]['dt_txt'][:10], '%Y-%m-%d').isoweekday()
    day2=DayOfWeek(wd2)
    temp21, max21, min21, wind21, pressure21, humidity21, desc21, icon21 = fcst.day_2[0]['main']['temp'],fcst.day_2[0]['main']['temp_max'],fcst.day_2[0]['main']['temp_min'], fcst.day_2[0]['wind']['speed'],fcst.day_2[0]['main']['pressure'],fcst.day_2[0]['main']['humidity'],fcst.day_2[0]['weather'][0]['description'],fcst.day_2[0]['weather'][0]['icon']
    temp22, max22, min22, wind22, pressure22, humidity22, desc22, icon22 = fcst.day_2[1]['main']['temp'],fcst.day_2[1]['main']['temp_max'],fcst.day_2[1]['main']['temp_min'], fcst.day_2[1]['wind']['speed'],fcst.day_2[1]['main']['pressure'],fcst.day_2[1]['main']['humidity'],fcst.day_2[1]['weather'][0]['description'],fcst.day_2[1]['weather'][0]['icon']
    temp23, max23, min23, wind23, pressure23, humidity23, desc23, icon23 = fcst.day_2[2]['main']['temp'],fcst.day_2[2]['main']['temp_max'],fcst.day_2[2]['main']['temp_min'], fcst.day_2[2]['wind']['speed'],fcst.day_2[2]['main']['pressure'],fcst.day_2[2]['main']['humidity'],fcst.day_2[2]['weather'][0]['description'],fcst.day_2[2]['weather'][0]['icon']
    temp24, max24, min24, wind24, pressure24, humidity24, desc24, icon24 = fcst.day_2[3]['main']['temp'],fcst.day_2[3]['main']['temp_max'],fcst.day_2[3]['main']['temp_min'], fcst.day_2[3]['wind']['speed'],fcst.day_2[3]['main']['pressure'],fcst.day_2[3]['main']['humidity'],fcst.day_2[3]['weather'][0]['description'],fcst.day_2[3]['weather'][0]['icon']
    temp25, max25, min25, wind25, pressure25, humidity25, desc25, icon25 = fcst.day_2[4]['main']['temp'],fcst.day_2[4]['main']['temp_max'],fcst.day_2[4]['main']['temp_min'], fcst.day_2[4]['wind']['speed'],fcst.day_2[4]['main']['pressure'],fcst.day_2[4]['main']['humidity'],fcst.day_2[4]['weather'][0]['description'],fcst.day_2[4]['weather'][0]['icon']
    temp26, max26, min26, wind26, pressure26, humidity26, desc26, icon26 = fcst.day_2[5]['main']['temp'],fcst.day_2[5]['main']['temp_max'],fcst.day_2[5]['main']['temp_min'], fcst.day_2[5]['wind']['speed'],fcst.day_2[5]['main']['pressure'],fcst.day_2[5]['main']['humidity'],fcst.day_2[5]['weather'][0]['description'],fcst.day_2[5]['weather'][0]['icon']
    temp27, max27, min27, wind27, pressure27, humidity27, desc27, icon27 = fcst.day_2[6]['main']['temp'],fcst.day_2[6]['main']['temp_max'],fcst.day_2[6]['main']['temp_min'], fcst.day_2[6]['wind']['speed'],fcst.day_2[6]['main']['pressure'],fcst.day_2[6]['main']['humidity'],fcst.day_2[6]['weather'][0]['description'],fcst.day_2[6]['weather'][0]['icon']
    temp28, max28, min28, wind28, pressure28, humidity28, desc28, icon28 = fcst.day_2[7]['main']['temp'],fcst.day_2[7]['main']['temp_max'],fcst.day_2[7]['main']['temp_min'], fcst.day_2[7]['wind']['speed'],fcst.day_2[7]['main']['pressure'],fcst.day_2[7]['main']['humidity'],fcst.day_2[7]['weather'][0]['description'],fcst.day_2[7]['weather'][0]['icon']

    wd3 = datetime.strptime(fcst.day_3[0]['dt_txt'][:10], '%Y-%m-%d').isoweekday()
    day3=DayOfWeek(wd3)
    temp31, max31, min31, wind31, pressure31, humidity31, desc31, icon31 = fcst.day_3[0]['main']['temp'],fcst.day_3[0]['main']['temp_max'],fcst.day_3[0]['main']['temp_min'], fcst.day_3[0]['wind']['speed'],fcst.day_3[0]['main']['pressure'],fcst.day_3[0]['main']['humidity'],fcst.day_3[0]['weather'][0]['description'],fcst.day_3[0]['weather'][0]['icon']
    temp32, max32, min32, wind32, pressure32, humidity32, desc32, icon32 = fcst.day_3[1]['main']['temp'],fcst.day_3[1]['main']['temp_max'],fcst.day_3[1]['main']['temp_min'], fcst.day_3[1]['wind']['speed'],fcst.day_3[1]['main']['pressure'],fcst.day_3[1]['main']['humidity'],fcst.day_3[1]['weather'][0]['description'],fcst.day_3[1]['weather'][0]['icon']
    temp33, max33, min33, wind33, pressure33, humidity33, desc33, icon33 = fcst.day_3[2]['main']['temp'],fcst.day_3[2]['main']['temp_max'],fcst.day_3[2]['main']['temp_min'], fcst.day_3[2]['wind']['speed'],fcst.day_3[2]['main']['pressure'],fcst.day_3[2]['main']['humidity'],fcst.day_3[2]['weather'][0]['description'],fcst.day_3[2]['weather'][0]['icon']
    temp34, max34, min34, wind34, pressure34, humidity34, desc34, icon34 = fcst.day_3[3]['main']['temp'],fcst.day_3[3]['main']['temp_max'],fcst.day_3[3]['main']['temp_min'], fcst.day_3[3]['wind']['speed'],fcst.day_3[3]['main']['pressure'],fcst.day_3[3]['main']['humidity'],fcst.day_3[3]['weather'][0]['description'],fcst.day_3[3]['weather'][0]['icon']
    temp35, max35, min35, wind35, pressure35, humidity35, desc35, icon35 = fcst.day_3[4]['main']['temp'],fcst.day_3[4]['main']['temp_max'],fcst.day_3[4]['main']['temp_min'], fcst.day_3[4]['wind']['speed'],fcst.day_3[4]['main']['pressure'],fcst.day_3[4]['main']['humidity'],fcst.day_3[4]['weather'][0]['description'],fcst.day_3[4]['weather'][0]['icon']
    temp36, max36, min36, wind36, pressure36, humidity36, desc36, icon36 = fcst.day_3[5]['main']['temp'],fcst.day_3[5]['main']['temp_max'],fcst.day_3[5]['main']['temp_min'], fcst.day_3[5]['wind']['speed'],fcst.day_3[5]['main']['pressure'],fcst.day_3[5]['main']['humidity'],fcst.day_3[5]['weather'][0]['description'],fcst.day_3[5]['weather'][0]['icon']
    temp37, max37, min37, wind37, pressure37, humidity37, desc37, icon37 = fcst.day_3[6]['main']['temp'],fcst.day_3[6]['main']['temp_max'],fcst.day_3[6]['main']['temp_min'], fcst.day_3[6]['wind']['speed'],fcst.day_3[6]['main']['pressure'],fcst.day_3[6]['main']['humidity'],fcst.day_3[6]['weather'][0]['description'],fcst.day_3[6]['weather'][0]['icon']
    temp38, max38, min38, wind38, pressure38, humidity38, desc38, icon38 = fcst.day_3[7]['main']['temp'],fcst.day_3[7]['main']['temp_max'],fcst.day_3[7]['main']['temp_min'], fcst.day_3[7]['wind']['speed'],fcst.day_3[7]['main']['pressure'],fcst.day_3[7]['main']['humidity'],fcst.day_3[7]['weather'][0]['description'],fcst.day_3[7]['weather'][0]['icon']

    wd4 = datetime.strptime(fcst.day_4[0]['dt_txt'][:10], '%Y-%m-%d').isoweekday()
    day4 = DayOfWeek(wd4)
    temp41, max41, min41, wind41, pressure41, humidity41, desc41, icon41 = fcst.day_4[0]['main']['temp'],fcst.day_4[0]['main']['temp_max'],fcst.day_4[0]['main']['temp_min'], fcst.day_4[0]['wind']['speed'],fcst.day_4[0]['main']['pressure'],fcst.day_4[0]['main']['humidity'],fcst.day_4[0]['weather'][0]['description'],fcst.day_4[0]['weather'][0]['icon']
    temp42, max42, min42, wind42, pressure42, humidity42, desc42, icon42 = fcst.day_4[1]['main']['temp'],fcst.day_4[1]['main']['temp_max'],fcst.day_4[1]['main']['temp_min'], fcst.day_4[1]['wind']['speed'],fcst.day_4[1]['main']['pressure'],fcst.day_4[1]['main']['humidity'],fcst.day_4[1]['weather'][0]['description'],fcst.day_4[1]['weather'][0]['icon']
    temp43, max43, min43, wind43, pressure43, humidity43, desc43, icon43 = fcst.day_4[2]['main']['temp'],fcst.day_4[2]['main']['temp_max'],fcst.day_4[2]['main']['temp_min'], fcst.day_4[2]['wind']['speed'],fcst.day_4[2]['main']['pressure'],fcst.day_4[2]['main']['humidity'],fcst.day_4[2]['weather'][0]['description'],fcst.day_4[2]['weather'][0]['icon']
    temp44, max44, min44, wind44, pressure44, humidity44, desc44, icon44 = fcst.day_4[3]['main']['temp'],fcst.day_4[3]['main']['temp_max'],fcst.day_4[3]['main']['temp_min'], fcst.day_4[3]['wind']['speed'],fcst.day_4[3]['main']['pressure'],fcst.day_4[3]['main']['humidity'],fcst.day_4[3]['weather'][0]['description'],fcst.day_4[3]['weather'][0]['icon']
    temp45, max45, min45, wind45, pressure45, humidity45, desc45, icon45 = fcst.day_4[4]['main']['temp'],fcst.day_4[4]['main']['temp_max'],fcst.day_4[4]['main']['temp_min'], fcst.day_4[4]['wind']['speed'],fcst.day_4[4]['main']['pressure'],fcst.day_4[4]['main']['humidity'],fcst.day_4[4]['weather'][0]['description'],fcst.day_4[4]['weather'][0]['icon']
    temp46, max46, min46, wind46, pressure46, humidity46, desc46, icon46 = fcst.day_4[5]['main']['temp'],fcst.day_4[5]['main']['temp_max'],fcst.day_4[5]['main']['temp_min'], fcst.day_4[5]['wind']['speed'],fcst.day_4[5]['main']['pressure'],fcst.day_4[5]['main']['humidity'],fcst.day_4[5]['weather'][0]['description'],fcst.day_4[5]['weather'][0]['icon']
    temp47, max47, min47, wind47, pressure47, humidity47, desc47, icon47 = fcst.day_4[6]['main']['temp'],fcst.day_4[6]['main']['temp_max'],fcst.day_4[6]['main']['temp_min'], fcst.day_4[6]['wind']['speed'],fcst.day_4[6]['main']['pressure'],fcst.day_4[6]['main']['humidity'],fcst.day_4[6]['weather'][0]['description'],fcst.day_4[6]['weather'][0]['icon']
    temp48, max48, min48, wind48, pressure48, humidity48, desc48, icon48 = fcst.day_4[7]['main']['temp'],fcst.day_4[7]['main']['temp_max'],fcst.day_4[7]['main']['temp_min'], fcst.day_4[7]['wind']['speed'],fcst.day_4[7]['main']['pressure'],fcst.day_4[7]['main']['humidity'],fcst.day_4[7]['weather'][0]['description'],fcst.day_4[7]['weather'][0]['icon']

    locTime = LocalTime(lat,lon)
    locTime.calculateLocalTime()
    offset = locTime.dstOffset+locTime.rawOffset

    return render(request, 'weather.html', locals())


#Rechercher l'id d'une ville à partir de son nom
def get_city_id(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            nom_ville=form.cleaned_data['city_name']
            json_data=open('cities.json')
            data = json.load(json_data)
            L=[]
            for i in range(0,len(data)):
                if data[i]['name']==nom_ville:
                    L=L+[data[i]]
            return render(request, 'city/results.html', locals())

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'city/find_city.html', {'form': form})

def find_city(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            nom_ville=form.cleaned_data['city_name']
            json_data=open('cities.json')
            data = json.load(json_data)
            L=[]
            for i in range(0,len(data)):
                if data[i]['name']==nom_ville:
                    L=L+[data[i]]
            return render(request, 'city/results.html', locals())

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, 'city/find_city.html', locals())

def login(request):
    return render(request, 'city/login.html', locals())
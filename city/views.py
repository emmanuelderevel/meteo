from django.shortcuts import render, redirect
import requests
import json
from django.http import HttpResponseRedirect
from .forms import NameForm, SignUpForm, ConnexionForm
from .weather import Weather
from datetime import datetime
from .forecast import Forecast
from .CityPic import Img
from .LocalTime import LocalTime
from .UV import UV


#Import Login functions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse


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
    pressure=weather1.dict['pressure']
    humidity=weather1.dict['humidity']
    wind=weather1.dict['wind']


    img=Img(lat,lon)
    img.retrieveImgRef()
    reference=img.reference
    width=int(img.width)


    fcst = Forecast(city_id)
    fcst.retrieve_forecast()

    d1 = fcst.list[0]
    day1=fcst.dt[0]
    max1, min1, wind1, pressure1, icon1, desc1 = d1[0],d1[1],d1[2],d1[3],d1[4],d1[5]

    d2 = fcst.list[1]
    day2=fcst.dt[1]
    max2, min2, wind2, pressure2, icon2, desc2 = d2[0], d2[1], d2[2], d2[3], d2[4], d2[5]

    d3 = fcst.list[2]
    day3 = fcst.dt[2]
    max3, min3, wind3, pressure3, icon3, desc3 = d3[0], d3[1], d3[2], d3[3], d3[4], d3[5]

    d4 = fcst.list[3]
    day4 = fcst.dt[3]
    max4, min4, wind4, pressure4, icon4, desc4 = d4[0], d4[1], d4[2], d4[3], d4[4], d4[5]


    locTime = LocalTime(lat,lon)
    locTime.calculateLocalTime()
    offset = locTime.dstOffset+locTime.rawOffset

    uv=UV(lat,lon)
    uv.retriveUVInfo()
    uv_value=uv.value
    return render(request, 'city/weather.html', locals())


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
                if data[i]['name'].upper()==nom_ville.upper():
                    L=L+[data[i]]
            return render(request, 'city/results.html', locals())

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, 'city/find_city.html', locals())

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username, email, password)
            return HttpResponseRedirect('alerts')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUpForm()
    return render(request, 'city/sign_up.html', locals())


def connexion(request):
    error = False
    next = request.GET.get('next')
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)
                next = request.POST.get('next')
                return HttpResponseRedirect(next)
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()
    return render(request, 'city/connexion.html', locals())


@login_required
def alerts(request):
    return render(request, 'city/alerts.html', locals())


def sign_out(request):
    logout(request)
    return redirect('find_city')

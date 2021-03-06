from django.shortcuts import render, redirect
import requests
import json
from django.http import HttpResponseRedirect
from .forms import NameForm, SignUpForm, ConnexionForm
from .weather import Weather
from datetime import datetime
from .forecast import Forecast
from .citypic import Img
from .localtime import LocalTime
from .alerts import all_alerts_display
from .uv import UV
from django.db import IntegrityError



#Import Login functions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

#Alert model
from city.models import Alert

# Method to determine day of week through day number
def DayOfWeek(wd):
    if wd == 1: return 'Monday'
    if wd == 2: return 'Tuesday'
    if wd == 3: return 'Wednesday'
    if wd == 4: return 'Thursday'
    if wd == 5: return 'Friday'
    if wd == 6: return 'Saturday'
    if wd == 7: return 'Sunday'

# Method to determine month of the year from month number
def MonofYear(month_nbr):
    if month_nbr == 1 : return 'January'
    if month_nbr == 2: return 'February'
    if month_nbr == 3: return 'March'
    if month_nbr == 4: return 'April'
    if month_nbr == 5: return 'May'
    if month_nbr == 6: return 'June'
    if month_nbr == 7: return 'July'
    if month_nbr == 8: return 'August'
    if month_nbr == 9: return 'September'
    if month_nbr == 10: return 'October'
    if month_nbr == 11: return 'November'
    if month_nbr == 12: return 'December'

#Display weather informations (current weather, forecast,...) for a city through city id
def weather(request, city_id):
    user=request.user
    if user.is_authenticated:
        alerts=all_alerts_display(user)
    weather1=Weather(int(city_id))
    weather1.retrieveWeathInfo()

    city_id = int(city_id)
    temp=weather1.temp
    max=weather1.temp_max
    min=weather1.temp_min
    city = weather1.city
    icon = weather1.icon
    description = weather1.description
    lon = float(weather1.lon)
    lat = float(weather1.lat)
    pressure = float(weather1.pressure)
    humidity = float(weather1.humidity)
    wind = float(weather1.wind)
    country = weather1.country


    img=Img(lat,lon)
    img.retrieveImgRef()
    if img.error=='n':
        try:
            bgref='https://maps.googleapis.com/maps/api/place/photo?maxwidth={}&photoreference={}&key=AIzaSyDK1zU_jWE0pWRqIdyiFD2SIlX7xmxP9WQ'.format(img.width,img.reference)
        except ConnectionError:
            print("No connexion available")
    elif img.error=='y':
        try:
            bgref='http://tof.canardpc.com/view/bd6bb2f8-cbef-4231-b219-7ab6a79866f5.jpg'
        except ConnectionError:
            print("No connexion available")

    fcst = Forecast(city_id)
    fcst.retrieve_forecast()

    day = fcst.dt[4]
    day_nbr=datetime.strptime(fcst.dt[4], '%Y-%m-%d').day
    month_nbr=datetime.strptime(fcst.dt[4], '%Y-%m-%d').month
    monthstr=MonofYear(month_nbr)
    year_nbr=datetime.strptime(fcst.dt[4], '%Y-%m-%d').year
    wd1 = datetime.strptime(fcst.dt[4], '%Y-%m-%d').isoweekday()
    daystr = DayOfWeek(wd1)

    d1 = fcst.list[0]
    wd1 = datetime.strptime(fcst.dt[0], '%Y-%m-%d').isoweekday()
    day1 = DayOfWeek(wd1)
    max1, min1, wind1, pressure1, icon1, desc1 = d1[0],d1[1],d1[2],d1[3],d1[4],d1[5]

    d2 = fcst.list[1]
    wd1 = datetime.strptime(fcst.dt[1], '%Y-%m-%d').isoweekday()
    day2 = DayOfWeek(wd1)
    max2, min2, wind2, pressure2, icon2, desc2 = d2[0], d2[1], d2[2], d2[3], d2[4], d2[5]

    d3 = fcst.list[2]
    wd1 = datetime.strptime(fcst.dt[2], '%Y-%m-%d').isoweekday()
    day3 = DayOfWeek(wd1)
    max3, min3, wind3, pressure3, icon3, desc3 = d3[0], d3[1], d3[2], d3[3], d3[4], d3[5]

    d4 = fcst.list[3]
    wd1 = datetime.strptime(fcst.dt[3], '%Y-%m-%d').isoweekday()
    day4 = DayOfWeek(wd1)
    max4, min4, wind4, pressure4, icon4, desc4 = d4[0], d4[1], d4[2], d4[3], d4[4], d4[5]


    locTime = LocalTime(lat,lon)
    locTime.calculateLocalTime()
    offset = locTime.dstOffset+locTime.rawOffset

    uv=UV(lat,lon)
    uv.retriveUVInfo()
    uv_value=uv.value
    return render(request, 'city/weather.html', locals())

#Search for a city
def find_city(request):
    user=request.user
    if user.is_authenticated:
        alerts=all_alerts_display(user)
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

#Create Alert
@login_required
def create_alert(request, city_id, city):
    error=False
    try:
        user=request.user
        alert=Alert(user_id=user, city_id=city_id, city_name=city)
        alert.save()
    except IntegrityError:
        error=True
    return redirect('alerts')

#Delete Alert
def delete_alert(request, alert_id):
    alert=Alert.objects.get(id=alert_id)
    alert.delete()
    return redirect('alerts')

#Display all alerts registred for a user
@login_required
def alerts(request):
    user=request.user
    alerts=all_alerts_display(user)
    registred_alerts=[]
    for alert in Alert.objects.filter(user_id=request.user):
        registred_alerts=registred_alerts+[alert]
    return render(request, 'city/alerts.html', locals())

# Sign Up
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

#Sign in
def connexion(request):
    error = False
    next = request.GET.get('next')
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)
                next = request.POST.get('next')
                return HttpResponseRedirect(next)
            else: # sinon une erreur sera affichée
                error = True
                next = request.POST.get('next')
    else:
        form = ConnexionForm()
    return render(request, 'city/connexion.html', locals())

#Sign out button
def sign_out(request):
    logout(request)
    return redirect('find_city')

# Sign in button
@login_required
def sign_in(request):
    return redirect('find_city')

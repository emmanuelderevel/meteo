import requests
import datetime

from city.models import Alert
from django.contrib.auth.models import User


def find_rain(user):
        alert_list=""
        for alert in Alert.objects.filter(user_id=user):
            city_id=alert.city_id
            r = requests.get('http://api.openweathermap.org/data/2.5/'
                             'forecast?id={}&units=metric&APPID=955716c6c3b27005023580d9021147ba'.format(city_id))
            j = r.json()
            alert_list=alert_list + ", "+  j['city']['name']
            l=j['list']
            M=[]
            dictionnaire=dict()
            for i in range(0, len(l)):
                try:
                    if l[i]['weather'][0]['main']=='Rain':
                        type_of_rain=l[i]['weather'][0]['description']
                        day1=datetime.datetime.strptime(l[i]['dt_txt'], "%Y-%m-%d %H:%M:%S")
                        day2=day1.strftime("%A")
                        dictionnaire[day2]=type_of_rain
                        M=M+["{0} : {1}".format(day2, type_of_rain)]
                        if len(dictionnaire)>=2:
                            break
                except KeyError:
                    pass
            for day in dictionnaire:
                alert_list=alert_list+" - {0} : {1}".format(day, dictionnaire[day])
        return alert_list[2:]

# Rain_alert.city_name
# Rain_alert.city_id
# Rain_alert.day_1
# Rain_alert.day_2
# Rain_alert.rain_type_1
# Rain_alert.rain_type_2

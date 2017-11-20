import requests
import datetime

from city.models import Alert
from django.contrib.auth.models import User


class Check_Alert():
    def __init__(self, city_id):
        self.city_id=city_id
        self.alert_display=''

    def retrieveRain_Alert(self):
        r = requests.get('http://api.openweathermap.org/data/2.5/'
                            'forecast?id={}&units=metric&APPID=955716c6c3b27005023580d9021147ba'.format(self.city_id))
        j = r.json()
        self.city_name=j['city']['name']
        l=j['list']
        alert_dict=dict()
        for i in range(0, 16):
            try:
                if l[i]['weather'][0]['main']=='Rain':
                    rain_type=l[i]['weather'][0]['description']
                    raw_day=datetime.datetime.strptime(l[i]['dt_txt'], "%Y-%m-%d %H:%M:%S")
                    day=raw_day.strftime("%A")
                    alert_dict[day]=rain_type
            except KeyError:
                pass
        for d in alert_dict:
            self.alert_display+=', on {0} : {1}'.format(d, alert_dict[d])
        self.alert_display=self.alert_display[2:]

def all_alerts_display(user):
     alerts=""
     for alert in Alert.objects.filter(user_id=user):
         check=Check_Alert(alert.city_id)
         check.retrieveRain_Alert()
         if check.alert_display!="":
            alerts+="{0} - {1}. ".format(check.city_name.upper(), check.alert_display)
     return alerts


# a=Check_Alert(2988507)
# a.retrieveRain_Alert()
# print(a.alert_display)

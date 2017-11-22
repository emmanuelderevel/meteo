import requests
import datetime

from city.models import Alert
from django.contrib.auth.models import User

#This class checks if there will be rain in a city in the coming days given its city_id
class Check_Alert():
    def __init__(self, city_id):
        self._city_id=city_id
        self._alert_display=''
        self._city_name=''

    @property
    def city_id(self):
        return self._city_id

    @city_id.setter
    def city_id(self, city_id):
        self._city_id=city_id

    @property
    def alert_display(self):
        return self._alert_display

    @alert_display.setter
    def alert_display(self, alert_display):
        self._alert_display=alert_display

    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, city_name):
        self._city_name=city_name

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
        alert_list=''
        for d in alert_dict:
            alert_list+=', on {0} : {1}'.format(d, alert_dict[d])
        self.alert_display=alert_list[2:]

#This method take a user, create Check_Alert objects for each alerts related to the user and return a sentence to be displayed on the navigation bar
def all_alerts_display(user):
     alerts=""
     for alert in Alert.objects.filter(user_id=user):
         check=Check_Alert(alert.city_id)
         check.retrieveRain_Alert()
         if check.alert_display!="":
            alerts+="{0} - {1}. ".format(check.city_name.upper(), check.alert_display)
     return alerts

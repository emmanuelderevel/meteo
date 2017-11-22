import requests
from _datetime import datetime
import datetime as dtime
# This class retrieves weather forecast informations of a city through city id

class Forecast:
    def __init__(self, city_id):
        if not isinstance(city_id,int):
            raise TypeError("City Id not valid")
        self._city_id=city_id
        self._days = list()
        self._dt = list()
        self._list = list()
    @property
    def city_id(self):
        return self._city_id
    @city_id.setter
    def city_id(self,city_id):
        self._city_id=city_id
    @property
    def days(self):
        return self._days
    @days.setter
    def days(self,days):
        self._days=days
    @property
    def dt(self):
        return self._dt
    @dt.setter
    def dt(self,dt):
        self._dt=dt
    @property
    def list(self):
        return self._list
    @list.setter
    def list(self,list):
        self._list=list

    # Method that retrieves weather forecast informations
    def retrieve_forecast(self):
        try:

            r = requests.get('http://api.openweathermap.org/data/2.5/'
                         'forecast?id={}&units=metric&APPID=8bb2f275ae9f1d35a616a1454f5dc8c5'.format(self.city_id))
            j = r.json()
            l=j['list']
            # Retrieves dates for comparison purpose
            dt0 = str(datetime.strptime(l[0]['dt_txt'][:10],'%Y-%m-%d'))[:10]
            dt1 = str(datetime.strptime(l[0]['dt_txt'][:10],'%Y-%m-%d') + dtime.timedelta(1))[:10]
            dt2 = str(datetime.strptime(l[0]['dt_txt'][:10], '%Y-%m-%d') + dtime.timedelta(2))[:10]
            dt3 = str(datetime.strptime(l[0]['dt_txt'][:10], '%Y-%m-%d') + dtime.timedelta(3))[:10]
            dt4 = str(datetime.strptime(l[0]['dt_txt'][:10], '%Y-%m-%d') + dtime.timedelta(4))[:10]
            self.dt=[dt1,dt2,dt3,dt4,dt0]
            # Retrieve tomorrow forecast informations
            day1=[]
            for i in range(len(l)):
                if l[i]['dt_txt'][:10]==dt1:
                    day1 += [l[i]]
            # Retrieve forecast informations in 2 days
            day2=[]
            for i in range(len(l)):
                if l[i]['dt_txt'][:10]==dt2:
                    day2 += [l[i]]
            # Retrieve forecast informations in 3 days
            day3=[]
            for i in range(len(l)):
                if l[i]['dt_txt'][:10]==dt3:
                    day3 +=[l[i]]

            # Retrieve forecast informations in 4 days
            day4=[]
            for i in range(len(l)):
                if l[i]['dt_txt'][:10]==dt4:
                    day4 +=[l[i]]

            self.days=[day1,day2,day3,day4]
            # since the api does not garantie regular informations per day,
            # we compute aggregate parameters. For example, we calculate
            # the average wind speed and humidity since the api does not garantie
            # the wind speed and the humidity each 3h per day as promise.


            for i in range(len(self.days)):
                # Retrieve the maximum temperature
                temp_max = self.days[i][0]['main']['temp_max']

                # Retrieve the minimum temperature
                temp_min = self.days[i][0]['main']['temp_min']
                for j in range(len(self.days[i])):
                    if self.days[i][j]['main']['temp_max'] >= temp_max:
                        temp_max = self.days[i][j]['main']['temp_max']
                for j in range(len(self.days[i])):
                    if self.days[i][j]['main']['temp_min'] <= temp_min:
                        temp_min = self.days[i][j]['main']['temp_min']

                # Compute the average wind speed
                wind = 0
                for j in range(len(self.days[i])):
                    wind+=self.days[i][j]['wind']['speed']
                wind = round(wind / len(self.days[i]),2)

                # Compute the average humidity
                pressure = 0
                for j in range(len(self.days[i])):
                    pressure += self.days[i][j]['main']['pressure']
                pressure = round(pressure / len(self.days[i]),2)

                self.list+=[[temp_max,temp_min,wind,pressure,self.days[i][len(self.days[i])//2]['weather'][0]['icon'],self.days[i][len(self.days[i])//2]['weather'][0]['description']]]

        except ConnectionError:
            print('Connection error, try again.')


if __name__=='__main__':
    f1=Forecast(6455259)
    f1.retrieve_forecast()
    print(f1.days)
    print(f1.list)


import requests

# This class retrieves from openweathermap weather api
# the weather informations (temperature, pressure,...) for a city through the city id
class Weather():
    #Definition of the protected weather attributes and their getters and setters
    def __init__(self, city_id):
        if not isinstance(city_id,int):
            raise TypeError("City ID is not valid")
        self._city_id=city_id
        self._lon=''
        self._lat=''
        self._temp=''
        self._temp_max=''
        self._temp_min=''
        self._main=''
        self._icon=''
        self._description=''
        self._wind=''
        self._country=''
        self._city=''
        self._humidity=''
        self._pressure=''

    @property
    def city_id(self):
        return self._city_id
    @city_id.setter
    def city_id(self, city_id):
        self._city_id = city_id
    @property
    def lon(self):
        return self._lon
    @lon.setter
    def lon(self,lon):
        self._lon=lon
    @property
    def lat(self):
        return self._lat
    @lat.setter
    def lat(self,lat):
        self._lat=lat
    @property
    def temp(self):
        return self._temp
    @temp.setter
    def temp(self,temp):
        self._temp=temp
    @property
    def temp_max(self):
        return self._temp_max
    @temp_max.setter
    def temp_max(self,a):
        self._temp_max=a
    @property
    def temp_min(self):
        return self._temp_min
    @temp_min.setter
    def temp_min(self,b):
        self._temp_min=b
    @property
    def main(self):
        return self._main

    @main.setter
    def main(self,b):
        self._main=b
    @property
    def icon(self):
        return self._icon
    @icon.setter
    def icon(self,c):
        self._icon=c
    @property
    def description(self):
        return self._description
    @description.setter
    def description(self,d):
        self._description=d
    @property
    def wind(self):
        return self._wind
    @wind.setter
    def wind(self,wind):
        self._wind=wind
    @property
    def country(self):
        return self._country
    @country.setter
    def country(self,c):
        self._country=c
    @property
    def city(self):
        return self._city
    @city.setter
    def city(self,d):
        self._city=d
    @property
    def humidity(self):
        return self._humidity
    @humidity.setter
    def humidity(self,d):
        self._humidity=d
    @property
    def pressure(self):
        return self._pressure
    @pressure.setter
    def pressure(self,d):
        self._pressure=d
    # function that retrieves all the weather info of a city
    def retrieveWeathInfo(self):
        try:
            html = 'http://api.openweathermap.org/data/2.5/weather?' \
               'id={}&units=metric&APPID=955716c6c3b27005023580d9021147ba'.format(self.city_id)
            client = requests.get(html)
            j = client.json()
            self.temp=j['main']['temp']
            self.temp_max=j['main']['temp_max']
            self.temp_min=j['main']['temp_min']
            self.main=j['weather'][0]['main']
            self.icon=j['weather'][0]['icon']
            self.description=j['weather'][0]['description']
            self.humidity=j['main']['humidity']
            self.pressure=j['main']['pressure']
            self.wind=j['wind']['speed']
            self.city=j['name']
            self.lon=j['coord']['lon']
            self.lat=j['coord']['lat']
            self.country=j['sys']['country']
        except ConnectionError:
            # Raise an exception if connection error
            print('No access to the API. Try later ')





if __name__ == '__main__':
    p=Weather(2643743)
    p.retrieveWeathInfo()
    print(p.humidity)
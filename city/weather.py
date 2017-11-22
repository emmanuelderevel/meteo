import requests

# This class retrieves from openweathermap weather api
# the weather informations (temperature, pressure,...) for a city through the city id
class Weather():
    #Definition of the protected weather attributes and their getters and setters
    def __init__(self, city_id):
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
    def city_id(self,city_id):
        self._city_id=city_id

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
    def temp_max(self,temp_max):
        self._temp_max=temp_max

    @property
    def temp_min(self):
        return self._temp_min

    @temp_min.setter
    def temp_min(self,temp_min):
        self._temp_min=temp_min

    @property
    def main(self):
        return self._main

    @main.setter
    def main(self,main):
        self._main=main

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self,icon):
        self._icon=icon

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self,description):
        self._description=description

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
    def country(self,country):
        self._country=country

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self,city):
        self._city=city

    @property
    def humidity(self):
        return self._humidity

    @humidity.setter
    def humidity(self,humidity):
        self._humidity=humidity

    @property
    def pressure(self):
        return self._pressure

    @pressure.setter
    def pressure(self,pressure):
        self._pressure=pressure


    def retrieveWeathInfo(self):
        try:
            html = 'http://api.openweathermap.org/data/2.5/weather?' \
               'id={}&units=metric&APPID=955716c6c3b27005023580d9021147ba'.format(self.city_id)
            client = requests.get(html)
            j = client.json()
            self.temp=j['main']['temp']
            self.temp_max(j['main']['temp_max'])
            self.settemp_min(j['main']['temp_min'])
            self.setmain(j['weather'][0]['main'])
            self.seticon(j['weather'][0]['icon'])
            self.setdescription(j['weather'][0]['description'])
            self.sethumidity(j['main']['humidity'])
            self.setpressure(j['main']['pressure'])
            self.setwind(j['wind']['speed'])
            self.setcity(j['name'])
            self.setlon(j['coord']['lon'])
            self.setlat(j['coord']['lat'])
            self.setcountry(j['sys']['country'])
        except ConnectionError:
            # Raise an exception if connection error
            print('No access to the API. Try later ')


if __name__ == '__main__':
    p=Weather(6455259)
    p.retrieveWeathInfo()
    print(p.gettemp())

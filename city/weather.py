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

    def setcity_id(self,city_id):
        self._city_id=city_id

    def getcity_id(self):
        return self._city_id

    def getlon(self):
        return self._lon

    def setlon(self,lon):
        self._lon=lon

    def getlat(self):
        return self._lat

    def setlat(self,lat):
        self._lat=lat

    def gettemp(self):
        return self._temp

    def settemp(self,temp):
        self._temp=temp

    def settemp_max(self,temp_max):
        self._temp_max=temp_max

    def gettemp_max(self):
        return self._temp_max

    def settemp_min(self,temp_min):
        self._temp_min=temp_min

    def gettemp_min(self):
        return self._temp_min

    def setmain(self,main):
        self._main=main

    def getmain(self):
        return self._main

    def seticon(self,icon):
        self._icon=icon

    def geticon(self):
        return self._icon

    def setdescription(self,description):
        self._description=description

    def getdescription(self):
        return self._description

    def setwind(self,wind):
        self._wind=wind

    def getwind(self):
        return self._wind

    def setcountry(self,country):
        self._country=country

    def getcountry(self):
        return self._country

    def setcity(self,city):
        self._city=city

    def getcity(self):
        return self._city

    def sethumidity(self,humidity):
        self._humidity=humidity

    def gethumidity(self):
        return self._humidity

    def setpressure(self,pressure):
        self._pressure=pressure

    def getpressure(self):
        return self._pressure

    def retrieveWeathInfo(self):
        try:
            html = 'http://api.openweathermap.org/data/2.5/weather?' \
               'id={}&units=metric&APPID=955716c6c3b27005023580d9021147ba'.format(self.getcity_id())
            client = requests.get(html)
            j = client.json()
            self.settemp(j['main']['temp'])
            self.settemp_max(j['main']['temp_max'])
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
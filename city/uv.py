import requests

class UV():
    #Attributes definition
    def __init__(self, lat,lon):
        if not isinstance(lat,float):
            raise TypeError("Latitude not a float")
        if not isinstance(lon,float):
            raise TypeError("Longitude is not a float")
        self._value = ''
        self._lon = lon
        self._lat = lat
    @property
    def lat(self):
        return self._lat
    @lat.setter
    def lat(self,lat):
        self._lat=lat
    @property
    def lon(self):
        return self._lon
    @lon.setter
    def lon(self,lon):
        self._lon=lon
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self,value):
        self._value=value
    #Function that retrieves the UV info from the API
    def retriveUVInfo(self):
        try:
            html = 'http://api.openweathermap.org/data/2.5/uvi?' \
           'lat={}&lon={}&appid=955716c6c3b27005023580d9021147ba'.format(self.lat,self.lon)
            client = requests.get(html)
            j = client.json()
            self.value = j['value']
        except ConnectionError:
            print("Connection Error")



if __name__ == '__main__':
    p=UV(51.51,-0.13)
    p.retriveUVInfo()
    print(p.value)
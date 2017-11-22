from datetime import datetime
import time

import requests


class LocalTime():
    def __init__(self, lat, lon):
        if not isinstance(lat,float):
            raise TypeError("Latitude is not a float")
        if not isinstance(lon,float):
            raise TypeError("Longitude is not a float")
        self._dict = {}
        self._lon=lon
        self._lat=lat
        self._dstOffset=''
        self._rawOffset=''
    @property
    def dict(self):
        return self._dict
    @dict.setter
    def dict(self,dict):
        self._dict=dict
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
    def dstOffset(self):
        return self._dstOffset
    @dstOffset.setter
    def dstOffset(self,dst):
        self._dstOffset=dst
    @property
    def rawOffset(self):
        return self._rawOffset
    @rawOffset.setter
    def rawOffset(self,raw):
        self._rawOffset=raw
    #Function that computes the local time
    def calculateLocalTime(self):
        timestamp=datetime.now().timestamp()
        try:
            html = 'https://maps.googleapis.com/maps/api/timezone/json?' \
               'location={},{}&timestamp={}&key=AIzaSyDi9JUY2BoQ6NQabLIR6PkCFjklrxreIMQ'.format(self.lat,self.lon,timestamp)
            client = requests.get(html)
            j = client.json()
            print(j)
            self.rawOffset = j['rawOffset']
            self.dstOffset = j['dstOffset']
        except ConnectionError:
            print("Connection Error")

    def __str__(self):
        return 'Informations météorologiques de la ville de Londre : {}'.format(self.dict)


if __name__ == '__main__':
    p=LocalTime(33.75,-84.39)
    p.calculateLocalTime()
    print(p.rawOffset, p.dstOffset)

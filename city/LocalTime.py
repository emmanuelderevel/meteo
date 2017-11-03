from datetime import datetime
import time

import requests


class LocalTime():
    def __init__(self, lat, lon):
        self.dict = {}
        self.lon=lon
        self.lat=lat
        self.dstOffset=''
        self.rawOffset=''

    def calculateLocalTime(self):
        timestamp=datetime.now().timestamp()
        html = 'https://maps.googleapis.com/maps/api/timezone/json?' \
               'location={},{}&timestamp={}&key=AIzaSyDi9JUY2BoQ6NQabLIR6PkCFjklrxreIMQ'.format(self.lat,self.lon,timestamp)
        client = requests.get(html)
        j = client.json()
        print(j)
        self.rawOffset = j['rawOffset']
        self.dstOffset = j['dstOffset']

    def __str__(self):
        return 'Informations météorologiques de la ville de Londre : {}'.format(self.dict)


if __name__ == '__main__':
    p=LocalTime(33.75,-84.39)
    p.calculateLocalTime()
    print(p.rawOffset, p.dstOffset)

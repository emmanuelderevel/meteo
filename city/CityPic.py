import requests
import random

# In this class we use an api of google to find randomly a picture of a given city from his latitude and longitude
class Img():
    def __init__(self, lat,lon):
        self._lon=lon
        self._lat=lat
        self._reference=''
        self._width=''
        self._error=''

    def getlon(self):
        return self._lon

    def setlon(self,lon):
        self._lon=lon

    def getlat(self):
        return self._lat

    def setlat(self,lat):
        self.lat=lat

    def getreference(self):
        return self._reference

    def setreference(self,reference):
        self._reference=reference

    def getwidth(self):
        return self._width

    def setwidth(self,width):
        self._width=width

    def geterror(self):
        return self._error

    def seterror(self,error):
        self._error=error

    def retrieveImgRef(self):
        html = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?' \
           'location={},{}&radius=50000&type=point_of_interest&key=AIzaSyDK1zU_jWE0pWRqIdyiFD2SIlX7xmxP9WQ'.format(
        self.getlat(), self.getlon())
        client = requests.get(html)
        k = client.json()
        n=int(len(k['results'])-1)
        r=random.randint(0,n)
        try:
            self.setreference(k['results'][r]['photos'][0]['photo_reference'])
            self.setwidth(k['results'][r]['photos'][0]['width'])
            self.seterror('n')
        except KeyError:
            self.seterror('y')
        except ConnectionError:
            print("Connection error")

if __name__ == '__main__':
    p=Img(42.98,-81.23)
    p.retrieveImgRef()
    print(p.getreference())
    print(p.getwidth())
    print(p.geterror())
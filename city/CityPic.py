import requests
import random
class Img():
    def __init__(self, lat,lon):
        #Exceptions sur les valeurs des propriétés
        if not isinstance(lat,float):
            raise TypeError(" Latitude is not a float")
        if not isinstance(lon,float):
            raise TypeError("Longitude is not a float")
        #Propriétés
        self._lon=lon
        self._lat=lat
        self._reference=''
        self._width=''
        self._error=''
    # Getters and setters des attributs
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
    def reference(self):
        return self._reference
    @reference.setter
    def reference(self,reference):
        self._reference=reference
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,width):
        self._width=width
    @property
    def error(self):
        return self._error
    @error.setter
    def error(self,error):
        self._error=error

    # Fonction qui détermine les images à afficher en fonction de la ville
    def retrieveImgRef(self):
        try:
            html = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?' \
               'location={},{}&radius=50000&type=point_of_interest&key=AIzaSyDK1zU_jWE0pWRqIdyiFD2SIlX7xmxP9WQ'.format(
            self.lat, self.lon)
            client = requests.get(html)
            k = client.json()
            print(k)
            n=int(len(k['results'])-1)
            r=random.randint(0,n)
            try:
                self.reference=k['results'][r]['photos'][0]['photo_reference']
                self.width=k['results'][r]['photos'][0]['width']
                self.error='n'
            except KeyError:
                self.error='y'
        except ConnectionError:
            print("Connection error")

if __name__ == '__main__':
    p=Img(42.98,-81.23)
    p.retrieveImgRef()
    print(p.reference)
    print(p.width)
    print(p.error)

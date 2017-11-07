import requests
import random
class Img():
    def __init__(self, lat,lon):
        self.lon=lon
        self.lat=lat
        self.reference=''
        self.width=''

    def retrieveImgRef(self):
        html = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?' \
               'location={},{}&radius=50000&type=point_of_interest&key=AIzaSyDK1zU_jWE0pWRqIdyiFD2SIlX7xmxP9WQ'.format(
            self.lat, self.lon)
        client = requests.get(html)
        k = client.json()
        print(k)
        n=int(len(k['results'])-1)
        r=random.randint(0,n)
        self.reference = k['results'][r]['photos'][0]['photo_reference']
        self.width = k['results'][r]['photos'][0]['width']


if __name__ == '__main__':
    p=Img(42.98,-81.23)
    p.retrieveImgRef()
    print(p.reference)
    print(p.width)
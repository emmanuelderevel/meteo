import requests

class UV():
    def __init__(self, lat,lon):
        self.value = ''
        self.lon = lon
        self.lat = lat

    def retriveUVInfo(self):
        html = 'http://api.openweathermap.org/data/2.5/uvi?' \
           'lat={}&lon={}&appid=955716c6c3b27005023580d9021147ba'.format(self.lat,self.lon)
        client = requests.get(html)
        j = client.json()
        print(j)
        self.value = j['value']

    #def __str__(self):
        #return 'Index UV : {}'.format(self.dict)

if __name__ == '__main__':
    p=UV(51.51,-0.13)
    p.retriveUVInfo()
    print(p.value)

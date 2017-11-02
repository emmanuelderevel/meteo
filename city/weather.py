import requests


class Weather():
    def __init__(self, city_id):
        self.dict = {}
        self.city_id=city_id
        self.lon=''
        self.lat=''

    def retriveWeathInfo(self):
        html = 'http://api.openweathermap.org/data/2.5/weather?' \
               'id={}&units=metric&APPID=955716c6c3b27005023580d9021147ba'.format(self.city_id)
        client = requests.get(html)
        j = client.json()
        self.dict['temp'] = j['main']['temp']
        self.dict['main'] = j['weather'][0]['main']
        self.dict['description'] = j['weather'][0]['description']
        self.dict['humidity'] = j['main']['humidity']
        self.dict['pressure'] = j['main']['pressure']
        self.dict['wind'] = j['wind']['speed']
        self.lon = j['coord']['lon']
        self.lat = j['coord']['lat']
        #self.dtime = j

    def __str__(self):
        return 'Informations météorologiques de la ville de Londre : {}'.format(self.dict)


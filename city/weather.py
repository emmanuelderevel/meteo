import requests


class Weather():
    def __init__(self, city_id):
        self.dict = {}
        self.city_id=city_id
        self.lon=''
        self.lat=''

    def retrieveWeathInfo(self):
        html = 'http://api.openweathermap.org/data/2.5/weather?' \
               'id={}&units=metric&APPID=955716c6c3b27005023580d9021147ba'.format(self.city_id)
        client = requests.get(html)
        j = client.json()
        self.dict['temp'] = j['main']['temp']
        self.dict['temp_max'] = j['main']['temp_max']
        self.dict['temp_min'] = j['main']['temp_min']
        self.dict['main'] = j['weather'][0]['main']
        self.dict['icon'] = j['weather'][0]['icon']
        self.dict['description'] = j['weather'][0]['description']
        self.dict['humidity'] = j['main']['humidity']
        self.dict['pressure'] = j['main']['pressure']
        self.dict['wind'] = j['wind']['speed']
        self.dict['city'] = j['name']
        self.dict['lon'] = j['coord']['lon']
        self.dict['lat'] = j['coord']['lat']

    def __str__(self):
        return 'Informations météorologiques de la ville de Londre : {}'.format(self.dict)


if __name__ == '__main__':
    p=Weather(4180439)
    p.retrieveWeathInfo()
    print(p.dict)
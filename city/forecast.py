import requests

class Forecast:
    def __init__(self, city_id):
        self.city_id=city_id
        #self.day={}
        self.day_1 = {}
        self.day_2 = {}
        self.day_3 = {}
        self.day_4 = {}




    def retrieve_forecast(self):
        r = requests.get('http://api.openweathermap.org/data/2.5/'
                         'forecast?id={}&units=metric&APPID=955716c6c3b27005023580d9021147ba'.format(self.city_id))
        j = r.json()
        print(j)
        l=j['list']
        print(l)
        dt=l[len(l)-1]['dt_txt'][11:]
        print(dt)
        while dt!='21:00:00':
            del l[-1]
            dt = l[len(l) - 1]['dt_txt'][11:]
            print(dt)
        self.day_4 = l[-8:]
        l=l[:-8]
        self.day_3 = l[-8:]
        l=l[:-8]
        self.day_2 = l[-8:]
        l=l[:-8]
        self.day_1 = l[-8:]



if __name__=='__main__':
    f1=Forecast(2362344)
    f1.retrieve_forecast()
    print(f1.day_4)
    print(f1.day_3)
    print(f1.day_2)
    print(f1.day_1)


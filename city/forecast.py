import requests
from _datetime import datetime
import datetime as dtime

class Forecast:
    def __init__(self, city_id):
        self.city_id=city_id
        self.days = list()
        self.dt = list()
        self.list = list()




    def retrieve_forecast(self):
        r = requests.get('http://api.openweathermap.org/data/2.5/'
                         'forecast?id={}&units=metric&APPID=8bb2f275ae9f1d35a616a1454f5dc8c5'.format(self.city_id))
        j = r.json()
        print(j)
        l=j['list']
        print(len(l))

        dt0 = str(datetime.strptime(l[0]['dt_txt'][:10],'%Y-%m-%d'))[:10]
        dt1 = str(datetime.strptime(l[0]['dt_txt'][:10],'%Y-%m-%d') + dtime.timedelta(1))[:10]
        print(dt1)
        dt2 = str(datetime.strptime(l[0]['dt_txt'][:10], '%Y-%m-%d') + dtime.timedelta(2))[:10]
        dt3 = str(datetime.strptime(l[0]['dt_txt'][:10], '%Y-%m-%d') + dtime.timedelta(3))[:10]
        dt4 = str(datetime.strptime(l[0]['dt_txt'][:10], '%Y-%m-%d') + dtime.timedelta(4))[:10]
        print(dt4)
        self.dt = [dt1,dt2,dt3,dt4,dt0]

        day1=[]
        for i in range(len(l)):
            if l[i]['dt_txt'][:10]==dt1:
                print(l[i]['dt_txt'][:10])
                day1 += [l[i]]
        day2=[]
        for i in range(len(l)):
            if l[i]['dt_txt'][:10]==dt2:
                print(l[i]['dt_txt'][:10])
                day2 += [l[i]]
        day3=[]
        for i in range(len(l)):
            if l[i]['dt_txt'][:10]==dt3:
                print(l[i]['dt_txt'][:10])
                day3 +=[l[i]]
        day4=[]
        for i in range(len(l)):
            if l[i]['dt_txt'][:10]==dt4:
                print(l[i]['dt_txt'][:10])
                day4 +=[l[i]]

        self.days=[day1,day2,day3,day4]

        for i in range(len(self.days)):

            temp_max = self.days[i][0]['main']['temp_max']
            temp_min = self.days[i][0]['main']['temp_min']
            for j in range(len(self.days[i])):
                if self.days[i][j]['main']['temp_max'] >= temp_max:
                    temp_max = self.days[i][j]['main']['temp_max']
            for j in range(len(self.days[i])):
                if self.days[i][j]['main']['temp_min'] <= temp_min:
                    temp_min = self.days[i][j]['main']['temp_min']
            wind = 0
            for j in range(len(self.days[i])):
                wind+=self.days[i][j]['wind']['speed']
            pressure = 0
            for j in range(len(self.days[i])):
                pressure += self.days[i][j]['main']['pressure']

            self.list += [[temp_max,temp_min,round(wind / len(self.days[i]),2),round(pressure / len(self.days[i]),2),self.days[i][len(self.days[i])//2]['weather'][0]['icon'],self.days[i][len(self.days[i])//2]['weather'][0]['description']]]




if __name__=='__main__':
    f1=Forecast(6455259)
    f1.retrieve_forecast()
    print(f1.days)
    print(f1.list)


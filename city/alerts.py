import requests
import datetime

def find_rain():
        city_id=2988507
        r = requests.get('http://api.openweathermap.org/data/2.5/'
                         'forecast?id={}&units=metric&APPID=955716c6c3b27005023580d9021147ba'.format(city_id))
        j = r.json()
        l=j['list']
        rain_list=[]
        for i in range(0, len(l)):
            try:
                if l[i]['rain']!={}:
                    day1=datetime.datetime.strptime(l[i]['dt_txt'], "%Y-%m-%d %H:%M:%S")
                    day2=day1.strftime("%A %H:%M")
                    rain_list=rain_list+[[day2, l[i]['rain']['3h']]]
            except KeyError:
                pass
        alerts1=""
        for j in rain_list:
            alerts1=alerts1 + "{0} : {1}mm".format(j[0], j[1]) + ", "
            alerts2=alerts1[0:-1]
        print(rain_list)
        print(alerts2)

# if l[i]['rain']!={}:
#     print(l[i]['dt_txt'])
#     print(l[i]['rain']['3h'])

find_rain()

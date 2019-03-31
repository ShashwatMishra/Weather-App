import Model_weather,json

class Logic(object):

    def __init__(self,city_name):
        self.city_name = city_name


    def getJson(self):
        weather = Model_weather.Model()
        data = weather.requestSetup(self.city_name)
        return self.dataFormatting(data)

    def dataFormatting(self,data):
        flag = True
        if data['cod'] == 200 :
            info =dict()
            info['name'] = data['name']
            info['country'] = data['sys']['country']
            info['temp'] = data['main']['temp']
            info['humidity'] = data['main']['humidity']
            info['temp_min'] = data['main']['temp_min']
            info['temp_max'] = data['main']['temp_max']
            info['weather'] = data['weather'][0]['description']
            info['lat'] = data['coord']['lat']
            info['lon'] = data['coord']['lon']
            info['pressure'] = data['main']['pressure']
            info['sunrise'] = data['sys']['sunrise']
            info['sunset'] = data['sys']['sunset']
            return flag, info
        else:
            flag = False
            info = {
                     "cod": "404",
                     "message": "city not found"
                   }
            return flag,info
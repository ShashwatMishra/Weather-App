import requests,json

url = 'http://api.openweathermap.org/data/2.5/weather?'
class Model(object):

    def __init__(self):
        self.api_key = '280181c2614d065125d9b884fb43eedb'

    def requestSetup(self,cityName):

        global url
        request_url = url + 'appid=' + self.api_key + '&q=' + cityName + '&units=metric'
        response = requests.request(url = request_url,method='GET')
        return response.json()

obj = Model()
res = obj.requestSetup('Patna')
print((json.dumps(res,indent = 4)))
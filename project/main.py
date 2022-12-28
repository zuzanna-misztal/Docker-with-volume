from bs4 import BeautifulSoup

with open('config.xml', 'r') as config:
    data = config.read()

bs_data = BeautifulSoup(data, "xml")
is_weather_good = bs_data.find('isWeatherGoodToday')
if is_weather_good.text == "True":
    print('The weather is good today')
else:
    print('The weather is bad today')

#  To build image in terminal inside dockerhome1 folder run "docker image build -t weather ."
#  Run "docker run -v ${pwd}\config\config.xml:/app/config.xml weather"
#  Is the weather good today? :)

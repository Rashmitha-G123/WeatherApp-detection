from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        try:
            res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=11077678a65409e0639201f8f763060e').read()
            json_data = json.loads(res)
            data = {
                "country_code": str(json_data['sys']['country']),
                "coordinate": str(json_data['coord']['lon']) + ', ' + str(json_data['coord']['lat']),
                "temp": str(json_data['main']['temp']) + 'K',
                "pressure": str(json_data['main']['pressure']),
                "humidity": str(json_data['main']['humidity']),
            }
        except urllib.error.HTTPError:
            error = "Unrecognized input. Search valid places"
            return render(request, 'index.html', {'error': error})


    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})
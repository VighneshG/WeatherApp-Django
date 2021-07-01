from django.shortcuts import render
import requests
from requests.api import post
from django.http import HttpResponse

# Create your views here.


def home(request):
    import json
    import requests

    if request.method == "POST":
        city = request.POST['City']
        api_request = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=9e1e111f0076dcac28fe3a3149a5e5b6&units=metric")

        api = json.loads(api_request.content)

        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'default.html')


def icon(request):
    return render(request, 'icon.html', {})

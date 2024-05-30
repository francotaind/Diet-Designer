from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.conf import settings
import json
import requests

# Create your views here.
def recipe(request):
    api_key = settings.API_NINJAS_API_KEY
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/recipe?query='
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': api_key})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'recipe.html', {'api': api})
    else:
        return render(request, 'recipe.html', {'query': 'Enter a valid query'})


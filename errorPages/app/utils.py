import requests
from django.conf import settings
SEARCH_API_KEY=getattr(settings,'SEARCH_API_KEY','')
SEARCH_API_ID=getattr(settings,'SEARCH_API_ID','')

def google_search(query):
    url="https://www.googleapis.com/customsearch/v1"
    params={   #Necesario para buscar
        "q":query,
        "key":SEARCH_API_KEY,
        "cx":SEARCH_API_ID
    }
    response =requests.get(url,params=params)
    print(response.json())
    return response.json()
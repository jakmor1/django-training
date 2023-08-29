import requests

from django.shortcuts import render

SOURCES = [
    {'id': 'new-scientist', 'name': 'The New Scientist'},
    {'id': 'techradar', 'name': 'TechRadar'},
    {'id': 'national-geographic', 'name': 'National Geographic'},
    {'id': 'ars-technica', 'name': 'Ars Technica'},
    {'id': 'mashable', 'name': 'Mashable'},
    {'id': 'the-next-web', 'name': 'The Next Web'},
]

def index_view(request, source="new-scientist"):
    API_KEY = '5d6ed3545a734b53bb70ce1361ae80f3'
    url = ('https://newsapi.org/v2/everything?'
           f'sources={source}&'
           f'apiKey={API_KEY}')
    response = requests.get(url)
    data = response.json()
    context = {'newsapi': data, 'sources': SOURCES, 'active_source': source}
    return render(request, 'news/index.html', context)
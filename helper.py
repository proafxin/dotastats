from json import loads
from requests import get
from pandas import DataFrame

with open('key.json') as _f:
    API_KEY = loads(_f.read())['api_key']

def form_url(url):
    if not url.endswith('?api_key={}'):
        url = url+'?api_key={}'
    url = url.format(API_KEY)

    return url

def get_data(url):
    url = form_url(url)
    response = get(url)
    content = response.content.decode()
    data = loads(content)
    
    return DataFrame(data)
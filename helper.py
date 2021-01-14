from json import loads

with open('key.json') as _f:
    API_KEY = loads(_f.read())['api_key']

def form_url(url):
    if not url.endswith('?api_key={}'):
        url = url+'?api_key={}'
    url = url.format(API_KEY)

    return url
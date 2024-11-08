import requests as rec
import pprint

par = {
    'q' : 'html'
}

res = rec.get('https://api.github.com')
print(res.status_code)
pprint.pprint(res.json())
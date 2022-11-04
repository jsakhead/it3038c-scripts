import json
import requests

r = requests.get('http://localhost:3000/')
data=r.json()
wid1name = (data[0]['name'])
wid1color = (data[0]['color'])
wid2name = (data[1]['name'])
wid2color = (data[1]['color'])
wid3name = (data[2]['name'])
wid3color = (data[2]['color'])

print(wid1name, "is", wid1color)

print(wid2name, "is", wid2color)

print(wid3name, "is", wid3color)

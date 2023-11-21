#import requests

#r = requests.get('https://api/github.com/events')
#print(r.encoding)

#for line in r.iter_lines():
#    print(line)

from jikanpy import Jikan
jikan = Jikan()

anime = Jikan.anime(52991, extension='episodes')
for episode in anime['data']:
    print(anime)
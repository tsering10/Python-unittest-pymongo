from Scrapping import *
from pymongo import MongoClient
import re

from MongoDB import *

client = MongoClient('localhost', 27017)
db = client.unittest_pymongo



actors = {}

for films in db.films.find():
    for act in films.get('actors'):

        actor = re.sub('ˆ\s+','',act)
        actor = re.sub('\n$','',actor)


        if actor not in actors:

            actors[actor] = []
            actors[actor].append(films.get('title'))


for x, y in actors.items():
    a = Actor(x)
    a.add_film(y)
    a.load(db)


client.close()

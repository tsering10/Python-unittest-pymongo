from Scrapping import *
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.unittest_pymongo

film_list = FilmList(2018)

for film_id in film_list.get_films_ids():
  film = Film(film_id)
  film.scrap()
  film.load(db)




client.close()

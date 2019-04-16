import unittest
from pymongo import MongoClient

from MongoDB import Film, Actor

class TestFilmMethods(unittest.TestCase):

    def test_get_nb_films(self):
        self.assertEqual(Film.get_nb_films(db), 450)
    def test_get_actor(self):
        film = Film('tt6674514')
        actors_list = film.get_actors(db)
        self.assertEqual(':'.join(actors_list),' Kangaroo Dundee\n: Terri Irwin\n: Phil Wollen\n: Tim Flannery\n: Peter Singer\n')



class TestActorMethods(unittest.TestCase):

        def test_constructor(self):
            actor = Actor('Javier Botet')
            self.assertIsInstance(actor, Actor)
            self.assertEqual(actor.name, "Javier Botet")
            self.assertIsInstance(actor.films, list)
            self.assertEqual(len(actor.films), 0)


        def test_add_film(self):

            actor = Actor('Tashi Tsering')
            actor.add_film('Seven Years in Tibet')
            self.assertEqual(len(actor.films), 1)
            self.assertEqual(actor.films[0], 'Seven Years in Tibet')
            actor.add_film('Life is beautiful')
            self.assertEqual(len(actor.films), 2)
            self.assertEqual(actor.films[0], 'Seven Years in Tibet')
            self.assertEqual(actor.films[1], 'Life is beautiful')


        def test_load(self):

            actor = Actor("Tashi Tsering")
            actor.add_film("Seven Years in Tibet")
            actor.add_film('Life is beautiful')

            actor.load(db)
            actor_document = db.actors.find_one({'name': 'Tashi Tsering'})
            self.assertIsNotNone(actor_document)
            self.assertEqual(actor_document.get('name'), "Tashi Tsering")
            self.assertEqual(actor_document.get('films'), ['Seven Years in Tibet', 'Life is beautiful'])
            db.actors.delete_many({'name': 'Tashi Tsering'})










if __name__ == '__main__':
    client = MongoClient('localhost', 27017)
    db = client.unittest_pymongo

    unittest.main()

    client.close()

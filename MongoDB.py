class Film:

  def __init__(self, id):
    self.id = id

  def get_nb_films(db):
    # retourne le nombre de films présents dans la base

   



    return db.films.count()


  def get_actors(self,db):
    # retourne la liste des acteurs du film
    

    film_document = db.films.find_one({'imdb_id': self.id})

    return film_document['actors']

class Actor:

  def __init__(self, name):
    self.name = name
    self.films = []

  def add_film(self, film):


    self.films.append(film)




  def load(self,db):
    # ajoute l'acteur dans la base de données

      actor_coll = db.actors

      actor_dict = {"name":self.name, "films":self.films}

      actor_coll.insert_one(actor_dict)





  def get_nb_actors(db):
    # retourne le nombre d'acteurs présents dans la base
      liste = []

      for x in db.films.find({},{"_id":0,"actors":1}):

         if x not in liste:
           liste.append(x)




      return  len(liste)
    


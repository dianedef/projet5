import os
import requests
import logging

from os.path import join, dirname
from config import URL, PAGE
from databaseconnexion import *

class DataGetter:

   def __init__(self):
      """This function """

      # dotenv.load()
      self.page = PAGE
      self.url = URL
      os.getenv("host")
      os.getenv("auth")

   def get_data(self, url, nb_pages):
      """ This function searches the OpenFoodFacts api for 10 pages in some category"""

      self.data = []
      for page in range(nb_pages):
         params = {
            "action": "process",
            "sort_by": "unique_scans_n",
            "page_size": 20,
            "page": page+1,
            "json": True
            }
         response = requests.get(url, params)
         if response.status_code == 200:
            data = response.json()
            print(response.status_code, ": Response Ok ", data)
      return(data)

class DataCleaner:

   def __init__(self):
      """ This function cleans data """
      self.data = data

   def clean_data(self, data):
      data = self.data
      if product.param = "code", "generic_name", "nutrition_grade_fr", "purchase_places", "stores", "categories", "url", "product_name":
         keep
      else:
         trash
      data.lower()


class Interface:

   def __init__(self):
      """ This function interacts with users. """

   def launchProgram(self):
      input("1. Quel aliment souhaitez-vous remplacer? Sélectionnez le chiffre correspondant et appuyez sur Entrée:")
         # if 1 = montrer produit 1 et un substitu, la description, un magasin ou l'acheter (le cas échéant) et un lien vers la page d'OFF
      question = input("Voulez-vous enregistrer ce produit dans vos favoris ? Oui ou Non")
      if question="Oui":
         #favorites.append(product)
      else:
         pass

   def favoritesProduct(self):
      input("Voulez-vous retrouver vos aliments substitués ?")
      else:
         print("désolée y'a rien")

class Product:

   def __init__(self, code, name, store, url, category):
      pass

   def save_to_db(self):
      cursor.execute(
         """CREATE TABLE IF NOT EXISTS categoy (
            id int primary key auto_increment,
            name varchar(150) not null unique
         )
         """
      cnx.close()
      # créer la bdd
      # 1 table pdt, cat, magasins
      # enregistrer ces données dans des tables mysql et les lier avec des clefs étrangères ou table d'associaion

class Category:

   def __init__(self)

class Store:
    def chercher_ptoduit()
 #proposer des pdt plus sains


def main():
   """ This function runs the program."""

   test = DataGetter()
   test.get_data("https://fr.openfoodfacts.org/cgi/search.pl", 1)

if __name__ == "__main__":
   main()
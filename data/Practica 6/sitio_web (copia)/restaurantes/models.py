from pymongo import MongoClient

client = MongoClient()
db = client.test                  # base de datos
restaurantes = db.restaurants     # colección
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://aparnaojha03:admin@fastapimongo.qn1hm.mongodb.net/?retryWrites=true&w=majority&appName=FastApiMongo"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.notes_db
collection = db["notes_data"]

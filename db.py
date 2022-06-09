from flask_pymongo import pymongo

CONNECTION_STRING = "mongodb+srv://mohammad:4WJKBwbabMclfxS8@cluster0.hly0n.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('Books')
# Example Python Code to Insert a Document
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to access the MongoDB
        # databases and collections. 
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'aacuser123'
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d/?authSource=admin' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    def create(self, data):
        # Insert a document into the animals collection
        # Returns True if successful, False otherwise
        if data is not None:
            result = self.database.animals.insert_one(data)
            return True if result.acknowledged else False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, query):
        # Query documents from the animals collection
        # Returns a list of results, or empty list if query is None
        if query is not None:
            cursor = self.database.animals.find(query)
            return list(cursor)
        else:
            return []
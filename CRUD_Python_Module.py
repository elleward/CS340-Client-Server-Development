# Example Python Code to Insert a Document
from pymongo import MongoClient
from bson.objectid import ObjectId

 #CRUD operations for Animal collection in MongoDB
class AnimalShelter(object):

    # Initializing the MongoClient. This helps to access the MongoDB databases and collections. 
    def __init__(self, username, password):
        
        # Connection Variables
        USER = 'aacuser'
        PASS = 'aacuser123'
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'
        
        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d/?authSource=admin' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
    
    
    ########### CRUD METHODS
    
    # Insert a document into the animals collection
    # Returns True if successful, False otherwise
    def create(self, data):
        if data is not None:
            result = self.database.animals.insert_one(data)
            return True if result.acknowledged else False
        else:
            raise Exception("Nothing to save, because data parameter is empty")


    # Query documents from the animals collection
    # Returns a list of results, or empty list if query is None
    def read(self, query):
        if query is not None:
            cursor = self.database.animals.find(query)
            return list(cursor)
        else:
            return []
    
    # Update documents in the collection
    def update(self, query, update_data):
        if query is not None and update_data is not None:
            result = self.database.animals.update_many(query, {"$set": update_data})
            return result.modified_count
        else:
            raise Exception("Query or update data is empty")

     # Delete documents from the collection
    def delete(self, query):
        if query is not None:
            result = self.database.animals.delete_many(query)
            return result.deleted_count
        else:
            raise Exception("Nothing to delete, query parameter is empty")
    
    
    ###### Methods to return specific queries for each rescue type
    
    # Filter for Water Rescue dogs
    def filter_water_rescue(self):
        return {
            "animal_type": "Dog",
            "breed": {
                "$in": [
                    "Labrador Retriever Mix",
                    "Chesapeake Bay Retriever",
                    "Newfoundland"
                ]
            },
            "sex_upon_outcome": "Intact Female",
            "age_upon_outcome_in_weeks": {
                "$gte": 26,
                "$lte": 156
            }
        }
    
    
    # Filter for Mountain or Wilderness Rescue dogs
    def filter_mountain_wilderness_rescue(self):
        return {
            "animal_type": "Dog",
            "breed": {
                "$in": [
                    "German Shepherd",
                    "Alaskan Malamute",
                    "Old English Sheepdog",
                    "Siberian Husky",
                    "Rottweiler"
                ]
            },
            "sex_upon_outcome": "Intact Male",
            "age_upon_outcome_in_weeks": {
                "$gte": 26,
                "$lte": 156
            }
        }
    
    
    # Filter for Disaster or Individual Tracking dogs
    def filter_disaster_tracking(self):
        return {
            "animal_type": "Dog",
            "breed": {
                "$in": [
                    "Doberman Pinscher",
                    "German Shepherd",
                    "Golden Retriever",
                    "Bloodhound",
                    "Rottweiler"
                ]
            },
            "sex_upon_outcome": "Intact Male",
            "age_upon_outcome_in_weeks": {
                "$gte": 20,
                "$lte": 300
            }
        }
    
    # Reset filter - returns all dogs
    def filter_reset(self):
        return {"animal_type": "Dog"}

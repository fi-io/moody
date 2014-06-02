'''
Created on 02-Jun-2014

@author: brij
'''
from pymongo import MongoClient

# Mongo DB settings
db_client = MongoClient()
moody_db = db_client.moody
answer_collection = moody_db.answers

def getAnswerID(ansText):
    aCursor = answer_collection.find_one({'text': ansText})
    aID = ''
    if aCursor:
        aID = str(aCursor['_id'])
    else:
        aID = str(answer_collection.insert({'text': ansText}))
        
    return aID
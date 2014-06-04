'''
Created on 02-Jun-2014

@author: brij
'''
from pymongo import MongoClient

'''
There are three collections in databse 'moody'
- questions - stores all questions as -----> |_id|text|
- answers - stores all answers as -----> |_id|text|
- qarelation - stores all question-answer relation as -----> |_id|qid|aid|
'''

# Mongo DB settings
db_client = MongoClient()
moody_db = db_client.moody
answer_collection = moody_db.answers
question_collection = moody_db.questions
qarelation_collection = moody_db.qarelation

def getAnswerID(ansText):
    aCursor = answer_collection.find_one({'text': ansText})
    aID = ''
    if aCursor:
        aID = str(aCursor['_id'])
    else:
        aID = str(answer_collection.save({'text': ansText}))
        
    return aID

def saveQARelation(quesText, ansId):
    qCursor = question_collection.find_one({'text': quesText})
    qID = ''
    if qCursor:
        qID = str(qCursor['_id'])
    else:
        qID = str(question_collection.save({'text': quesText}))
    
    qaCursor = qarelation_collection.find_one({'qid': qID, 'aid': ansId})
    if not qaCursor:
        qarelation_collection.save({'qid': qID, 'aid': ansId})
        
        
        
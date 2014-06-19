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

- seanswers - stores all stack-exchange answers as -----> |_id|aid|body|
- sequestions - stores all stack-exchange questions as -----> |_id|qid|body|title|aid
'''

# Mongo DB settings
db_client = MongoClient()
moody_db = db_client.moody
answer_collection = moody_db.answers
question_collection = moody_db.questions
qarelation_collection = moody_db.qarelation

# Collections for StackExchange QA
seanswers_collection = moody_db.seanswers
sequestions_collection = moody_db.sequestions

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
        
def saveSEQuestion(qid, body, title, aid):
    sequestions_collection.save({'qid': qid, 'body': body, 'title': title, 'aid': aid})
 
def saveSEAnswer(aid, body):
    seanswers_collection.save({'aid': aid, 'body': body})
    
def readSEQAData():
    for ques in sequestions_collection.find(timeout=False).batch_size(1000):
        aid = ques['aid']
        ac = seanswers_collection.find_one({'aid': aid})
        if ac:
            yield (ques['title'], ques['body'], ac['body'])
        
        
#readSEQAData()
        
'''
Created on 04-Jun-2014

@author: brij
'''
from collections import Counter
from com.moody.utils import MongoUtil
from com.moody.utils.NLPUtil import stemmer
from com.moody.utils.NLPUtil import STOP_WORDS
from com.moody.utils import TextUtil
from com.moody.utils import FileUtil

'''
This script is written to parse NIST QA data and compose an inverted index.
symbols:
    p - title (70%)
    q - question (25%)
    r - answer (5%)
'''

VOCAB_DICT = {}  # Dictionary to hold word#ansID-p:p_score&q:q_score&r:r_score values
VOCAB_DICT_LIMIT = 50000
OUTPUT_DIR = '/home/brij/Documents/moody/index/jeopardy/'
qaFilePath = '/home/brij/Documents/moody/datasets/jeopardy_data.json'
TEMP_FILE_PREFIX = 'moody.jeopardy.tempindex.'
TEMP_FILE_COUNTER = 0

# Function to categorize the word into proper place and priority
def addToVocab(word, answer_id, priority_type, priority_val):
    global TEMP_FILE_COUNTER
    if len(VOCAB_DICT) >= VOCAB_DICT_LIMIT:
        # create a temporary index file
        outfilePath = OUTPUT_DIR + TEMP_FILE_PREFIX + str(TEMP_FILE_COUNTER)
        FileUtil.writeToFile(VOCAB_DICT, outfilePath)
        TEMP_FILE_COUNTER = TEMP_FILE_COUNTER + 1
        VOCAB_DICT.clear()
    
    if word in VOCAB_DICT:
        answers = VOCAB_DICT[word]
        if answer_id in answers:
            prts = answers[answer_id]
            if priority_type in prts:
                prts[priority_type] = prts[priority_type] + priority_val
            else:
                prts[priority_type] = priority_val
        else:
            answers[answer_id] = {priority_type: priority_val}
    else:
        VOCAB_DICT[word] = {answer_id: {priority_type: priority_val}}
        
def processText(text, priority):
    tFreq = Counter([stemmer.stem(kw) for kw in TextUtil.cleanUpText(text).split()])
    for tWord in tFreq:
        if tWord not in STOP_WORDS and len(tWord) > 2:
            addToVocab(tWord, ans_id, priority, tFreq[tWord])
        

linecount = 0
for (title, ques, ans) in FileUtil.readJeopardyQAData(qaFilePath):
    ans_id = MongoUtil.getAnswerID(ans)
    MongoUtil.saveQARelation(ques, ans_id)
    
    # Work on title
    processText(title, 'p')
            
    # Work on ques
    processText(ques, 'q')
    
    # Work on ans
    processText(ans, 'r')
        
    linecount = linecount + 1
    if linecount % 100 == 0:
        print "Read %d QA files..." % linecount
            
# Write to file if its still left
if len(VOCAB_DICT) > 0:
    # create a temporary index file
    outfilePath = OUTPUT_DIR + TEMP_FILE_PREFIX + str(TEMP_FILE_COUNTER)
    FileUtil.writeToFile(VOCAB_DICT, outfilePath)
    VOCAB_DICT.clear()
    
print 'Done!'
            
    
'''
Created on 15-Jun-2014

@author: brij
'''
from collections import Counter
from com.moody.utils import MongoUtil
from com.moody.utils.NLPUtil import stemmer
from com.moody.utils.NLPUtil import STOP_WORDS
from com.moody.utils import TextUtil
from com.moody.utils import FileUtil
import time

'''
This script is written to parse NIST QA data and compose an inverted index.
symbols:
    p - title (70%)
    q - question (25%)
    r - answer (5%)
'''

VOCAB_DICT = {}  # Dictionary to hold word#ansID-p:p_score&q:q_score&r:r_score values
VOCAB_DICT_LIMIT = 50000
OUTPUT_DIR = '/home/brij/Documents/moody/index/stackexchange/'
TEMP_FILE_PREFIX = 'moody.stackexchange.tempindex.'
TEMP_FILE_COUNTER = 0
SE_ANSID_PREFIX = 'seans.'
SE_ANSID_COUNTER = 0
SE_ANSID_FILE = 'se_ansid_index'

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
start_t = time.time()
tot_t = time.time()
ansid_file = open(OUTPUT_DIR + SE_ANSID_FILE,  'w')
print 'Started SE data parsing...'
for (title, ques, ans) in MongoUtil.readSEQAData():
    ans_id = SE_ANSID_PREFIX + str(SE_ANSID_COUNTER)    #MongoUtil.getAnswerID(ans)
    SE_ANSID_COUNTER += 1
    #MongoUtil.saveQARelation(ques, ans_id)
    ansid_file.write((ans_id + '\t' + ques + '\t' + ans + '\n').encode('utf-8'))
    
    # Work on title
    processText(title, 'p')
    
    # Work on ques
    processText(ques, 'q')

    # Work on ans
    processText(ans, 'r')
        
    linecount = linecount + 1
    if linecount % 1000 == 0:
        print "time taken to read %d : " % linecount, time.time() - start_t
        start_t = time.time()
            
# Write to file if its still left
if len(VOCAB_DICT) > 0:
    # create a temporary index file
    outfilePath = OUTPUT_DIR + TEMP_FILE_PREFIX + str(TEMP_FILE_COUNTER)
    FileUtil.writeToFile(VOCAB_DICT, outfilePath)
    VOCAB_DICT.clear()
    
ansid_file.close()
print "Total time : ", time.time() - tot_t
print 'Done!'
            
    
'''
Created on 02-Jun-2014

@author: brij
'''
from com.moody.utils import TextUtil

def writeToFile(vocabDict, filepath):
    # function to write vocabulary to file
    tempFile = open(filepath, 'w')
    
    for word in vocabDict:
        line = word + '#'
        docs = vocabDict[word]
        for doc in docs:
            line = line + doc + '-' + '&'.join("%s:%s" % (key, val) for (key, val) in docs[doc].iteritems()) + ';'
        tempFile.write(line + '\n')
    tempFile.close()
    
def readCMUQAData(filepath):
    qaFile = open(filepath)
    for line in qaFile:
        if line.strip() != '':
            line_sp = line.split('\t')
            # Check if line is permissible
            if TextUtil.isValidValue(line_sp[0]) and TextUtil.isValidValue(line_sp[1]) and TextUtil.isValidValue(line_sp[2]):
                yield (' '.join(line_sp[0].split('_')), line_sp[1], unicode(line_sp[2], "utf-8"))
                
                
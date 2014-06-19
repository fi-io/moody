'''
Created on 02-Jun-2014

@author: brij
'''
from com.moody.utils import TextUtil
from os import listdir
from os.path import isfile, join, splitext, basename
import xml.etree.ElementTree as ET
import json
from subprocess import call

def writeToFile(vocabDict, filepath):
    # function to write vocabulary to file
    print "writing to file : %s" % filepath
    tempFile = open(filepath, 'w')
    
    for word in vocabDict:
        line = word + '#'
        docs = vocabDict[word]
        for doc in docs:
            line = line + doc + '-' + '&'.join("%s:%s" % (key, val) for (key, val) in docs[doc].iteritems()) + ';'
        tempFile.write(line + '\n')
    tempFile.close()
    
# Funstion to read the qa files of CMU and producing (title, ques, ans) tuples
def readCMUQAData(filepath):
    qaFile = open(filepath)
    for line in qaFile:
        if line.strip() != '':
            line_sp = line.split('\t')
            # Check if line is permissible
            if TextUtil.isValidValue(line_sp[0]) and TextUtil.isValidValue(line_sp[1]) and TextUtil.isValidValue(line_sp[2]):
                yield (' '.join(line_sp[0].split('_')), unicode(line_sp[1], "utf-8"), unicode(line_sp[2], "utf-8"))

# Funstion to read the qa files of NIST xml and producing (title, ques, ans) tuples from all files of directory               
def readNistQAData(filesDir):
    allfiles = [ f for f in listdir(filesDir) if isfile(join(filesDir, f)) ]
    for filename in allfiles:
        tree = ET.parse(join(filesDir, filename))
        root = tree.getroot()
        ans_count = int(root[0][9].text)
        if ans_count > 0:
            subj = root[0][0].text
            ques = root[0][1].text
            ans = root[0][11].text
            # print filename, ans
            if not TextUtil.isValidValue(ans) and root[0][16].__len__() > 0:
                ans = root[0][16][0][0].text
            if TextUtil.isValidValue(subj) and TextUtil.isValidValue(ques) and TextUtil.isValidValue(ans):
                yield (subj, ques, ans)
                
def readJeopardyQAData(jsonFilePath):
    jsonFile = open(jsonFilePath)
    json_str = ''
    for line in jsonFile:
        json_str = json_str + line
    json_val = json.loads(json_str)
    for jObj in json_val:
        yield (jObj['category'], jObj['question'][1:-1], jObj['answer'])

def extractPostsXml(compressedFile, outputFile):
    call('7z x -o' + outputFile + ' ' + compressedFile + ' -y', shell=True)

def getSO7zFiles(filesdir):
    allfiles = [ join(filesdir, f) for f in listdir(filesdir) if isfile(join(filesdir, f)) and f.endswith('7z') ]
    return allfiles

def getFilenameWithoutExt(fullpath):
    return splitext(basename(fullpath))[0]

# getSO7zFiles("/home/brij/Documents/moody/datasets/stackexchange_data/")
# extractPostsXml("/home/brij/Documents/moody/datasets/stackexchange_data/academia.stackexchange.com.7z", "/home/brij/Documents/moody/index/stackexchange/out.xml")    
    
    
    

'''
Created on 02-Jun-2014

@author: brij
'''
import re

NP_WORDS = ['NULL', '', 'Question', 'Answer']  # Non-Permissible words
ALPHABETS_REGEX = re.compile('[^a-zA-Z ]')

def isValidValue(text):
    return (text.strip() not in NP_WORDS)

def cleanUpText(text):
    ctext = ALPHABETS_REGEX.sub('', text)  # keep only alphabets and white spaces
    ctext = ' '.join(ctext.split())  # combine multiple white spaces
    ctext = ctext.lower()  # lower case the text
    return ctext
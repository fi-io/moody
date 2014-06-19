'''
Created on 02-Jun-2014

@author: brij
'''
import re
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    t = ' '.join(s.get_data().split())
    return t.strip()
NP_WORDS = ['NULL', '', 'Question', 'Answer']  # Non-Permissible words
ALPHABETS_REGEX = re.compile('[^a-zA-Z0-9 ]')

def isValidValue(text):
    return (text and text.strip() not in NP_WORDS)

def cleanUpText(text):
    ctext = text.replace("'s", '')
    ctext = ALPHABETS_REGEX.sub('', ctext)  # keep only alphabets and white spaces
    ctext = ' '.join(ctext.split())  # combine multiple white spaces
    ctext = ctext.lower()  # lower case the text
    return ctext

#print strip_tags("<p> hello <br/> what's up </p> <h3></h3>")


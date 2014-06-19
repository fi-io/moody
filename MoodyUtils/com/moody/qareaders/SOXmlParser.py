'''
Created on 15-Jun-2014

@author: brij
'''
import xml.sax
from com.moody.utils import FileUtil, MongoUtil, TextUtil

OUTPUT_FOLDER = '/home/brij/Documents/moody/index/stackexchange/'
OUTPUT_XML = OUTPUT_FOLDER + 'Posts.xml'

class SEPostXmlHandler(xml.sax.ContentHandler):
    
    def __init__(self, id_prefix):
        self.id_prefix = id_prefix
    
    def startElement(self, name, attrs):
        if name == 'row':
            try:
                if attrs['PostTypeId'] == '1' and 'AcceptedAnswerId' in attrs:
                    # Handle questions
                    qid = self.id_prefix + '.' + attrs['Id']
                    body = TextUtil.strip_tags(attrs['Body'])
                    title = attrs['Title']
                    aid = self.id_prefix + '.' + attrs['AcceptedAnswerId']
                    MongoUtil.saveSEQuestion(qid, body, title, aid)
                else:
                    # Handle answers
                    aid = self.id_prefix + '.' + attrs['Id']
                    body = TextUtil.strip_tags(attrs['Body'])
                    MongoUtil.saveSEAnswer(aid, body)
            except:
                pass
                
parser = xml.sax.make_parser()
for cfile in ['/home/brij/Documents/moody/datasets/stackexchange_data/stackoverflow/stackoverflow.com-Posts.7z']: #FileUtil.getSO7zFiles("/home/brij/Documents/moody/datasets/stackexchange_data/"):
    fname = FileUtil.getFilenameWithoutExt(cfile)
    print "Extracting %s ..." % fname
    FileUtil.extractPostsXml(cfile, OUTPUT_FOLDER)
    print "Parsing %s ..." % fname
    parser.setContentHandler(SEPostXmlHandler(fname))
    parser.parse(open(OUTPUT_XML, 'r'))
    print "Done parsing %s ..." % fname
    
    
    
    
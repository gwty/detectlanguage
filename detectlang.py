# -*- coding: utf-8 -*-
## Usage ##
import sys, locale
import unicodedata
import re
import os


def _makeNonAlphaRe():
    nonAlpha = [u'[^']
    for i in range(sys.maxunicode):
      c = unichr(i)
      if c.isalpha(): nonAlpha.append(c)
    nonAlpha.append(u']')
    nonAlpha = u"".join(nonAlpha)
    return re.compile(nonAlpha)


nonAlphaRe = _makeNonAlphaRe()
spaceRe = re.compile('\s+', re.UNICODE)


def normalize(u):
    ''' Convert to normalized unicode.
        Remove non-alpha chars and compress runs of spaces.
    '''
    u = unicodedata.normalize('NFC', u)
    u = nonAlphaRe.sub(' ', u)
    u = spaceRe.sub(' ', u)
    #for debugging purposes
    #for i, c in enumerate(u):
      #print i, '%04x' % ord(c), unicodedata.category(c),
      #print unicodedata.name(c)
    return u

from guess_language import guess_language
print "Enter the sentence. Let me guess the language"
text= raw_input().decode('utf_8')
#text=text.encode("UTF-8")
#if isinstance(text, str):
  #text = unicode(text, 'utf-8')
text = normalize(text)
lang=guess_language.guessLanguageName(text)

shown=0
token_list_ascii=[]
#make a list of words in the sentence
token_list=text.split()
for words in token_list:
  words=words.encode("ascii","ignore")
  token_list_ascii.append(words)

fileList=os.listdir('wordlist/processed')
#for the files ending with dic extension
#print "Languages checked for, written using English script"
for files in fileList:
  filename= os.path.splitext(files)[0]
  #print "checking if sentence is in "+filename+ " language"
  extension = os.path.splitext(files)[1]
  openlist = open("wordlist/processed/"+filename+extension,"r")
  dictlist=[]
  for words in openlist:
    dictlist.append(words)
  presentwords=0
  absentwords=0
  wordcount=0
  #now check if sentence words are there in the language list
  #print token_list_ascii
  for words in token_list_ascii:
    wordcount=wordcount+1
    #print words
    #print dictlist
    for sentencewords in token_list_ascii:
        for dictwords in dictlist:
          dictwords=dictwords.rstrip('\n')
          dictwords=dictwords.rstrip(' ')
          if sentencewords==dictwords:
            presentwords=presentwords+1
      
    #Scaling up
    #print "word list"
    #print token_list
    #print "dict list"
    #print dictlist
  absentwords=wordcount-presentwords
  #print "Present words are "+str(presentwords)
  #print "Absent words are "
  #print absentwords
  #print "Wordcount is "+str(wordcount)
  presentwords=presentwords*100
  #absentwords=absentwords*100
  wordcount=wordcount*100
  threshold=1      #have to tweak it
  #if (presentwords-absentwords)/wordcount>threshold:
  if(presentwords/wordcount)>=threshold:
    print "The sentence may be in "+filename+ " language written in English"
    shown=1        
      
if shown==0:
  print "The sentence is in the language "+lang


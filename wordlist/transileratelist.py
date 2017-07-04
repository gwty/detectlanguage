import os.path
from transliteration import getInstance
t = getInstance()
fileList=os.listdir('.')

#for the files ending with dic extension
for files in fileList:
  filename= os.path.splitext(files)[0]
  extension = os.path.splitext(files)[1]
  if extension == ".dic":
    readFile=filename+extension
    print "Reading "+ readFile
    lang_trans=[]
    langlist=open(readFile,"r")
    for langword in langlist:
      langword=unicode(langword,"utf-8")
      converted_text = t.transliterate(langword, "en_IN")
      converted_text=converted_text.splitlines()
      converted_text=converted_text[0]
      converted_text=converted_text.encode("ascii","ignore")
      lang_trans.append(converted_text)
      
    lang_trans=set(lang_trans)
    lang_trans=sorted(lang_trans)
    langwrite=open("processed/"+filename+".txt","w")
    for word in lang_trans:
      word=word.encode("ascii","ignore")
      langwrite.write(word)
      langwrite.write("\n")
    print "Wrote "+filename+".txt"
    langwrite.close()
    langlist.close()

#custom extension cuz the hindi wordlist was too small
hi_en=[]

openme=open("processed/hindi.txt","r")
for words in openme:
  words=words.rstrip('\n')
  words=words.rstrip(' ')
  hi_en.append(words)
  
hindilist=open("hindi-word-frequencies.txt","r")
print "Reading hindi-word-frequencies.txt"
for line in hindilist:
  splitme=line.split()
  hindiword=unicode(splitme[0],"utf-8")
  converted_text = t.transliterate(hindiword, "en_IN")
  converted_text=converted_text.encode("ascii","ignore")
  hi_en.append(converted_text)
  
hi_en=set(hi_en)
hi_en=sorted(hi_en)
convertedfile=open("processed/hindi.txt","w")
print "Appended hindi.txt"
for word in hi_en:
    word=word.encode("ascii","ignore")
    convertedfile.write(word)
    convertedfile.write("\n")
      
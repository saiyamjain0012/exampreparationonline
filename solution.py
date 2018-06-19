import PyPDF2 #for reading pdf file

import math
from textblob import TextBlob as tb    #to extract key words
 
pdfFileObj = open('JavaBasics-notes.pdf', 'rb')
 
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
 
# printing number of pages in pdf file
print(pdfReader.numPages)
# creating a page object
docs1=" "
docs2=" "
docs3=" "

for i in range (1,9):

    pageObj = pdfReader.getPage(i)
    docs1=docs1+(pageObj.extractText()) 
    
for i in range (9,19):

    pageObj = pdfReader.getPage(i)
    docs2=docs2+(pageObj.extractText())
            
for i in range (19,23):

    pageObj = pdfReader.getPage(i)
    docs3=docs3+(pageObj.extractText())           
        
pdfFileObj.close()



def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

document1=tb(docs1)
document2=tb(docs2)
document3= tb(docs3)
bloblist = [document1,document2,document3]

no_of_keywords=input("Enter the number of keywords you want to extract-") 

print(no_of_keywords+" Key words in the given pdf file are-")
for i, blob in enumerate(bloblist):
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:int(no_of_keywords)]:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 10)))
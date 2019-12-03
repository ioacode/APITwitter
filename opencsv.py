
import nltk
import json
import pandas as pd  
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

rd = pd.read_csv("data.csv")

print("--- menampilkan data keseluruhan ------->", rd)
print("--- menampikan sepuluh data  ----------->", rd.head(10))

titleCsv = rd["title"].values 
print("--- menampikan semua deta berdasarkan title ---->", titleCsv)

titleCsv = rd.head(10)["title"].values
print("--- menampikan sepuluh data berdasarkan title -->", titleCsv)

arradatabaru = []
for i, title in enumerate (titleCsv):  
    arradatabaru.append(title)
print ("--- membuat array baru berdasarkan data sebelumnya --->",arradatabaru)

datatokeniza = []
dataleght = len(datatokenize)
for i, title in enumerate(arradata):
   kalimat = title.translate(str.maketrans('','',string.punctuation)).lower()
   datatokenize.append( word_tokenize(kalimat))
   
print("--------- data dari datatokenize ----->", datatokenize)

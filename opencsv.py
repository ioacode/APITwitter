
import pandas as pd  


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

#SERIES
'''
import numpy as np
import pandas as pd

myDictionary= {"Melike":21,"Ayşe":30,"Gül":55}
pd.Series(myDictionary) #verileri alt alta yazmani saglar
print(pd.Series(myDictionary))

myAges= [21,30,55]
myNames=["Melike","Ayşe","Gül"]

pd.Series(myAges) #0 21  1 30 gibi cikti verir alt alta kendi numaralandirir.

print(pd.Series(myAges,myNames)) #bununla ustte yazdigimiz ciktinin aynisini elde ederiz.
#karismamasi icin isim atariz direkt, bknz: 
print(pd.Series(data=myAges, index=myNames)) #data ve index outputta gorunmez

#numpy ile de aynisini yapabiliriz.bknz:
numpyDizisi=np.array ([50,40,30])
print(numpyDizisi)
print(pd.Series(numpyDizisi,myNames))

print(pd.Series(["Melike","Ayse","Gul"],[1,2,3])) # 1 Melike 2 Ayse 3 gül diye verir outputu

print(pd.Series([3,2,1],["Selcan","Kerem","Hakan"])) #Selcan 3, Kerem 2, Hakan1 aldı
#yani saga yazilan sola cikioyr outputu
'''

#DATA FRAME PANDAS:
import pandas as pd
import numpy as np

data= np.random.randn(4,3) #4 satir 3 sutunlu data

dataFrame= pd.DataFrame(data)
print(dataFrame) #excel gibi tablo olusturur

newDataFrame =pd.DataFrame(data,index=["Melike","Sinem","Ayse","Sevval"],columns=["Maas","Yas","Calisma Saati"])
print(newDataFrame) #index ve columns LABEL atadık

print(newDataFrame["Yas"]) #sadece yas sutunundaki bilgileri alirsin
#(newDataFrame["Yas","Yas"]) dersen iki sutun görürsün

print(newDataFrame.loc["Melike"]) #Melike'nin bilgilerini verir sana
#newDataFrame.iloc[1]) dersem Sinemin bilgierini görürüz. 
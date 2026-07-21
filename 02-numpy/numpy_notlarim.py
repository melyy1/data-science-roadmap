#NUMPY ARRAYS (DIZILER)
'''
import numpy as np

myList= [20,30,40]
np.array(myList) #listeden array oluşturur
print(np.array(myList)) #output: [20 30 40]

matrixListesi = [[20,30,40],[50,60,70],[80,90,100]]
print(matrixListesi[1][0]) #output: 50

np.array(matrixListesi) #listeden array oluşturur
print(np.array(matrixListesi))
 #output:[ 20  30  40]
 #       [ 50  60  70]
 #       [ 80  90 100]   '''


'''
#ARANGE (array+range) fonksiyonu: belirli bir aralıkta array oluşturur.

import numpy as np

np.arange(0,10) #0-10 arası array oluşturur
print(np.arange(0,10)) #output: [0 1 2 3 4 5 6 7 8 9]

#np.arange(baslangic,bitis,adim_miktari) #adım miktarı default olarak 1'dir. eğer farklı bir adım miktarı istiyorsak onu da belirtebiliriz.
#bitis kendini dahil etmez. 

np.arange(0,10,2)
print(np.arange(0,10,2)) #output: [0 2 4 6 8]


#ZEROS: 0'lardan oluşan bir array oluşturur. np.zeros((satir,sutun)) şeklinde kullanılır.
np.zeros((3,4)) #3 satır, 4 sütunlu bir array oluşturur
print(np.zeros((3,4)))
np.zeros(3)
print(np.zeros(3)) #output: [0. 0. 0.] 3 tane 0'lardan oluşan bir array oluşturur.

#ONES: 1'lerden oluşan bir array oluşturur. np.ones((satir,sutun)) şeklinde kullanılır.
np.ones((3,4)) #3 satır, 4 sütunlu bir array oluşturur
print(np.ones((3,4))) 

#linspace: belirli bir aralıkta eşit aralıklı sayılar üretir. np.linspace(baslangic,bitis,adet) şeklinde kullanılır.

np.linspace(0,20,5) #0-20 arası 5 tane eşit aralıklı sayı üretir
print(np.linspace(0,20,6)) #output: [ 0.  4.  8. 12. 16. 20.] 6 tane eşit aralıklı sayı üretir.
#aralıkları esit olan sayilar verir sana. bitis dahildir.

#eye: birim matris oluşturur. np.eye(satir,sutun) şeklinde kullanılır.
np.eye(3) #3x3 birim matris oluşturur
print(np.eye(3))  '''

'''
#RANDOM: rastgele sayılar üretir. np.random.rand(satir,sutun) şeklinde kullanılır.
import numpy as np
np.random.randn(8)
print(np.random.randn(8)) #output: [-0.12345678  0.98765432 -1.23456789  0.12345678  1.23456789 -0.98765432  0.56789012 -0.56789012] 8 tane rastgele sayı üretir.

np.random.randint(1,10)
print(np.random.randint(1,10)) #output: 5 1-10 arası rastgele bir sayı üretir. 1 dahil, 10 dahil değil.

np.random.randint(1,10,5) #sondaki sayi kac tane istedigini belirtir. 1-10 arası 5 tane rastgele sayı üretir.
print(np.random.randint(1,10,5)) #output: [3 7 1 9 4] 1-10 arası 5 tane rastgele sayı üretir.

myNumpyList = np.arange(30)
print(myNumpyList) #output: [0 1 2 3] 0-4 arası 4 tane sayı üretir.
'''

'''
import numpy as np
myRandomList =np.random.randint(0,30,20)
print(myRandomList)


myNumpyList = np.arange(30)
print(myNumpyList) #output: [0 1 2 3] 0-4 arası 4 tane sayı üretir.


#numpy dizi methodları:

myNumpyList.reshape(6,5)
print(myNumpyList.reshape(6,5)) #matrix yaptık listemizi, ama içinde tam 30 tane olmalı

myNumpyList.max() #max değeri verir
print(myNumpyList.max()) #output: 29

myRandomList.argmax() #listedeki en büyük degerin kacinci sirada oldugunu soyler
print(myRandomList.argmax())

print(myNumpyList[3:8]) #output:[3,4,5,6,7] sagdaki dahil edilmez

myNumpyList[3:8] =-5
print(myNumpyList) #output: !!! [ 0  1  2 -5 -5 -5 -5 -5  8  9 10 11...]

newDizi = np.arange(0,24)

slicingDizisi= newDizi[4:9]
print(slicingDizisi) #output: [4 5 6 7 8]

#peki slicingDizisinin sayılarını 700 yapmak istesek mesela? bknz: [:] kullaniriz.
#BURAYA BAKARLAR    
slicingDizisi[:] = 700
print(slicingDizisi) #output: [700 700 700 700 700] 

print(newDizi) #NOT!! NewDizideki sayılar da degisir. bknz:[  0   1   2   3 700 700 700 700 700   9  10  11  12...]

#eger orijinal listeyi degistirmek istemezsen:newDizi.copy kullanirsin.

ornekDizi= np.arange(0,24)
ornekDiziKopyasi =ornekDizi.copy()

print(ornekDiziKopyasi) #ornekdizinin aynisi oldu simdi bu, bunun ustunden oynicaz

ornekDiziKopyaSlicing = ornekDiziKopyasi[3:6]
print(ornekDiziKopyaSlicing) #output:[3 4 5]

ornekDiziKopyaSlicing[:] =800
print(ornekDiziKopyaSlicing) #output:[800 800 800]

#simdi bakalim gercek listemiz degismis mi? hayir, kopyamiz degisti.

print(ornekDizi) #[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
print(ornekDiziKopyasi) #[  0   1   2 800 800 800   6   7   8   9  10  11  12  13  14  15  ]

'''

#MATRIX
'''
import numpy as np

myList =[[10,20,30],[20,30,40],[40,50,60]]
myMatrixList = np.array(myList)
print(myMatrixList) #matrix haline donustu
print(myMatrixList[0]) #[10,20,30]
print(myMatrixList[1][2]) #40 cunku ilki satir, ikinci sutunu gosterir.
#print(myMatrixList[1,2]) ayni sonucu verir 40 cikar outputumuz.

myMatrixList[1:,2]
print(myMatrixList[1:,2]) #[40 60] 1. satir ve sonrasinin 2. sutunlarindaki sayilari alir.

myMatrixList[2:,2]
print(myMatrixList[2:,2]) #[60] 2. satir ve sonraki satirilaron 2. sutun sayilarini verir.

myMatrixList[2:,1:]
print(myMatrixList[2:,1:]) #output:[[50 60]] 2. satir ve sonrasindan 1. sutun ve sonrasindakileri kapsae

'''

#OPERASYONLAR:
'''
import numpy as np

newList2 = np.random.randint(1,100,20)

print(newList2) #[82 33 95 53 55 40 70  9 37 94 66 38 44 33  6 98 41 23  6 23]

print(newList2 > 24) #[ True  True  True  True False  True  True False  True False False False
#sonucu gercekten degistirmez ana listemizde istersen sonuclistesi = newList>24 dersen olur

sonucDizisi = newList2>24
print(newList2 [sonucDizisi]) #24'ten kucukleri cikartti [76 67 46 93 99 60 70 51 98 75 87 59 26 65 47 67 42]

'''


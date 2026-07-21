'''class Meyve():
    def __init__ (self,isim,kalori):
        self.isim=isim
        self.kalori=kalori
    
    #print(muz) yazarsam direkt çikti alamazsin bunun yerine: __str__ methodunu kullanırız. classın icine yap
    def __str__(self):
        return f"{self.isim} şu kadar kaloriye sahiptir: {self.kalori}"
    
    def __len__(self):
        return self.kalori

muz =Meyve("Muz",150)
print(muz.isim)
print(muz.kalori)  #output: 150

elma=Meyve("Elma",100)

print(muz) #output: Muz şu kadar kaloriye sahiptir: 150
print(len(muz)) #output: 150

print(len(elma))   '''


#BOLUM2: HATALARI ELE ALMA
'''
def toplama(no1,no2):
    return no1 + no2
x= int(input("Birinci sayiyi giriniz: " ))
y= int(input("Ikinci sayiyi giriniz: " ))
toplama(x,y)  #eger kullanıcı string girerse hata verir. bunu "try except" ile ele alabiliriz.

print(toplama(x,y))  '''

#TRY EXCEPT & ELSE & FINALLY 
'''
while True:
    try:
        benimSayi =int(input("Bir sayi giriniz: "))
    except:
        print("Lütfen geçerli bir sayi giriniz!")
        continue
    else:
        print("Teşekkürler")  #geçerli sayı girdiğinde bu satır çalışır ve döngüden çıkar.
        break
    finally:
        print("Finally bloğu her zaman çalisir. Hata olsa da olmasa da çalisirr.")
'''



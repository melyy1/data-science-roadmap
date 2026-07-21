'''class superkahraman():
    def __init__(self, isimInput, yasInput, meslekInput):
        """__init__ ve parantezin içine hep 'self' yazman gerekir"""
        print("init çağrildi")
        self.isim = isimInput
        self.yas = yasInput
        self.meslek = meslekInput
#farkli bir method tanimlayabilriz, bknz: superman.ornekMethod()
    def ornekMethod(self):
        print(f"Benim meslegim: {self.meslek}")

superman = superkahraman("Superman", 30, "gazeteci")

#print(superman.meslek)

#superman.isim = "Clark Kent"
#print(superman.isim)
        
print (superman.ornekMethod())     
'''
'''Soru: Bu sınıfa odunc_al() adında bir metot ekleyip durumu nasıl güncellersin?

(İpucu: Sınıfın içine yazılan her fonksiyona da ilk parametre olarak self vermeyi unutmamalıyız. def odunc_al(self): gibi.)
class kitap():
    def __init__(self,isim,yazar,basimyili):
        self.isim=isim
        self.yazar=yazar
        self.basimyili=basimyili
        self.oduncalindimi=False

    def oduncal(self):
        self.oduncalindimi=True
kitap1=kitap("Simyacı", "Paulo Coelho", 1988)


kitap1.oduncal()
print(kitap1.oduncalindimi) '''

#soru: bir köpek X yaşındaysa insan kaç yasındadır? (insan köpeğin 7 katı yaşındadır)
'''
class hesaplama():
    def __init__(self,isim,yas):
        self.isim=isim
        self.yas=yas
    def kopekYasi(self):
        print(f"{self.isim} köpek {self.yas} yaşındadir.")
    def insanYasi(self):
        print(f"{self.isim} kisisi {self.yas} yaşındadir.")

kopek1=hesaplama("Pug",2)
insan1=hesaplama("Ahmet",kopek1.yas*7)
kopek1.kopekYasi()
insan1.insanYasi()'''

#farklı bir yol ile:
'''
class hesaplama():
    yilCarpani=7
    def __init__(self,yas=5):
        self.yas=yas

    def insanYasiniHesapla(self):
        return self.yas*self.yilCarpani
    
kopek1= hesaplama()
print(kopek1.yas)
print(kopek1.insanYasiniHesapla())
#ONEMLI!! insanYasiniHesapla bir fonksiyondur methoddur o yüzden sonda () kullandik
'''
'''
#INHERITANCE: bir sınfın özelliklerini miras almak(başka bir sınıtan) ve o sınıfın özelliklerini kullanmak icindir

class hayvan():
    def __init__(self):
        print("Hayvan sinifi init cagrildi")
    def method1(self):
        print("hayvan sinifi method1 cagrildi")
    def method2(self):
        print("hayvan sinifi method2 cagrildi")

benimHayvanim = hayvan()
benimHayvanim.method1()


#bu sefer bir classı inheritance ettik yani onun özelikleirni aldık.
class kedi(hayvan): 
    def __init__(self):
        hayvan.__init__(self) #bu satır ile hayvan sınıfının init fonksiyonunu çağırdık
        print("Kedi sinifi init cagrildi")
    def miyavla(self):
        print("Miyav miyav")
benimKedim= kedi()
benimKedim.method1() #bu methodu çağırdığımızda hayvan sınıfının method1 fonksiyonu çağrıldı çünkü kedi sınıfı hayvan sınıfını miras aldı
#yani kedi sınfıının içinde bile hayvan sınıfını çağırabiliriz.
benimKedim.miyavla()  '''


#POLIMORPHISM: aynı method ismi ile farklı sınıflarda farklı işlemler yapabilmek demektir.

'''
class muz():
    def __init__(self,isim):
        self.isim=isim
    def bilgiver(self):
        return self.isim + "150 kaloridir"
    
class elma():
    def __init__(self,isim):
        self.isim=isim
    def bilgiver(self):
        return self.isim + "100 kaloridir"

meyve = muz("Muz")
meyve2= elma("Elma")

print(meyve.bilgiver())
print(meyve2.bilgiver())

meyveListesi = [meyve,meyve2]
for meyveler in meyveListesi:
    print(meyveler.bilgiver())   #burda polimorphism işe yaradı çünkü aynı method ismi ile farklı sınıflarda farklı işlemler yaptık.

def bilgiAl(meyveler):
    print(meyveler.bilgiver())

bilgiAl(meyve) #output: Muz150 kaloridir
bilgiAl(meyve2) #output: Elma100 kaloridir    '''

     

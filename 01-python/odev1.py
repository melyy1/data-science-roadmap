

#odev Soru1 Bir degisken tanımla, ad=kaan, yas=25,ortalam=3.45, degidken tiplerini type ile sınıflandır.
'''
ad= "Kaan"
yas= 25
ortalama= 3.45

print(type(ad))
print(type(yas))
print(type(ortalama))

#SORU2: kullanicidan yas bilgisini input olarak alalım. yasin tipini ekrana basalim ve 5 yil ekleyip ekrana yazdiralim. 

kullanici_yasi= int(input("Lütfen yasinizi giriniz"))
print(type(kullanici_yasi))
yeni_kulanici_yasi= kullanici_yasi +  5
print(f"Yeni kullanici yasiniz {yeni_kulanici_yasi}")

#SORU3: bir urun fiyatı(float) alalim. %18 KDV hesaplayalım. Toplam fiyatı iki basamak olacak sekilde bastıralim.

urun_fiyati= float(input("Urun fiyatini giriniz:"))
KDV_hesaplama= (urun_fiyati*18) /100
KDV_li_fiyat= urun_fiyati + KDV_hesaplama
print(f"Toplam fiyat:{round(KDV_li_fiyat,2)}") 

#SORU4: Bir liste olusturalim. sayilar=[10,20,30,40,50]. ilk elemanı yazdir, son elemnani yazdir. 2. indexten sona kadar olanlari yazdir. listeye 60 ekle. listedeki 20 yi sil.

sayilar=[10,20,30,40,50]
print("ilk deger",sayilar[0])
print("Son deger",[4])
print(sayilar[2:])
sayilar.append(60)
print("60 eklendi:",sayilar)
sayilar.remove(20)
print("20 cikarildi",sayilar)

#SORU5: tuple olustur. koordinat=(12,34).degerleri unpacking ile x,y ye alalim.x,y yi yazdir. tuple degistirlimez yorum yaz.

koordinat = (12,34)
x,y = koordinat
print("x:",x)
print("y:",y)
koordinat[0] #tuple degistirilemez 

#SORU6: 
ogrenci= {"isim":"ayse","yas":22,"bolum":"yazilim"}
print("ogrenci ismi",ogrenci["isim"])

ogrenci["not"]=90
ogrenci["yas"]=23
print("Guncel hal:",ogrenci)
print("Anahtarlar",list(ogrenci.keys()))
print("degerler",list(ogrenci.values()))

#SORU7:set olusturalim ve tekrar edenleri sil. listeyi sete cevirip benzersiz isimleri yazdiralim.benzersiz isim sayisini yazdiralim.

liste= ["Ali","Ayse","Ali","Mehmet","Ayse"]
benzersiz_isimler= set(liste)
print("Benzersiz isimler",benzersiz_isimler)
print("benzersiz isim sayisi:",len(benzersiz_isimler))'''




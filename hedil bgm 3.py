#Tabloyu sinav_sonuc isimli bir sözlük oluşturarak ona aktardım.
sinav_sonuc = {'isimler':['Ayse K.','Ahmet M.','Nuri C.','Nawar T.','Suzan T.','Ala B.'],
'cinsiyet':['K','E','E','E','K','K'],
'matematik notu':[60,40,97,45,56,95],
'türkce notu':[70,30,23,80,78,46]}

#Klavyeden girilen bilgileri yerine atayan fonksiyon kurdum
def yeniBilgi(isim,cinsiyeti,matematik, türkce):
   sinav_sonuc['isimler'].append(isim)
   sinav_sonuc['cinsiyet'].append(cinsiyeti)
   sinav_sonuc['matematik notu'].append(matematik)
   sinav_sonuc['türkce notu'].append(türkce)

 
#Klavyeden 1. öğrencinin bilgilerini girme
isim=input('1.Öğrencinin ismini "isim + soyisiminin ilk harfi" seklinde giriniz=')
cinsiyet=input("Öğrencinin cinsiyeti erkek ise E Kız ise K harfini giriniz=")
matematik=input("Öğrencinin matematik notunu giriniz=")
Türkçe=input("Öğrencinin Türkçe notunu giriniz=")

yeniBilgi(isim,cinsiyet,matematik,Türkçe)

#Klavyeden 2. öğrencinin bilgilerini girme
isim=input('2. Öğrencinin ismini "isim + soyisiminin ilk harfi" seklinde giriniz=')
cinsiyet=input("Öğrencinin cinsiyeti erkek ise E Kız ise K harfini giriniz=")
matematik=input("Öğrencinin matematik notunu giriniz=")
Türkçe=input("Öğrencinin Türkçe notunu giriniz=")

yeniBilgi(isim,cinsiyet,matematik,Türkçe)

#Girilen yeni bilgilerle tabloyu güncelleme ve ekrana yazdırma

for key in sinav_sonuc:
   print(key,":", sinav_sonuc[key])
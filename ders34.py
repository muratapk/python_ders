from ders33 import ogrenci
#burda öğrenci class buraya dahil ettim
ad=input("Öğrencini Adını Girin :")
soyad=input("Öğrencinin Soyadını  Girin: ")
notlar=[]
for i in range(3):
    notum=int(input(f"{i}.Notu Girin"))
    notlar.append(notum)
a1=ogrenci(ad,soyad,notlar)
a1.durum()
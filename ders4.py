import random
meyveler=["Elma","Armut","Muz","Kivi"]#liste yazıyı
print(meyveler[0])
print(meyveler[3])
for meyve in meyveler:
    print(meyve)
ogrenci=[]
ogrenci.append("Ali")
ogrenci.append("Veli")
ogrenci.append("Hasan")
ogrenci.append("Hüseyin")
for ogr in ogrenci:
    print(ogr)

print(random.choice(ogrenci))
sayilar=[1,5,10,20,35]
print(sayilar[2])
print(sayilar)
sayilar.insert(1,99)
print(sayilar)
sayilar.remove(1)
print(sayilar)
sayilar.pop()
print(sayilar)
#sayilar.clear()
sayilar.sort()#kucukten buyuke
print(sayilar)
sayilar.sort(reverse=True)
print(sayilar)
#tek=sayilar.count()
#print(tek)
sayilar2=sayilar.copy()
#dizi kopyalama copy
print("Sayilar2 Kopyala",sayilar2)
sebze=["Domates","Patates"]
meyve=["Muz","Kivi"]
birles=sebze+meyve
print(birles)
print(len(birles))
if "Patates" in birles:
    print("Var")
else:
    print("Yok")
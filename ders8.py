ogrenci={"Id":1,"ad":"Ahmet","sinif":"11FenA"}
print(ogrenci['ad'])
print(ogrenci["sinif"])
ogrenci["ad"]="Kerim"
print(ogrenci["ad"])
ogrenci["Okul"]="Etiler Lisesi"
print(ogrenci)
ogrenci.pop("Okul")
print(ogrenci)
del ogrenci["sinif"]
print(ogrenci)
ogretmen={"Ad":"Faruk","Ad":"Rauf","Yas":30,"Yas":45}
print(ogretmen)
ogretmenler=[{"Ad":"Faruk","Yas":40},{"Ad":"Rauf","Yas":50}]
print(ogretmenler)
print(ogretmenler[0]["Ad"])
for anahtar,deger in ogrenci.items():
    print(anahtar,":",deger)
print(ogrenci.keys())
print(ogrenci.values())
print(ogrenci.items())
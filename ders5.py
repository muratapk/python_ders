ogrenci=[]
for i in range(5):
    ad=input("Bir Öğrenci Adını Girin :")
    ogrenci.append(ad)
print(ogrenci)
bul=input("Aranan Öğrenci Adını Girin :")
if bul in ogrenci:
    print("Bu Öğrenci Var")
else:
    print("Bu Öğrenci Yok")
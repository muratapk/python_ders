for i in range(1000):
    print(i)

toplam=0
#global döngü içinde olmayan 
#fonksiyon içinde olmayan 
#genel veriyi tutan değişken global
for i in range(1000):
    if i%2==0:
        #print(i)
        toplam=toplam+i
print("Toplam :",toplam)

for t in range(0,11,2):
    print(t)

#ekrana 10 defa kendi isminiz yazdırın
for y in range(11):
    print("Murat")

topla=0
for k in range(1,7):

    notu=int(input(f"{k}.Not Girin...  :"))
    topla=topla+notu

ortalama=topla/6
print("Öğrencinin Ortalaması  :",ortalama)
if ortalama>=50:
    print("Geçti")
else:
    print("Kaldı")

isim="Murat Çıplak"
for g in isim:
    print(g)
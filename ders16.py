def selam():
    print("Dikkat")

selam()

def merhaba(a):
    print("Merhaba",a)

merhaba("Sude")

def topla(a,b):
    print(a+b)

def sonuc(c,d):
    return c+d
topla(10,15)

islem=sonuc(50,71)
print(islem)
def kdv(fiyat,oran):
    return (fiyat*oran)/100

fatura=1200
geri=kdv(fatura,20)
toplam=geri+fatura
print(f"Girilen Fatura {fatura} Kdv'si {geri} Toplam Tutar {toplam}")
import random
rast=random.randint(1,10)
hak=3
for i in range(3):
    hak=hak-1
    sayi=int(input("1-10 Arasında Bir Sayı Girin...:"))
    if sayi>rast:
      print("Tuttuğunuz Sayı Küçültün....")
    elif sayi==rast:
      print("*****Tebrikler Bildiniz********")
    else:
      print("Tuttuğunuz Sayı Büyültünüz........")
    if hak==0:
       print("Hakkınız Bitti")
       exit()

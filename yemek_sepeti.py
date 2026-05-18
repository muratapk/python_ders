#yemek seimi yapınız
#1.Tavuk Döner
#2.Et Döner
#3.İskender
#seçim yapınız
#kac adet döner :
#icecek istiyor musun 1.Ayran 2.Kola 3.Soda
#kaç adet icecek
import math

def main():
    print("yemek seçimi yapınız")
    print("1.tavuk döner 20tl")
    print("2.et döner 40tl")
    print("3.iskender 60 tl")

    secim = int(input("yemek seçimi yapınız...:"))
    adet = int(input("kaç adet istiyorsunuz....:"))

    print("içecek seçimi yapınız....:")
    print("1.ayran 5")
    print("2.kola 10")
    print("3.soda 2")

    isecim = int(input("icecek seçimi yapınız....:"))
    iadet = int(input("kaç adet istiyorsunuz....:"))

    top_yemek = yemek(secim, adet)
    top_icecek = icecek(isecim, iadet)

    genel = top_yemek + top_icecek

    print(f"Yemek {top_yemek} TL")
    print(f"İçecek {top_icecek} TL")
    print(f"Genel Toplam {genel} TL")

def yemek(ysecim, adet):
    if ysecim == 1:
        return 20 * adet
    elif ysecim == 2:
        return 40 * adet
    elif ysecim == 3:
        return 60 * adet
    else:
        return 0

def icecek(secim, adet):
    if secim == 1:
        return 5 * adet
    elif secim == 2:
        return 10 * adet
    elif secim == 3:
        return 2 * adet
    else:
        return 0

main()
#Adi ADI aDi
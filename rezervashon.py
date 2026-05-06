#4 adet oda olacak 1.suit kişi 500 2.Vip 600 3.Kral 1000
#kalacak kişi sayısı alacak
#cocuklar sayısı girin ücretin yarısı alınacak
#giriş tarihi 
#cikiş tarihi 
#buna göre ücreti hesap eden  programı yazınız....05054426841
from datetime import datetime
import math
def main():
    print("***Otel Rezervasyon***")
    print("1.Oda Suit 500TL ")
    print("2.Oda Vip 600TL")
    print("3.Oda Vip 1000TL")
    secim=int(input("Bir Oda Seçiniz.....: "))
    kalacak_kisi=int(input("Kaç Kişi Kalacak..........:"))
    cocuk_sayisi=int(input("Çocuk Sayısı..........:"))
    giris_tarih=input("Giriş Tarihini Yazınız...Gün.Ay.Yıl Saat:Dakika ")
    cikis_tarih=input("Çıkış Tarihi Gün.Ay.Yıl Saat:Dakika ")
    saat=gun_fark(giris_tarih,cikis_tarih)
    #gun fark methodun çağrırark  saat alıyorum
    fiyat=fiyatim(secim)
    #fiyat methodun içinden fiyat al
    cocuk=cocuk_hesapla(cocuk_sayisi)
    #cocuk sayısı method içinde çağırarak alıyorum
    hesap=(saat*fiyat)*(kalacak_kisi+cocuk)
    print(f"Ödenecek Tutar {hesap}")

def gun_fark(giris_tarih,cikis_tarih):
    format="%d.%m.%Y %H:%M"
    girtar=datetime.strptime(giris_tarih,format)
    ciktar=datetime.strptime(cikis_tarih,format)
    fark=ciktar-girtar
    saat=(fark.total_seconds()/3600)/24
    gun=fark.days #gun farkını buradan bulabiliriz....
    return saat

def fiyatim(secim):
    fiyat=0
    if secim==1:
        fiyat=500
    elif secim==2:
        fiyat=600
    elif secim==3:
        fiyat=1000
    else:
         fiyat=0
    return fiyat


def cocuk_hesapla(cocuks):
    #içinde boşluk ifadesi boş olarak kabul ediyor
    if cocuks==0:
        cocuk=0
    else:
        cocuk=cocuks/2
    return cocuk




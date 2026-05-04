from datetime import datetime
import math

def main():
    print("Araba Kiralama")
    print("*********************")
    print("1.Mercedes (3000)TL......:")
    print("2.Bmw (2500)TL.........")
    print("3.Reanult (1250)TL......")
    print("4.Fiat (1000)TL.......")
    print("***************")
    secim=int(input("Araba Seçimi Yapınız.......:"))
    baslangic=input("Başlangıç Zamanı Girin......(GG.AA.YY ss:dd):")
    bitis=input("Bitiş Zamanı Girin.....(GG.AA.YYY ss:dd).:")
    #tarih formatı  d m y h m day gün m ay y yil h saat m minute dakika
    
    
    saat=fark_tarih(baslangic,bitis)
    fiyat=secimyap(secim)
    toplam_ucret=saat*math.ceil(fiyat)
    print(f"Ödenmesi Gereken Ücret {toplam_ucret}")

def fark_tarih(bastar,bittar):
    format="%d.%m.%Y %H:%M"
    #str int
    bastarih=datetime.strptime(bastar,format)
    bittarih=datetime.strptime(bittar,format)
    fark=bittarih-bastarih
    #print(fark)
    saat_fark=fark.total_seconds()/3600
    #farkı saniye cinsine çevirdim 3600 saniye bölerek
    #saat farkını bul
    #print(saat_fark)
    gun=fark.days
    #gun kaç gün olduğunu
    saat=fark.total_seconds()/3600
    #kaç saat
    dakika=fark.total_seconds()%3600
    #print(f"Kiralanan Gün Sayısı {gun} Kiralanan Saat {saat} Dakika {dakika}")
    #Kiralanan Gün Sayısı 4  Kiralama Saat 2 Dakika 40
    return saat


def secimyap(secim):
    fiyat=0
    if secim==1:
        fiyat=3000
    elif secim==2:
        fiyat=2500
    elif secim==3:
        fiyat=1250
    elif secim==4:
        fiyat=1000
    else:
        print("Hatalı Seçim Yaptınız:")
    return fiyat

main()

sude=fark_tarih('04.05.1972 16:15','04.05.2026 16:15')
print(sude)


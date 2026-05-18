#ad=input("Adınız Girin....:")
##kitap[]
##uyeler[]

#aynı klass defalarca çağırıp kullabilir.Kod Tekrar ortan kaldırıyor
#temiz kullanı sizin oluşturacağız kodları class içinde saklıyorum 
#kutuphane kisiler uyeler kitaplar
#class tanımlanılmaz otomatik olarak çalışması istediği her bilgi __init_ yapısı
#costurctor mutlaka bu bilgi girilecek
#self class kendi adı self.ad o içerisinde yeni değişken tanımlanıyor
class Kutuphane:
    def __init__(self,ad):
        self.ad=ad
        self.__kitap=[]#boş bir liste oluşturur
        self.__uyeler=[]#boş bir uye listesi oluştur

    def kitap_ekle(self,kitap):
        self.__kitap.append(kitap)
        print(f"{kitap} Adlı Kitap Eklendi")

    def kitap_sil(self,isim):
        for kitap in self.__kitap:
            if kitap==isim:
                self.__kitap.remove(isim)
                print(f"{kitap} Silindi")
                return True
            else:
                return False
        
        print("Kitap Bulunamadı...")
        return False
    def kitap_ara(self,ara):
        sonuc=[]
        for kitap in self.__kitap:
            if kitap.lower() == ara.lower():
                sonuc.append(kitap)
        return sonuc
    def kitap_bul(self,isim):
        for kitap in self.__kitap:
            if kitap.lower()==isim.lower():
                print(f"{kitap} Bulundu")
                return True
            else:
                print(f"{isim} kitap bulunamadı...")
                return False
#miras verdik kutuphane özelliklerini sedat
class Sedat(Kutuphane):
    def __init__(self):
        pass

buse=Sedat()
buse.ad="Sedat Kütühane"


deniz=Kutuphane("Deniz Kütüphanesi")
deniz.kitap_ekle("Aşk ve Gurur")
deniz.kitap_ekle("Sefiller")
deniz.kitap_ekle("Çalıkuşu")
deniz.kitap_ekle("Kaşağı")
sonuc=deniz.kitap_bul("Aşk ve Gurur")
if(sonuc==True):
    print("Kitap Var")
else:
    print("Kitap Yok")
sil=deniz.kitap_sil("Aşk ve Gurur")
if sil==True:
    print("Kitap Silindi")




            
    






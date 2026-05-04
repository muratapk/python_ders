class film():
    def __init__(self,ad,sure,fiyat):
        self.ad=ad
        self.sure=sure
        self.fiyat=fiyat

class Musteri():
    def __init__(self,ad,yas):
        self.ad=ad
        self.yas=yas

    def indirim(self):
        if self.yas<18:
            return 0.5
        elif self.yas>60:
            return 0.3
        else:
            return 0
class Bilet():
    def __init__(self,musteri,film):
        self.musteri=musteri
        self.film=film
    def ucret_hesapla(self):
        indirim=self.musteri.indirim()
        normal_fiyat=self.film.fiyat
        indirim_fiyat=normal_fiyat-(normal_fiyat*indirim)
        return indirim_fiyat
    
    def bilgi_goster(self):
        print("-----Bilet Bilgisi----")
        print("Müşteri Adı:",self.musteri.ad)
        print("Filma Adı",self.film.ad)
        print("Süre",self.film.sure)
        print("Ödenecek Tutar ",self.ucret_hesapla())

film_isim=film("Batman",60,100)
musteri_isim=Musteri("Deniz",15)
bilet1=Bilet(musteri_isim,film_isim)
bilet1.bilgi_goster()
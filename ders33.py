class ogrenci:
    def __init__(self,ad,soyad,notlar):
        self.isim=ad
        self.soyisim=soyad
        self.notlar=notlar
    def ortalam(self):
        return sum(self.notlar)/len(self.notlar)
    def durum(self):
        if self.ortalam()>=50:
            print(f"Öğrencinin Adı {self.isim} soyadı {self.soyisim},Durumu Geçti")
        else:
             print(f"Öğrencinin Adı {self.isim} soyadı {self.soyisim},Durumu Kaldı")


# deniz=ogrenci("Deniz","Irmak",[60,70,80])
# deniz.durum()
# berfin=ogrenci("Berfin","Yılmaz",[50,75,85])
# berfin.durum()


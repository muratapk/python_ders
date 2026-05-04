class ogrenci():
    def __init__(self,ad,soyad):
        self.ad=ad
        self.soyad=soyad
    def bilgi_goster(self):
        print(f"Öğrenci Adı {self.ad} Öğrencinin Soyadı {self.soyad}")

veli=ogrenci("Ali","Yılmaz")
ali=ogrenci("Vehbi","Kaçar")
veli.bilgi_goster()
ali.bilgi_goster()


    

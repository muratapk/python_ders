class ogreni():
    def __init__(self,adsoyad,yasim):
        self.adi=adsoyad
        self.yas=yasim
    def __new__(cls):
        print("Sistem Çalıştı")




a=ogreni("Yeşim",45)
print(a.adi)
# a.adi="Buse"
# a.yas=25
# print(a.adi)
# print(a.yas)
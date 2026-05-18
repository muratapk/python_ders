#@staticmethod
#static class
#sınıf olarak oluşturulmuyor
#sedat=Banka()
#static self yapısı yok cls yeni yok
class Matematik:
    def topla(self,a,b):
        print(a+b)

    @staticmethod
    def carp(a,b):
        print(a*b)

buse=Matematik()
buse.topla(10,50)
Matematik.carp(50,60)

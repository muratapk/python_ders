class Banka:
    def __init__(self):
        self.__bakiye=5000
    def bakiye_goster(self):
        print(self.__bakiye)

    #setter
    def para_yatir(self,para):
        if para>0:
            self.__bakiye+=para
    #getter
    def para_cek(self,cek):
        if self.__bakiye<=cek:
            print("Yetersiz Bakiye")
        else:
            self.__bakiye-=cek
    #private
    
    #getter
    @property
    def bakiye_getir(self):
        print(f"Mevcut Bakiye {self.__bakiye}")
    #setter

    @bakiye.setter
    def bakiye_ayarla(self,deger):
        if deger>0:
            self.__bakiye+=deger
    
sedat=Banka()
sedat.bakiye_goster()
sedat.para_yatir(500)
sedat.para_yatir(500)
sedat.bakiye_goster()
sedat.para_cek(3000)
sedat.bakiye_goster()


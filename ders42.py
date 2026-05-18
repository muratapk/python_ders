class Kisi:
    def __init__(self,ad):
        self.ad=ad
    
    def yazdir(self):
        print(f"Kişinin Adı {self.ad}")

class ogrenci(Kisi):
    def __init__(self,ad,numara):
        super().__init__(ad)
        self.numara
#miras almış olduğuna nesne içindeki constructor yapısın içindek ifade devir al

ali=ogrenci("Murat","911")

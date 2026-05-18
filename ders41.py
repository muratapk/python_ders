class Hayvan():
    def ses_cikar(self):
        print("Genel Hayvan Sesi")

class Kedi(Hayvan):
    def __init__(self):
        pass
    def ses_cikar(self):
        print("Mivav")
    
class Kopek(Hayvan):
    def __init__(self):
        pass
    def ses_cikar(self):
        print("Hav Hav")
bobi=Kopek()
bobi.ses_cikar()    
boncuk=Kedi()
boncuk.ses_cikar()
##overwrite ezme üzerine yazma

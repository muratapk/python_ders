def bilgiler(**veri):
    for v,i in veri.items():
        print(f"Anahtar {v} Değer {i}",)

#**kwargs dictinoary tarzında veri ekran veri basmak method
bilgiler(isim="Veli",yas="25",adres="Maltepe")
#bu methodun ismi login  kul=admin sifre=123

def login(kul,sifre):
    if kul=="admin" and sifre=="123":
        print("Giriş Başarılı")
    else:
        print("Başarısız")

login("Sude","758")
kullanici=input("Kullanıcı Adını Girin.......  :")
sifrem=input("Şifrenizi Girin...........:")
login(kullanici,sifrem)
while True:
    isim = input("İsminizi Girin....... : ")
    
    durum = input("Çıkmak İçin 1 Basın: ")
    
    if durum == "":
        print("Boş giriş yaptınız!")
        continue
    
    durum = int(durum)
    
    if durum == 1:
        break

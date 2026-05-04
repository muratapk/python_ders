#öğrencinin girilen değere geçti ve kaldı hesap eden methodu yazın
#kaç adet not girilecek onu sorsun
#bu notların ortalamasına göre geçti veya kaldı hesap etsin
#liste[]
notlar=[]

def not_gir():
    adet=int(input("Kaç Adet Not Girilecek....:"))
    for i in range(adet):
        not_deger=int(input("Notuzu Girin ............:"))
        notlar.append(not_deger)
        
    #üç notu aldıktan  aşağıdak işlemi yapacak
        
    ortalama=sum(notlar)/len(notlar)
        #sum dizi içindeki tüm değerleri toplar
        #len dizi adet verir
    print(f"Ortalaması.....:{ortalama}")
    if ortalama>=50:
        print("Geçti")
    else:
        print("Kaldı")

not_gir()
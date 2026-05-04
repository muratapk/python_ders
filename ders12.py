while True:
  print("1.Toplama:")
  print("2.Çıkarma")
  print("3.Çarpma")
  print("4.Bölme")
  print("5.Çıkış")
  secim=int(input("Seçim Yapın...... :"))
 
  if secim==1:
     sayi=int(input("Bir Sayı Girin ....:"))
     sayi2=int(input("İkinci Sayı Girin....:"))
     sonuc=sayi+sayi2
     print(f"İşlem Sonucu {sonuc}")
  elif secim==2:
    sayi=int(input("Bir Sayı Girin ....:"))
    sayi2=int(input("İkinci Sayı Girin....:"))
    sonuc=sayi-sayi2
    print(f"İşlem Sonucu {sonuc}")
  elif secim==3:
    sayi=int(input("Bir Sayı Girin ....:"))
    sayi2=int(input("İkinci Sayı Girin....:"))
    sonuc=sayi*sayi2
    print(f"İşlem Sonucu {sonuc}")
  elif secim==4:
    sayi=int(input("Bir Sayı Girin ....:"))
    sayi2=int(input("İkinci Sayı Girin....:"))
    sonuc=sayi/sayi2
    print(f"İşlem Sonucu {sonuc}")
  elif secim==5:
     break
 
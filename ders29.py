


def ucret_hesapla(arac_tipi, saat):
   
   arac={"otomobil":100,"kamyon":200,"otobüs":300}
   if arac_tipi not in arac:
      print("Geçersiz Veri Girişi")
      return
   saat_ucreti=arac[arac_tipi]
   if saat<=1:
      toplam=saat_ucreti
   else:
      ekstra_saat=saat-1
      zamli_ucret=saat_ucreti+saat_ucreti*0.20
      toplam=saat_ucreti+(ekstra_saat*zamli_ucret)
      return toplam

print("Ana Menü")
print("1.Otomobil :100TL")
print("2.Kamyon  :200TL")
print("3.Otobüs  :300TL")
secim=input("Bir Seçim Yapınız..... :").lower()#upper büyük harf lower küçük harf çevir
saat=int(input("Kaç Saat Kaldı.........:"))
ucret=ucret_hesapla(secim,saat)

if ucret is not None:
   print(f"Girilen Araç {secim} Kalanına Saat {saat} Toplam Ücret:{ucret:.2f}")
      

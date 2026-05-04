from datetime import datetime
import math
kod=input("Qr Kodu Girin..........:")
baslangic=input("Başlangıç Saati Girin......:")
bitis=input("Bitiş Saati Girin.....:")
ucret=80
#format
format="%d.%m.%Y %H:%M"
bastar=datetime.strptime(baslangic,format)
bittar=datetime.strptime(bitis,format)
fark=bittar-bastar
saat=fark.total_seconds()/3600
toplam_ucret=ucret*math.ceil(saat)
print(f"Toplam Ödenecek Ücret {toplam_ucret}")


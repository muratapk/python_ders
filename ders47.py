#open dosya
# r read  w yazma a ekleme x yeniden dosya oluşturma r+ okuma yazma
file=open("deniz.txt","r",encoding="utf-8")
#dosya açma komutu open
#icerik=file.read()
#print(icerik)
for satir in file:
    print(satir.strip())
    #strip kelime satir içindeki boşluk siliyor

file.close()



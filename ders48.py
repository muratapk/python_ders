#open dosya
# r read  w yazma a ekleme x yeniden dosya oluşturma r+ okuma yazma
file=open("deniz.txt","r",encoding="utf-8")
satirlar=file.readlines()
print(satirlar)
file.close()

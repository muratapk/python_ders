import shutil
import os
#shutil.rmtree("Resimler")
#shutil.move("deniz.txt","Deniz/deniz.txt")
#move işlemi dosya taşımak için kullanıyoruz
#dosya kopyalama
#shutil.copy("sedat.html","sude.html")
#shutil.copytree("Deniz","Fener")
if os.path.exists("sedat.html"):
    print("Dosya Mevcut")
else:
    print("Mevcut Değil")
#dosya mevcut olup olmadığı kontrol için kullanıyoruz
dosyalar=os.listdir(".")
print(dosyalar)
#klasör içindeki listelemeyi al

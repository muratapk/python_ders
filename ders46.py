from bs4 import BeautifulSoup
dosya=open("sedat.html",encoding="utf-8")
#sedat.html dosyasındaki oku encoding türkçe font olarak gör aç
#dosya okuma yazma read write open
icerik=dosya.read()
#dosya içindeki verileri oku her veriyi içerik isimmli değişkene ata

soup=BeautifulSoup(icerik,"html.parser")
#içerik içindeki html.parser html kodlarını soup içerisine ayrırarak ata


print(soup.h1)
print(soup.h2)
print(soup.h3)
print(soup.title.text)
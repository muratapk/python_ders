with open("deniz.txt","r",encoding="utf-8") as file:
    icerik=file.read()
    print(icerik)
    file.close()

with open("deniz.txt","w",encoding="utf-8") as file:
    file.write("Pyhon Dosya Okuma ve yazma öğrendim")
    file.close()

with open("deniz.txt","a",encoding="uft-8") as file:
    file.write("\n Yeni geç alt satıra geç ")
    file.close()



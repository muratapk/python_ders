#varsayılan dğerli bir method
def sonuc(a,b=20):
    print(a+b)
#birden fazla parametreli işlem yapıyoruz
def toplamlar(*sayilar):
    topla=0
    for s in sayilar:
        topla+=s
    return topla
#########################################################

deger=toplamlar(10,20,30,50,80)
print(deger)



sonuc(10,80)

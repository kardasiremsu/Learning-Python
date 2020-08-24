import random
import time
print("""
********************
SAYI TAHMİN OYUNU

1-40 ARASI BİR SAYI TAHMİN EDİNİZ.
********************
""")
tahmin_hakki = 7
rastgele_sayi = random.randint(1,40)
while True:
    sayi = int(input("Tahmininiz:"))
    print("Bilgiler Sorgulanıyor...")
    time.sleep(1)
    if(sayi > rastgele_sayi):
        print("Daha küçük bir sayi giriniz:")
        tahmin_hakki-=1
    elif(sayi < rastgele_sayi):
        print("Daha büyük bir sayi giriniz:")
        tahmin_hakki-=1
    else:
        print("Doğru girdiniz kalan tahmin hakkınız {}".format(tahmin_hakki))
    if(tahmin_hakki ==0):
        print("Tahmin hakkınız bitti")
        break

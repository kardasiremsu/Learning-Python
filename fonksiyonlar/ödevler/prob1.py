"""
Problem 1
1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın.
Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.

Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır.
 Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).
"""

def mukemmel_mi():
    mukemmel = []
    for i in range(1,1001):
        toplam =0
        for j in range(1,i):
            if(i%j ==0):
                toplam +=j
        if(toplam ==i):
            mukemmel.append(i)
    return mukemmel

print("Mükemmel sayılar",mukemmel_mi(), sep=":")
"""
Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın. Bu fonksiyon, eğer sayı çift ise return ile bu değeri dönsün.
Ancak sayı tek sayı ise fonksiyon raise ile ValueError hatası fırlatsın. Daha sonra,
içinde çift ve tek sayılar bulunduran bir liste tanımlayın ve liste üzerinde gezinerek ekrana sadece çift sayıları bastırın.
"""
def ciftmi(sayi):
    if sayi%2==0:
        return sayi
    else:
       raise ValueError

liste = [1,5,10,26,11,96,41]
for i in liste:
    try:
        print(ciftmi(i))
    except ValueError:
        print("Tek")
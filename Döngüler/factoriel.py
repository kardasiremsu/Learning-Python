print("""
****FACTORIAL****
çıkmak için q
""")
while True:
    sayi = input("Sayıyı giriniz:")
    if (sayi =="q"):
        print("Çıkılıyor")
        break
    else:
        sayi = int(sayi)
        factorial = 1
        for i in range(factorial, sayi+1):
            factorial *= i
        print("Factorial: {}".format(factorial))
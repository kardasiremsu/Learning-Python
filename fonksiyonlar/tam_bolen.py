def tam_bolen(sayi):
    tambolenler = []
    for i in range(2,sayi):
        if sayi % i ==0:
            tambolenler.append(i)
    return tambolenler

while True:
    sayi = input("Sayi:")
    if(sayi == "q"):
        print("Sonlandırılıyor...")
        break
    else:
        sayi = int(sayi)
        print("Tam bolenler:",tam_bolen(sayi))

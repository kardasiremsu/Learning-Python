print(""""***********************************
      HESAP MAKİNESİ
      1. TOPLAMA
      2. ÇIKARMA
      3. ÇARPMA
      4. BÖLME
***********************************""")
a = int(input("Birinci sayı:"))
b = int(input("İkinci sayı:"))
islem = int(input("İslemi giriniz:"))

if islem ==1:
    print("{} + {} = {}".format(a,b,a+b))
elif islem ==2:
    print("{} - {} = {}".format(a, b, a - b))
elif islem == 3:
    print("{} * {} = {}".format(a, b, a * b))
elif islem ==4:
    print("{} / {} = {}".format(a, b, a / b))
else:
    print("Gecersiz islem...")
#Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.

a = int(input("1. sayı:"))
b = int(input("2. sayı:"))
c = int(input("3. sayı:"))
print("{}, {}, {} nın çarpımı {}'dır.".format(a,b,c,a*b*c))
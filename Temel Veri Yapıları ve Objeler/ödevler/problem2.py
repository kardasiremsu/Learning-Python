#Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

boy = float(input("Boy:"))
kilo = int(input("Kilo:"))

bki = kilo / (boy*boy)
print("Beden Kitle İndeksiniz:",bki)
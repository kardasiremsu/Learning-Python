#Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.

a = int(input())
b = int(input())
c = int(input())
if a>b and a>c:
    print("En büyük sayı",a)
elif b>a and b>c:
    print("En büyük sayı",b)
elif c>a and c>b:
    print("En büyük sayı",c)
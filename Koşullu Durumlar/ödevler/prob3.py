"""
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre toplam hesaplayın.

    Vize1 toplam notun %30'una etki edecek.
    Vize2 toplam notun %30'una etki edecek.
    Final toplam notun %40'ına etki edecek.

"""
vize1 = int(input("Vize1:"))
vize2 = int(input("Vize2:"))
final = int(input("Final:"))
toplam = vize1*0.3 + vize2 *0.3 + final *0.4
print(toplam)
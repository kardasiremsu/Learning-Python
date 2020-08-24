import math
import time
class Bilgisayar():
    def __init__(self,pc_durum ="KAPALI", pc_parlaklık = 10 , fotolistesi = []):
        self.pc_durum = pc_durum
        self.pc_parlaklık = pc_parlaklık
        self.fotolistesi= fotolistesi

    def pc_ac(self):
        if(self.pc_durum == "AÇIK"):
            print("Bilgisayar zaten açık")
        else:
            print("Bilgisayar açılıyor...")
            self.pc_durum = "AÇIK"
            print(self.pc_durum)
    def pc_kapat(self):
        if (self.pc_durum == "KAPALI"):
            print("Bilgisayar zaten kapalı")
        else:
            print("Bilgisayar kapanıyor...")
            self.pc_durum = "KAPALI"
            print(self.pc_durum)
    def parlaklık(self):
        while True:
            cevap = input("Arttırmak için +, azaltmak için - ye basın.")
            if(cevap == "+"):
                self.pc_parlaklık+=1
                print("Parlaklık:",self.pc_parlaklık)
            elif(cevap =="-"):
                self.pc_parlaklık -=1
                print("Parlaklık:", self.pc_parlaklık)
            else:
                print("Parlaklık güncellendi: {}".format(self.pc_parlaklık))
                break
    def fotoekle(self):
        while True:
            eklenecek_foto = input("Eklenecek fotoğrafları ',' ile yazın, çıkmak için q ya basın:")
            if (eklenecek_foto == "q"):
                break
            eklenecek_listesi = eklenecek_foto.split(",")
            for i in eklenecek_listesi:
                self.fotolistesi.append(i)
                print("Fotoğraf eklendi..")
                time.sleep(1)
            print("Fotoğraflar: {}".format(self.fotolistesi))

    def fotosayisi(self):
        sayi = len(self.fotolistesi)
        print(sayi)
    def foto_sil(self):
        while True:
            cevap = int(input("Kacıncı fotoyu silmek istersiniz çıkmak için '0':"))
            if(cevap ==0):
                break
            elif(cevap <=len(self.fotolistesi)):
                print("{} Siliniyor......".format(self.fotolistesi[cevap-1]))
                del(self.fotolistesi[cevap-1])
                time.sleep(1)
                print("Güncellendi: {}".format(self.fotolistesi))
            else:
                print("Bu sayıda fotoğraf yok çıkılıyor...")
                break



    def __str__(self):
        return "PC DURUMU:{}\n EKRAN PARLAKLIĞI: {}\n FOTO LİSTESİ:{}".format(self.pc_durum,self.pc_parlaklık,self.fotolistesi)
    def hesapmakinesi(self):

        while True:
            print(""" 
            *******************
            İŞLEM SEÇİNİZ
            1) TOPLAMA
            2) ÇIKARMA
            3) BÖLME
            4) ÇARPMA
            5) SİN ALMA
            6) COS ALMA
            *********************
            """)
            islem = int(input("İsleminiz:"))
            if(islem ==1):
                a = float(input())
                b = float(input())
                print(a+b)
            elif(islem ==2):
                a = float(input())
                b = float(input())
                print(a-b)
            elif (islem == 3):
                a = float(input())
                b = float(input())
                print(a / b)
            elif (islem == 4):
                a = float(input())
                b = float(input())
                print(a * b)
            elif (islem == 5):
                a = float(input())
                print(math.sin(math.radians(a)))
            elif (islem == 6):
                a = float(input())
                print(math.cos(math.radians(a)))
            else:
                print("GECERSİZ İSLEM.....")
                break

bilgisayarım = Bilgisayar()
print("""

Bilgisayar


1. Bilgisayar Aç

2. Bilgisayar Kapat

3. Bilgisayar Parlaklık Ayarları

4. Foto Ekle

5. Foto Sayısını Öğrenme

6. Foto Silme

7. Bilgisayar Bilgileri

8. Hesap Makinesi

Çıkmak için '0' ya basın.
""")


while True:
    islem = int(input("İşlem seçiniz:"))
    if(islem ==1):
        bilgisayarım.pc_ac()
    elif(islem ==2):
        bilgisayarım.pc_kapat()
    elif(islem ==3):
        bilgisayarım.parlaklık()
    elif(islem ==4):
        bilgisayarım.fotoekle()
    elif(islem ==5):
        bilgisayarım.fotosayisi()
    elif(islem ==6):
        bilgisayarım.foto_sil()
    elif (islem == 7):
        print(bilgisayarım)
    elif (islem == 8):
        bilgisayarım.hesapmakinesi()
    else:
        print("GECERSİZ İSLEM.....")
        break

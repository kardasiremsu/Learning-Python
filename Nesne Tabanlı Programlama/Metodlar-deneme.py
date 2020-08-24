import time

class Yazilimci():
    def __init__(self,isim,soyisim,numara,maas,diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maas = maas
        self.diller = diller
    def bilgilerigoster(self):
        print("""
        ******************
        Yazılımcının:
        Adı: {}
        Soyadı:  {}
        Numarası: {}
        Maaşı: {}
        Bildiği Diller: {}
        *****************
        """.format(self.isim,self.soyisim,self.numara,self.maas,self.diller))
    def zam_yap(self,zam_miktarı):
        print("Zam yapılıyor...")
        time.sleep(1)
        self.maas += zam_miktarı
        print("Yeni maas: {}".format(self.maas))
    def dil_ekle(self,dil):
        print("Dil ekleniyor...")
        time.sleep(1)
        self.diller.append(dil)
        print("Yeni bildiği diller: {}".format(self.diller))
    def isim_degistir(self,yeni_isim):
        self.isim = yeni_isim

Yazılımcı1 = Yazilimci("İremsu","Kardaş",123,15000,["C","HTML","CSS","Python"])
Yazılımcı1.bilgilerigoster()
Yazılımcı1.zam_yap(2000)
Yazılımcı1.bilgilerigoster()
Yazılımcı1.dil_ekle("Java")
Yazılımcı1.bilgilerigoster()
Yazılımcı1.isim_degistir("Usmeri")
Yazılımcı1.bilgilerigoster()
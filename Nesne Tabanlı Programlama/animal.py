"""
Hayvan Sınıfı ------> Bütün hayvanların ortak özelliklerinin toplandığı sınıf olacak.

Köpek Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa köpeklere ait ek özellikler ve metodlar ekleyin.
.
"""
class Hayvan():
    def __init__(self,sinirsistemi="var", cokhücrelilik ="evet",eseyliüreme = "var",hareket = "var",hayat = "Bilgi Yok"):
        print("Hayvanın initi")
        self.sinirsistemi = sinirsistemi
        self.cokhücrelilik = cokhücrelilik
        self.eseyliüreme = eseyliüreme
        self.hareket = hareket
        self.hayat = hayat
    def hayattamı(self):
        self.hayat = input("E/H")
        if(self.hayat =="E"):
            print("Hayattadır..")
        elif(self.hayat =="H"):
            print("Hayatta değildir..")
        else:
            print("Geçersiz..")
class Köpek(Hayvan):
    def __init__(self,sinirsistemi,cokhücrelilik,eseyliüreme,hareket,hayat,havlama ="Var"):

        super().__init__(sinirsistemi,cokhücrelilik,eseyliüreme,hareket,hayat)
        print("Köpeğin initi")
        self.havlama = havlama
    def hırcınmı(self):
        hırcın = input("E/H")
        if (hırcın == "E"):
            print("hırcın..")
        elif (hırcın == "H"):
            print("hırcın değildir..")
        else:
            print("Geçersiz..")

köpek1 = Köpek("var","var","var","var","var")
hayvan1 = Hayvan()
köpek1.hayattamı()
köpek1.hırcınmı()
hayvan1.hayattamı()



def mutlak(a,b):
    if(a>b):
        print(a-b)
    else:
        print(b-a)

def faktoriyel(a):
    if(a<0):
        print("0'dan büyük bir sayı giriniz")
    else:
        fak = 1
        while(a>1):
            fak = a*fak
            a-=1
    print("Faktoriyel = {}".format(fak))

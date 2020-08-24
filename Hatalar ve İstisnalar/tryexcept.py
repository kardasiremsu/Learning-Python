liste = ["345","sadas","324a","14","kemal"]
for i in liste:
    try:
        print(int(i))
    except ValueError:
        print("Hata")
        #pass yazarsan hatasız devam eder.
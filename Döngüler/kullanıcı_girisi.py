print("""
****************************
   User Checking Program
****************************
""")
sys_username = "usmeri"
sys_password = "12345" #if it isnt string we should change input too
entry =0

while True:

    user = input("Username:")
    password = input("Password:")
    if(user == sys_username and password != sys_password):
        print("Your password is wrong.")
        entry +=1
    elif(user != sys_username and password == sys_password):
        print("Your username is wrong.")
        entry += 1
    elif(user != sys_username and password != sys_password):
        print("Your username and password is wrong.")
        entry += 1
    else:
        print("Successful login to the system...")
        break
    if(entry == 3):
        print("Your right of entry is finished...")
        break


print("""
****************************
        ATM MACHINE
        
1. Querying the Balance (bakiyeyi sorgulama)

2. Deposit Money (para yatırma)

3. Withdrawal (para çekme)

If you want to exit program, press 'q'

****************************
""")

balance =1000
while True:
    operation = input("Select your operation:")
    if(operation != "q"):
        operation = int(operation)
    else:
        print("Program exits...")
        break

    if(operation ==1):
        print("Your balance is:",balance)
    elif(operation ==2):
        deposit = int(input("How much money will you deposit?:"))
        balance += deposit
    elif(operation ==3):
        withdrawal = int(input("How much money will you withdraw?:"))
        if(balance-withdrawal <0):
            print("Not enough money for this.")
            continue
        balance -= withdrawal
    else:
        print("Please choose valid operation")

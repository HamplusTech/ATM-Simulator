#A program to simulate the ATM - Deposit, Withdrawal, Transfer, Recharge and Check Balance
banks = {"Access" :
                 [{1012311453 : ["James Peter", 3000, 2347056423211]},
                     {1101234156 : ["Rita Kings", 39000, 2347050923211]},
                   {1011211222 : ["Paul Pamela", 45000, 2347056429911]}],
                 "Ecobank" :
                 [{1012531453 : ["James Paul", 12300, 2348036423211]},
                  {1101278866 : ["Grace James", 3000, 2347045223211]},
                   {1011000022 : ["Anna Rita", 608230, 2347032123211]}],
                 "Gtb":
                 [{1222311453 : ["John Peters", 21334, 2347033323211]},
                  {1102211156 : ["Timilayo Grace James", 23924, 2347023423211]},
                   {1241211222 : ["Agatha Miracle Eze", 452111, 2347012423211]}]}

def deposit(acc_num=3581042343, bank="Ecobank", amount=1000):
    try:
        acc_num = int(input("Please account number\n"))
        bank = input("Please bank name\n")
        
        if len(str(acc_num)) != 10 or type(acc_num) != int:
            print (f"{acc_num} must be integer and the length must be 10 digits\n")
        elif bank not in banks:
            print(f"{bank} does not exist. Please enter the bank name correctly entered\n")
        else:
            for i in range(len(banks[bank])):
                if acc_num not in banks[bank][i]:
                    print(f"Wrong Account Number. You entered {acc_num} in {bank}\n")
                    break
                elif acc_num in banks[bank][i]:
                    print (f"This is the account name - {banks[bank][i][acc_num][0]}")
                    amount = float(input("Please enter amount to deposit (no punctuation marks)\n"))
                    print(f"Account has been credited!")
                    break
    except:
        print("There was an error from your input")
    
def withdrawal(acc_num=3581042343, bank="Ecobank", amount=1000):
    try:
        acc_num = int(input("Please account number\n"))
        bank = input("Please bank name\n")
        
        if len(str(acc_num)) != 10 or type(acc_num) != int:
            print (f"{acc_num} must be integer and the length must be 10 digits\n")
        elif bank not in banks:
            print(f"{bank} does not exist. Please enter the bank name correctly entered\n")
        else:
            for i in range(len(banks[bank])):
                if acc_num not in banks[bank][i]:
                    print(f"Wrong Account Number. You entered {acc_num} in {bank}\n")
                    break
                elif acc_num in banks[bank][i]:
                    print (f"This is the account name - {banks[bank][i][acc_num][0]}")
                    amount = float(input("Please enter amount to withdraw (no punctuation marks)\n"))
                    if banks[bank][i][acc_num][1] < amount:
                        print(f"Insufficient account balance - Present account balance is {banks[bank][i][acc_num][1]}")
                    else:
                        print(f"Account has been debited!")
                    break
    except:
        print("There was an error from your input")
    
def transfer(acc_source=3581042343, bank_source="Ecobank", acc_destination=3581042343, bank_destination="Ecobank", amount=1000):
    try:
        acc_source = int(input("Please source account number\n"))
        bank_source = input("Please source bank name\n")
        acc_destination = int(input("Please destination account number\n"))
        bank_destination = input("Please destination bank name\n")
        
        if len(str(acc_source)) != 10 or type(acc_source) != int:
            print (f"{acc_source} must be integer and the length must be 10 digits\n")
        elif len(str(acc_destination)) != 10 or type(acc_destination) != int:
            print (f"{acc_destination} must be integer and the length must be 10 digits\n")
        elif bank_source not in banks:
            print(f"{bank_source} does not exist. Please enter the source bank name correctly entered\n")
        elif bank_destination not in banks:
            print(f"{bank_destination} does not exist. Please enter the destination bank name correctly entered\n")
        else:
            for i in range(len(banks[bank_source])):
                if acc_source not in banks[bank_source][i]:
                    print(f"Wrong Source Account Number. You entered {acc_source} in {bank_source}\n")
                    break
                elif acc_source in banks[bank_source][i]:
                    print (f"This is the source account name - {banks[bank_source][i][acc_source][0]}")
                    amount = float(input("Please enter amount to transfer (no punctuation marks)\n"))
                    if banks[bank_source][i][acc_source][1] < amount:
                        print(f"Insufficient account balance - Present account balance is {banks[bank_source][i][acc_source][1]}")
                    else:
                        for i in range(len(banks[bank_destination])):
                            if acc_destination not in banks[bank_destination][i]:
                                print(f"Wrong Destination Account Number. You entered {acc_destination} in {bank_destination}\n")
                                break
                            elif acc_destination in banks[bank_destination][i]:
                                print (f"This is the destination account name - {banks[bank_destination][i][acc_destination][0]}")
                                print(f"{acc_destination} has been credited with {amount}!")
                                break
                        print(f"{acc_source} has been debited with {amount}!")
                    break
    except:
        print("There was an error from your input")    

def recharge(acc_num=3581042343, bank="Ecobank", amount=1000, mobile=2347063047037):
    try:
        acc_num = int(input("Please account number\n"))
        bank = input("Please bank name\n")
        
        if len(str(acc_num)) != 10 or type(acc_num) != int:
            print (f"{acc_num} must be integer and the length must be 10 digits\n")
        elif bank not in banks:
            print(f"{bank} does not exist. Please enter the bank name correctly entered\n")
        else:
            for i in range(len(banks[bank])):
                if acc_num not in banks[bank][i]:
                    print(f"Wrong Account Number. You entered {acc_num} in {bank}\n")
                    break
                elif acc_num in banks[bank][i]:
                    print (f"This is the account name - {banks[bank][i][acc_num][0]}")
                    amount = float(input("Please enter amount to recharge (no punctuation marks)\n"))
                    if banks[bank][i][acc_num][1] < amount:
                        print(f"Insufficient account balance - Present account balance is {banks[bank_source][i][acc_source][1]}")
                    else:
                        mobile = int(input("Please enter the mobile number (e.g 2348050736053)\n"))
                        if mobile not in banks[banks.keys()][i]:
                            print(f"Invalid Mobile --- {mobile}")
                        else:
                            print(f"Account ({acc_num}) has been debited and mobile ({mobile}) has been credited!")
                    break

    except ValueError:
        print("There was an error from your input")
    

def check_balance(acc_num=3581042343, bank="Ecobank"):
    try:
        acc_num = int(input("Please account number\n"))
        bank = input("Please bank name\n")
        
        if len(str(acc_num)) != 10 or type(acc_num) != int:
            print (f"{acc_num} must be integer and the length must be 10 digits\n")
        elif bank not in banks:
            print(f"{bank} does not exist. Please enter the bank name correctly entered\n")
        else:
            for i in range(len(banks[bank])):
                if acc_num not in banks[bank][i]:
                    print(f"Wrong Account Number. You entered {acc_num} in {bank}\n")
                    break
                elif acc_num in banks[bank][i]:
                    print (f"Your account balance is {banks[bank][i][acc_num][1]}")
                    break
    except:
        print("There was an error from your input")
        
    
while True:
    ops = int(input("Welcome! Please select an operation\
                    \n1 --- Check Balance\n2 --- Deposit\n3 --- Transfer\
                    \n4 --- Withdrawal\n5 --- Recharge\n\nType 0 to exit.\n\n"))
    if ops == 0:
        break
    elif ops == 1:
        check_balance()
    elif ops == 2:
        deposit()
    elif ops == 3:
        transfer()
    elif ops == 4:
        withdrawal()
    elif ops == 5:
        recharge()
    else:
        print("You did not select an operation. \nBye!!!")
        break

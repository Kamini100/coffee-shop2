def welcome():
    print("welcome to our coffee shop!!!")

def menu():
    print("press 1:for hot coffee Rs.70\npress 2:for cold coffee Rs.110\npress 3:for chocolate coffee Rs.150\n")

def size():
    print("press 1:for small Rs.25\npress 2:for medium Rs.50\npress 3:for large Rs.75")

def invoice(choice1,choice2,quantity):
    global bill
    if choice1==1 and choice2==1:
        bill=quantity*(70+25)
        print("take your small hot coffee")
        print("here's your bill : ",bill)
    elif choice1==1 and choice2==2:
        bill=quantity*(70+50)
        print("take your medium hot coffee")
        print("here's your bill : ",bill)
    elif choice1==1 and choice2==3:
        bill=quantity*(70+75)
        print("take your large hot coffee")
        print("here's your bill : ",bill)
    elif choice1==2 and choice2==1:
        bill=quantity*(110+25)
        print("take your small cold coffee")
        print("here's your bill : ",bill)
    elif choice1==2 and choice2==2:
        bill=quantity*(110+50)
        print("take your medium cold coffee")
        print("here's your bill : ",bill)
    elif choice1==2 and choice2==3:
        bill=quantity*(110+75)
        print("take your large cold coffee")
        print("here's your bill : ",bill)
    elif choice1==3 and choice2==1:
        bill=quantity*(150+25)
        print("take your small chocolate coffee")
        print("here's your bill : ",bill)
    elif choice1==3 and choice2==2:
        bill=quantity*(150+50)
        print("take your medium chocolate coffee")
        print("here's your bill : ",bill)
    elif choice1==3 and choice2==3:
        bill=quantity*(150+75)
        print("take your large chocolate coffee")
        print("here's your bill : ",bill)
    else:
        print("entered option is wrong")

def return_amt(user_pay,bill):
    exchange=user_pay-bill
    print("take your remaing amount : ",exchange)
    

while True:
    welcome()
    menu()
    flavour=int(input("enter number to select your flavour : "))
    size()
    size=int(input("enter number to select size : "))
    quan=int(input("enter number of quantity you want : "))
    invoice(flavour,size,quan)
    user_pay=int(input("pay the amount : "))
    return_amt(user_pay,bill)
    reply=input("want to take another coffee press y/n : ")
    if reply=='n':
        break

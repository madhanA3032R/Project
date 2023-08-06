ch="y"
while ch=="y" or ch=="Y":
    ch=input("do you want to continue[y/n]")
    if ch=="n":
        break
    b=int(input("enter the value"))
    print("according to value")
    if b%2==0:
        print("It is even")
        print("please enter even number in a")
        a=int(input("enter the number 1-6"))
        print("Throw the dice")
    elif b%2==1:
        print("It is odd")
        print("please enter odd number in a")
        a=int(input("enter the number 1-6"))
    if a==1:
        print("one")
        print("You won the Match")
    elif a==2:
        print("two")
        print("You won the Match") 
    elif a==4:
        print("five")
        print("Better luck next time")
    elif a==5:
        print("Four")
        print("Better luck next time")
    elif a==6:
        print("six")
        print("You won the Match")
    elif a==3:
        print("three")
        print("You won the Match")
    elif a>6:
        print("you will not get the result because the number is greater than 6")
              
    
    
        
        
    

import random

again="y"
while again.lower()=="y":
    r=random.randint(1,100)
    chances=0
    while True:
        num=int(input("Enter your Guess (0-100): "))

        if num==r:
            chances+=1
            print("you Won")
            print("You took ",chances,"to Guess right")
            again=input("Do you want to try again?(Y/N):")
            if again.lower()!="y":
                break
        elif num>r:
            chances+=1
            print("Your Guess is Higher")
        else:
            chances+=1
            print("Your guess is Lower")


    

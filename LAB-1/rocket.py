def launch(n):
    if n==0:
        print("Launch")
        return
    print(n)
    launch(n-1)
n=int(input("Enter the duration of the Countdown : "))
launch(n)

#Alternate
"""
def launch(n):
    while n>0:
        return n
    else:
        return "Launch"
n=int(input("Enter Number : "))
while n>=0:
    print(launch(n))
    n-=1
"""

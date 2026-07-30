print(f"welcome to List method Simulator :\n1.Remove duplicates \n2.Count frequency\n3.Maximim number in arr\n4.Minimum number in array \n5.Exit") 
l=int(input("Enter the length of the Array : "))
l1=[]
for i in range(l):
    a=int(input("Enter the value : "))
    l1.append(a)
c=int(input("Enter the choice between 1 to 4 : "))
def remove_dup():
    u=[]
    for i in l1:
        if i not in u:
            u.append(i)
    return u
def count():
    d={}
    for i in l1:
        d[i]=d.get(i,0) +1
    return d    
def maxi():
    return max(l1)
def mini():
    return min(l1)
while True:
    if c==1:
        print("Unique list: ",remove_dup())
    elif c==2:
        print("Count : ",count())
    elif c==3:
        print("Maximum Number : ",maxi())
    elif c==4:
        print("Minimum Number : ",mini())
    else:
        print("Invalid Choice")
    print()

    c=int(input("Enter your Choice (1-5) :"))
    print()

    if c ==5:
        print("Thank You")
        break

def primenumber(m):
    flag=0
    for i in range(2,m):
        if(m%i==0):
            flag+=1
            break
    return flag        
s=int(input("Enter the Number="))
k=primenumber(s)
if(k==1):
    print("Not Prime Number")
elif(s==1):
    print("Your entered number is 1 so it is not a prime and non primenumber")
else:
    print("Prime Number")

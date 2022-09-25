def Oddnumber(m,n):
    i=m
    while i<n:
        if(i%2!=0):
            print(i)
        i+=1
        
m=int(input("Enter the Start Number="))
n=int(input("Enter the last Number="))
Oddnumber(m,n)

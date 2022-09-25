def fibonacciseries(n):
    a=0;
    b=1
    print(a,end=" ")
    print(b,end=" ")
    for i in range(1,n):
        c=a+b
        print(c,end=" ")
        a=b
        b=c

n=int(input('Enter the number'))
fibonacciseries(n)
        
        

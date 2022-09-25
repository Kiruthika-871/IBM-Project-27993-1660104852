def primenumber(m):
    flag=0
    for i in range(2,m):
        if(m%i==0):
            flag+=1
            break
    return flag        
s=int(input("Enter a number="))
for i in range(2,s):
      k=primenumber(i)
      if(k==0):
          print(i)

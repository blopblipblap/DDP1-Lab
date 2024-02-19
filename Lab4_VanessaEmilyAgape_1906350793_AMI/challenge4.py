list=[]
X=input()
N=input()
x=X.split(" ")
n=N.split(" ")
for c in x:
    f=int(c)
for a in n:
    list.append(a)
for b in list:
    for d in list:
        h=int(b)
        i=int(d)
        if h+i==f:
            j=str(h)
            k=str(i)
            print(j+'+'+k)
        break
            
        
    

n=int(input())
c=0
for b in range(c, n+1):
    while (1<=n<=100):
        c+=1
        a=int(input())
        if (a!=c):
            print(c)
            c+=1
            if (a==n):
                break
            continue
        elif (c==n):
            break
        else:
            continue
    break



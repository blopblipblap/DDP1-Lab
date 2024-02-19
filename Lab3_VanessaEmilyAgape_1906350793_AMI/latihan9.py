oke=0
oke+=1
x=0
print(x)
while (oke==1):
    counter=0
    counter+=1
    perintah=input()
    while (counter==1):
        if (perintah=="TAMBAH"):
            x+=1
            print(x)
            counter-=1
        elif (perintah=="KURANG"):
            if (x==0):
                oke-=1
                break
            else:
                x-=1
                print(x)
                counter-=1
        else:
            break
    continue

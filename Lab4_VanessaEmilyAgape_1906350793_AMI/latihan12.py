f=open('input.txt', 'r')
list=[]
for baris in f.read().split('\n'):
    if baris.isnumeric()==True:
        num=int(baris[::-1])
        list.append(num)
a=max(list)
for i in list:
    if i!=a:
        print(i)
    else:
        pass


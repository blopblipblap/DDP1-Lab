f=open('input.txt', 'r')
counter=0
for baris in f.read().split('\n'):
   if baris.isnumeric()==True:
       counter+=1
print(counter)

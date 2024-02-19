def hitung_kelipatan(A, x):
    counter1=0
    for oke in A:
        okee=int(oke)
        if (okee%x==0):
            counter1+=1
            continue
    return counter1
            
A = input().split()
for i in range(len(A)):
    A[i] = int(A[i])
print(hitung_kelipatan(A, 3) + hitung_kelipatan(A, 5) - hitung_kelipatan(A, 15))

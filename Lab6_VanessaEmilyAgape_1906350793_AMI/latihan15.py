# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:28:48 2019

@author: Vanessa
"""

def isi_matriks(N, M):
    list1=[]
    for baris in range(N):
        isi1=input("isi woi: ").split(" ")
        list1.append(isi1)
        if len(isi1)==M:
            continue
    return list1
def jml_matriks(A, B):
    lista=[]
    listb=[]
    listjml=[]
    for a in A:
        for satuan in a:
            satuan=int(satuan)
            lista.append(satuan)
    for b in B:
        for satuan2 in b:
            satuan2=int(satuan2)
            listb.append(satuan2)
    for i in range(len(lista)):
        jml=lista[i]+listb[i]
        listjml.append(jml)
    return listjml
def print_matriks(A):
    if int(len(A)%2!=0):
        print(c, end=" ")
    for c in range(int(len(A)/2)):
        print(A[c], end=" ")
    print("\n")
    for c in range(int(len(A)/2), int(len(A))):
        print(A[c], end=" ")

N, M = input().split(" ") 
N = int(N) 
M = int(M)
A= isi_matriks(N, M)
B= isi_matriks(N, M)
print(A)
print_matriks(jml_matriks(A, B))



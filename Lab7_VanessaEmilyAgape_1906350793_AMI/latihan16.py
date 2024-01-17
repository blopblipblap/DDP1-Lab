# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:02:51 2019

@author: Vanessa
"""
def angkataan(a):
    for i in range(a):
        mhs=input()
        mhs_split=mhs.split(" ")
        if mhs_split[1] in angkatan:
            angkatan[mhs_split[1]].append(mhs_split[0])
        else:
            angkatan[mhs_split[1]]=[mhs_split[0]]
    return angkatan
        
def print_indah():
    for key,value in angkatan.items():
        print(key, ":", value)
        
angkatan={}
yang_hadir=int(input())
angkataan(yang_hadir)
print_indah()
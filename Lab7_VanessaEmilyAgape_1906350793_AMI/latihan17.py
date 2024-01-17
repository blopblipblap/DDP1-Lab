def absen():
    daftar=open("daftar-kucing.txt", "r")
    for kucing in daftar.read().split('\n'):
        if kucing not in ok_SET:
            yang_tidak_hadir.append(kucing)
        else:
            yang_hadir.append(kucing)
    yang_tidak_hadir_SET=set(yang_tidak_hadir)
    return yang_tidak_hadir_SET 

def print_tdk_hadir(b):
    for a in b:
        print(a)

def persentase(b):
    daftar=open("daftar-kucing.txt", "r")
    for kucing in daftar.read().split('\n'):
        semua.append(kucing)
    semua_SET=set(semua)
    banyak_kocheng=len(semua_SET)
    banyak_tidacc_datang=len(b)
    if ((banyak_kocheng-banyak_tidacc_datang)/banyak_kocheng)<(50/100):
        print("Yuk ikut eval!")
    else:
        pass
        

ok=[]
semua=[]
yang_hadir=[]
yang_tidak_hadir=[]

kocheng=int(input())
for i in range(kocheng):
    cat=str(input())
    ok.append(cat)
    
ok_SET=set(ok)

absen()
print_tdk_hadir(absen())
persentase(absen())

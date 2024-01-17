def decipher_requiem(a):
    if len(a)==1:
        return a
    else:
        return a[-1] + decipher_requiem(a[0:len(a)-1])

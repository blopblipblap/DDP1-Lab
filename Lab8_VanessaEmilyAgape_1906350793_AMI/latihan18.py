def decipher(a,b):
    if len(a)==1:
        if a in b:
            return ""
        else:
            return a
    else:
        if a[0] in b:
            return "" + decipher(a[1::],b)
        else:
            return a[0] + decipher(a[1::],b)


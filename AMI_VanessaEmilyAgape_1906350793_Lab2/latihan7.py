andi_budi=input("Andi vs Budi: ")
andi_cakra=input("Andi vs Cakra: ")
budi_cakra=input("Budi vs Cakra: ")

cakra="Gunting"

if (andi_budi=="Andi menang"):
    andi="batu"
    budi="gunting"
    cakra="batu"
elif (andi_budi=="Budi menang"):
    andi="gunting"
    budi="batu"
    cakra="gunting"
elif (andi_budi=="Seri"):
    andi="batu"
    budi="batu"
    cakra="batu"
elif (andi_budi=="Seri"):
    andi="gunting"
    budi="gunting"
    cakra="gunting"
    
    
if (andi_cakra=="Andi menang"):
    if (andi=="batu"):
        cakra="gunting"
    else:
        cakra="tidak mungkin"
elif (andi_cakra=="Cakra menang"):
    if (andi=="gunting"):
        cakra="batu"
    else:
        cakra="tidak mungkin"
elif (andi_cakra=="Seri"):
    if (andi=="batu"):
        cakra="batu"
    else:
        cakra="gunting"

        
if (budi_cakra=="Budi menang"):
    if (budi=="gunting"):
        cakra="tidak mungkin"
    else:
        if (cakra=="batu"):
            cakra="tidak mungkin"
elif (budi_cakra=="Cakra menang"):
    if (budi=="gunting"):
        if (cakra=="gunting"):
            cakra="tidak mungkin"
        else:
            cakra="batu"
    else:
        cakra="tidak mungkin"
else:
    if (budi=="gunting"):
        if(cakra=="batu"):
            cakra="tidak mungkin"
        else:
            cakra="gunting"
    else:
        if (cakra=="gunting"):
            cakra="tidak mungkin"
        else:
            cakra="batu"


if (cakra=="tidak mungkin"):
    print("Tidak mungkin")
else:
    print("Andi bermain", andi)
    print("Budi bermain", budi)
    print ("Cakra bermain",cakra)
            


            
        
    

def dari_txt(a):
    f=open('okeh.txt','r')
    list=[]
    for baris in f.read().split('\n'):
        if (baris==("Myrmidon" or "Berserker" or "Lancer")):
            bariss="Fighter"
            list.append(bariss)
            continue
        elif (baris==("Jester" or "Marksman" or "Ninja")):
            bariss="Thief"
            list.append(bariss)
            continue
        elif (baris==("Warlock" or "Illusionist" or "Summoner")):
            bariss="Mage"
            list.append(bariss)
            continue
        else:
            pass
        list.append(baris)
    a=list[a]
    a=a.title()
    return a

f=open('okeh.txt','r')
print("Nama :",dari_txt(1),
      "\nTitle :",dari_txt(2),
      
      "\nClass :",dari_txt(3),
      "\n",
      "\n",dari_txt(1),"has these skills:",
      "\n",dari_txt(5),
      "\n",dari_txt(6),
      "\n",dari_txt(7),
      "\n",dari_txt(1),"has these weapons: ",
      "\n",dari_txt(1))
      
      
      




Extend = { "ADD"  : 0
         , "ADDC" : 0
         , "SUB"  : 0
         , "SUBB" : 0
         , "AND"  : 0
         , "NAND" : 0
         , "XOR"  : 0
         , "XNOR" : 0
         , "OR"   : 0
         , "NOR"  : 0
         , "LOAD" : 0
         , "STOR" : 0
         , "LDIO" : 0
         , "STIO" : 0
         , "JUMP" : 0
         , "BRCH" : 0
         , "MOVA" : 1
         , "MOVB" : 1
         , "PTRL" : 1
         , "PTRS" : 1
         , "INTL" : 1
         , "INTS" : 1
         , "HIGH" : 1
         , "LOW"  : 1
         , "BADD" : 1
         , "INC"  : 1
         , "DEC"  : 1
         , "SHFL" : 1
         , "SHFR" : 1
         , "FUNC" : 1
         , "ADFN" : 1
         , "RMFN" : 1
         , "MON"  : 1
         }

def extend(source,dest):
#Dictionary of which Instructions are in which Extension

    ilines = source.readlines()
    Toklist = []
    for i in ilines:
        tok = i.strip('\n').split()
        if tok == ['END']:
            break
        elif tok[0] == "##":
            pass
        elif tok[0] == '':
            pass
        else:
            Toklist.append(tok)

    Extlist = []
    for i in Toklist:
        if i[0] in Extend:
            Extlist.append((Extend[i[0]], i))
        else:
            Extlist.append((-1, i))

    Grouplist = []
    temp = []
    for i in Extlist:
        if i == []:
            pass
        elif temp == []:
            temp = [ i[0],i[1] ]
        elif i[0] == temp[0]:
            temp.append(i[1])
        elif i[0] == -1:
            temp.append(i[1])
        else:
            Grouplist.append(temp)
            temp = [i[0],i[1]]
    Grouplist.append(temp)

    Extended = []
    State = 0
    for i in Grouplist:
        if i[0] == -1:
            i = i[1:]
        elif State != i[0]:
            if len(i) > 2:
                i[0] = ['EXTT', str(i[0])]
                State = i[0]
            else:
                i[0] = ['EXT', str(i[0])]
        else:
            i = i[1::]
    print(Grouplist)
    Extendedlist = []
    for i in Grouplist:
        for j in i:
            Extendedlist.append(j)

    return(Extendedlist)

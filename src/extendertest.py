
def extend(source,dest):
#Dictionary of which Instructions are in which Extension
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
             , "MON"  : 1}

    ilines = source.readlines()
    stat = 0
    it = 0
    Temps = []
    x = " "
    for i in ilines: #Turns the input file into a list of lists
        tok = i.strip('\n').split()
        if tok == ['END']: #Ends the file -> List of lists function
            Temps.append(tok)
            break
        elif tok[0] == "##": #used to denote a comment line
            pass
        else:
            Temps.append(tok)
    One = False
    Two = False
#Scans the Temps list of lists 1 list at a time
    for i in Temps:
        Q = i[0]
#Skips "LIMM" since it can go in any Extension
        if Q == 'LIMM':
            continue
        elif Q == 'END':
            break
        elif Extend[Q] != stat:
            if it + 1 <= len(Temps):
                y = Temps[it + 1]
                if y[0] in Extend:
                    TOne = y
                    if Extend[TOne[0]] == Extend[i[0]]:
                        One = True
            if it + 2 <= len(Temps):
                z = Temps[it + 2]
                if z[0] in Extend:
                    TTwo = z
                    if Extend[TTwo[0]] == Extend[i[0]]:
                        Two = True
            if One and Two:
                Temps.insert(it, ["EXTT", str(Extend[i[0]])])
                stat = Extend[i[0]]
                it += 1
            else:
                Temps.insert(it, ["EXT", str(Extend[i[0]])])
                it += 1
        elif Extend[Q] == stat:
            continue
        it += 1
    print(Temps)

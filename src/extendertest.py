
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
             , "MON"  : 1
             }

    ilines = source.readlines()
    stat = 0
    it = 0
    Temps = []
    x = " "
    One = False
    Two = False
    for i in ilines: #Turns the input file into a list of lists
        tok = i.strip('\n').split()
        if tok == ['END']: #Ends the file -> List of lists function
            Temps.append(tok)
            break
        elif tok[0] == "##": #used to denote a comment line
            pass
        else:
            Temps.append(tok)
#Scans the Temps list of lists 1 list at a time
    for i in Temps:
        Q = i[0]
#Skips "LIMM" since it can go in any Extension
        if Q == 'LIMM':
            continue
        elif Q == 'END':
            break
        elif Q == "##": #used to denote a comment line
            continue
        print(Extend[Q])
        if Extend[Q] == stat:
            continue
#Checks if the current Inst's needed Extension status, matches the CPU's
#Extension state
        elif Extend[Q] != stat:
#Checks if the next Inst and the current Inst have the same Ext
            if it + 1 <= len(Temps):
                TOne = Temps[it + 1]
                if TOne[0] in Extend:
                    if Extend[TOne[0]] == Extend[Q]:
                        One = True
#Checks if the next next Inst and the current Inst have the same Extension
            if it + 2 <= len(Temps):
                TTwo = Temps[it + 2]
                if TTwo[0] in Extend:
                    if Extend[TTwo[0]] == Extend[Q]: Two = True
#If the current and next 2 following Inst need the same Ext; toggle to that Ext
            if One and Two:
                Temps.insert(it, ["EXTT", str(Extend[Q])])
                stat = Extend[Q]
                it += 1
#Else-If the current Inst needs a different Ext state than the CPU is currently
#in, and neither or only 1 of the next 2 inst need the new Ext, temp Ext into
#the needed Inst
            else:
                Temps.insert(it, ["EXT", str(Extend[Q])])
                it += 1
#Else-if the current Inst and the CPU's current Ext match, do nothing
        print(Extend[Q])
        print('NEXT')
        it += 1
    print(Temps)

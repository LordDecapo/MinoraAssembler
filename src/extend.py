def extend(source,dest):
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
    status = [0,0]
    Temps = []

    for i in ilines:
        tok = i.strip('\n').split()
        if tok[0] in Extend:
            if Extend[tok[0]] == 0:
                if status[0] == 0:
                    status[1] = status[1] + 1
                elif status[0] == 1:
                    status[1] = 1
                    status[0] = 0
            elif Extend[tok[0]] == 1:
                if status[0] == 0:
                    status[1] = 1
                    status[0] = 1
                elif status[0] == 1:
                    status[1] = status[1] + 1
#            print(status)
        elif tok == ['END']:
            break
        x = " "
        stat = str(status[0])
        stat2 = str(status[1])
        line = x.join(tok)
        out = str(status[0])+ " " + str(status[1]) + " " + line
        out = out.split()
        print(out)
        Temps.append(out)

    stat = 0
    it = 0

    for i in Temps[::-1]:
        tik = i
        length = len(Temps)
        if tik[0] == stat:
            del tik[:2]
            #it ++
        elif tik[0] != stat:
            if tik[1] < 3:
                ins = ['EXT', str(tik[0])]
                print(ins)
                ##Temps.insert(i, ins)
                del tik[:2]
            elif tik[1] > 2:
                stat = tik[0]
                ins = ['EXTT', str(tik[0])]
                #print(ins)
                #Temps.insert(i, ins)
                del tik[:2]
#        print(tik)
#        print(stat)
    #print(Temps)
    #print(len(Temps))
    dest.close()

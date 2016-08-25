def extend(source, temp):
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
        elif tok == ['END']:
            break
        x = " "
        stat = str(status[0])
        stat2 = str(status[1])
        line = x.join(tok)
        out = stat + " " + stat2 + " " + line
        #print(out)
        temp.write(out + '\n')

    temp.close()

    return(temp)




def insert(source,dest):

    elines = reversed(source.readlines())
    stat = 0
    x = ' '
    for i in elines:
        tik = i.strip("\n").split(" ")
        if tik[0] == stat:
            del tik[0,1]
        elif tik[0] != stat:
            if tik[1] < 3:
                del tik[0,1]
                #Insert Ext.tik[0]
            if tik[1] > 2:
                del tik[0,1]
                stat = tik[0]
        print(tik)
    dest.close()

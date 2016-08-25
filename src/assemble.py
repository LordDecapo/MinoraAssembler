def assemble(source,dest):
    #Dictionaries of common instruction formats.
    Logical = { "ADD"  : "0000"
              , "ADDC" : "0001"
              , "SUB"  : "0010"
              , "SUBB" : "0011"
              , "AND"  : "0100"
              , "NAND" : "0101"
              , "XOR"  : "0110"
              , "XNOR" : "0111"
              , "OR"   : "1000"
              , "NOR"  : "1001"
              , "SHFL" : "0100"
              , "SHFR" : "0101"}

    Memory =  { "LOAD" : "10100"
              , "STOR" : "10110"
              , "LDIO" : "10101"
              , "STIO" : "10111"
              , "LIMM" : "11001"
              , "JUMP" : "11100"
              , "ADFN" : "10010"}

    VarBuff = { "EXT"  : "11000"
              , "EXTT" : "11010"
              , "MOVA" : "00001"
              , "MOVB" : "00000"
              , "INC"  : "00100"
              , "DEC"  : "00110"
              , "FUNC" : "10000"
              , "RMFN" : "10001"}

    ilines = source.readlines()

    def normalize(variable , length):
        D = length - len(variable)
        variable = D * '0' + variable
        return(variable)

    for i in ilines:
        tok = i.strip('\n').split()
        if tok == ['END']:
            break

        if tok != []:

            length = len(tok)

            if tok[0] == 'NOP':
                inst0 = '00000000' 
                dest.write(chr(int(inst0,2)))

            elif tok[0] == 'HALT':
                inst0 = '11011000' 
                inst1 = '00000000'
                dest.write(chr(int(inst0,2)))
                dest.write(chr(int(inst1,2)))

    #Decode 1st variable in instruction.
            elif length == 2:
                v0 = str(bin(int(tok[1])))
                v0 = v0[2:]
                v0 = normalize(v0 , 3)

    #VarBuff are the only instructions
    #that take just 1 variable.
                if tok[0] in VarBuff:
                    Op = VarBuff[str(tok[0])]
                    inst0 = Op + v0
                    inst1 = '00000000'
                    dest.write(chr(int(inst0,2)))
                    dest.write(chr(int(inst1,2)))

                elif tok[0] == 'HIGH':
                    inst0 = '00100' + v0
                    inst1 = '00000010'
                    dest.write(chr(int(inst0,2)))
                    dest.write(chr(int(inst1,2)))

                elif tok[0] == 'LOW':
                    inst0 = '00100' + v0
                    inst1 = '00000011'
                    dest.write(chr(int(inst0,2)))
                    dest.write(chr(int(inst1,2)))

                elif tok[0] == 'BADD':
                    inst0 = '00100' + v0
                    inst1 = '00000001'
                    dest.write(chr(int(inst0,2)))
                    dest.write(chr(int(inst1,2)))

    #Decode 2nd variable in instruction.
            elif length == 3:
                v0 = str(bin(int(tok[1])))
                v0 = v0[2:]
                v1 = str(bin(int(tok[2])))
                v1 = v1[2:]

                if tok[0] in Logical:
                    Op = Logical[str(tok[0])]
                    v0 = normalize(v0 , 1)
                    v1 = normalize(v1 , 3)
                    inst0 = Op + v0 + v1
                    dest.write(chr(int(inst0,2)))

                elif tok[0] in Memory:
                    Op = Memory[str(tok[0])]
                    v0 = normalize(v0 , 3)
                    v1 = normalize(v1 , 8)
                    inst0 = Op + v0
                    inst1 = v1
                    dest.write(chr(int(inst0,2)))
                    dest.write(chr(int(inst1,2)))

                elif tok[0] == 'PTRL':
                    v0 = normalize(v0 , 3)
                    v1 = normalize(v1 , 3)
                    inst0 = '00010' + v0
                    inst1 = '00000' + v1
                    dest.write(chr(int(inst0,2)))
                    dest.write(chr(int(inst1,2)))

                elif tok[0] == 'PTRS':
                    v0 = normalize(v0 , 3)
                    v1 = normalize(v1 , 3)
                    inst0 = '00010' + v0
                    inst1 = '00001' + v1
                    dest.write(chr(int(inst0,2)))
                    dest.write(chr(int(inst1,2)))

    #decodes the 3rd variable in the instruction.
            elif length == 4:
                v0 = str(bin(int(tok[1])))
                v0 = v0[2:]
                v0 = normalize(v0 , 2)
                v1 = str(bin(int(tok[2])))
                v1 = v0[2:]
                v1 = normalize(v1 , 3)
                v2 = str(bin(int(tok[3])))
                v2 = v1[2:]
                v2 = normalize(v2 , 8)

                if tok[0] == 'MON':
                    inst0 = '111' + v0 + v1
                    inst1 = v2
                    dest.write(chr(int(inst0,2)))
                    dest.write(chr(int(inst1,2)))

                elif tok[0] == 'BRCH':
                    inst0 = '111' + v0 + v1
                    inst1 = v2
                    dest.write(chr(int(inst0,2)))
                    dest.write(chr(int(inst1,2)))
                    print(tok[0])

    dest.close()
    status = 'Done'
    return(status)

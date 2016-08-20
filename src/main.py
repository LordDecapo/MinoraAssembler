import argparse

parser = argparse.ArgumentParser(description='An assembler for the Minora CPU\
        \ emulator')
parser.add_argument('Input', metavar='Input',  type=str,
        help='The file you want to run the Assembler and Scheduler on.')
parser.add_argument('Format', metavar='Format', type=str,
        help='The output format you want.')
parser.add_argument('Output', metavar='Output', type=str,
        help="path to output file")

args = parser.parse_args()
Input = args.Input
Format = args.Format
Output = args.Output
Ext = 0


try:
    source = open(Input, 'r')
except Exception as err:
    print("Unexpected error\n%s" % err)
    exit(1)
try:
    dest = open(Output, 'w')
except Exception as err:
    print("Unexpected error\n%s" % err)
    exit(1)

#Scan, auto add Ext ops here

#Scan, auto add Nop buffs here





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

for i in ilines:
    tok = i.strip('\n').split()
    if tok == ['END']:
        break

    if tok != []:

        length = len(tok)

    #Decode 1st variable in instruction.
        if length == 2:
            #print(tok)
            v0 = str(bin(int(tok[1])))
            v0 = v0[2:]

    #VarBuff are the only instructions
    #that take just 1 variable.
            if tok[0] in VarBuff:
                Op = VarBuff[str(tok[0])]
                Inst0 = Op + v0
                Inst1 = '00000000'
                print(tok[0])
                print(Inst0)
                print(Inst1)

            elif tok[0] == 'HIGH':
                Inst0 = '00100' + v0
                Inst1 = '00000010'
                print(tok[0])
                print(Inst0)
                print(Inst1)

            elif tok[0] == 'LOW':
                Inst0 = '00100' + v0
                Inst1 = '00000011'
                print(tok[0])
                print(Inst0)
                print(Inst1)

            elif tok[0] == 'BADD':
                Inst0 = '00100' + v0
                Inst1 = '00000001'
                print(tok[0])
                print(Inst0)
                print(Inst1)

    #Decode 2nd variable in instruction.
        elif length == 3:
            v0 = str(bin(int(tok[1])))
            v0 = v0[2:]
            v1 = str(bin(int(tok[2])))
            v1 = v1[2:]

            if tok[0] in Logical:
                Op = Logical[str(tok[0])]
                Inst0 = Op + v0 + v1
                print(tok[0])
                print(Inst0)

            elif tok[0] in Memory:
                Op = Memory[str(tok[0])]
                Inst0 = Op + v0
                Inst1 = v1
                print(tok[0])
                print(Inst0)
                print(Inst1)

            elif tok[0] == 'PTRL':
                Inst0 = '00010' + v0
                Inst1 = '00000' + v1
                print(tok[0])
                print(Inst0)
                print(Inst1)

            elif tok[0] == 'PTRS':
                Inst0 = '00010' + v0
                Inst1 = '00001' + v1
                print(tok[0])
                print(Inst0)
                print(Inst1)

            elif tok[0] == 'NOP':
                Inst0 = '00000000'
                print(tok[0])
                print(Inst0)

            elif tok[0] == 'HALT':
                Inst0 = '11011000'
                print(tok[0])
                print(Inst0)

    #decodes the 3rd variable in the instruction.
        elif length == 4:
            v0 = str(bin(int(tok[1])))
            v0 = v0[2:]
            v1 = str(bin(int(tok[2])))
            v1 = v0[2:]
            v2 = str(bin(int(tok[3])))
            v2 = v1[2:]

            if tok[0] == 'MON':
                Inst0 = '111' + v0 + v1
                print(tok[0])
                print(Inst0)
                print(Inst1)

            elif tok[0] == 'BRCH':
                Inst0 = '111' + v0 + v1
                Inst1 = '111' + v0 + v1
                print(tok[0])
                print(Inst0)
                print(Inst1)

source.close()
dest.close()

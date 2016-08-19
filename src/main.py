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

OpFormat0 =  { "ADD"  : "0000"
        , "ADDC" : "0001"
        , "SUB"  : "0010"
        , "SUBB" : "0011"
        , "AND"  : "0100"
        , "NAND" : "0101"
        , "XOR"  : "0110"
        , "XNOR" : "0111"
        , "OR"   : "1000"
        , "NOR"  : "1001"
        , "LD"   : "10100"
        , "ST"   : "10110"
        , "LDIO" : "10101"
        , "STIO" : "10111"
        , "EXT"  : "11000"
        , "EXTT" : "11010"
        , "LIMM" : "11001"
        , "JUMP" : "11100"
        , "SHFL" : "0100"
        , "SHFR" : "0101"
        , "ADFN" : "10010"
        , "RMFN" : "10001"}
OpFormat1 =  {
        }


ilines = source.readlines()

for i in ilines:
    tok = i.strip("\n").split()
    if tok == ['END']:
        break
#    if tok[0] == "BRCH" or "MON"

    if tok != []:
        #print(tok)
        v0 = str(bin(int(tok[1])))
        v1 = str(bin(int(tok[2])))

        v0 = v0[2:]
        v1 = v1[2:]

        Op = OpFormat1[str(tok[0])]

        Inst = Op + v0 + v1
        print(Inst)

source.close()
dest.close()

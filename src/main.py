import argparse
import extendertest
import assemble
import insert

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



try:
    source = open(Input, 'r')
except Exception as err:
    print("Unexpected error\n%s" % err)
    exit(1)
try:
    temp = open('temp.t', 'r+')
except Exception as err:
    print("Unexpected error\n%s" % err)
    exit(1)
try:
    dest = open(Output, 'r+')
except Exception as err:
    print("Unexpected error\n%s" % err)
    exit(1)

extendertest.extend(source, temp)
#temp = open('temp.t', 'w+')

#assemble.assemble(temp2,dest)

#ilines = dest.readlines()
#for i in ilines:
#    print(iline)


source.close()
dest.close()
temp.close()

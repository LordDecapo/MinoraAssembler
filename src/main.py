import argparse
#import extender
import assemble

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
    dest = open(Output, 'w')
except Exception as err:
    print("Unexpected error\n%s" % err)
    exit(1)

#extend.extend(source, dest)

assemble.assemble(source,dest)

source.close()
dest.close()

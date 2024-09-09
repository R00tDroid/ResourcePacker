import os, argparse

# Parse arguments from commandline
argument_parser = argparse.ArgumentParser(description='')

argument_parser.add_argument('-output', nargs=1, help="")
argument_parser.add_argument('-include', nargs="+",  help="")

arguments = argument_parser.parse_args()
os.makedirs(arguments.output[0], exist_ok=True)

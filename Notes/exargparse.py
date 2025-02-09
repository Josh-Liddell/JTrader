import argparse as ap

# NOTE:
# There is pretty much a way to handle arugments however you want just go back through and learn argparse
# Here I just have listed some exampples I am thinking I will use

# The add help part is default but you can turn it off.
parser = ap.ArgumentParser(description='A tool to run trade strategies on historical data', add_help=True)

# Action is 'store' by default which I thing stores the argument they entered to that flag
# You could use nargs=2 after filename below to force two filenesm to be entered instead of once, etc
# using * lets you add as many as you want + is same but requires 1 whereas * does not
parser.add_argument('filename', nargs='+', help='Filename of your historical price data')
parser.add_argument('-c', '--copy', metavar='N', type=int, help='Make N copies of the file')  # long form name not needed but it is nice to have
parser.add_argument('-s', '--something', action='store_const', const=15)  # Just an example, there is also store_true, etc
parser.add_argument('-v', '--version', action='version', version='example.py v1.0')  # Just an example, there is also store_true, etc
# parser.add_argument('-n', '--name', default='file_copy', choices=['name1', 'name2'])

# append action lets you add argument multiple, -s 1 -s 2 -s 3
# there is also append cost
# Multiple have have the same dest so you can add to it or whatever
#


# You can also use dest='destname to store the value of the variable in a name other than say copy or whatever'
# There is a useful parameter to convert values to specific type for validation or says it is not possible: Type
# There is also required=True to make option mandatory but not really recomended to do so


arguments = parser.parse_args()

print(arguments)
# print(arguments.filename)  # set this = file and can use it later

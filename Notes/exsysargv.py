import sys


def func1():
    print('First function')


def func2():
    print('Second function')


arguments = sys.argv[1:]

if len(arguments) != 1:
    print('Error you need 1 argument')

argument = arguments[0]

if argument in ('f', 'first'):
    func1()
elif argument in ('s', 'second'):
    func2()

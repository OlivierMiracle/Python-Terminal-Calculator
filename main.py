#!/usr/bin/env python3

import sys



def main():
    print("""    Welcome in my calculator!
    It doesn't work at all, yet!""")

    calc = input("Write your calculation here: ")
    interpretate(calc)

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def interpretate(calc):
    signs = {"+": add, "-": subtract}
    equasion = list()
    x = calc.rsplit()
    print(x)
    for i in x:
        for sign in list(signs.keys()):
            if sign == i:
                print(signs[sign](int(x[x.index(i) - 1]), int(x[x.index(i) + 1])))

if __name__ == '__main__': main()
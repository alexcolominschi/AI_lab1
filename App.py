from ReadWrite import *
from GenerareSiValidare import *


def main():
    for h in range(3):
        n = 0
        obiecte = list()
        capacitate = 0
        x = list()
        valoare = list()
        k = 10
        n, obiecte, capacitate = read()
        max = 0
        if(h == 1): k=15
        if (h == 2): k = 100
        for i in range(10):
            x1 = NEXT_ASCENT_HILL_CLIMBING(n, obiecte, capacitate, k)
            valoare1 = fitness(n, obiecte, x1)
            x.append(x1)
            valoare.append(valoare1)
            if(max < valoare1):
                max = valoare1
        for i in range(10):
            str = 'avarage'
            if(valoare[i]==max):
                str = 'best'
            write(x[i], valoare[i], k, str)
        write("", "", "", "")


main()

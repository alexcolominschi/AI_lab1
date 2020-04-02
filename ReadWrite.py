def read():
    obiecte = list()
    filepath = 'Read.TXT'
    f = open(filepath, 'r')
    n = int(f.readline())
    for i in range(n):
        line = f.readline()
        line = line.split()
        obiecte.append(line)
    capacitate = int(f.readline())
    f.close()
    return n, obiecte, capacitate


def write(afisare, valoare, k, st):
    f = open("Write.TXT", "a")
    if(afisare.__len__()):
        f.write('Valoare=')
        f.write(str(valoare))
        f.write(' k=')
        f.write(str(k))
        f.write(' ')
        f.write(st)
        f.write(' ')
        for i in afisare:
            f.write(str(i))
            f.write(' ')
        f.write("\n")
    else: f.write("\n")
    f.close()


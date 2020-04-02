import random


def generare(n):
    x = list()
    for i in range(n):
        x.append(random.randrange(0, 2))
    return x



def validare(n, obiecte, x, capacitate):
    suma = 0
    for i in range(n):
        suma = suma + x[i] * int(obiecte[i][2])
    if (suma > capacitate):
        return 0
    return suma


def fitness(n, obiecte, x):
    fit = 0
    for i in range(n):
        fit = fit + x[i] * int(obiecte[i][1])
    return fit


def rez_final(n, obiecte, capacitatea, k):
    rez = list()
    for i in range(n):
        rez.append(0)
    x = list()
    for i in range(1, k):
        x = generare(n)
        if (validare(n, obiecte, x, capacitatea)):
            if (fitness(n, obiecte, x) > fitness(n, obiecte, rez)):
                rez = x
    return x


def vecinatateaRHC(x):
    if(x.__len__()):
        i = random.randrange(0, x.__len__() - 1)
        x[i] = (x[i] + 1) % 2
    return x


# def random_hill_climbing(n, obiecte, capacitate, k):
#     c = rez_final(n, obiecte, capacitate, k)
#     p = 0
#     for i in range(k):
#         x = list()
#         while(p < k):
#             x = vecinatateaRHC(c)
#             if(validare(n, obiecte, x, capacitate)): break
#             p += 1
#             x.clear()
#         if(fitness(n, obiecte, x) > fitness(n, obiecte, c)):
#             c = x
#     return c


# def steepest_ascent_hill_climbing(n, obiecte, capacitate, k):
#     c = rez_final(n, obiecte, capacitate, k)
#     maxim = list()
#     for j in range(k):
#         for i in range(len(c)):
#             if(c[i] == 0):
#                 x = list(c)
#                 x[i] = 1
#                 if(validare(n, obiecte, x, capacitate)):
#                     if(fitness(n, obiecte, c) < fitness(n, obiecte, x)):
#                         c = x
#                         if(maxim.__len__()):
#                             if(fitness(n, obiecte, c) > fitness(n, obiecte, maxim)):
#                                 maxim = list(c)
#                         else: maxim = list(c)
#         c = rez_final(n, obiecte, capacitate, k)
#     return maxim


def NEXT_ASCENT_HILL_CLIMBING(n, obiecte, capacitate, k):
    maxim = list() #Maximul este punctul c cu cea mai mare valoare
    for j in range(k): #pasul 4
        c = rez_final(n, obiecte, capacitate, k) #Pasul 1
        gasit = True
        i = 0
        while(gasit):
            gasit = False #Pasul 3
            while(i < len(c)):
                if(c[i] == 0):
                    x = list(c)
                    x[i] = 1 #Noul vecin a lui c
                    if(validare(n, obiecte, x, capacitate)):    #Validam daca vecinul incape in ghiozdan
                        if(fitness(n, obiecte, c) < fitness(n, obiecte, x)): #Comparam fitnesurile
                            c = x   #Daca x e mai mare se salceaza x in c
                            gasit = True
                            if(maxim.__len__()): #In cazul in care maxim e o lista goala sa sara pe else
                                if(fitness(n, obiecte, c) > fitness(n, obiecte, maxim)):
                                    maxim = list(c)
                            else: maxim = list(c)
                if(gasit): break #Daca gasit e True la final atunci repetam while(i < len(c)): pana nu mai gaxim voaloare noua pt c
                i += 1
    return maxim
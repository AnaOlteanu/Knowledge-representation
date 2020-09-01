""" Evadarea lui Mormolocel """
""" 243 Olteanu Ana-Maria """

import time
from copy import deepcopy
from math import sqrt


class Frunza: # retine informatiile despre fiecare frunza, cum se dau in fisierul de input
    def __init__(self, index, x, y, insecte, g_max):
        self.index = index
        self.x = x
        self.y = y
        self.insecte = insecte
        self.g_max = g_max

    def __str__(self):
        return f"({self.index}, {self.x}, {self.y}, {self.insecte}, {self.g_max})"

    def __repr__(self):
        return f"({self.index}, {self.x}, {self.y}, {self.insecte}, {self.g_max})"

lista_input = ['input_1.txt','input_2.txt','input_3.txt', 'input_4.txt'] # lista cu fisierele cu datele de test

def citire_date(cale_fisier): # citirea datelor din fisier

    file = open(cale_fisier)
    raza = int(file.readline().split('\n')[0])
    greutate = int(file.readline().split('\n')[0])
    id_start = file.readline().split('\n')[0]

    line = file.readline()
    frunze = [] # lista ce contine obiecte de tip Frunza (toate frunzele de pe lac)
    while line:
        l = line.split()
        frunza = Frunza(l[0], int(l[1]), int(l[2]), int(l[3]), int(l[4]))
        frunze.append(frunza)
        line = file.readline()

    for f in frunze:
        if f.index == id_start:
            frunza_s = Frunza(f.index,f.x,f.y,f.insecte,f.g_max) # detaliile pt frunza de start
            break

    return raza, greutate, frunza_s, frunze # returnez raza lacului, greutatea inititala a broscutei, frunza de start si lista de frunze



def euristica(info): # calculeaza distanta dintre o frunza si mal (raza - distanta de la centru la o frunza)
    distanta_mal = raza - sqrt((info[1].x) **2 + (info[1].y)**2)
    return distanta_mal


class Nod:

    def __init__(self, frunze, frunza_crt, greutate):
        self.frunze = frunze
        self.frunza_crt = frunza_crt
        self.greutate = greutate
        self.info = (frunze, frunza_crt, greutate)
        self.h = euristica(self.info)

    def __str__(self):
        return "({}, h={})".format(self.info, self.h)

    def __repr__(self):
        return f"({self.info}, h={self.h})"


class Problema:
    def __init__(self):
        self.nod_start = Nod(frunze, frunza_start, greutate)  # de tip Nod, contine lista de frunze, info despre frunza de start si greutatea initiala

    def cauta_nod_nume(self, info):
        """Stiind doar informatia "info" a unui nod,
        trebuie sa returnati fie obiectul de tip Nod care are acea informatie,
        fie None, daca nu exista niciun nod cu acea informatie."""
        for nod in self.noduri:
            if nod.info == info:
                return nod
        return None


""" Sfarsit definire problema """
""" Clase folosite in algoritmul A* """


class NodParcurgere:
    """O clasa care cuprinde informatiile asociate unui nod din listele open/closed
        Cuprinde o referinta catre nodul in sine (din graf)
        dar are ca proprietati si valorile specifice algoritmului A* (f si g).
        Se presupune ca h este proprietate a nodului din graf
    """

    problema = None  # atribut al clasei (se suprascrie jos in __main__)

    def __init__(self, nod_graf, parinte=None, g=0, f=None):
        self.nod_graf = nod_graf  # obiect de tip Nod
        self.parinte = parinte  # obiect de tip NodParcurgere
        self.g = g  # costul drumului de la radacina pana la nodul curent
        if f is None:
            self.f = self.g + self.nod_graf.h
        else:
            self.f = f

    def drum_arbore(self):
        """
            Functie care calculeaza drumul asociat unui nod din arborele de cautare.
            Functia merge din parinte in parinte pana ajunge la radacina
        """
        nod_c = self
        drum = [nod_c]
        while nod_c.parinte is not None:
            drum = [nod_c.parinte] + drum
            nod_c = nod_c.parinte
        return drum

    def contine_in_drum(self, nod):
        """
            Functie care verifica daca nodul "nod" se afla in drumul dintre radacina si nodul curent (self).
            Verificarea se face mergand din parinte in parinte pana la radacina
            Se compara doar informatiile nodurilor (proprietatea info)
            Returnati True sau False.

            "nod" este obiect de tip Nod (are atributul "nod.info")
            "self" este obiect de tip NodParcurgere (are "self.nod_graf.info")
        """
        nod_curent = self
        while nod_curent.parinte is not None:
            if nod_curent.nod_graf.info == nod.info:
                return True
            nod_curent = nod_curent.parinte
        return False

    # se modifica in functie de problema
    def expandeaza(self):
        """Pentru nodul curent (self) parinte, trebuie sa gasiti toti succesorii (fiii)
        si sa returnati o lista de tupluri (nod_fiu, cost_muchie_tata_fiu),
        sau lista vida, daca nu exista niciunul.
        (Fiecare tuplu contine un obiect de tip Nod si un numar.)
        """
        succesori = []

        frunze, frunza_crt, greutate_crt = self.nod_graf.info #preiau informatiile nodului curent
        dist_crt_mal = raza - sqrt((frunza_crt.x) **2 + (frunza_crt.y) **2) #distanta dintre mal si frunza curenta

        #caut frunzele pe care pot sa sar si care ma apropie de mal
        for i in range(len(frunze)):
            if frunze[i].index != frunza_crt.index:
                frunza = frunze[i] # frunza posibila succesoare
                greutate_noua = greutate_crt
                insecte = frunza_crt.insecte # insectele de pe frunza curenta
                distanta = sqrt((frunza.x - frunza_crt.x) **2 + (frunza.y - frunza_crt.y) **2) # distanta (euclidiana) dintre frunza curenta si posibilul succesor
                dist_mal = raza - sqrt((frunza.x) **2 + (frunza.y) **2) # distanta dintre frunza succesoare si mal
                if dist_crt_mal > dist_mal: # daca frunza gasita ma apropie de mal
                    # cat timp nu pot sari pe frunza gasita, dar am insecte si nu depasesc greutate max a frunzei mananc cate o insecta
                    while greutate_noua <= frunza_crt.g_max and insecte > 0 and greutate_noua/3 < distanta:
                        greutate_noua += 1
                        insecte -= 1
                    if distanta <= greutate_noua/3: # daca pot sari pe frunza gasita
                        greutate_noua -= 1 # scad din greutate costul unei sarituri
                        succesori.append((Nod(frunze,frunza,greutate_noua),1)) # am gasit un succesor

        return succesori


    # se modifica in functie de problema
    def test_scop(self):
        # verific daca pot sari de pe o frunza la mal, inclusiv daca mananc insectele de pe frunza curenta

        frunza, greutate = self.nod_graf.info[1], self.nod_graf.info[2]
        copie = deepcopy(frunza)
        copie_g = deepcopy(greutate)

        distanta = raza - sqrt((frunza.x) **2 + (frunza.y) **2) # distanta pana la mal de la frunza curenta

        while copie_g/3 < distanta and copie_g < copie.g_max and copie.insecte > 0: # la fel ca la succesori
            copie_g += 1
            copie.insecte -= 1

        if distanta <= copie_g / 3:
            return True
        return False


    def __str__(self):
        parinte = self.parinte if self.parinte is None else self.parinte.nod_graf.info[1]
        return f"({self.nod_graf.info[1]}, h={round(self.nod_graf.h,2)}, parinte={parinte}, f={self.f}, g={self.g})"


def afisare(lista, cale): # cand avem drum de la start la mal

    file = open(cale, 'w')
    sarituri = 1
    file.write('---------------------CONCLUZIE----------------------' + '\n')
    for i in range(len(lista)):
        frunza = lista[i].nod_graf.info[1]
        greutate = lista[i].nod_graf.info[2]
        if frunza.index == frunza_start.index:
            file.write("Broscuta se afla pe frunza initiala " + str(frunza.index) + '(' + str(frunza.x) + ',' + str(frunza.y) +'). Greutate broscuta:' + str(greutate) + '\n')
        else:
            sarituri += 1
            frunza_anterioara = lista[i-1].nod_graf.info[1]
            greutate_anterioara = lista[i-1].nod_graf.info[2]
            insecte = abs(greutate - greutate_anterioara + 1)
            file.write("Broscuta a sarit de la " + str(frunza_anterioara.index)  + '(' + str(frunza_anterioara.x) + ',' + str(frunza_anterioara.y) +') la ' + str(frunza.index) + '(' + str(frunza.x) + ',' + str(frunza.y) +'). Broscuta a mancat:' + str(insecte) + ' insecte. Greutate broscuta:' + str(greutate) + '\n')
    file.write("Broscuta a sarit de la " + str(lista[len(lista)-1].nod_graf.info[1].index) + " la mal." + '\n')
    file.write("Broscuta a facut " + str(sarituri) + " sarituri.")

def afisare_2(cale): # cand nu avem drum de la start la mal
    file = open(cale, 'w')
    file.write("Lista open este vida, broasca nu a ajuns la mal.")

""" Algoritmul A* """


def str_info_noduri(l):
    """
        o functie folosita strict in afisari - poate fi modificata in functie de problema
    """
    sir = "["
    for x in l:
        sir += str(x) + "  "
    sir += "]"
    return sir


def afis_succesori_cost(l):
    """
        o functie folosita strict in afisari - poate fi modificata in functie de problema
    """
    sir = ""
    for (x, cost) in l:
        sir += "\nnod: " + str(x) + ", cost arc:" + str(cost)

    return sir


def in_lista(l, nod):
    """
    lista "l" contine obiecte de tip NodParcurgere
    "nod" este de tip Nod
    """
    for i in range(len(l)):
        if l[i].nod_graf.info == nod.info:
            return l[i]
    return None


def a_star(cale):
    rad_arbore = NodParcurgere(NodParcurgere.problema.nod_start)

    open = [rad_arbore]  # open va contine elemente de tip NodParcurgere
    closed = []  # closed va contine elemente de tip NodParcurgere

    while len(open) > 0:

        # print("open:",str_info_noduri(open))
        # print("closed:", str_info_noduri(closed),'\n')
        nod_curent = open[0]
        closed.append(nod_curent) #adaugam primul nod din open in closed
        # print("nod_curent",str(nod_curent))
        if nod_curent.test_scop(): #verific daca am atins un nod scop
            break
        open.pop(0)
        lista_succesori = nod_curent.expandeaza() #iau succesorii nodului curent
        for pair in lista_succesori:
            fiu = pair[0]
            cost = pair[1]
            if nod_curent.contine_in_drum(fiu) == False: #verific daca un fiu se afla deja in drumul de la nodul start la nodul curent
                g_succesor = nod_curent.g + cost
                f = g_succesor + fiu.h
                if in_lista(closed, fiu) is not None: #verific daca un fiu se afla in closed
                    if f < nod_curent.f: #compar f urile si actualizez datele pt fiu
                        n = in_lista(closed, fiu)
                        n.parinte = nod_curent
                        n.f = f
                        n.g = g_succesor
                else:
                    if in_lista(open, fiu):  #verific daca un fiu se afla in open
                        n = in_lista(open, fiu)
                        if n.g > g_succesor: #compar g urile si acualizez datele pt fiu
                            n.parinte = nod_curent
                            n.f = f
                            n.g = g_succesor
                    else: #daca fiul nu se afla nici in open nici in closed, il vom adauga in open
                        nod = NodParcurgere(fiu, nod_curent, g_succesor)
                        open.append(nod)

        open.sort(key = lambda x:(x.f, -x.g)) #sortam open crescator dupa f si descrescator dupa g



    if (len(open) == 0):
        afisare_2(cale)
    else:
        afisare(nod_curent.drum_arbore(), cale)


if __name__ == "__main__":
    i = 1
    for file in lista_input:
        cale_fisier_in = file
        raza, greutate, frunza_start, frunze = citire_date(cale_fisier_in) # preiau datele din fiecare fisier de input
        t_inainte = int(round(time.time() * 1000))
        problema = Problema()
        NodParcurgere.problema = problema
        cale_fisier_out = 'output_' + str(i) + '.txt'
        a_star(cale_fisier_out)
        t_dupa = int(round(time.time() * 1000))
        print(str(i) + ". timp de rulare : " + str(t_dupa - t_inainte) + " milisecunde.")
        i += 1
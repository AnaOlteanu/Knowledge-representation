import time
from copy import deepcopy

# verific toate mutarile posibile pt o piesa anume
def miscare_piesa(matr, poz):
    i = poz[0] # linia pe care se afla piesa
    j = poz[1] # coloana pe care se afla piesa
    miscari = [] # retine tabla modificata dupa o mutare (lista de matrici(lista de liste))
    pozitii = [] # retine pozitiile unde a fost mutata piesa, in concordanta cu miscarile
    sar_piesa = 0 # daca pot sa sar peste o piesa a adversarului -> 1; pentru a lua mai intai miscarile in care sar peste o piesa

    # pt piesele albe ma deplasez in jos
    if matr[i][j] == 'a' or matr[i][j] == 'A':
        if i < len(matr) - 1: # ca sa nu fiu pe ultima linie
            # jos stanga o casuta
            if j >= 1: # ca sa nu fiu pe prima coloana
                if matr[i+1][j-1] == '#' and sar_piesa == 0:
                    tabla_noua = deepcopy(matr)
                    if i + 1 == len(matr) - 1: # sunt pe ultima linie
                        tabla_noua[i+1][j-1] = matr[i][j].upper()
                    else:
                        tabla_noua[i+1][j-1] = matr[i][j]
                    tabla_noua[i][j] = '#'
                    poz_noua = (i+1, j-1)
                    miscari.append(tabla_noua)
                    pozitii.append(poz_noua)
            #jos dreapta o casuta
            if j < len(matr) - 1: # ca sa nu fiu pe ultima coloana
                if matr[i+1][j+1] == '#' and sar_piesa == 0:
                    tabla_noua = deepcopy(matr)
                    if i + 1 == len(matr) - 1: # sunt pe ultima linie
                        tabla_noua[i + 1][j + 1] = matr[i][j].upper()
                    else:
                        tabla_noua[i + 1][j + 1] = matr[i][j]
                    tabla_noua[i][j] = '#'
                    poz_noua = (i + 1, j + 1)
                    miscari.append(tabla_noua)
                    pozitii.append(poz_noua)
        if i < len(matr) - 2: # sa nu fiu pe ultimele 2 linii
            # jos stanga si sar piesa neagra
            if j > 1: # sa nu fiu pe primele 2 coloane
                if (matr[i+1][j-1] == 'n' or matr[i+1][j-1] == 'N') and matr[i+2][j-2] == '#': # verific daca am piesa de sarit
                    if sar_piesa == 0:
                        del miscari[:] # sterg toate miscarile de pana atunci pt a avea prioritate saritul piesei
                        del pozitii[:] # la fel si pt pozitii
                        sar_piesa = 1
                    tabla_noua = deepcopy(matr)
                    if i + 2 == len(matr) -1:
                        tabla_noua[i+2][j-2] = matr[i][j].upper()
                    else:
                        tabla_noua[i+2][j-2] = matr[i][j]
                    tabla_noua[i][j] = '#'
                    tabla_noua[i + 1][j - 1] = '#'
                    poz_noua = (i+2, j-2)
                    miscari.append(tabla_noua)
                    pozitii.append(poz_noua)
            # jos dreapta si sar piesa neagra
            if j < len(matr) - 2: # sa nu fiu pe ultimele 2 coloane
                if (matr[i+1][j+1] == 'n' or matr[i+1][j+1] == 'N') and matr[i+2][j+2] == '#':
                    if sar_piesa == 0:
                        del miscari[:]
                        del pozitii[:]
                        sar_piesa = 1
                    tabla_noua = deepcopy(matr)
                    if i + 2 == len(matr) - 1:
                        tabla_noua[i+2][j+2] = matr[i][j].upper()
                    else:
                        tabla_noua[i+2][j+2] = matr[i][j]
                    tabla_noua[i][j] = '#'
                    tabla_noua[i + 1][j + 1] = '#'
                    poz_noua = (i+2, j+2)
                    miscari.append(tabla_noua)
                    pozitii.append(poz_noua)

    #pt piesa REGE A ma deplasez in sus
    if matr[i][j] == 'A':
        if i > 0:
            # sus stanga o casuta
            if j > 0:
                if matr[i-1][j-1] == '#' and sar_piesa == 0:
                    tabla_noua = deepcopy(matr)
                    tabla_noua[i-1][j-1] = matr[i][j]
                    tabla_noua[i][j] = '#'
                    poz_noua = (i-1, j-1)
                    miscari.append(tabla_noua)
                    pozitii.append(poz_noua)
            # sus dreapta o casuta
            if j < len(matr) - 1:
                if matr[i-1][j+1] == '#' and sar_piesa == 0:
                    tabla_noua = deepcopy(matr)
                    tabla_noua[i-1][j+1] = matr[i][j]
                    tabla_noua[i][j] = '#'
                    poz_noua = (i-1, j+1)
                    miscari.append(tabla_noua)
                    pozitii.append(poz_noua)
        if i > 1:
            # sus stanga si sar piesa neagra
            if j > 1:
                if (matr[i - 1][j - 1] == 'n' or matr[i - 1][j - 1] == 'N') and matr[i - 2][j - 2] == '#':
                    if sar_piesa == 0:
                        del miscari[:]
                        del pozitii[:]
                        sar_piesa = 1
                    tabla_noua = deepcopy(matr)
                    tabla_noua[i-2][j-2] = matr[i][j]
                    tabla_noua[i-1][j-1] = '#'
                    tabla_noua[i][j] = '#'
                    poz_noua = (i-2, j-2)
                    miscari.append(tabla_noua)
                    pozitii.append(poz_noua)
            # sus dreapta si sar piesa neagra
            if j < len(matr) - 2:
                if (matr[i - 1][j + 1] == 'n' or matr[i - 1][j + 1] == 'N') and matr[i - 2][j + 2] == '#':
                    if sar_piesa == 0:
                        del miscari[:]
                        del pozitii[:]
                        sar_piesa = 1
                    tabla_noua = deepcopy(matr)
                    tabla_noua[i-2][j+2] = matr[i][j]
                    tabla_noua[i-1][j+1] = '#'
                    tabla_noua[i][j] = '#'
                    poz_noua = (i-2, j+2)
                    miscari.append(tabla_noua)
                    pozitii.append(poz_noua)



    #pt piesele negre ma deplasez in sus
    if matr[i][j] == 'n' or matr[i][j] == 'N':
        if i > 0:
            # sus stanga o casuta
            if j > 0:
                if matr[i-1][j-1] == '#' and sar_piesa == 0:
                    tabla_noua = deepcopy(matr)
                    if i - 1 == 0:
                        tabla_noua[i-1][j-1] = matr[i][j].upper()
                    else:
                        tabla_noua[i-1][j-1] = matr[i][j]
                    tabla_noua[i][j] = '#'
                    poz_noua = (i-1, j-1)
                    miscari.append(tabla_noua)
                    pozitii.append(poz_noua)
            # sus dreapta o casuta
            if j < len(matr) - 1:
                if matr[i-1][j+1] == '#' and sar_piesa == 0:
                    tabla_noua = deepcopy(matr)
                    if i - 1 == 0:
                        tabla_noua[i-1][j+1] = matr[i][j].upper()
                    else:
                        tabla_noua[i-1][j+1] = matr[i][j]
                    tabla_noua[i][j] = '#'
                    poz_noua = (i-1, j+1)
                    miscari.append(tabla_noua)
                    pozitii.append(poz_noua)
        if i > 1:
            if j > 1:
            # sus stanga si sar piesa alba
                if (matr[i-1][j-1] == 'a' or matr[i-1][j-1] == 'A') and matr[i-2][j-2] == '#':
                    if sar_piesa == 0:
                        del miscari[:]
                        del pozitii[:]
                        sar_piesa = 1
                    tabla_noua = deepcopy(matr)
                    if i - 2 == 0:
                        tabla_noua[i-2][j-2] = matr[i][j].upper()
                    else:
                        tabla_noua[i-2][j-2] = matr[i][j]
                    tabla_noua[i][j] = '#'
                    poz_noua = (i-2, j-2)
                    miscari.append(tabla_noua)
                    pozitii.append(poz_noua)
            #sus dreapta si sar piesa alba
            if j < len(matr) - 2:
                if (matr[i-1][j+1] == 'a' or matr[i-1][j+1] == 'A') and matr[i-2][j+2] == '#':
                    if sar_piesa == 0:
                        del miscari[:]
                        del pozitii[:]
                        sar_piesa = 1
                    tabla_noua = deepcopy(matr)
                    if i - 2 == 0:
                        tabla_noua[i-2][j+2] = matr[i][j].upper()
                    else:
                        tabla_noua[i-2][j+2] = matr[i][j]
                    tabla_noua[i][j] = '#'
                    poz_noua = (i-2, j+2)
                    miscari.append(tabla_noua)
                    pozitii.append(poz_noua)
    # pt piesa REGE N ma deplasez in jos
    if matr[i][j] == 'N':
        if i < len(matr) - 1:
            # jos stanga o casuta
            if j > 0 :
                if matr[i+1][j-1] == '#' and sar_piesa == 0:
                    tabla_noua = deepcopy(matr)
                    tabla_noua[i+1][j-1] = matr[i][j]
                    tabla_noua[i][j] = '#'
                    poz_noua = (i+1, j-1)
                    miscari.append(tabla_noua)
                    pozitii.append(poz_noua)
            # jos dreapta o casuta
            if j < len(matr) - 1:
                if matr[i+1][j+1] == '#' and sar_piesa == 0:
                    tabla_noua = deepcopy(matr)
                    tabla_noua[i+1][j+1] = matr[i][j]
                    tabla_noua[i][j] = '#'
                    poz_noua = (i + 1, j + 1)
                    miscari.append(tabla_noua)
                    pozitii.append(poz_noua)
        if i < len(matr) - 2:
            # jos stanga si sar piesa
            if j > 1:
                if (matr[i + 1][j - 1] == 'a' or matr[i + 1][j - 1] == 'A') and matr[i + 2][j - 2] == '#':
                    if sar_piesa == 0:
                        del miscari[:]
                        del pozitii[:]
                        sar_piesa = 1
                    tabla_noua = deepcopy(matr)
                    tabla_noua[i + 2][j - 2] = matr[i][j]
                    tabla_noua[i + 1][j - 1] = tabla_noua[i][j] = '#'
                    poz_noua = (i+2, j-2)
                    miscari.append(tabla_noua)
                    pozitii.append(poz_noua)
            if j < len(matr) - 2:
                # jos dreapta si sar piesa
                if (matr[i + 1][j + 1] == 'a' or matr[i + 1][j + 1] == 'A') and matr[i + 2][j + 2] == '#':
                    if sar_piesa == 0:
                        del miscari[:]
                        del pozitii[:]
                        sar_piesa = 1
                    tabla_noua = deepcopy(matr)
                    tabla_noua[i + 2][j + 2] = matr[i][j]
                    tabla_noua[i + 1][j + 1] = tabla_noua[i][j] = '#'
                    poz_noua = (i+2, j+2)
                    miscari.append(tabla_noua)
                    pozitii.append(poz_noua)

    return  miscari, pozitii, sar_piesa

class Joc:
    """
    Clasa care defineste jocul. Se va schimba de la un joc la altul.
    """
    NR_LINII = 8
    NR_COLOANE = 8
    JMIN = None
    JMAX = None
    GOL = '#'
    TABLA = [['#', 'a', '#', 'a', '#', 'a', '#', 'a'],
            ['a', '#', 'a', '#', 'a', '#', 'a', '#'],
            ['#', 'a', '#', 'a', '#', 'a', '#', 'a'],
            ['#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#'],
            ['n', '#', 'n', '#', 'n', '#', 'n', '#'],
            ['#', 'n', '#', 'n', '#', 'n', '#', 'n'],
            ['n', '#', 'n', '#', 'n', '#', 'n', '#']]

    def __init__(self, tabla=None):
        self.matr = tabla or self.TABLA
        self.nr_albe, self.nr_negre = self.numara_piese()

    def numara_piese(self):
        nr_albe = 0
        nr_negre = 0
        for l in self.matr:
            for el in l:
                if el == 'a' or el == 'A':
                    nr_albe += 1
                elif el == 'n' or el == 'N':
                    nr_negre += 1
        return nr_albe, nr_negre

    def final(self):
        if len(self.mutari_joc(self.JMAX)) == 0:
            return self.JMIN
        elif len(self.mutari_joc(self.JMIN)) == 0:
            return self.JMAX
        else:
            return None

    def mutari_joc(self, jucator):
        """
        Pentru configuratia curenta de joc "self.matr" (de tip lista, cu 9 elemente),
        trebuie sa returnati o lista "l_mutari" cu elemente de tip Joc,
        corespunzatoare tuturor configuratiilor-succesor posibile.

        "jucator" este simbolul jucatorului care face mutarea
        """
        l_mutari = []

        sar_piesa = 0
        for i in range(self.NR_LINII):
            for j in range(self.NR_COLOANE):
                if self.matr[i][j] == jucator or (jucator == 'a' and self.matr[i][j] == 'A') or (jucator == 'n' and self.matr[i][j] == 'N'):
                    poz = (i, j)
                    miscari, pozitii, sar_piesa_crt = miscare_piesa(self.matr, poz) # imi iau toate miscarile posibile
                    if (sar_piesa_crt == 0 or sar_piesa_crt == 1) or sar_piesa == 0:
                        for miscare in miscari:
                            l_mutari.append(Joc(miscare))
                    if sar_piesa_crt == 1 and sar_piesa == 0:
                        l_mutari.clear()
                        sar_piesa = 1

        return l_mutari



    def estimeaza_scor(self):
        if self.JMAX == 'a':
            return self.nr_albe - self.nr_negre
        elif self.JMAX == 'n':
            return self.nr_negre - self.nr_albe

    def __str__(self):
        sir = ''
        for i in range(self.NR_LINII):
            for j in range(self.NR_COLOANE):
                if self.matr[i][j] == '#':
                    sir += ' . '
                else:
                    sir += ' ' + self.matr[i][j] + ' '

            sir += '\n'
        return sir


class Stare:
    """
    Clasa folosita de algoritmii minimax si alpha-beta
    Are ca proprietate tabla de joc
    Functioneaza cu conditia ca in cadrul clasei Joc sa fie definiti JMIN si JMAX (cei doi jucatori posibili)
    De asemenea cere ca in clasa Joc sa fie definita si o metoda numita mutari_joc() care ofera lista cu
    configuratiile posibile in urma mutarii unui jucator
    """

    ADANCIME_MAX = None

    def __init__(self, tabla_joc, j_curent, adancime, parinte=None, scor=None):
        self.tabla_joc = tabla_joc  # un obiect de tip Joc => „tabla_joc.matr”
        self.j_curent = j_curent  # simbolul jucatorului curent

        # adancimea in arborele de stari
        #	(scade cu cate o unitate din „tata” in „fiu”)
        self.adancime = adancime

        # scorul starii (daca e finala, adica frunza a arborelui)
        # sau scorul celei mai bune stari-fiice (pentru jucatorul curent)
        self.scor = scor

        # lista de mutari posibile din starea curenta
        self.mutari_posibile = []  # lista va contine obiecte de tip Stare

        # cea mai buna mutare din lista de mutari posibile pentru jucatorul curent
        self.stare_aleasa = None

    def jucator_opus(self):
        if self.j_curent == Joc.JMIN:
            return Joc.JMAX
        else:
            return Joc.JMIN

    def mutari_stare(self):
        l_mutari = self.tabla_joc.mutari_joc(self.j_curent)
        juc_opus = self.jucator_opus()

        l_stari_mutari = [Stare(mutare, juc_opus, self.adancime - 1, parinte=self) for mutare in l_mutari]
        return l_stari_mutari

    def __str__(self):
        sir = str(self.tabla_joc) + "(Juc curent:" + self.j_curent + ")\n"
        return sir


""" Algoritmul MinMax """


def min_max(stare):
    # Daca am ajuns la o frunza a arborelui, adica:
    # - daca am expandat arborele pana la adancimea maxima permisa
    # - sau daca am ajuns intr-o configuratie finala de joc
    if stare.adancime == 0 or stare.tabla_joc.final():
        # calculam scorul frunzei apeland "estimeaza_scor"
        stare.scor = stare.tabla_joc.estimeaza_scor()
        return stare

    # Altfel, calculez toate mutarile posibile din starea curenta
    stare.mutari_posibile = stare.mutari_stare()

    # aplic algoritmul minimax pe toate mutarile posibile (calculand astfel subarborii lor)
    mutari_scor = [min_max(mutare) for mutare in stare.mutari_posibile]

    if stare.j_curent == Joc.JMAX:
        # daca jucatorul e JMAX aleg starea-fiica cu scorul maxim
        stare.stare_aleasa = max(mutari_scor, key=lambda x: x.scor)
    else:
        # daca jucatorul e JMIN aleg starea-fiica cu scorul minim
        stare.stare_aleasa = min(mutari_scor, key=lambda x: x.scor)

    # actualizez scorul „tatalui” = scorul „fiului” ales
    stare.scor = stare.stare_aleasa.scor
    return stare


def alpha_beta(alpha, beta, stare):
    # Daca am ajuns la o frunza a arborelui, adica:
    # - daca am expandat arborele pana la adancimea maxima permisa
    # - sau daca am ajuns intr-o configuratie finala de joc
    if stare.adancime == 0 or stare.tabla_joc.final():
        # calculam scorul frunzei apeland "estimeaza_scor"
        stare.scor = stare.tabla_joc.estimeaza_scor()
        return stare

    # Conditia de retezare:
    if alpha >= beta:
        return stare  # este intr-un interval invalid, deci nu o mai procesez

    # Calculez toate mutarile posibile din starea curenta (toti „fiii”)
    stare.mutari_posibile = stare.mutari_stare()

    if stare.j_curent == Joc.JMAX:
        scor_curent = float('-inf')  # scorul „tatalui” de tip MAX

        # pentru fiecare „fiu” de tip MIN:
        for mutare in stare.mutari_posibile:
            # calculeaza scorul fiului curent
            stare_noua = alpha_beta(alpha, beta, mutare)

            # incerc sa imbunatatesc (cresc) scorul si alfa
            # „tatalui” de tip MAX, folosind scorul fiului curent
            if scor_curent < stare_noua.scor:
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor

            if alpha < stare_noua.scor:
                alpha = stare_noua.scor
                if alpha >= beta:  # verific conditia de retezare
                    break  # NU se mai extind ceilalti fii de tip MIN


    elif stare.j_curent == Joc.JMIN:
        scor_curent = float('inf')  # scorul „tatalui” de tip MIN

        # pentru fiecare „fiu” de tip MAX:
        for mutare in stare.mutari_posibile:
            stare_noua = alpha_beta(alpha, beta, mutare)

            # incerc sa imbunatatesc (scad) scorul si beta
            # „tatalui” de tip MIN, folosind scorul fiului curent
            if scor_curent > stare_noua.scor:
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor

            if beta > stare_noua.scor:
                beta = stare_noua.scor
                if alpha >= beta:  # verific conditia de retezare
                    break  # NU se mai extind ceilalti fii de tip MAX

    # actualizez scorul „tatalui” = scorul „fiului” ales
    stare.scor = stare.stare_aleasa.scor

    return stare


def afis_daca_final(stare_curenta):
    final = stare_curenta.tabla_joc.final()
    if (final):
        if (final == "remiza"):
            print("Remiza!")
        else:
            print("A castigat " + final)

        return True

    return False


def main():
    # initializare algoritm
    raspuns_valid = False
    while not raspuns_valid:
        tip_algoritm = input("Algorimul folosit? (raspundeti cu 1 sau 2)\n 1.Minimax\n 2.Alpha-Beta\n ")
        if tip_algoritm in ['1', '2']:
            raspuns_valid = True
        else:
            print("Nu ati ales o varianta corecta.")

    # initializare nivel de dificultate
    raspuns_valid = False
    while not raspuns_valid:
        nivel = input("Alegeti nivelul de dificultate: (raspundeti cu 1, 2 sau 3)\n 1.Incepator\n 2.Mediu\n 3.Avansat\n")
        if nivel in ['1', '2', '3']:
            if nivel == '1':
                Stare.ADANCIME_MAX = 2
                raspuns_valid = True
            elif nivel == '2':
                Stare.ADANCIME_MAX = 4
                raspuns_valid = True
            elif nivel == '3':
                Stare.ADANCIME_MAX = 6
                raspuns_valid = True
        else:
            print("Nu ati ales o varianta corecta.")

    # initializare jucatori
    raspuns_valid = False
    while not raspuns_valid:
        Joc.JMIN = input("Doriti sa jucati cu a sau cu n? ").lower()
        if (Joc.JMIN in ['a', 'n']):
            raspuns_valid = True
        else:
            print("Raspunsul trebuie sa fie a sau n.")
    Joc.JMAX = 'a' if Joc.JMIN == 'n' else 'n'

    # initializare tabla
    tabla_curenta = Joc()
    print("Tabla initiala")
    print(str(tabla_curenta))

    # creare stare initiala
    stare_curenta = Stare(tabla_curenta, 'a', Stare.ADANCIME_MAX)

    while True:
        if (stare_curenta.j_curent == Joc.JMIN):
            # muta jucatorul
            raspuns_valid = False
            while not raspuns_valid:
                try:
                    print("Doriti sa iesiti? (da/nu)")
                    exit = input()
                    if exit == 'nu':
                        print("Ce piesa vreti sa mutati? (dati linie si coloana). ")
                        linie = int(input("linie="))
                        coloana = int(input("coloana="))
                        if linie in range(0, Joc.NR_LINII) and coloana in range(0, Joc.NR_LINII):
                            # daca piesa selectata este a jucatorului
                            if stare_curenta.tabla_joc.matr[linie][coloana] == Joc.JMIN or ord(stare_curenta.tabla_joc.matr[linie][coloana]) + 32 == ord(Joc.JMIN):
                                print("Unde vreti sa mutati piesa? (dati linie si coloana)")
                                linie_noua = int(input("linie noua="))
                                coloana_noua = int(input("coloana noua="))
                                if linie_noua in range(0, Joc.NR_LINII) and coloana_noua in range(0, Joc.NR_LINII):
                                    poz = (linie, coloana)
                                    mutari, pozitii, sar_piesa = miscare_piesa(stare_curenta.tabla_joc.matr, poz)

                                    index = 0
                                    for poz in pozitii:
                                        if poz[0] == linie_noua and poz[1] == coloana_noua: # daca exista o miscare valida
                                            raspuns_valid = mutari[index]
                                        index += 1

                                    if not raspuns_valid:
                                        print("Mutare invalida")
                                else:
                                    print("Linia sau coloana invalida")
                            else:
                                print("Piesa nu va apartine")
                        else:
                            print("Linie sau coloana invalida")
                    else:
                        print("Scor computer:", -stare_curenta.tabla_joc.estimeaza_scor())
                        print("Scor jucator:", stare_curenta.tabla_joc.estimeaza_scor())
                        return

                except ValueError:
                    print("Linia si coloana trebuie sa fie numere intregi! Doriti sa iesiti (da/nu)?")
                    exit_func = input()
                    if exit_func == 'da':
                        print("Scor computer:", -stare_curenta.tabla_joc.estimeaza_scor())
                        print("Scor jucator:", stare_curenta.tabla_joc.estimeaza_scor())
                        return

            # dupa iesirea din while sigur am valide atat linia cat si coloana
            # deci pot plasa simbolul pe "tabla de joc"
            stare_curenta.tabla_joc.matr = raspuns_valid

            # afisarea starii jocului in urma mutarii utilizatorului
            print("\nTabla dupa mutarea jucatorului")
            print(str(stare_curenta))

            # testez daca jocul a ajuns intr-o stare finala
            # si afisez un mesaj corespunzator in caz ca da
            if (afis_daca_final(stare_curenta)):
                break

            # S-a realizat o mutare. Schimb jucatorul cu cel opus
            stare_curenta.j_curent = stare_curenta.jucator_opus()

        # --------------------------------
        else:  # jucatorul e JMAX (calculatorul)
            # Mutare calculator

            # preiau timpul in milisecunde de dinainte de mutare
            t_inainte = int(round(time.time() * 1000))
            if tip_algoritm == '1':
                stare_actualizata = min_max(stare_curenta)
            else:  # tip_algoritm==2
                stare_actualizata = alpha_beta(-500, 500, stare_curenta)
            stare_curenta.tabla_joc = stare_actualizata.stare_aleasa.tabla_joc
            print("Tabla dupa mutarea calculatorului")
            print(str(stare_curenta))

            # preiau timpul in milisecunde de dupa mutare
            t_dupa = int(round(time.time() * 1000))
            print("Calculatorul a \"gandit\" timp de " + str(t_dupa - t_inainte) + " milisecunde.")

            if (afis_daca_final(stare_curenta)):
                break

            # S-a realizat o mutare. Schimb jucatorul cu cel opus
            stare_curenta.j_curent = stare_curenta.jucator_opus()


if __name__ == "__main__":
    main()
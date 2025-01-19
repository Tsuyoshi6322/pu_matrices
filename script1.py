from functools import partial
from collections import defaultdict
from tabulate import tabulate
import random


# Definicja wymiarów macierzy
class WymiaryMacierzy:
    def __init__(self, iloscKolumn, iloscWierszy):
        self.iloscKolumn = iloscKolumn
        self.iloscWierszy = iloscWierszy


# Suma dwóch macierzy
def sumaMacierzy(macierz1, macierz2):
    # Wymiary obu macierzy muszą być takie same
    if len(macierz1) != len(macierz2) or len(macierz1[0]) != len(macierz2[0]):
        raise ValueError("Macierze muszą mieć takie same wymiary.")
    
    # Dodawanie elementów obu macierzy
    wynik = [
        [macierz1[i][j] + macierz2[i][j] for j in range(len(macierz1[0]))]
        for i in range(len(macierz1))
    ]

    # Wyświetl wynik
    try:
        print("Suma macierzy:")
        for wiersz in wynik:
            print(wiersz)
    except ValueError:
        print("Macierze muszą mieć takie same wymiary.")


# Różnica dwóch macierzy
def roznicaMacierzy(macierz1, macierz2):
    # Wymiary obu macierzy muszą być takie same
    if len(macierz1) != len(macierz2) or len(macierz1[0]) != len(macierz2[0]):
        raise ValueError("Macierze muszą mieć takie same wymiary.")
    
    # Odejmowanie elementów obu macierzy
    wynik = [
        [macierz1[i][j] - macierz2[i][j] for j in range(len(macierz1[0]))]
        for i in range(len(macierz1))
    ]

    # Wyświetl wynik
    try:
        print("Różnica macierzy:")
        for wiersz in wynik:
            print(wiersz)
    except ValueError:
        print("Macierze muszą mieć takie same wymiary.")


# Iloczyn dwóch macierzy
def iloczynMacierzy(macierz1, macierz2):
    # Liczba kolumn jednej macierzy musi być równa liczbie wierszy drugiej
    if len(macierz1[0]) != len(macierz2):
        raise ValueError("Liczba kolumn pierwszej macierzy musi być równa liczbie wierszy drugiej macierzy.")

    # Mnożenie elementów obu macierzy
    wynik = [
        [
            sum(macierz1[i][k] * macierz2[k][j] for k in range(len(macierz2)))
            for j in range(len(macierz2[0]))
        ]
        for i in range(len(macierz1))
    ]

    # Wyświetl wynik
    try:
        print("Iloczyn macierzy:")
        for wiersz in wynik:
            print(wiersz)
    except ValueError:
        print("Liczba kolumn pierwszej macierzy musi być równa liczbie wierszy drugiej macierzy.")


# Transpozycja jednej macierzy
def transpozycjaMacierzy(macierz1):
    wynik = [
        [macierz1[i][j] for i in range(len(macierz1))]
        for j in range(len(macierz1[0]))
    ]

    # Wyświetl wynik
    print("Macierz transponowana:")
    for wiersz in wynik:
        print(wiersz)


# Zerowanie elementów głównej przekątnej danej macierzy
def zerowanieElementow(macierz1):
    wynik = macierz1
    for i in range(min(len(wynik), len(wynik[0]))): 
        wynik[i][i] = 0

    # Wyświetl wynik
    print("Macierz z wyzerowanymi elementami:")
    for wiersz in wynik:
        print(wiersz)


# Iloczyn odwrotności wszystkich niezerowych elementów
def iloczynOdwrotnosci(macierz1):
    # Zmienna sterująca
    iloczynWartosci = 1

    # Iloczyn zmiennej z odwrotnością elementu macierzy
    for wiersz in macierz1:
        for element in wiersz:
            if element != 0:
                iloczynWartosci *= 1 / element
    
    # Wyświetl wynik
    print("Iloczyn odwrotności wszystkich niezerowych elementów: ", iloczynWartosci)


# Średnia arytmetyczna podanych liczb
def sredniaArytmetyczna(macierz1):
    # Zmienne sterujące 
    sumaElementow = 0
    liczbaElementow = 0

    # Przejdź przez wszystkie elementy macierzy
    for wiersz in macierz1:
        for element in wiersz:
            sumaElementow += element # Dodaj element do sumy
            liczbaElementow += 1 # Licz kolejno liczbę elementów

    # Wyświetl wynik
    if liczbaElementow == 0:
        wynik = 0
    else:
        wynik = sumaElementow / liczbaElementow

    print("Średnia arytmetyczna elementów macierzy: ", wynik)
    

# Średnia geometryczna wartości bezwzględnej podanych liczb
def sredniaGeometryczna(macierz1):
    # Zmienne sterujące
    iloczynElementow = 1
    liczbaElementow = 0

    for wiersz in macierz1:
        for element in wiersz:
            iloczynElementow *= element
            liczbaElementow += 1
    
    # Wyświetl wynik
    wynik = iloczynElementow ** (1 / liczbaElementow)
    print("Średnia geometryczna elementów macierzy: ", wynik)


# Częstotliwość występowania każdej wartości
def czestoscWystepowania(macierz1):
    # Słownik sterujący, pełen zer
    czestotliwosc = defaultdict(int)

    for wiersz in macierz1:
        for element in wiersz:
            czestotliwosc[element] += 1

    # Wyświetl wynik w tabeli, posortowanej
    tableData = [(key, value) for key, value in czestotliwosc.items()]
    tableData_sorted = sorted(tableData, key=lambda x: x[1], reverse=True)
    print(tabulate(tableData_sorted, headers=["Element", "Ilość"], tablefmt="grid"))

# Rozklad LU metodą Dolittle'a
def rozkladLU(macierz1):
    print("rozkladLU")


# Zarządzanie inputem użytkownika
def getValidInput(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Podaj liczbę dodatnią!")
        except ValueError:
            print("Podaj liczbę całkowitą!")



# Ustalenie wymiarów macierzy (n x m) i wypełnienie jej    
def tworzenieMacierzy():
    print("Proszę podać wymiary macierzy: ")                                  # input
    wymiary = WymiaryMacierzy(0,0)                                            # reset
    wymiary.iloscKolumn = getValidInput("Podaj ilość kolumn: ")               # set n
    wymiary.iloscWierszy = getValidInput("Podaj ilość wierszy: ")             # set m
    print(f"Macierz ma wymiary {wymiary.iloscKolumn}x{wymiary.iloscWierszy}") # log

    # Wypełnienie macierzy o wymiarach n x m losowymi liczbami <1,100>
    macierz = [
        [random.randint(1, 100) for _ in range(wymiary.iloscKolumn)]
        for _ in range(wymiary.iloscWierszy)
    ]

    # Wyświetl wygenerowaną macierz
    print("Wygenerowana macierz:") 
    for wiersz in macierz:
        print(wiersz)

    # Zwrócenie wartości w celu ponownego użycia
    return wymiary, macierz

# Pierwsza macierz
wymiary1, macierz1 = tworzenieMacierzy()



# Menu zadań
def displayMenu():
    while True:
        print("""
        ===================================================
                            Menu zadań                     
        ===================================================
            [1] Zadania 1.1-7    Własności liczby a       
        ===================================================\n""")

        choice = getValidInput("Proszę podać liczbę (1-10): ")

        if 1 <= choice <= 10:
            print(f"Wybrano zadanie {choice}")
            return choice
        else:
            print("Nie ma takiego zadania!")
            print("Spróbuj ponownie.")
            
choice = displayMenu()

# Ustalenie wymiarów drugiej macierzy dla zadań 1-3
if choice < 4:
    wymiary2, macierz2 = tworzenieMacierzy()



# Egzekucja wybranego zadania
def taskChoice():
    match choice:
        case 1: sumaMacierzy(macierz1,macierz2)
        case 2: roznicaMacierzy(macierz1,macierz2)
        case 3: iloczynMacierzy(macierz1,macierz2)
        case 4: transpozycjaMacierzy(macierz1)
        case 5: zerowanieElementow(macierz1)
        case 6: iloczynOdwrotnosci(macierz1)
        case 7: sredniaArytmetyczna(macierz1)
        case 8: sredniaGeometryczna(macierz1)
        case 9: czestoscWystepowania(macierz1)
        case 10: rozkladLU(macierz1)
        case _: print("Nie ma takiego zadania!")

taskChoice()









# Koniec programu
print("""
        ===================================================
                        Koniec programu                    
        ===================================================""")
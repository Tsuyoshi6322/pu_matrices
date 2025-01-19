from functools import partial
import random

# Definicja wymiarów macierzy
class WymiaryMacierzy:
    def __init__(self, iloscKolumn, iloscWierszy):
        self.iloscKolumn = iloscKolumn
        self.iloscWierszy = iloscWierszy

# Suma dwóch macierzy
def sumaMacierzy():
    print("sumaMacierzy")

# Różnica dwóch macierzy
def roznicaMacierzy():
    print("roznicaMacierzy")

# Iloczyn dwóch macierzy
def iloczynMacierzy():
    print("iloczynMacierzy")

# Transpozycja jednej macierzy
def transpozycjaMacierzy():
    print("transpozycjaMacierzy")

# Zerowanie elementów głównej przekątnej danej macierzy
def zerowanieElementow():
    print("zerowanieElementow")

# Iloczyn odwrotności wszystkich niezerowych elementów
def iloczynOdwrotnosci():
    print("iloczynOdwrotnosci")

# Średnia arytmetyczna podanych liczb
def sredniaArytmetyczna():
    print("sredniaArytmetyczna")

# Średnia geometryczna wartości bezwzględnej podanych liczb
def sredniaGeometryczna():
    print("sredniaGeometryczna")

# Częstotliwość występowania każdej wartości
def czestoscWystepowania():
    print("czestoscWystepowania")

# Rozklad LU metodą Dolittle'a
def rozkladLU():
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
print("Proszę podać wymiary macierzy: ")                                  # input
wymiary = WymiaryMacierzy(0,0)                                            # reset
wymiary.iloscKolumn = getValidInput("Podaj ilość kolumn: ")               # set n
wymiary.iloscWierszy = getValidInput("Podaj ilość wierszy: ")             # set m
print(f"Macierz ma wymiary {wymiary.iloscKolumn}x{wymiary.iloscWierszy}") # log

# Wypełnienie macierzy o wymiarach n x m losowymi liczbami <1,100>
macierz = [[random.randint(1, 100) for _ in range(wymiary.iloscKolumn)] for _ in range(wymiary.iloscWierszy)]
print("Wygenerowana macierz:") # Wyświetl wygenerowaną macierz
for wiersz in macierz:
    print(wiersz)

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
            print(f"Wybrano: {choice}")
            return choice
        else:
            print("Nie ma takiego zadania!")
            print("Spróbuj ponownie.")
            
choice = displayMenu()

# Ustalenie wymiarów drugiej macierzy dla zadań 1-3
if choice < 4:
    print("Proszę podać wymiary drugiej macierzy:")

    wymiary2 = WymiaryMacierzy(0,0)

    wymiary2.iloscKolumn = getValidInput("Podaj ilość kolumn: ")
    wymiary2.iloscWierszy = getValidInput("Podaj ilość wierszy: ")

    print(f"Druga macierz ma wymiary {wymiary2.iloscKolumn}x{wymiary2.iloscWierszy}")

# Egzekucja wybranego zadania
def taskChoice():
    dispatch = {
        1: partial(sumaMacierzy),
        2: partial(roznicaMacierzy),
        3: partial(iloczynMacierzy),
        4: partial(transpozycjaMacierzy),
        5: partial(zerowanieElementow),
        6: partial(iloczynOdwrotnosci),
        7: partial(sredniaArytmetyczna),
        8: partial(sredniaGeometryczna),
        9: partial(czestoscWystepowania),
        10: partial(rozkladLU)
    }

    if choice in dispatch:
        dispatch[choice]()
    else:
        print("Nie ma takiego zadania!")

taskChoice()









# Koniec programu
print("""
        ===================================================
                        Koniec programu                    
        ===================================================""")
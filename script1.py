from functools import partial

# Główne działanie programu
class WymiaryMacierzy:
    def __init__(self, iloscKolumn, iloscWierszy):
        self.iloscKolumn = iloscKolumn
        self.iloscWierszy = iloscWierszy

def sumaMacierzy():
    print("Suma dwoch macierzy")

def roznicaMacierzy():
    print("Roznica dwoch macierzy")

def iloczynMacierzy():
    print("Iloczyn dwoch Macierzy")

def transpozycjaMacierzy():
    print("Transpozycja jednej macierzy")

def zerowanieElementow():
    print("""Zerowanie elementow na glownej 
    przekatnej danej macierzy""")

def iloczynOdwrotnosci():
    print("""Iloczyn odwrotnosci wszystkich 
    niezerowych elementow""")

def sredniaArytmetyczna():
    print("Srednia arytmetyczna podanych liczb")

def sredniaGeometryczna():
    print("Srednia geometryczna podanych liczb")

def czestoscWystepowania():
    print("Czestotliwosc wystepowania kazdej wartosci")

def rozkladLU():
    print("Rozklad LU metoda Dolittle'a")

# Zarządzanie inputem użytkownika
def getValidInput(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Podaj liczbę całkowitą!")

# podanie wymiarow macierzy      
print("Proszę podać wymiary macierzy: ")
wymiary = WymiaryMacierzy(0,0) # reset

wymiary.iloscKolumn = getValidInput("Podaj ilość kolumn: ")
wymiary.iloscWierszy = getValidInput("Podaj ilość wierszy: ")

print(f"Macierz ma wymiary {wymiary.iloscKolumn}x{wymiary.iloscWierszy}")

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

if choice < 4:
    print("Proszę podać wymiary drugiej macierzy:")

    wymiary2 = WymiaryMacierzy(0,0)

    wymiary2.iloscKolumn = getValidInput("Podaj ilość kolumn: ")
    wymiary2.iloscWierszy = getValidInput("Podaj ilość wierszy: ")

    print(f"Druga macierz ma wymiary {wymiary2.iloscKolumn}x{wymiary2.iloscWierszy}")

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

print("""
        ===================================================
                        Koniec programu                    
        ===================================================""")
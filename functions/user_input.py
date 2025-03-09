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
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
def rozkladLU(wymiary1, macierz1):
    # Ilość kolumn macierzy musi być równa ilości jej wierszy
    if wymiary1.iloscKolumn != wymiary1.iloscWierszy:
        print("Ilość kolumn macierzy musi być równa ilości wierszy")

    n = len(macierz1)

    # Macierze sterujące, pełne zer
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        # Elementy macierzy U
        for j in range(i, n):
            U[i][j] = macierz1[i][j] - sum(L[i][k] * U[k][j] for k in range(i))

        # Elementy macierzy L
        for j in range(i, n):
            if i == j:
                L[i][i] = 1
            else:
                L[j][i] = (macierz1[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]
    
    print("Macierz L:\n", L)
    print("Macierz U:\n", U)    
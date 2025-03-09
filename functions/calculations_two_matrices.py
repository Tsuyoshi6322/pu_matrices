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

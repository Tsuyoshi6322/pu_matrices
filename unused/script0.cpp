#include <iostream>
#include <string>
#include <cmath>
#include <sstream> // getValidInput()

using namespace std;

struct wymiaryMacierzy{
    int n;
    int m;
} wymiary, wymiary2;

void sumaMacierzy(int n1, int m1, int n2, int m2){
    // 1
    cout << "suma dwoch macierzy\n";
    cout << n1 << m1 << n2 << m2 << endl;;
};

void roznicaMacierzy(){
    // 2
    cout << "roznica dwoch macierzy\n";
};

void iloczynMacierzy(){
    // 3
    cout << "iloczyn dwoch macierzy\n";
};

void transpozycjaMacierzy(){
    // 4
    cout << "transpozycja jednej macierzy\n";
};

void zerowanieElementow(){
    // 5
    cout << "zerowanie elementow na glownej przekatnej danej macierzy\n";
};

void iloczynOdwrotnosci(){
    // 6
    cout << "iloczyn odwrotnosci wszystkich niezerowych elementow\n";
};

void sredniaArytmetyczna(){
    // 7
    cout << "srednia arytmetyczna podanych liczb\n";
};

void sredniaGeometryczna(){
    // 8
    cout << "srednia geometryczna wartosc bezwgl. podanych liczb\n";
};

void czestoscWystepowania(){
    // 9
    cout << "czestosc wystepowania kazdej wartosci\n";
};

void rozkladLU(){
    // 10
    cout << "Rozklad LU metoda Dolittle'a\n";
}

int main() {

  int getValidInput(const string& prompt);
  int displayMenu0(int& choice0);
  
  // Wymiary macierzy
  cout << "Proszę podać wymiary macierzy\n";
  wymiary.n = getValidInput("Podaj ilość kolumn: ");
  wymiary.m = getValidInput("Podaj ilość wierszy: ");

  // Wypelnienie liczbami macierzy o danych wymiarach ---tbd

  // Menu zadan
  int choice0;
  displayMenu0(choice0);

  // Wymiary drugiej macierzy
  if (choice0 < 4) {
    cout << "Proszę podać wymiary drugiej macierzy\n";
    wymiary2.n = getValidInput("Podaj ilość kolumn: ");
    wymiary2.m = getValidInput("Podaj ilość wierszy: ");

    // Wypelnienie liczbami tej macierzy ---tbd
  }

  // Egzekucja zadan
  switch (choice0) {
    case 1: sumaMacierzy(wymiary.n, wymiary.m, wymiary2.n, wymiary2.m); break;
    case 2: roznicaMacierzy(); break;
    case 3: iloczynMacierzy(); break;
    case 4: transpozycjaMacierzy(); break;
    case 5: zerowanieElementow(); break;
    case 6: iloczynOdwrotnosci(); break;
    case 7: sredniaArytmetyczna(); break;
    case 8: sredniaGeometryczna(); break;
    case 9: czestoscWystepowania(); break;
    case 10: rozkladLU(); break;

    default:
      cout << "Nie ma takiego zadania!\n";
      break;
  }

  // Powrot do menu?? ---tbd

  // Koniec
  cout << "=================================================== \n";
  cout << "                  Koniec programu                   \n";
  cout << "=================================================== \n";
  return 0;
}

// Funkcja do zabezpieczenia programu przed nieporządanym inputem
int getValidInput(const string& prompt) {
  string input; // Input
  int value; // Output

  while (true) {
    cout << prompt; // Tekst inputu
    getline(cin, input); // Pobranie linijki inputu

    // Traktowanie input jako danych wejściowych
    stringstream stream(input);
    
    // Czy input da się wpisać w float i czy strumień jest pusty?
    if (stream >> value && stream.eof()) {
      return value;
    } else {
      cout << "Podaj liczbę całkowitą!\n\n";
    }
  }
  
  return value;
}

// Menu zadań -- tbd
int displayMenu0(int &choice0){
  do {
    cout << "=================================================== \n";
    cout << "                    Menu zadań                      \n";
    cout << "=================================================== \n";
    cout << "[1] Zadania 1.1-7    Własności liczby a             \n";
    cout << "=================================================== \n";
    
    choice0 = getValidInput("Proszę podać liczbę (1-10): ");
    if (choice0 < 1 || choice0 > 10){
      cout << "Nie ma takiego zadania!\n";
      cout << "Sprobuj ponownie.\n\n";
    }
  } while (choice0 < 1 || choice0 > 10);

  cout << "Wybrano: " << choice0 << endl << endl;
  return choice0;
};


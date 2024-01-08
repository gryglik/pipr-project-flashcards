# 1. Informacje

## Dane autora projektu
* imie i nazwisko: **Michał Gryglicki**
* nr indeksu: **331380**
* uczelnia: **Politechnika Warszawska**
* wydział: **Elektroniki i Technik informacyjnych**
* kierunek: **Informatyka**
* semestr: **2023 zimowy**
* przedmiot: **Podstawy Informatyki i Programowania**

## Założenia projektu
### Tematem projektu jest realizacja elektronicznej wersji fiszek, na których umiescza się słowa w dwóch językach. Aplikacja ma mieć następujące funkcjonalności:
* definiowanie fiszek
* importowanie oraz eksportowanie fiszek
* zarządzanie fiszkami (ustawienie priorytetu, usunięcie),
* planowanie czasu testów
* przeprowadzenie testu z predefiniowaną liczbą fiszek
* wygenerowanie statystyk dotyczących efektów nauki
* wygenerowanie statystyk dotyczących korzystania z aplikacji

# 2. Realizacja

## Struktura projektu
### Projekt został podzielony na następujące moduły:
1. moduł interfejsu graicznego [flashcards_gui.py](flashcards_gui.py)
2. moduł logiki aplikacji [flashcards_logic.py](flashcards_logic.py)
3. moduł obsługi wejścia i wyjścia [flashcards_io.py](flashcards_io.py)

### 1. Moduł interfejsu graficznego
#### 1.1. Opis
Odpowiada za komunikacje między uzytkownikiem a logiką programu. inicjalizuje okno aplikacji oraz sesję. Interakcja z konkretnym elementem interfejsu przez uzytkowinka powoduje przekazanie informacji do logiki aplikacji a następnie, po przetworzeniu zmian, zwraca odpowiedni komunikat klientowi.

#### 1.2. Biblioteki
Moduł korzysta z następujących bibliotek
* wbudowane biblioteki Pythona:
    * **sys**
    * **typing** - obsługa statycznego typowania (type hints)
* zewnętrzne biblioteki:
    * **PySide6** - obsługa interfejsu graficznego (GUI)
* własne bibliotek:
    * **[biblioteka interfejsu](lib/ui)**
        * [ikony](lib/ui/icons/)
        * [moduł własnych okien dialogowych](lib/ui/dialogs.py)
        * [moduł własnych podstawowych widżetów](lib/ui/widgets_basic.py)
        * [moduł własnych zaawsowanych widżetów](lib/ui/widgets.py)
        ----
        * [główny moduł konfiguracyjny głównego okna aplikacji](lib/ui/flashcards_ui.py) - wykonany z wykorzystaniem oprogramowania z biblioteki **PySide6**. Wykorzystuje funkcjonalność **kaskadowych arkuszy stylów (CSS)**, dzięki temu interfejs graficzny jest spójny graficznie.
        * [moduły konfiguracyjne widżetów oraz okien dialogowych ](lib/ui/widgets_ui/) - wykonanych z wykorzystaniem oprogramowania z biblioteki **PySide6**
    * **[biblioteka logiki gry](flashcards_logic.py)** - do obsługi zachowań użytkownika

#### 1.3. Opis klas
Plik zawiera jedną klasę FlaschcardWindow odpowiedzialną za obsługę głównego okna aplikacji.
Dokładny opis klasy oraz metod znajduje się w docstring-ach w **[kodzie źródłowym modułu](flashcards_gui.py)**

### 2. Moduł logiki aplikacji
#### 2.1. Opis
Odpowiada za dostarczanie funkcjonalności programu. Obsługuje zapytania wysyłane przez moduł interfejsu użytkownika.

#### 2.2. Biblioteki
Moduł korzysta z następujących bibliotek:
* biblioteki wbudowane Pythona
    * **__future__** - do wykorzystania pełnej funkcjonalność statycznego typowania w kodzie
    * **random** - obsługa losowania obieków
    * **time** - obsługa pomiaru czasu
* biblioteki własne
    * **[biblioteka własnych wyjątków](lib/errors.py)**
#### 2.3. Opis klas
* **Flashcard** - przechowuje informacje o pojedynczej fiszce (daną frazę, definicję oraz priorytem)
* **FlashcardsSet** - przechowuje zbiór fiszek (Flashcards) o danej nazwie
* **TestItem** - reprezentuje jedno zadanie testowe (pytanie)
* **Test** - reprezentuje zbiór zadań testowych (TestItem)
* **TestResult** - reprezentuje wynik testu (Test)
* **Session** - przechowuje informacje o aktualnej sesji użytkownika - ta klasa obsługuje zapytania kierowane przez zalogowanego użytkownika
* **SessionStats** - przechowuje statystyki aktualnej sesji (Session) tworzy się automatycznie przy inicjacji sesji

Szczegółowy opis klas oraz ich metod znajduje się w docstringach w [kodzie źródłowym modułu](flashcards_logic.py)

### 3. Moduł obsługi wejścia i wyjścia
#### 3.1. Opis
Moduł odpowiada za komunikację programu z zewnętrznymi danymi.

#### 3.2. Biblioteki
Moduł korzysta z następujących bibliotek:
* biblioteki wbudowane Pythona
    * **typing** - obsługa statycznego typowania (type hints)
    * **os.path** - obsługa operacji na ścieżkach
    * **csv** - obsługa serializacji danych do pliku csv
* biblioteki własne
    * **lib.errors** - obsługa własnych wyjątków
    * **flashcards_logic** - połączenie z modułem logiki

#### 3.3. Opis klas
* **Import** - obiekt importu w tym obiekcie są ładowane oraz interpretowane dane z zewnętrznego źródła
* **Export** - obiekt eksportu, w tym obiekcie dane programu są zachowywane w zewnętrznym źródle

Szczegółowy opis klas oraz ich metod znajduje się w docstringach w [kodzie źródłowym modułu](flashcards_logic.py)

## Testowanie
Projekt obejmuje niemal **100 testów jednostkowych** sprawdzających kluczowe funkcjonalności. Moduły został także przetestowany pod kątem możliwych błędów.
* [testy jednostkowe modułu logiki](tests/test_flashcards_logic.py)
* [testy jednostkowe modułu obsługi wejścia i wyjścia](tests/test_flashcards_io.py)

# 3. Funkcjonalności
### 1. Krytyczne
* Definiowanie fiszek
* Import / export fiszek do pliku csv
* Zarządzanie fiszkami (ustawienie priorytetu, usunięcie)
* przeprowadzenie testu z predefiniowaną liczbą fiszek
* wygenerowanie statystyk dotyczących efektów nauki
* planowanie czasu testów
* wygenerowanie statystyk dotyczących korzystania z aplikacji

### 2. Dodatkowe
* Podział fiszek na zestawy
* Zarządzenie zestawami (zmiana nazwy, usuwanie)
* Możliwość przeglądania fiszek w odwróconej formie
* Generowanie testu z możliwością wyboru rodzaju odpowiedzi

### 3. Planowane
* Możliwość zapisu całej sesji - profilu użytkownika - i ponownego uruchomienia aplikacji bez koniczności importowania zestawów

# 4. Instrukcja obsługi

## Uruchomienie:
### Wymagania:
- Python: 3.12.0 wraz z pakietami z pliku [requirements.txt](requirements.txt)
### Uruchomienie:
- Aby uruchomić program należy uruchomić plik [flashcards_gui.py](flashcards_gui.py)

# 5. Refleksje
Projekt okazał się bardzo ciekawy i rozwijający. Konieczność samodzielnego szukania rozwiącań celem uzyskania założonego efektu sprawiła, że zdobyłem dużo nowych umiejętności.
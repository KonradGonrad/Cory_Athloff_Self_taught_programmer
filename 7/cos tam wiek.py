#1. Wyświetl trzy różne łańcuchy znaków
lancuch_1 = "Witaj drogi użytkowniku!"
lancuch_2 = "oprogramowanie Windows."
print(lancuch_1,"\nZ tej strony",lancuch_2)


#2. Napisz program wyświetlający komunikat, jeśli wartość zmiennej będzie mniejsza od 10 oraz inny komunikat, jeśli wartość tej zmiennej będzie większa lub równa 10
liczba = int(input("Podaj liczbe: "))
if (liczba < 10):
    print("Liczba jest mniejsza niż 10.")
elif (liczba >= 10):
    print("Liczba jest większa niż 10")


#3. Napisz program, który będzie wyświetlał komunikat, jeśli wartość zmiennej będzie mniejsza lub równa 10, inny komunikat, jeśli wartość tej zmiennej będzie większa od 10, lecz mniejsza lub 
#   równa 25 oraz jeszcze inny komunikat, kiedy wartość ta będzie większa od 25
liczba = int(input("Podaj liczbe: "))
if (liczba < 10):
    print("Liczba jest mniejsza niż 10")
elif (10 < liczba <= 25):
    print("Liczba jest większa od 10, lecz mniejsza lub równa 25")
elif (liczba > 25):
    print("Liczba jest większa od 25")


#4. Napisz program, który podzieli dwie zmienne i wyświetli uzyskaną resztę z dzielenia
x = int(input("Podaj pierwsza liczbe: "))
y = int(input("Podaj druga liczbe: "))

wynik = x % y
print("reszta z dzielenia to: ", wynik)

#5. Napisz program, który podzieli dwie zmienne i wyświetli ich iloraz

wynik = x // y
print("iloraz podanych liczb wynosi: ", wynik)


#6. Napisz program ze zmienną 'age' przypisaną do liczby całkitej, który w zaleznosci od jej wartosci będzie wyswietlał różne łańcuchy znaków
print("\nProgram do sprawdzania pelnoletnosci i zakresu wieku")
wiek = int(input("Proszę podać swój wiek: "))

if (wiek < 18):
    print("jesteś osobą niepełnoletnią!")
if (15 < wiek <= 18):
    print("twój zakres wieku to młodzież")
if (10 < wiek <= 15):
        print("twój zakres wieku to nastolatek")    
if (5 < wiek <= 10):
    print("twój zakres wieku to dziecko")
if (1 < wiek <= 5):
    print("twój zakres wieku to małe dziecko")


if (wiek >= 18):
    print("jesteś osobą pełnoletnią!")
if (18 < wiek <=25):
    print("twój zakres wieku to młody dorosły")
elif (25 < wiek <= 30):
    print("twój zakres wieku to dorosły przed 30")
elif (30 < wiek <= 40):
    print("twój zakres wieku to dorosły po 30")
elif (40 < wiek <= 50):
    print("twój zakres wieku to dorosły po 40")
elif (50 < wiek <= 60):
    print("twój zakres wieku to dorosły po 50")
elif (60 < wiek):
    print("twój zakres wieku to emeryt")
    

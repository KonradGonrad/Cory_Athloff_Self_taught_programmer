# Pomnóż wszystkie liczby z listy [8, 19, 148, 4] przez wszystkie liczby z listy [9, 1, 33, 83], a zapisane wyniki zapisz w trzeciej liście

pierwsza = [8, 19, 148, 4]
druga = [9, 1, 33, 83]
wyniki = []

for i in pierwsza:
    for j in druga:
        wynik = i * j
        wyniki.append(wynik)
    print(wyniki)


# Napisz program, który pozwoli użytkownikowi pytać o różne informacje dotyczące Ciebie, takie jak wzrost, ulubiony kolor, ulubiony autor, a następnie będzie je zwracać ze słownika
# utworzonego w poprzednim zadaniu

Konrad = {"wzrost": "181 cm",
          "ulubiony_kolor": "niebieski",
          "ulubiony_artysta": "Kendrick Lamar",
          "miejsce_zamieszkania": "Ostrowiec Św",
          "kolor_oczu": "zielony",
          "miejsce_urodzenia": "Opatów",
          "wiek": "19 lat"}

ask = input("Powiedz, o co chcesz zapytać? ")

if ask in Konrad:
    print(Konrad[ask])
else:
    print("Nie znaleziono")
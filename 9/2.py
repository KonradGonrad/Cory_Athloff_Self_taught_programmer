# Napisz program który zada użytkownikowi pytanie i zapisze odpowiedź w pliku

Pytanie = str(input("Jak się dzisiaj czujesz? "))

with open(r"C:\Users\konra\Desktop\Python\Programista samouk\9 - Pliki\samopoczucie.txt", "w") as f:
    f.write(Pytanie)

with open(r"C:\Users\konra\Desktop\Python\Programista samouk\9 - Pliki\samopoczucie.txt", "r") as f:
    print(f.read())
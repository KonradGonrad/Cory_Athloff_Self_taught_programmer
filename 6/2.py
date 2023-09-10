#Napisz program, który będzie pobierać od użytkownika dwa łańcuchy znaków, a następnie wstawiać je do łańcucha: “Wczoraj napisałem [łańcuch_1] i wysłałem do [łańcuch_2]” oraz wyświetlać
string_1 = input("Podaj pierwszy ciąg znaków: ")
string_2 = input("Podaj drugi ciąg znaków: ")

print("Wczoraj napisałem {} i wysłałem do {}".format(string_1, string_2))
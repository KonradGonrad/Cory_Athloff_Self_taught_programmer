# Napisz funkcję, która konwertuje łańcuch znaków na wartość typu float i zwraca uzyskaną wartość. Zastosuj obsługę wyjątków, by przechwytywać ewentualne błędy.

def str_to_float():
    """
    convert str into float type and then print out.
    :words: str.
    :words: float.
    :print(words): float.
    """
    try:
        words = input("Podaj łańcuch znaków: ")
        words = float(words)
        print(words)
    except(ValueError):
        print("Nieprawidłowe dane wejściowe")

str_to_float()
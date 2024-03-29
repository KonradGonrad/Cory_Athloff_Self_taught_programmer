import re

text = """Żyrafy od samego momentu odkrycia 
Stanowią __RZECZOWNIK_LPOJ__ świata zwierząt. 
Są one najwyższymi ze wszystkich żyjących 
na świecie __RZECZOWNIK_LMNOGA__, jednak 
naukowcy nie są w stanie wyjaśnić, w jaki 
sposób ich __CZESC_CIALA__ stała się tak długa. 
Żyrafy zawdzięczają swoją niesamowitą 
wysokość, która może dochodzić do 
__LICZBA__ __RZECZOWNIK_LMNOGA__, swoim 
nogom i __CZESC_CIALA__."""

def mad_libs(mls):
    """
    :param mls: Łańcuch znaków,
    zawierający części otoczone podwójnymi 
    znakami podkreślenia, które użytkownik
    powinien zastąpić samodzielnie wybranymi
    słowami. W sugestiach nie można
    umieszczać znaków podkreślenia; np:
    nie _to_sugestia_, tylko _sugestia_.
    """
    print(text,"\n")
    

    hints = re.findall("__.*?__",
                        mls,)
    if hints is not None:
        for word in hints:
            q = "Wpisz {}:"\
                    .format(word)
            new = input(q)
            mls = mls.replace(word,
                              new,
                              1)
            print("\n")
            mls = mls.replace("\n", "")
            print(mls)
        else:
            print("\nUkończono!")

mad_libs(text)
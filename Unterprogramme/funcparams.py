# Demonstration von Parametern für Funktionen


def dump(p1, p2=2, p3=None):
    """ Funktion mit drei Parametern, wobei p2 und p3 optional sind
    """
    print(p1)
    print(p2)
    print(p3)

# Positionsparameter und benannte parameter im Vergleich
# (zwei gleiche Aufrufe)
dump(1,2,3)          # Positionsparameter
dump(p2=2,p1=1,p3=3) # benannte Parameter

# Nutzung der Defaultparameter
dump(1)       # p1=1, p2 und p3 default
dump(1,3)     # p1=1, p2=3, p3 default
dump(1, p3=3) # p1=1, p2 default, p3=3

# Was nicht funktioniert:
# dump(p2=1, 3) # FALSCH: Positionsparameter müssen am Anfang stehen
# dump(1, p4=3) # FALSCH: benannter Parameter nicht vorhanden
#
# def myfuc(p1="default", p2): # FALSCH: Defaultwerte müssen
#     pass                     # am Ende der Parameterliste stehen
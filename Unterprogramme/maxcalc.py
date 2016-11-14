# Demonstration von Funktionen

def calc_max(z1, z2):
    if z1 > z2:
        return z1
    else:
        return z2


maxval = 0
i = 0
while i >= 0:
    i = int(input("Bitte positive Zahl eingeben (negativ beendet): "))
    maxval = calc_max(maxval, i)

print(maxval)
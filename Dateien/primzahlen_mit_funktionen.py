# -*- coding: utf-8 -*-

def inputRange():
    """ Input number range from console
    @return: (min, max) tuple with including numbers
    @rtype: 2 tuple of int
    """
    print("Bitte geben sie einen Zahlenbereich ein, in der alle Primzahlen")
    print("ermittelt werden sollen.")

    print() 

    print("erste Zahl")              # die erste Zahl des Bereiches
    minval = int(input())


    print("letzte Zahl")             # die letzte Zahl des Bereiches
    maxval = int(input())

    print()

    return (minval, maxval)

def calcPrimes(minval, maxval):
    """Calculate prime numberd from minval to maxval
    @param minval: minimum value
    @type minval: int
    @param maxval: maximum value (included)
    @type maxval: int
    @return: prime numbers
    @rtype: list of int
    """

    primes = []                     # Liste der Primzahlen, zu Beginn noch leer
    num = minval                    # Anfangen mit der ersten gefragten Zahl

    while num <= maxval:            # Solange die Zahl nicht groesser als der
                                    # Bereich ist, wird die Schleife ausgefuehrt
        divisor = 2                 # der erste divisor ist 2
        flag = True


        while divisor <= num / 2 and flag:  # die schleife wird solange ausgefuehrt,
                                            # bis entweder die num halbsogross ist
                                            # wie der divisor und flag wahr ist

            rest = num % divisor    # es wird der rest ermittelt
            if rest == 0:           # nun wird geschaut ob eine rest ueberbleibt
                flag=False          # wenn ja ist flag falsch
            divisor += 1            # der divisor wird um eins erhoet

        if flag:                    # wenn die num eine primzahl ist
            primes.append(num)      # wird sie der liste hinzugefuegt
            num += 1                # die naechste num wird ueberprueft

        else:                       # wenn die num keine primzahl ist
            num += 1                # wird die naechste num ueberprueft

    return primes


def write_list_to_file(data, filename):
    """ Write a list to a file with each element in one line.

    :param data: list of elements
    :param filename: name of output file
    :return: nothing
    """

    with open(filename, "w") as outfile:
        for item in data:
            outfile.write(str(item)+"\n")

primerange = inputRange()
primes = calcPrimes(primerange[0], primerange[1])
filename = input("Bitte Dateinamen zur Ausgabe eingeben: ")
if len(filename) > 0:
    write_list_to_file(primes, filename)
else:
    print("Primzahlen sind:")
    print()
    for prime in primes:
        print(prime)


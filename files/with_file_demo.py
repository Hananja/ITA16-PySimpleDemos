#
# Umgang mit with

def read_from_file(filename):
    # automatisches .close() beim Verlassen
    # des with-Blocks (egal wie)
    with open(filename) as infile:
        # return verlässt den Block und
        # die Datei wird geschlossen
        return infile.readline()


print(read_from_file("myfile.txt"))


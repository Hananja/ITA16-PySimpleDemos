# Zeilen zählen mit Python

with open(input("Dateiname: ")) as infile:
    print(len(infile.readlines()))
#
# Einfache Demonstration zur Verwendung von Dateien
#

# Datei myfile.txt anlegen und zum Schreiben öffnen
myfile = open(r"myfile.txt", 'w')

# Schreiben in die Datei
myfile.write("Dies ist ein Test\n")
print("Dies ist ein print", file=myfile)

# Datei schliessen
myfile.close()

# Datei myfile.txt zum lesen öffnen
myfile = open("myfile.txt")

# zwei Zeilen aus der Datei lesen und auf der
# Konsole ausgeben (.strip() entfernt \n)
line = myfile.readline().strip()
print(line)
line = myfile.readline()
print(line)

# Datei schliessen
myfile.close()
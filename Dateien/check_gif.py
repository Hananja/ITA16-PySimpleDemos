# GIF Dateien prüfen und ggf. Auflösung ausgeben
#

with open(input("Dateiname: "), "rb") as infile:
    infile.seek(0) # gehe zum Anfang der Datei
                   # (direkt nach dem Öffnen nicht notwendig)

    fileid = infile.read(4) # 4 Bytes lesen

    if fileid == b"GIF8":
        # Breite auslesen
        infile.seek(6)
        width = ord(infile.read(1)) + 256 * ord(infile.read(1))

        # Höhe auslesen
        height = ord(infile.read(1)) + 256 * ord(infile.read(1))

        print("Ist ein GIF Bild mit %d x %d Pixeln!" %(width, height))
    else:
        print("Ist kein GIF Bild!")
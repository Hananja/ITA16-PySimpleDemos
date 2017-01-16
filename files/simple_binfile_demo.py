
# binary file demo
#

# Binärdatei öffnen
myfile = open("c:\\windows\\write.exe", "rb")

# ein Byte lesen
myfile.seek(100)         # bei Byte 10 starten
result = myfile.read(2) # 2 Bytes lesen

myfile.close()

print(result)
print(result[0], result[1])

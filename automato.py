path = "./"
arquivo = "entrada.txt"

f = open(path+arquivo,"r")
loaded = f.read()
f.close()

loadedSplit = loaded.split("\n")
print(loadedSplit[5:5+int(loadedSplit[4])])
print(loadedSplit[5+int(loadedSplit[4]):])
dictEntrada = {
    "N_Estados" : loadedSplit[0],
    "Terminais" : loadedSplit[1],
    "Estados_Iniciais" : loadedSplit[2],
    "Estados_Aceitacao" : loadedSplit[3],
    "N_Transicoes" : loadedSplit[4],
    "Transicoes" : loadedSplit[5:5+int(loadedSplit[4])],
    "N_Cadeias" : loadedSplit[5+int(loadedSplit[4])],
    "Cadeias" : loadedSplit[int(loadedSplit[4]):],
    }
print(dictEntrada)
print(dictEntrada)
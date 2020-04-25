def leEntrada():
    path = "./"
    arquivo = "entrada.txt"

    f = open(path+arquivo,"r")
    loaded = f.read()
    f.close()


    loadedSplit = loaded.split("\n")
    quantidadeEstadoInicial = int(loadedSplit[2])
    estadosIniciais = [str(x) for x in range(0,quantidadeEstadoInicial)]
    dictEntrada = {
        "N_Estados" : loadedSplit[0],
        "N_Terminais" : loadedSplit[1].split(" ")[0],
        "Terminais" : loadedSplit[1][2:].split(" "),
        "Estados_Iniciais" : estadosIniciais,
        "Estados_Aceitacao" : loadedSplit[3].split(" ")[1:],
        "N_Transicoes" : loadedSplit[4],
        # "Transicoes" : loadedSplit[5:5+int(loadedSplit[4])],
        "Transicoes" : [transicao.split(" ") for transicao in loadedSplit[5:5+int(loadedSplit[4])]],
        "N_Cadeias" : loadedSplit[5+int(loadedSplit[4])],
        # "Cadeias" : loadedSplit[int(loadedSplit[4]):],
        "Cadeias" : [cadeia.split(" ") for cadeia in loadedSplit[6+int(loadedSplit[4]):]],
        }
    dictTransicoes = {}
    for transicao in dictEntrada.get("Transicoes"):
        estadoAtual = dictTransicoes.get(transicao[0])
        if estadoAtual is not None:
            transicaoDesseEstado = estadoAtual.get("Transicoes")
            transicaoAtual = transicaoDesseEstado.get(transicao[1])
            if transicaoAtual is not None:
                transicaoAtual.append(transicao[2])
            else:
                transicaoDesseEstado.update({
                    transicao[1] : [transicao[2]] 
                })   
                
            verificaTransicao = dictTransicoes.get(transicao[2]) 
            if verificaTransicao is None:
                dictTransicoes.update({
                    transicao[2] : {
                        "Transicoes" : {}
                    }
                })
        else:
            dictTransicoes.update({
                transicao[0] : {
                    "Transicoes" : {
                        transicao[1] : [transicao[2]] 
                    }}})

            verificaTransicao = dictTransicoes.get(transicao[2]) 
            if verificaTransicao is None:
                dictTransicoes.update({
                    transicao[2] : {
                        "Transicoes" : {}
                    }
                })


        
    deterministico = True   
    if len(dictEntrada.get("Estados_Iniciais")) > 1:
        deterministico = False
        
    for estado in dictTransicoes:
        if estado in dictEntrada.get("Estados_Iniciais"):
            incial = True
        else:
            incial = False
            
        if estado in dictEntrada.get("Estados_Aceitacao"):
            final = True
        else:
            final = False   
        
        transicoes = dictTransicoes.get(estado).get("Transicoes")
        for transicao in transicoes:
            transicaoAtual = transicoes.get(transicao)
            if len(transicaoAtual) > 1:
                deterministico = False
        dictTransicoes.get(estado).update({
            "final" : final,
            "inicial" : incial,
            # "deterministico" : deterministico
        })
    
    return dictTransicoes,dictEntrada,deterministico
    
# def trasformaDeterministico(dictTransicoes,dictEntrada):
#     entradas = dictEntrada.get("Estados_Iniciais")
#     terminais = dictEntrada.get("Terminais")
#     # estadoInicial = "+".join(entradas)
#     estadosProcessados = entradas.sort()
#     estadosNãoProcessados [] 
#     dictEstadosTerminais = {terminal:[] for terminal in terminais}
#     for estado in entradas:
#         print(estado)
#         transicoes = dictTransicoes.get(estado).get("Transicoes")
#         if len(transicoes) > 0:
#             for transicaoAtual in transicoes:
#                 print(transicaoAtual)
#                 for estadoTransicaoAtual in transicoes.get(transicaoAtual):
#                     print(estadoTransicaoAtual)
#                     if estadoTransicaoAtual not in dictEstadosTerminais.get(transicaoAtual):
#                         dictEstadosTerminais.get(transicaoAtual).append(estadoTransicaoAtual)
#                 print(dictEstadosTerminais.get(transicaoAtual))
#                 print(transicoes.get(transicaoAtual))
    
#     print("a")

# dictTransicoes,dictEntrada,derteminisico = leEntrada()
# trasformaDeterministico(dictTransicoes,dictEntrada)

# a,b,c = le_entrada()
# print(a,b,c)
# print(dictTransicoes)
# a = [x.split(" ") for x in loadedSplit[5:5+int(loadedSplit[4])]]
# print(a)
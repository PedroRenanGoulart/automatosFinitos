def processa_cadeia(automato, terminais, estados_iniciais, estados_aceitacao, cadeias):
    for index_cadeia in range(len(cadeias)):
        cadeia = cadeias[index_cadeia][0]
        # print("PROCESSANDO CADEIA: ", cadeia)
        rejected = False
        #COLOCANDO ESTADO INICIAL
        caminho_estados = [get_proximo_passo(automato, estados_iniciais[0], cadeia[0])]

        for i in range(len(cadeia)):
            processando = cadeia[i]
            # print("----- index: ", i, "-----")
            # print("processando: ", processando)

            # if i == 0:
            #     # pegar pelo estado inicial. Como é AFD sempre um estado só.
            # else :
            estado = caminho_estados[i - 1].get('estado')
            estado = estado[0]

            proximo_passo = get_proximo_passo(automato, estado, processando)
            if proximo_passo == "ERROR_KEY_TRANSICOES" or proximo_passo == "ERROR_KEY_FINAL":
                print("NÃO ACHOU  A TRANSIÇÃO PARA ", processando, "NO ESTADO ", estado)
                rejected = True
                break


            # print("PROXIMO PASSO: ", proximo_passo)
            caminho_estados.append(proximo_passo)
            # print("PASSOS DADOS: ", caminho_estados)
            if proximo_passo == "STATE_NOT_FOUND":
                print("Cadeia: ", cadeia, "rejeitada \n")
                rejected = True
                break
            #Se for processar uma variável que não está nas variáveis terminais
            # rejeita ela;
            if processando not in terminais:
                print("Cadeia: ", cadeia, "rejeitada \n")
                rejected = True

        # print("CAMINHO PROCESSADO: ", caminho_estados)
        if not rejected:
            final = caminho_estados[len(caminho_estados)- 1].get("final")
            # print("FINAL: ", final)
            if not final:
                print("Cadeia: ", cadeia, "rejeitada \n")
            else:
                print("Cadeia: ", cadeia, "aceita \n")

        



def get_proximo_passo(automato, estadoAtual, processando):
    aux = automato.get(estadoAtual, "STATE_NOT_FOUND")
    # print(aux)
    if aux == "STATE_NOT_FOUND":
        return "STATE_NOT_FOUND"

    estado = aux.get("Transicoes", "ERROR_KEY_TRANSICOES")
    if estado == "ERROR_KEY_TRANSICOES":
        return "ERROR_KEY_TRANSICOES"

    final = aux.get("final", "ERROR_KEY_FINAL")
    if final == "ERROR_KEY_FINAL":
        return "ERROR_KEY_FINAL"

    return { 'estado': estado.get(processando, "REJECT"), 'final': final }
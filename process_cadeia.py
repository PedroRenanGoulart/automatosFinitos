def processa_cadeia(automato, terminais, estados_iniciais, estados_aceitacao, cadeias):
    result = []
    for index_cadeia in range(len(cadeias)):
        cadeia = cadeias[index_cadeia][0]
        # print("PROCESSANDO CADEIA: ", cadeia)
        # print("(", len(cadeia), ")")
        rejected = False
        #COLOCANDO ESTADO INICIAL
        automato_estado_inicial = get_no_inicial(automato, estados_iniciais[0])
        caminho_estados = [automato_estado_inicial]

        for i in range(len(cadeia)):
            # if cadeia == "bbabbabbabbb":
            #     print("BATATAo")
            #     pass
            processando = cadeia[i]
            if processando == '-':
                # print(index_cadeia + 1, ". Cadeia: ", cadeia, "rejeitada \n")
                print("rejeita")
                result.append("rejeita")
                rejected = True
                break
            # print("----- index: ", i, "-----")
            # print("processando: ", processando)

            # if i == 0:
            #     # pegar pelo estado inicial. Como é AFD sempre um estado só.
            # else :
            # mudei aqui
            if caminho_estados[i - 1] == "REJECT":
                # print(index_cadeia + 1, ". Cadeia: ", cadeia, "rejeitada \n")
                print("rejeita")
                result.append("rejeita")
                rejected = True
                break

            estado = caminho_estados[i].get('estado')
            # estado = estado[0]

            proximo_passo = get_proximo_passo(automato, estado, processando)
            # print(proximo_passo)
            if proximo_passo == "ERROR_KEY_TRANSICOES" or proximo_passo == "ERROR_KEY_FINAL" or proximo_passo == "REJECT":
                # print("NÃO ACHOU  A TRANSIÇÃO PARA ", processando, "NO ESTADO ", estado)
                print("rejeita")
                result.append("rejeita")
                rejected = True
                break


            # print("PROXIMO PASSO: ", proximo_passo)
            caminho_estados.append(proximo_passo)
            # print("PASSOS DADOS: ", caminho_estados)
            if proximo_passo == "STATE_NOT_FOUND":
                # print(index_cadeia + 1, ". Cadeia: ", cadeia, "rejeitada \n")
                print("rejeita")
                result.append("rejeita")
                rejected = True
                break
            #Se for processar uma variável que não está nas variáveis terminais
            # rejeita ela;
            if processando not in terminais:
                # print(index_cadeia + 1, ". Cadeia: ", cadeia, "rejeitada \n")
                print("rejeita")
                result.append("rejeita")
                rejected = True

        # print("CAMINHO PROCESSADO: ", caminho_estados)
        # print("tamanho percorrido: ", len(caminho_estados))
        if not rejected:
            estado_final_da_cadeia = caminho_estados[len(caminho_estados)- 1].get("estado")
            # print("FINAL: ", final)
            # if not final:
            if estado_final_da_cadeia not in estados_aceitacao:
                # print(index_cadeia + 1, ". Cadeia: ", cadeia, "rejeitada \n")
                print("rejeita")
                result.append("rejeita")
            else:
                # print(index_cadeia + 1, ". Cadeia: ", cadeia, "aceita \n")
                print("aceita")
                result.append("aceita")
        
        caminho_estados = []
    return result


def get_no_inicial(automato, estado_inicial):
    aux = automato.get(estado_inicial, "STATE_NOT_FOUND")

    if aux == "STATE_NOT_FOUND":
        return "STATE_NOT_FOUND"
    
    # final = aux.get("final", "ERROR_KEY_FINAL")
    
    # if final == "ERROR_KEY_FINAL":
    #     return "ERROR_KEY_FINAL"
    #, 'final': final
    return { 'estado': estado_inicial }


def get_proximo_passo(automato, estadoAtual, processando):
    aux = automato.get(estadoAtual, "STATE_NOT_FOUND")
    # print(aux)
    if aux == "STATE_NOT_FOUND":
        return "STATE_NOT_FOUND"

    transacoes = aux.get("Transicoes", "ERROR_KEY_TRANSICOES")
    if transacoes == "ERROR_KEY_TRANSICOES":
        return "ERROR_KEY_TRANSICOES"
    prox_estado_nome = transacoes.get(processando, "REJECT")

    if prox_estado_nome == "REJECT":
        return "REJECT"
    # print("PROX ESTADO NOME: ", prox_estado_nome)
    # aux.get("final", "ERROR_KEY_FINAL")
    # prox_estado_no = automato.get(prox_estado_nome[0])
    # final = prox_estado_no.get("final", "ERROR_KEY_FINAL")
    # prox_estado = prox_estado_no.get()
    # if final == "ERROR_KEY_FINAL":
    #     return "ERROR_KEY_FINAL"
    # , 'final': final
    return { 'estado': prox_estado_nome[0] }
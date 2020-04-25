from automato import leEntrada
# Lê entrada e retorna string
def le_entrada():
    dictTransicoes,dictEntrada,deterministico = leEntrada()
    return dictTransicoes,dictEntrada,deterministico

# Pega string de entrada e retorna estrutura definida
def entrada_para_estrutura(entrada):
    pass


# Recebe estrutura e retorna true se é determinístico e false se é não determinístico
def eh_deterministic0(automato):
    pass


# Recebe estrutura de automato deterministico e printa aceito ou não aceito
def avalia_automato_deterministico(automato):
    pass


# Recebe um automato nao deterministico e retorna um automato deterministico equivalente
def transforma_em_deterministico(automato_nao_deterministico):
    pass


if __name__ == '__main__':
    dictTransicoes,dictEntrada,deterministico = le_entrada()
    automato = entrada_para_estrutura()
    if eh_deterministico(automato):
        avalia_automato_deterministico(automato)
    else:
        avalia_automato_deterministico(
            transforma_em_deterministico(automato)
        )

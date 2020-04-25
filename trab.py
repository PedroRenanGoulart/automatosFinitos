from automato import leEntrada
from process_cadeia import processa_cadeia
import pprint
from automato import trasformaDeterministico
# pp = pprint.PrettyPrinter(indent=4)

# Lê entrada e retorna string
def le_entrada():
    dictTransicoes,dictEntrada,deterministico = leEntrada()
    return dictTransicoes,dictEntrada,deterministico

# Pega string de entrada e retorna estrutura definida
def gera_automato(entrada_tratada):
    pass


# Recebe estrutura e retorna true se é determinístico e false se é não determinístico
def eh_deterministic0(automato):
    pass


# Recebe estrutura de automato deterministico e as cadeias. para cada cadeia printa aceito ou rejeita
def avalia_cadeias(automato, terminais, estados_iniciais, estados_aceitacao, cadeias):
    return processa_cadeia(automato, terminais, estados_iniciais, estados_aceitacao, cadeias)

    


# Recebe um automato nao deterministico e retorna um automato deterministico equivalente
def transforma_em_deterministico(dictTransicoes,dictEntrada):
    return trasformaDeterministico(dictTransicoes,dictEntrada)


if __name__ == '__main__':
    dictTransicoes, dictEntrada, deterministico = le_entrada()
    print("\n")
    if not deterministico:
        dictTransicoes,dictEntrada = transforma_em_deterministico(dictTransicoes,dictEntrada)
    # pp.pprint(dictTransicoes)
    # print("\n")
    # print(dictEntrada)
    # print("\n")
    # print(deterministico)
    
    # automato = gera_automato()
    
    result = avalia_cadeias(dictTransicoes, dictEntrada.get("Terminais"), dictEntrada.get("Estados_Iniciais"), dictEntrada.get("Estados_Aceitacao"), dictEntrada.get("Cadeias"))
    print(result)
    # if eh_deterministico(automato):
    #     avalia_automato_deterministico(automato)
    # else:
    #     avalia_automato_deterministico(
    #         transforma_em_deterministico(automato)
    #     )

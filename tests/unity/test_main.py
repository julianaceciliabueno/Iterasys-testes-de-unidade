import csv

import pytest

from main import somar, dividir, subtrair, imprimir_oi
# se um dia for mexer com o banco de dados, pedir uma view somente leitura


#as funcões vem antes dos testes, pois podem seer usadas mais de uma vez
def ler_csv(arquivo_csv):
    dados_csv = [] #caixa vazia
    try:
        with open(arquivo_csv, newline='') as massa: #abriu o arquivo, newline ignora o titulo da tabela
            campos = csv.reader(massa, delimiter=',') #dividiu em pedaços
            next(campos)#muda para as proximas linhas
            for linha in campos:
                dados_csv.append(linha) #está organizando as linhas
        return dados_csv #retorna com a lista montada
    except FileExistsError: #se der errado tudo
        print(f'arquivo não encontrado: {arquivo_csv}')
    except Exception as fail: #para outras falhas genericas
        print(f'falha imprevista: {fail}') #$ significa que virá uma variavel

def somar(numero_a, numero_b):
    return numero_a + numero_b

def dividir(numero_a, numero_b):
    return numero_a / numero_b

def subtrair(numero_a, numero_b):
    return numero_a - numero_b

# coloque 2 linhas para baixo para ele saber que são dois blocos diferentes.
if __name__ == '__main__': #__name__ palavra mágica, aqui inicia o programa.
    imprimir_oi('Luiza Takeda :D')

    resultado = somar(5,7)
    print(f'A soma é: {resultado}')

#usos teste unitário todo teste é feito em 3 part es.
def teste_somar():
    #1- configura (o que vc acha que vai dar? ex: resultado 15)

    numero_a = 8
    numero_b = 7
    resultado_esperado = 15

    #2- executa   (chamar função colocando os valores ex: resultado_obtido = somar(numero_a, numero_b)

    resultado_obtido = somar(numero_a, numero_b)

    #3- Valida    (verificar se o resultado esperado apareceu, se acertou passou, se não deu bug Ex: assert resultado_esperado == resultado_obtido)

    assert resultado_obtido == resultado_esperado


def teste_subtrair():
        # 1- configura (o que vc acha que vai dar? ex: resultado 15)

    numero_a = 8
    numero_b = 7
    resultado_esperado = 1

        # 2- executa   (chamar função colocando os valores ex: resultado_obtido = somar(numero_a, numero_b)

    resultado_obtido = subtrair(numero_a, numero_b)

        # 3- Valida    (verificar se o resultado esperado apareceu, se acertou passou, se não deu bug Ex: assert resultado_esperado == resultado_obtido)

    assert resultado_obtido == resultado_esperado
#================================================================================================
@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado',ler_csv('C:\\Users\\julia\\PycharmProjects\\134inicial\\vendors\\CSV\\massa_teste_subtrair_positivo.csv'))
def teste_subtrair_leitura_csv(numero_a, numero_b, resultado_esperado):
    # 1 - Prepara / Configura

    # 2 - Executa
    resultado_obtido = subtrair(int(numero_a), int(numero_b))

    # 3 - Valida / Checa
    assert resultado_obtido == int(resultado_esperado)

def teste_dividir():
    # 1- Configura

    numero_a = 27
    numero_b = 3
    # 1.2- Resultados esperados
    resultado_esperado = 9

    # 1- Executa
    dividir(numero_a, numero_b)
    resultado_obtido = dividir(numero_a, numero_b)

    #3- Valida
    assert resultado_obtido == resultado_esperado

#==============================================================================================================
     #tem colchete pois é como se fosse uma tabela------- a tupla é a lista.
lista_de_valores = [
    (8, 7, 15),
    (9, 9, 18),

    (7, 7, 14)#não vai virgula no ultimo
]
    #1- configura (utilizamos a lista como massa de teste)
    #parametrize= lê os dados e informar da onde os dados vêm
@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', lista_de_valores)
def teste_somar_leitura_de_lista(numero_a, numero_b, resultado_esperado):

    #2- executa

    resultado_obtido = somar(numero_a, numero_b)

    #3- Valida

    assert resultado_obtido == resultado_esperado
#=============================================================================
@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', ler_csv('C:\\Users\\julia\\PycharmProjects\\134inicial\\vendors\\CSV\\massa_teste_somar_positivo.csv'))
def teste_somar_leitura_de_csv(numero_a, numero_b, resultado_esperado):

    #2- executa

    resultado_obtido = somar(int(numero_a), int(numero_b)) #int para transformar a string em numero

    #3- Valida

    assert resultado_obtido == int(resultado_esperado)#int para transformar a string em numero
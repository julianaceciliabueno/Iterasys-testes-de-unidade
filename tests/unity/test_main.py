from main import somar, dividir, subtrair


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


def teste_dividir():
    # 1- Configura
    # 1.1- Dados de entrada
    numero_a = 27
    numero_b = 3
    # 1.2- Resultados esperados
    resultado_esperado = 9

    # 1- Executa
    dividir(numero_a, numero_b)
    resultado_obtido = dividir(numero_a, numero_b)

    #3- Valida
    assert resultado_obtido == resultado_esperado
teste
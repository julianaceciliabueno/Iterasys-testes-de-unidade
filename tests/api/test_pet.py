#bibliotecas
import pytest
import requests

#definições das funções
#variaveis publicas
url = "https://petstore.swagger.io/v2/pet"
headers = {"Content-Type": "aplication/jason"}


def teste_incluir_pet():
    #prepara
    # Dados de entrada via Json

    #Resultados esperados
    status_code_esperado = 200
    pet_id_esperado = 6033070
    pet_name_esperado = "Pipoca"
    pet_nome_categoria_esperado = "cadela"
    pet_nome_tag_esperado = "vacinada"

    #executa
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open('C:\\Users\\julia\\PycharmProjects\\134inicial\\vendors\\json\\pet1.json')
    )

    #valida

    print(resultado_obtido)

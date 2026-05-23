#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades.
"""
__version__ = "0.1.1"


##############################################
#      ATENçÃO: MODIFIQUE ESSE CÓDIGO!       #
#   Tente utilizar dicionários               #
##############################################

# Dados
alunos = {
"sala1":["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
"sala2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]
}

aulas = {
"aula_ingles": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
"aula_musica": ["Erik", "Carlos", "Maria"],
"aula_danca": ["Gustavo", "Sofia", "Joana", "Antonio"]
}

atividades = {
    "Ingles": ["aula_ingles"], 
    "Música": ["aula_musica"], 
    "Dança": ["aula_danca"]
}

# Listar alunos em cada atividade por sala

for nome_atividade, atividade in atividades.items():

    print(f"Alunos da atividade {nome_atividade}")
    print("-" * 45)

    # Retornar todos os alunos da sala1 que tem interseção com atividade
    atividades_sala1 = set(alunos["sala1"]) & set(aulas[atividade[0]])
    atividades_sala2 = set(alunos["sala2"]) & set(aulas[atividade[0]])

    print("Sala1 " , atividades_sala1)
    print("Sala2 ", atividades_sala2)
    
    print()
    print("-" * 45)
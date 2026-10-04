from dados import listaCandidatos
def reset():

    listaCandidatos = [{'nome': 'nulo', 'numero': 0, 'voto': 0}]
    for candidato in listaCandidatos:
        print(candidato['nome'], "-", candidato['numero'], "-", candidato['voto'], "votos")

    print("\n=========== NOVA VOTAÇÃO =============")

    criarCandidato()

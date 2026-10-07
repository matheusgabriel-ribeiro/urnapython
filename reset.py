# reset.py - Função para reiniciar a lista de candidatos para uma nova eleição.
from dados import listaCandidatos

def reset():
    """Limpa todos os candidatos e restaura apenas o voto nulo inicial."""
    listaCandidatos.clear()
    listaCandidatos.append({'nome': 'nulo', 'numero': 0, 'voto': 0})
    print("\n=========== NOVA VOTAÇÃO =============")

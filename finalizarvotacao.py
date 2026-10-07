# finalizarvotacao.py - Exibe o resultado final e pergunta se deseja reiniciar o sistema.
from dados import listaCandidatos

def finalizarVotacao():
    print("\n === V O T A Ç Ã O  E N C E R R A D A ===")
    
    # Exibe a apuração de votos de cada candidato
    for candidato in listaCandidatos:
        print(f"{candidato['numero']} - {candidato['nome']} - {candidato['voto']} votos")
        
    print("\n =======================================")
    
    while True:
        opc = input("\nDeseja criar uma nova eleição? [y/n]: ").strip().lower()
        
        if opc == 'y':
            # Reseta a lista mantendo apenas o voto nulo inicial
            listaCandidatos.clear()
            listaCandidatos.append({
                "nome": "nulo",
                "numero": 0,
                "voto": 0
            })
            print("\n=========== NOVA VOTAÇÃO =============")
            return True  # Retorna True para sinalizar que o main deve recomeçar
            
        elif opc == 'n':
            print("\nPrograma encerrado.")
            return False  # Retorna False para encerrar normalmente
        else:
            print("Digite apenas 'y' ou 'n'.")
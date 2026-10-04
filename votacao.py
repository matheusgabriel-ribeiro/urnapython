# votacao.py - Controla a coleta de votos dos eleitores.
from dados import listaCandidatos
from finalizarvotacao import finalizarVotacao

def votacao():
    print("\n ==== V O T A Ç Ã O ====")
    
    while True:
        # Pega o número do voto garantindo que seja um número inteiro
        while True:
            try:
                votar = int(input("Digite o número do seu candidato: "))
                break
            except ValueError:
                print("ERRO: Só pode números!")

        candidato_encontrado = False

        # Varre a lista de candidatos procurando o número digitado
        for candidato in listaCandidatos:
            if candidato['numero'] == votar:
                candidato['voto'] += 1  # Incrementa o voto do candidato correto
                print(f"Voto validado! Você votou no candidato(a) {candidato['nome']}")
                candidato_encontrado = True
                break  # Sai do loop de busca pois já encontrou

        # Se o número não pertencer a nenhum candidato cadastrado
        if not candidato_encontrado:
            print("Candidato não encontrado!")
            while True:
                opc = input("Deseja votar nulo? [y/n]: ").strip().lower()
                if opc == 'y':
                    # O voto nulo está na posição 0 da lista (índice 0)
                    listaCandidatos[0]['voto'] += 1
                    print("Você votou nulo!")
                    break
                elif opc == 'n':
                    print("Retornando...")
                    break
                else:
                    print("Digite apenas 'y' ou 'n'")

        # Pergunta se o próximo eleitor deseja votar ou se a eleição deve encerrar
        while True:
            digite = input("\nQuer continuar a votação? [y/n]: ").strip().lower()
            if digite == 'y':
                break
            elif digite == 'n':
                print("Encerrando a votação...")
                reiniciar = finalizarVotacao() # Chama a apuração e verifica se vai reiniciar
                if reiniciar:
                    return 'reiniciar'  # Retorna o sinal para recomeçar o fluxo no main
                return
            else:
                print("Digite apenas 'y' ou 'n'")
# main.py - Ponto de entrada do programa (gerencia cadastros e o menu inicial).
from dados import listaCandidatos
from votacao import votacao

def criarCandidato():
    print("========= Adicionar Candidatos =================")
    
    # Pergunta quantos candidatos serão cadastrados
    while True:
        try:
            numCandidatos = int(input("Quantos candidatos: "))
            break
        except ValueError:
            print("ERROR: Só pode usar números")

    # Loop para cadastrar cada candidato
    for i in range(numCandidatos):
        while True:
            nome = input(f"Digite o nome do {i + 1}º candidato: ")
            
            # Validação se o nome está vazio
            if not nome.strip():
                print("Você não digitou nada. Tente novamente.")
                continue
                
            # Validação se contém apenas letras (ignorando espaços para nomes compostos)
            if not nome.replace(" ", "").isalpha():
                print("ERRO: O nome deve conter apenas letras.")
                continue

            # Validação do número do candidato
            try:
                numero = int(input("Digite o número do candidato (apenas 2 números): "))
            except ValueError:
                print("ERROR: Só são válidos números inteiros.")
                continue

            # Validação de intervalo de dois dígitos (10 a 99)
            if numero < 10 or numero > 99:
                print("ERRO: O número só pode ter dois (2) dígitos.")
                continue

            # Verificação se o número já foi cadastrado anteriormente
            numeroExiste = False
            for candidato in listaCandidatos:
                if candidato["numero"] == numero:
                    numeroExiste = True
                    break
                    
            if numeroExiste:
                print("ERRO: Número já cadastrado.")
                continue

            # Adiciona o candidato com sucesso na lista global compartilhada
            listaCandidatos.append({
                "nome": nome,
                "numero": numero,
                "voto": 0
            })
            break

    # Menu principal do sistema
    print("\n ==== M E N U ====")
    print("""
    1. Iniciar votação
    2. Sair
    """)
    
    while True:
        try:
            opc = int(input("Digite sua opção: "))
        except ValueError:
            print("ERRO: Apenas números")
            continue
            
        match opc:
            case 1:
                resultado = votacao()
                # Se a votação retornou o comando para reiniciar, chama o cadastro de novo
                if resultado == 'reiniciar':
                    criarCandidato()
                break
            case 2:
                exit()
            case _:
                print("ERRO: Digite um valor válido!")
                continue

if __name__ == '__main__':
    criarCandidato()
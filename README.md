# Sistema de Votação em Python

## 📋 Sobre o projeto

Este projeto consiste em um **sistema de votação desenvolvido em Python**, executado pelo terminal, com o objetivo de simular o funcionamento básico de uma eleição.

O sistema permite:

- Cadastrar candidatos;
- Definir um número de identificação para cada candidato;
- Validar os dados informados pelo usuário;
- Iniciar uma votação;
- Registrar votos para os candidatos;
- Registrar votos nulos;
- Encerrar a votação;
- Exibir a apuração final;
- Iniciar uma nova eleição sem precisar fechar o programa.

O projeto foi desenvolvido de forma modular, separando as principais responsabilidades em diferentes arquivos Python. Os dados dos candidatos são compartilhados entre os módulos por meio da variável `listaCandidatos`.

---

## 🗂️ Estrutura do projeto

```text
projeto/
│
├── main.py
├── dados.py
├── votacao.py
├── finalizarvotacao.py
└── reset.py
```

### `main.py`

É o **ponto de entrada principal** do sistema.

Suas principais responsabilidades são:

1. Solicitar a quantidade de candidatos;
2. Cadastrar os candidatos;
3. Validar os nomes;
4. Validar os números dos candidatos;
5. Impedir números de candidatos repetidos;
6. Exibir o menu principal;
7. Iniciar a votação;
8. Encerrar o programa quando solicitado.

A função principal desse arquivo é `criarCandidato()`.

O programa começa por:

```python
if __name__ == '__main__':
    criarCandidato()
```

Isso faz com que o cadastro seja iniciado somente quando `main.py` for executado diretamente.

---

### `dados.py`

É responsável por armazenar os **dados compartilhados dos candidatos**.

A variável principal é:

```python
listaCandidatos
```

Ela começa contendo um candidato especial chamado `nulo`:

```python
listaCandidatos = [
    {
        "nome": "nulo",
        "numero": 0,
        "voto": 0
    }
]
```

Cada candidato é representado por um dicionário contendo três informações:

- `nome`: nome do candidato;
- `numero`: número utilizado para votar;
- `voto`: quantidade de votos recebidos.

Essa lista é importada pelos outros módulos para que todos trabalhem sobre os mesmos dados.

---

### `votacao.py`

É responsável pelo **processo de votação**.

A função:

```python
votacao()
```

solicita ao eleitor o número do candidato.

O programa percorre a `listaCandidatos` procurando um candidato com o número informado.

Quando encontra:

```python
candidato['voto'] += 1
```

o sistema adiciona um voto ao candidato.

Caso o número informado não exista, o sistema pergunta se o eleitor deseja registrar um **voto nulo**.

Se a resposta for `y`, o voto é registrado no candidato `nulo`, que fica na posição `0` da lista.

Depois de cada voto, o sistema pergunta se deseja continuar a votação.

---

### `finalizarvotacao.py`

É responsável por **encerrar a eleição e apresentar os resultados**.

A função:

```python
finalizarVotacao()
```

percorre todos os candidatos e exibe:

```text
número - nome - quantidade de votos
```

Depois da apuração, o sistema pergunta:

```text
Deseja criar uma nova eleição? [y/n]:
```

Se o usuário escolher `y`, a lista de candidatos é limpa e o candidato `nulo` é cadastrado novamente.

Dessa forma, uma nova eleição pode ser criada utilizando o mesmo programa.

A função retorna:

```python
return True
```

para avisar ao `main.py` que uma nova eleição deve ser iniciada.

---

### `reset.py`

Este arquivo contém uma função chamada `reset()` que tenta preparar a lista para uma nova votação.

Atualmente, porém, o fluxo principal do projeto **não utiliza essa função**. O próprio `finalizarvotacao.py` realiza o reset da lista quando o usuário escolhe criar uma nova eleição.

Além disso, a implementação atual de `reset.py` possui alguns pontos que precisariam ser corrigidos para que possa ser utilizada diretamente:

- A atribuição `listaCandidatos = [...]` cria uma nova variável local em vez de alterar a lista importada;
- `criarCandidato()` não foi importada nem definida dentro do arquivo.

Por isso, o mecanismo efetivamente utilizado para reiniciar a eleição está em `finalizarvotacao.py`.

---

## 🔄 Fluxo de funcionamento

O funcionamento geral do programa pode ser representado da seguinte maneira:

```text
                    ┌─────────────────┐
                    │    main.py      │
                    │ Início do       │
                    │ programa        │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Cadastro de     │
                    │ candidatos      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Menu principal  │
                    └────────┬────────┘
                             │
                   ┌─────────┴─────────┐
                   │                   │
                   ▼                   ▼
             Iniciar votação         Sair
                   │
                   ▼
             ┌───────────────┐
             │  votacao.py   │
             └───────┬───────┘
                     │
                     ▼
             Digitar número
                     │
             ┌───────┴────────┐
             │                │
             ▼                ▼
        Candidato         Número não
        encontrado         encontrado
             │                │
             ▼                ▼
        +1 voto          Pergunta se
                          deseja votar
                            nulo
                              │
                              ▼
                    Continuar votação?
                       │           │
                      sim         não
                       │           │
                       └─────┐     ▼
                             │  finalizarvotacao.py
                             │     │
                             │     ▼
                             │  Apuração
                             │     │
                             │     ▼
                             │  Nova eleição?
                             │    │      │
                             │   sim    não
                             │    │      │
                             └────┘      ▼
                                      Encerrar
```

---

## 👤 Cadastro de candidatos

Antes de iniciar a votação, o sistema pergunta quantos candidatos serão cadastrados.

Para cada candidato, são solicitados:

```text
Nome do candidato
Número do candidato
```

### Validação do nome

O sistema verifica se o nome não está vazio:

```python
if not nome.strip():
```

Também verifica se o nome contém somente letras e espaços:

```python
if not nome.replace(" ", "").isalpha():
```

Isso permite nomes compostos, como:

```text
João Silva
Maria Santos
```

mas impede entradas contendo números ou caracteres inválidos.

### Validação do número

O número precisa ser um inteiro entre `10` e `99`.

```python
if numero < 10 or numero > 99:
```

Portanto, são aceitos números com dois dígitos.

O sistema também verifica se o número já foi utilizado por outro candidato. Isso evita que dois candidatos tenham o mesmo número.

---

## 🗳️ Como um voto é registrado

Durante a votação, o eleitor informa o número do candidato.

O programa percorre a lista:

```python
for candidato in listaCandidatos:
```

e compara:

```python
if candidato['numero'] == votar:
```

Quando encontra o candidato correspondente, o número de votos é incrementado:

```python
candidato['voto'] += 1
```

Por exemplo, se um candidato possui:

```python
"voto": 3
```

e receber outro voto, passará a ter:

```python
"voto": 4
```

---

## ⚠️ Voto nulo

O sistema possui um candidato especial:

```text
nome: nulo
número: 0
```

Quando o eleitor digita um número que não pertence a nenhum candidato, o programa informa:

```text
Candidato não encontrado!
```

Em seguida, pergunta:

```text
Deseja votar nulo? [y/n]:
```

Se escolher `y`, o voto é contabilizado no candidato `nulo`.

Isso permite diferenciar os votos válidos dos votos nulos na apuração final.

---

## 🧠 Compartilhamento dos dados entre arquivos

Um dos conceitos importantes utilizados no projeto é a **importação de módulos**.

Por exemplo, `main.py` utiliza:

```python
from dados import listaCandidatos
```

e `votacao.py` também utiliza:

```python
from dados import listaCandidatos
```

Isso permite que diferentes partes do sistema trabalhem com a mesma estrutura de dados.

A arquitetura pode ser resumida assim:

```text
                dados.py
                   │
          listaCandidatos
             │     │
       ┌─────┘     └─────┐
       ▼                 ▼
    main.py          votacao.py
                         │
                         ▼
                finalizarvotacao.py
```

---

## 🔁 Reinício de uma eleição

Quando a votação termina, `finalizarvotacao.py` mostra os resultados.

Se o usuário escolher criar uma nova eleição, o código executa:

```python
listaCandidatos.clear()
```

Isso remove todos os candidatos existentes.

Depois, o candidato nulo é adicionado novamente:

```python
listaCandidatos.append({
    "nome": "nulo",
    "numero": 0,
    "voto": 0
})
```

Assim, o sistema volta ao estado inicial e permite cadastrar novos candidatos.

O retorno:

```python
return True
```

é utilizado por `votacao.py` e `main.py` para controlar o fluxo de reinicialização.

---

## 🛡️ Tratamento de erros

O projeto utiliza `try/except` para evitar que o programa seja encerrado quando o usuário informa um valor inválido.

Exemplo:

```python
try:
    numero = int(input("Digite o número do candidato: "))
except ValueError:
    print("ERROR: Só são válidos números inteiros.")
```

Se o usuário digitar:

```text
abc
```

o Python não consegue converter o texto para inteiro e gera uma exceção `ValueError`.

O `except` captura esse erro e permite que o programa continue funcionando.

Esse tratamento também é utilizado para:

- Quantidade de candidatos;
- Número do candidato;
- Número do voto;
- Opção do menu.

---

## ▶️ Como executar

É necessário ter o **Python 3** instalado.

Com todos os arquivos na mesma pasta, abra o terminal dentro da pasta do projeto e execute:

```bash
python main.py
```

Em alguns sistemas, pode ser necessário utilizar:

```bash
python3 main.py
```

O programa será iniciado pelo arquivo `main.py`.

---

## 💻 Exemplo de execução

Um fluxo simplificado pode ser:

```text
========= Adicionar Candidatos =================

Quantos candidatos: 2

Digite o nome do 1º candidato: João
Digite o número do candidato: 10

Digite o nome do 2º candidato: Maria
Digite o número do candidato: 20

==== M E N U ====

1. Iniciar votação
2. Sair

Digite sua opção: 1
```

Durante a votação:

```text
==== V O T A Ç Ã O ====

Digite o número do seu candidato: 10

Voto validado! Você votou no candidato(a) João

Quer continuar a votação? [y/n]: y
```

Ao finalizar:

```text
=== V O T A Ç Ã O  E N C E R R A D A ===

0 - nulo - 1 votos
10 - João - 3 votos
20 - Maria - 2 votos
```

---

## 🧩 Conceitos de Python utilizados

O projeto utiliza diversos conceitos importantes para quem está aprendendo Python:

- Variáveis;
- Listas;
- Dicionários;
- Funções;
- `for`;
- `while`;
- `if`, `elif` e `else`;
- `match/case`;
- `try/except`;
- `input()`;
- `print()`;
- Conversão de tipos com `int()`;
- Métodos de strings como `.strip()`, `.lower()` e `.isalpha()`;
- Importação de módulos com `from ... import ...`;
- Retorno de funções com `return`;
- Manipulação de listas com `.append()` e `.clear()`;
- Estruturas de repetição e validação de entrada.

---

## 📌 Resumo da arquitetura

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Cadastro dos candidatos e menu inicial |
| `dados.py` | Armazenamento da lista compartilhada de candidatos |
| `votacao.py` | Registro dos votos e controle da votação |
| `finalizarvotacao.py` | Apuração, encerramento e reinício da eleição |
| `reset.py` | Tentativa de função separada para reset; atualmente não participa do fluxo principal |

---

## 🚀 Possíveis melhorias futuras

O projeto pode evoluir com recursos como:

- Identificação de vencedor automaticamente;
- Empate entre candidatos;
- Porcentagem de votos;
- Relatório mais detalhado da eleição;
- Persistência dos dados em arquivo `.json` ou banco de dados;
- Interface gráfica;
- Sistema de login para administradores;
- Separação entre área administrativa e área do eleitor;
- Validação mais completa dos dados;
- Testes automatizados;
- Correção e integração do módulo `reset.py`.

---

## 📄 Licença

Projeto desenvolvido para fins educacionais e de estudo de programação em Python.

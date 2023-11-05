import random
import itertools
import os

# Defina as quatro seções com seus limites e nomeie-as
secao_a = (0, 14)
secao_b = (15, 29)
secao_c = (30, 44)
secao_d = (45, 60)

grupos = [("a", "b"), ("a", "c"), ("a", "d"), ("b", "c"), ("b", "d"), ("c", "d")]

# Pasta para armazenar as sequências geradas
diretorio = "sequencias_geradas"
if not os.path.exists(diretorio):
    os.mkdir(diretorio)

# Arquivo para registrar as sequências geradas
arquivo_sequencias = os.path.join(diretorio, "sequencias.txt")

sequencias_registradas = set()

# Verificar e carregar sequências registradas do arquivo
if os.path.isfile(arquivo_sequencias):
    with open(arquivo_sequencias, "r") as file:
        for line in file:
            sequencias_registradas.add(line.strip())

while True:
    todas_combinacoes = []

    # Inicialize um conjunto para acompanhar os números já escolhidos
    numeros_escolhidos = set()

    # Escolha 6 números exclusivos em cada grupo de seções
    for grupo in grupos:
        secao1, secao2 = grupo
        selecao = []

        # Use um conjunto para garantir números exclusivos
        numeros_exclusivos = set()

        while len(numeros_exclusivos) < 6:
            numero_secao1 = random.randint(secao_a[0], secao_a[1]) if secao1 == "a" else (
                random.randint(secao_b[0], secao_b[1]) if secao1 == "b" else (
                    random.randint(secao_c[0], secao_c[1]) if secao1 == "c" else (
                        random.randint(secao_d[0], secao_d[1])
                    )
                )
            )
            numero_secao2 = random.randint(secao_a[0], secao_a[1]) if secao2 == "a" else (
                random.randint(secao_b[0], secao_b[1]) if secao2 == "b" else (
                    random.randint(secao_c[0], secao_c[1]) if secao2 == "c" else (
                        random.randint(secao_d[0], secao_d[1])
                    )
                )
            )

            # Verifique se o número já foi escolhido antes
            if numero_secao1 not in numeros_escolhidos and numero_secao2 not in numeros_escolhidos:
                numeros_exclusivos.add(numero_secao1)
                numeros_exclusivos.add(numero_secao2)
                selecao.extend([numero_secao1, numero_secao2])
                numeros_escolhidos.add(numero_secao1)
                numeros_escolhidos.add(numero_secao2)

        todas_combinacoes.append(selecao)

    # Gere a sequência de 6 números
    sequencia = todas_combinacoes

    # Verifique se a sequência já foi gerada anteriormente
    sequencia_str = ",".join(map(str, sequencia))
    sequencia_str = ",".join(map(str, sequencia))
    if sequencia_str not in sequencias_registradas:
        print("Nova sequência de 6 números gerada:", sequencia)

        # Registre a sequência (como uma string)
        sequencias_registradas.add(sequencia_str)
        with open(arquivo_sequencias, "a") as file:
            file.write(sequencia_str + "\n")
        break

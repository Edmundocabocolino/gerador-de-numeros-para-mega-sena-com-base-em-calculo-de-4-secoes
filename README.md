# gerador de numeros para mega sena com base em 4 seçoes
Objetivo:
O programa tem como objetivo gerar sequências de 6 números, onde cada número é escolhido aleatoriamente a partir de quatro seções diferentes (A, B, C e D). O programa evita repetições de números dentro de cada sequência.

Funcionamento:

O programa define quatro seções (A, B, C e D), cada uma com limites específicos.
Há grupos predefinidos de combinações entre as seções (por exemplo, A+B, A+C, A+D, B+C, B+D, C+D).
Ele verifica a existência de uma pasta para armazenar as sequências geradas. Se não existir, cria a pasta.
Verifica se há um arquivo chamado "sequencias.txt" na pasta para carregar sequências registradas anteriormente. As sequências registradas são armazenadas em um conjunto (set).
O programa entra em um loop até que uma nova sequência única seja gerada.
Em cada iteração do loop, ele escolhe 6 números exclusivos em cada grupo de seções. Para fazer isso:
Inicializa um conjunto para acompanhar os números já escolhidos.
Utiliza um segundo conjunto para garantir que os números sejam exclusivos.
Enquanto o conjunto de números exclusivos não tiver 6 números, escolhe aleatoriamente números de seções específicas, garantindo que não haja repetições dentro de uma sequência.
Adiciona os números escolhidos ao conjunto de números exclusivos e ao conjunto de números já escolhidos.
Cria uma sequência com os números escolhidos e a adiciona à lista de todas as combinações.
Quando uma nova sequência exclusiva é gerada, ela é registrada no arquivo "sequencias.txt" e o loop é encerrado.
Resultado:
 O programa gera sequências únicas de 6 números a partir das seções A, B, C e D, evitando a repetição de números dentro de cada sequência. As sequências geradas são exibidas no console e registradas em um arquivo para referência futura.

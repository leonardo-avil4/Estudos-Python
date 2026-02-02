# Variáveis, constantes e complexidade de código - Parte 1

# Boas práticas de programação e como escrever bons códigos para outras pessoas.
# → Você deve escrever um código que tanto você quanto outras pessoas consigam entender (código limpo).

"""
velocidade = 61
RADAR_1 = 60

print(RADAR_1) # 60

RADAR_1 = 'radar'

print(RADAR_1) # 'radar'
"""

# No python, não existem constantes que evitem uma nova atribuição de valor, o que existe é uma convenção que diz que 'variáveis' escritas em letras maiúsculas indicam que o seu valor não será alterado durante a execução do código. Ex: linha que faz conexão com o banco de dados.


# Outro ponto importante: Evite usar muitas expressões em um mesma condição if, por exemplo: if 1 and -1 and 0 or 'abc', pois isso dificulta a leitura do código.

# Python-zen: "Simples é melhor do que complexo" / "Explícito é melhor do que ímplicito"

# → Evite também usar muitos blocos de código dentro de outros blocos
# if ...
#   if ...
#       if ...
#           if ...
# Evite complexidade

velocidade = 65
local_carro = 80

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

multado = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
# Variáveis também podem ser utilizadas para dar nomes a um trecho específico de um código, tornando o código mais legível.


if carro_passou_radar_1:
    print("O carro passou no radar 1.")

    if multado:
        print("O carro foi multado no radar 1.")

        
# if multado:
#     print("O carro foi multado no radar 1.")

# → Achei interessante colocar esse if dentro do bloco do carro_passou_radar_1, pois do lado de fora, ele verifica se o carro foi multado mesmo que não tenha sido, o que gera um processamento desnecessário, já que o carro é multado somente no alcance do radar.

# if local_carro_antes and local_carro_depois:
#     if passou_radar_1:
#         print("O carro passou da velocidade permitida.")
#     else:
#         print("O carro está na velocidade permitida.")


# \ → indica para o interpretador python que o código continua na próxima linha (quebra).


# Sempre que você ver uma linha de código complexa, tente pensar em como você pode simplifica-la para facilitar o seu entendimento.
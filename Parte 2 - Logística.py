lista_caixa = []
lista_caminhao = []

print('~-' * 35)
print(f'{"Programa de Logística para Transporte de Caixas de Ampolas de Vacina":^70}')  # Cabeçalho do Programa.
print('~-' * 35)
print('\n')

qtd_caminhoes = int(input('Quantos caminhões estão disponíveis? '))  # Primeira parte do programa, inputs de dados.
while True:
    opcao = int(input('Digite 1 para cadastrar caixa ou 0 para sair. '))
    if opcao == 1:
        ampola_caixa = int(input('Quantas ampolas vai ser colocado nesta caixa? (Mínimo de 1 e Máximo de 100): '))
        if ampola_caixa < 1 or ampola_caixa > 100:
            print('Quantidade errada, tente novamente.')
        else:
            lista_caixa.append(ampola_caixa)
    elif opcao == 0:
        break
    else:
        print('Opção Inválida, tente novamente.')

lista_caixa.sort(
    reverse=True)  # Ordenando a lista de caixas em ordem decrescente para o cálculo a seguir das combinações.
lista_ordenada = lista_caixa
# Essa parte do programa combina as caixas de modo que se tenha 100 ou o mais próximo possível no somatório de
# caixas. E cria uma lista de lista com essa combinação.
while len(lista_ordenada) > 0:
    lista_restante = []
    lista_caixa_caminhao = []
    caixa = 0
    for elemento in lista_ordenada:
        if caixa + elemento <= 100:
            caixa += elemento
            lista_caixa_caminhao.append(elemento)
        else:
            lista_restante.append(elemento)
    lista_caminhao.append(lista_caixa_caminhao)
    lista_ordenada = lista_restante

print('-' * 90)
print('\n')
if qtd_caminhoes >= len(lista_caminhao):  # Parte final do programa que da o resultado.
    print(f'Com {qtd_caminhoes} caminhões será possível transportar todas as caixas de ampolas.')
    for count in range(0, len(lista_caminhao)):
        print(f'O {count + 1}º caminhão levará as caixas contendo {lista_caminhao[count]} ampolas.')
else:
    print(f'Com {qtd_caminhoes} caminhões não será possível transportar todas as caixas de ampolas.')
    print(f'A lista das unidades que não serão transportadas são: {lista_caminhao[qtd_caminhoes:]}.')

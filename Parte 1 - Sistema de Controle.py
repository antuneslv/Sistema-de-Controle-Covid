lista_geral_vacinados = []
lista_vacinados_pfizer = []
lista_vacinados_coronavac = []
lista_vacinados_astrazeneca = []
lista_estoque_pfizer = [0]
lista_estoque_coronavac = [0]
lista_estoque_astrazeneca = [0]
media_geral = 0
media_pfizer = 0
media_coronavac = 0
media_astrazeneca = 0

print('~-' * 32)
print(f'{"Programa de Controle de Vacinação":^64}')  # Cabeçalho do Programa.
print('~-' * 32)

while True:  # Essa parte começa o loop do menu principal.
    print('\n')
    print('-' * 64)
    menu = int(input('''Escolha a opção desejada:
[1] Registrar Vacinação
[2] Adicionar Estoque de uma Vacina
[3] Obter Número Total de Vacinados
[4] Obter Média de Vacinação Diária
[5] Obter a Quantidade Atual de Doses de um Tipo de Vacina
[6] Fechar Programa\n'''))
    if menu == 1:  # Essa parte é a primeira opção do menu.
        lista_vacinados = []
        nome = input('Nome da pessoa: ')
        while True:
            vacina = int(input('''Qual vacina vai ser aplicada?
[1] Pfizer
[2] CoronaVac
[3] Astrazeneca\n'''))
            if vacina < 1 or vacina > 3:
                print('Opção Inválida, tente novamente.')
            else:
                break
        if vacina == 1:
            if lista_estoque_pfizer[0] == 0:
                print('Pfizer em falta, espere abastecer o estoque ou tente outra vacina.')
            else:
                lista_vacinados.append(nome)
                lista_vacinados.append('Pfizer')
                lista_estoque_pfizer[0] -= 1
                dia = input('Qual o dia da vacinação? ')
                lista_vacinados.append(dia)
                hora = input('Qual a hora da vacinação? ')
                lista_vacinados.append(hora)
                lista_vacinados_pfizer.append(lista_vacinados)
        elif vacina == 2:
            if lista_estoque_coronavac[0] == 0:
                print('CoronaVac em falta, espere abastecer o estoque ou tente outra vacina.')
            else:
                lista_vacinados.append(nome)
                lista_vacinados.append('CoronaVac')
                lista_estoque_coronavac[0] -= 1
                dia = input('Qual o dia da vacinação? ')
                lista_vacinados.append(dia)
                hora = input('Qual a hora da vacinação? ')
                lista_vacinados.append(hora)
                lista_vacinados_coronavac.append(lista_vacinados)
        else:
            if lista_estoque_astrazeneca[0] == 0:
                print('Astrazeneca em falta, espere abastecer o estoque ou tente outra vacina.')
            else:
                lista_vacinados.append(nome)
                lista_vacinados.append('Astrazeneca')
                lista_estoque_astrazeneca[0] -= 1
                dia = input('Qual o dia da vacinação? ')
                lista_vacinados.append(dia)
                hora = input('Qual a hora da vacinação? ')
                lista_vacinados.append(hora)
                lista_vacinados_astrazeneca.append(lista_vacinados)
        if lista_vacinados != []:
            lista_geral_vacinados.append(lista_vacinados)
    elif menu == 2:  # Segunda opção do menu.
        while True:
            vacina_estoque = int(input('''Qual vacina você quer adicionar ao estoque?
[1] Pfizer
[2] CoronaVac
[3] Astrazeneca\n'''))
            if vacina_estoque < 1 or vacina_estoque > 3:
                print('Opção Inválida, tente novamente.')
            else:
                break
        if vacina_estoque == 1:
            qtd_pfizer = int(input('Qual a quantidade da vacina Pfizer que você deseja adicionar ao estoque? '))
            if qtd_pfizer < 0:
                print('Erro, informe um valor positivo.')
            else:
                lista_estoque_pfizer[0] += qtd_pfizer
        elif vacina_estoque == 2:
            qtd_coronavac = int(input('Qual a quantidade da vacina CoronaVac que você deseja adicionar ao estoque? '))
            if qtd_coronavac < 0:
                print('Erro, informe um valor positivo.')
            else:
                lista_estoque_coronavac[0] += qtd_coronavac
        else:
            qtd_astrazeneca = int(
                input('Qual a quantidade da vacina Astrazeneca que você deseja adicionar ao estoque? '))
            if qtd_astrazeneca < 0:
                print('Erro, informe um valor positivo.')
            else:
                lista_estoque_astrazeneca[0] += qtd_astrazeneca
    elif menu == 3:  # Terceira opção do menu.
        if lista_geral_vacinados == []:
            print('Ninguem foi vacinado.')
        else:
            for count, cadastros in enumerate(lista_geral_vacinados):
                total_vacinados = count + 1
            if lista_vacinados_pfizer == []:
                total_vacinados_pfizer = 0
            else:
                for count_p, cadastros in enumerate(lista_vacinados_pfizer):
                    total_vacinados_pfizer = count_p + 1
            if lista_vacinados_coronavac == []:
                total_vacinados_coronavac = 0
            else:
                for count_c, cadastros in enumerate(lista_vacinados_coronavac):
                    total_vacinados_coronavac = count_c + 1
            if lista_vacinados_astrazeneca == []:
                total_vacinados_astrazeneca = 0
            else:
                for count_a, cadastros in enumerate(lista_vacinados_astrazeneca):
                    total_vacinados_astrazeneca = count_a + 1
            print(f'''A quantidade total de vacinados é de {total_vacinados} pessoas, sendo {total_vacinados_pfizer} 
vacinados com Pfizer, {total_vacinados_coronavac} vacinados com CoronaVac e {total_vacinados_astrazeneca} vacinados com 
Astrazeneca.''')
    elif menu == 4:  # Quarta opção do menu.
        media_geral = len(lista_geral_vacinados) / 30
        media_pfizer = len(lista_vacinados_pfizer) / 30
        media_coronavac = len(lista_vacinados_coronavac) / 30
        media_astrazeneca = len(lista_vacinados_astrazeneca) / 30
        print(
            f'''Ao todo foram aplicadas {len(lista_geral_vacinados)} vacinas e a média de vacinação é de 
{media_geral:.2f} doses por dia.''')
        print(f'''A média de vacinação com Pfizer é de {media_pfizer:.2f} doses por dia, a média de vacinação com 
CoronaVac é de {media_coronavac:.2f} doses por dia e a média de vacinação com Astrazeneca é de {media_astrazeneca:.2f}
doses por dia.''')
    elif menu == 5:  # Quinta opção do menu.
        print(f'''A quantidade restante da Pfizer é de {lista_estoque_pfizer[0]} doses, da CoronaVac é de 
{lista_estoque_coronavac[0]} doses e da Astrazeneca é de {lista_estoque_astrazeneca[0]} doses.''')
    elif menu == 6:  # Ultima opção do menu.
        print('Fim do Programa.')
        break
    else:
        print('Opção Inválida, tente novamente.')

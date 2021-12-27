# Sistema de Controle Covid

Projeto final do curso Coding Tank da Let's Code

## Parte 1 - Sistema de Controle

Nesta parte do projeto você deverá construir um sistema para realizar o controle da vacinação. Você deverá considerar que existem somente os seguintes tipos de vacina: Pfizer, CoronaVac, Astrazeneca.

O programa deverá exibir um menu inicial com as seguintes opções:

  1. Registrar uma vacinação.
  
  - Nesta opção você deverá perguntar:    
    - O nome da pessoa.
    - Qual a vacina.
    - Você deverá salvar além desses dados, o valor do dia e da hora de vacinação.
      
  2. Adicionar estoque de uma vacina.
  
  - Nesta opção você deverá perguntar:    
    - O nome da vacina.
    - A quantidade a ser adicionada.
      
  3. Obter número total de vacinados.
  
  - Nesta opção você deverá imprimir a quantidade total de vacinados e além disso a quantidade total de vacinados por cada uma das vacinas.
  
  4. Obter média de vacinação diária.
  
  - Nesta opção você deverá imprimir a média diária somando todas as vacinas e além disso a média diária por cada uma das vacinas.
  
  5. Obter a quantidade atual de doses de um tipo de vacina.
  
  - Você deverá imprimir a quantidade restante de doses para cada uma das vacinas.
  
  6. Fechar programa.

Observações:  
Caso a pessoa digite uma opção inválida, a programa deverá imprimir "Opção inválida" e perguntar novamente uma nova opção.

## Parte 2 - Logística
Uma unidade de aplicação precisa receber mais ampolas de vacinas dado o seu estoque baixo, porém ela só tem K caminhões para buscar o produto com o fornecedor. Considere que cada caminhão consegue carregar até 100 ampolas mas o galpão do fornecedor é uma bagunça e eles embalaram caixas que podem conter de 1 até 100 ampolas.
Crie uma função que receba a quantidade K de caminhões disponíveis e a lista de caixas que o fornecedor tem para serem carregadas, ou seja, a quantidade de ampolas por caixa, e retorne se os caminhões conseguirão trazer todas as ampolas ou não. Caso não seja possível retorne a lista das unidades que não serão transportadas. Caso seja possível retorne como estão organizadas as caixas por caminhão, isto é, a lista de caixas que cada um está levando.

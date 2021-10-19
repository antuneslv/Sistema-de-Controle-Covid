# Sistema-de-Controle-Covid

<p>Projeto final do curso Coding Tank da Let's Code</p>

  <h2>Parte 1 - Sistema de Controle</h2>

  <p>Nesta parte do projeto você deverá construir um sistema para realizar o controle da vacinação. Você deverá considerar que existem somente os seguintes tipos de vacina: Pfizer, CoronaVac, Astrazeneca.</p>
  
  <p>O programa deverá exibir um menu inicial com as seguintes opções:</p>
  
  <ol>
    <li>Registrar uma vacinação.</li>
    <ul>
      <li type ="square">Nesta opção você deverá perguntar:</li>
      <ul>
        <li type ="circle">O nome da pessoa.</li>
        <li type ="circle">Qual a vacina.</li>
        <li type ="circle">Você deverá salvar além desses dados, o valor do dia e da hora de vacinação.</li>
      </ul>
    </ul>
    <li>Adicionar estoque de uma vacina.</li>
    <ul>
      <li type ="square">Nesta opção você deverá perguntar:</li>
      <ul>
        <li type ="circle">O nome da vacina.</li>
        <li type ="circle">A quantidade a ser adicionada.</li>
      </ul>
    </ul>
    <li>Obter número total de vacinados.</li>
    <ul>
      <li type ="square">Nesta opção você deverá imprimir a quantidade total de vacinados e além disso a quantidade total de vacinados por cada uma das vacinas.</li>
    </ul>
    <li>Obter média de vacinação diária.</li>
    <ul>
      <li type ="square">Nesta opção você deverá imprimir a média diária somando todas as vacinas e além disso a média diária por cada uma das vacinas.</li>
    </ul>
    <li>Obter a quantidade atual de doses de um tipo de vacina.</li>
    <ul>
      <li type ="square">Você deverá imprimir a quantidade restante de doses para cada uma das vacinas.</li>
    </ul>
    <li>Fechar programa.</li>
  </ol>
  
  <p>
    Observações:<br>
    Caso a pessoa digite uma opção inválida, a programa deverá imprimir "Opção inválida" e perguntar novamente uma nova opção.
  </p>
  <h2>Parte 2 - Logística</h2>
  <p>Uma unidade de aplicação precisa receber mais ampolas de vacinas dado o seu estoque baixo, porém ela só tem K caminhões para buscar o produto com o fornecedor. Considere que cada caminhão consegue carregar até 100 ampolas mas o galpão do fornecedor é uma bagunça e eles embalaram caixas que podem conter de 1 até 100 ampolas.</p>
  <p>Crie uma função que receba a quantidade K de caminhões disponíveis e a lista de caixas que o fornecedor tem para serem carregadas, ou seja, a quantidade de ampolas por caixa, e retorne se os caminhões conseguirão trazer todas as ampolas ou não. Caso não seja possível retorne a lista das unidades que não serão transportadas. Caso seja possível retorne como estão organizadas as caixas por caminhão, isto é, a lista de caixas que cada um está levando.</p>

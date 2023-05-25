# Poker Guloso

**Número da Lista**: 5<br>
**Conteúdo da Disciplina**: GULOSOS 😏<br>

## Alunos
| Matrícula  | Aluno                |
| ---------- | -------------------- |
| 18/0027239 | Renato Britto Araujo |

## Sobre 
<!-- Descreva os objetivos do seu projeto e como ele 
funciona.  -->

Poker guloso: jogo de poker entre 2 algoritmos gulosos para ver qual heurística é melhor.
Os arquivos `scriptA.py` e `scriptB.py` irão implementar a função `desistiu, aumentou fazer_jogada(estado)` 
onde vai receber o estado do jogo (com as suas cartas) e retornará qual carta irá jogar.

O JOGO É [TEXAS HOLD'EM](https://en.wikipedia.org/wiki/Texas_hold_%27em).

Na pasta `estrategias` haverão diversas implementações para se testar.

### Proximos passos

- Implementar all-in

<!-- O objetivo é investigar as condições que tornam ou não um problema em guloso. Vamos comparar diferentes modelos de problemas e analisar onde que uma solução gulosa pode se encaixar ou não, e qual ela é.

Uma ideia lúdica para fazer isso será montar uma simulação de guerra estilo pedra papel e tesoura, onde existe "nosso exército" e o "exército deles". O exército deles usará (atacará usando) "armas" contra nós, e nós precisamos retornar (contratacar) cada ataque inimigo utilizando as "armas" que possuímos. Cada arma destroi um conjunto de outras armas:

| Arma                   | Contrataca                                |
| ---------------------- | ----------------------------------------- |
| Lança míssel terrestre | Tanque, Antiaéreo, Destruidor, Couraçador |
| Lança míssel aéreo     | Helicóptero, Caça                         |
| Soldado                | Soldado, Antiaéreo                        |
| Tanque                 | Soldado, Tanque, Antiaéreo                |
| Antiaéreo              | Caça, Bombardeiro, Helicóptero            |
| Caça                   | Caça, Bombardeiro                         |
| Bombardeiro            | Tanque, Destruidor, Couraçador            |
| Helicóptero            | Soldado, Tanque                           |
| Destruidor             | Submarino                                 |
| Submarino              | Destruidor, Jato                          |
| Couraçador             | Destruidor                                |

Note que o número de grupos e contrataques são arbitrários e podem ser alterados, mas o exemplo acima serve como um modelo finito pro problema a ser resolvido. Será implementado assim.

### Conjecturas sobre o modelo


#### Sobre a condição de derrota (a ser evitada)

A derrota é causada por não contratacar alguma ameaça por um período de tempo T. Por exemplo, se o inimigo usa um jato, mas não é contratacado em T rodadas, isso caracteriza uma derrota. A rodada x pode ser definida temporalmente por Tx.

Uma implicação dessa restrição é que o **custo de não contratacar alguma arma inimiga na jogada Tx é sempre constante** - não importa qual arma ou arma de contrataque envolvida.

Quanto maior o tempo que a derrota pode ser prolongada, melhor. Queremos minimizar o tempo de derrota.

#### Sobre a decisão de qual arma utilizar em dado momento.

Note que, se estamos em um jogo de pedra, papel e tesoura, a escolha de qual ataque utilizar (supondo que você saiba o que seu inimigo jogou) é trivial. Por exemplo, pedra é sempre a jogada ideal se seu inimigo jogou tesoura.

Essa condição permite que, se você estivesse jogando mil jogos de pedra, papel e tesoura simultaneamente e possuisse um número limitado de pedras, papeis ou tesouras a se jogar, para maximizar o número de vitórias é necessário jogar o contrataque dos seus inimigos um por um, sendo o número de derrotas que você terá é exatamente igual a todas as jogadas que você não consegue responder do seu adversário. Ou seja: uma solução gulosa.

Essa condição cria um cenário similar ao **interval partitioning**, porque neste você pode aplicar uma **soluçao gulosa** que evitará de calcular o espaço de possibilidade e sempre retornará o resultado ótimo a partir de uma simples regra de escolha e alocação.

Portanto, para poder implementar uma solução gulosa, precisaremos encontrar uma forma de fazer a decisão ideal de qual arma usar ser sempre a mesma para cada cenário. Outra forma de dizer isso seria: sempre precisa existir uma única escolha correta dentro do cenário. Note como isso de assemelha ao problema do **coin change**, onde a decisão de qual moeda escolher é sempre a maior moeda possível dentro do valor que deve ser pago, dado que cada denominação de moeda maior que outra é sempre >= duas vezes o valor da moeda menor.    

Se cada arma só for contrataque efetivo para uma outra arma, a escolha correta continua sendo difusa. O que vale mais a pena sacrificar no xadrez: um bispo ou 3 peões? Depende, né? Precisamos modelar a solução de forma que ela nunca "depende" de nada exceto o cenário. Ou seja, a decisão ideal é uma função determinística f(x,y,z...).

Tendo isso em mente, vamos fazer algumas definições:

- N: int - número de tipos de armas.
- Vetor X: int[X1,X2,...,XN] - número de armas que possuo de cada tipo.
- Vetor Y: int[Y1,Y2,...YN] - onde Yi representa o número de armas que eu possuo que podem atacar o tipo i de arma.
- Vetor E: int[E1,E2,...,EN] - número de armas de cada tipo que o inimigo usou (contrataques necessários).

Suponha N=4. Se meu inimigo joga ataque 3 e eu posso contratacar com arma 1 ou 2, qual escolha eu faço? Note que isso representa E=[0,0,1,0].

Caso 1:
- X=[2,1,0,0]
- Se arma 1 destroi 3 e 4.
- Se arma 2 destroi 3.
- Y=[0,0,3,2]
- Eu escolho a arma que causaria o maior valor mínimo no vetor Y. Ou seja, se uso 1 e Y vira [0,0,2,1] mas se eu uso 2, o Y vira [0,0,2,2], eu escolho 2, porque causa a menor queda de valores do vetor Y.

Caso 2:
- X=[2,1,0,0]
- Se arma 1 destroi 3 e 4.
- Se arma 2 destroi 3 e 1.
- Y=[1,0,3,2]
- Eu escolho a arma que causaria o maior valor mínimo no vetor Y. Ou seja, se uso 1 e Y vira [1,0,1,0] mas se eu uso 2, o Y vira [0,0,1,1], eu escolho o 2 porque o primeiro elemento do vetor é menor que qualquer elemento do vetor no caso de usar o 1 - a chance de derrota se torna maior por possuir menos contrataques.

Caso 3:
- X=[1,1,0,0]
- Se arma 1 destroi 3 e 4.
- Se arma 2 destroi 3 e 1.
- Y=[1,0,2,1]
- Qualquer escolha que eu faço reduzirá o vetor Y em mesma proporção, portanto qualquer escolha é correta. 

Portanto, a escolha sempre será definida por: o que causa a menor variação do valor mínimo no vetor Y, e no caso de empate, será o que causa a menor variação dentro do vetor Y (que sempre será negativa). Se a resposta não pode ser determinada assim, qualquer escolha é igualmente válida.

Como todas as armas representa uma união distinta do conjunto de armas que são contratacadas e contratacam, isso representa a solução da escolha porque é sempre uma escolha ideal dado o cenário apresentado - ela é gulosa.

#### Sobre tempo e as rodadas

Se modelarmos o jogo de forma que o inimigo realize todos os ataques na rodada 0, a solução acima se aplica sem maiores dificuldades. Esse é a **Versão 1**.

Se modelarmos o jogo de forma que o inimigo possa atacar em uma rodada > 0 e nós podemos contratacar rodadas > 0. A solução acima não serve para fazer decisões.

Perguntas novas:
- Eu posso evitar de jogar numa rodada? Existe algum caso onde essa escolha é ideal?
- Minhas armas são renovadas de alguma forma? Algumas formas como isso poderia acontecer:
  - Recebo uma arma a cada U(i) rodadas
  - Quando uso uma arma, ao final de seu uso que gasta R tempo, ela retorna pra mim ou desaparece?
    - Em ambos os casos anteriores, eu sempre sei em quanto tempo terei armas pra resolver algum ataque caso não tenha nenhuma agora.
    - Sendo assim, é possível calcular um vetor Yi onde i é uma rodada no futuro.
    - Cada elemento no vetor Yi pode ser maior que o mesmo elemento em Yi-1.
    - Seja o vetor bidimensional Yf = [Y0, Y1, Y2,...,YN] (note que Y0 é o vetor Y atual)

X = [1,1,0,0]
D = [[2,3],[3,4]]
U = [3,3,-1,-1]
Yf = [
    [0,1,1,1],
    [0,1,1,1],
    [0,1,1,1],
    [0,2,2,2],
]
mj(X):


    return 

- Meu inimigo renova armas de alguma forma?
  - Se lança i arma a cada P(i) partidas
  

### Proposta de implementação

Em passos:
1. Faz interface para realizar escolhas e criar cenários
2. Desenha interface, incluindo as escolhas de alguma forma
3. Faz sistema de gerar os ataques
  - Implementa múltiplas soluções

| Versão | Descrição                                                                                                                 |
| ------ | ------------------------------------------------------------------------------------------------------------------------- |
| 1      | O inimigo faz todas as jogadas, e nos respondemos todas (dentro da medida do possível)                                    |
| 2      | O mesmo do anterior, mas cada arma tem uma velocidade de derrota (tempo Xi para cada arma em X sem reposta causa derrota) |
| 3      | O inimigo faz jogadas em todo turno, e todo turno nos fazemos a decisão de como tratar as jogadas em aberto               | -->

## Screenshots
<!-- Adicione 3 ou mais screenshots do projeto em funcionamento. -->

## Instalação 
**Linguagem**: xxxxxx<br>
**Framework**: (caso exista)<br>
<!-- Descreva os pré-requisitos para rodar o seu projeto e os comandos necessários. -->

## Uso 
<!-- Explique como usar seu projeto caso haja algum passo a passo após o comando de execução. -->

## Outros 
<!-- Quaisquer outras informações sobre seu projeto podem ser descritas abaixo. -->




### Perguntas interessantes respondidas pela chatgpt

#### How can we mathematically decide that a problem can be solved using a greedy algorithm?

To determine if a problem can be solved using a greedy algorithm, you generally need to evaluate the problem's properties and characteristics. While there is no definitive mathematical test, you can consider the following factors:

- Greedy Choice Property: A greedy algorithm makes locally optimal choices at each step in the hope of finding a global optimum. If the problem exhibits the greedy choice property, meaning that a locally optimal choice always leads to a globally optimal solution, a greedy algorithm may be applicable.

- Optimal Substructure: A problem has optimal substructure if an optimal solution to the problem contains optimal solutions to its subproblems. This property is important because it allows a greedy algorithm to make a series of choices that collectively lead to an optimal solution.

- Proof or Counterexamples: Analyze the problem and try to prove that a greedy algorithm will always yield an optimal solution. Alternatively, look for counterexamples where a greedy approach fails to produce an optimal solution. By examining the problem's specific characteristics, you can gain insight into the applicability of a greedy algorithm.

While these considerations can guide your decision, keep in mind that they do not guarantee the success of a greedy approach. It's crucial to thoroughly understand the problem and analyze its properties to determine the most appropriate algorithmic approach.

#### how can i try to best determine a local optimal solution? what are some analytical steps I should take in a general solution to a problem?

When attempting to find a local optimal solution to a problem, you can follow these analytical steps:

- Define the Problem: Clearly understand the problem statement, its constraints, and the desired outcome. This step ensures you have a solid understanding of what needs to be solved.

- Identify the Objective Function: Determine the metric or objective that defines the quality of a solution. This could be maximizing or minimizing a certain value, such as profit, cost, efficiency, or error.

- Analyze the Problem Structure: Break down the problem into its constituent elements, such as variables, constraints, dependencies, and relationships between different components. Understand how these elements interact and affect the objective function.

- Explore the Solution Space: Determine the range of possible solutions for the problem. This could involve analyzing the feasible region or identifying the set of valid solutions based on the constraints.

- Develop a Heuristic: A heuristic is a problem-solving strategy or rule of thumb that helps guide the search for a solution. It provides a direction or guideline for making decisions at each step. This could involve leveraging prior knowledge, intuition, or insights gained from analyzing the problem structure.

- Design a Local Search Strategy: Identify a method for iteratively improving solutions by making incremental changes. This could involve exploring neighboring solutions, evaluating their quality based on the objective function, and moving towards better solutions.

- Implement and Evaluate: Implement the local search strategy and start with an initial solution. Iterate and evaluate the quality of the solutions obtained. Keep track of the best solution found so far.

- Termination Condition: Determine the stopping criteria for the local search algorithm. This could be a specific number of iterations, reaching a certain threshold of improvement, or when a predefined condition is met.

- Analyze the Solution: Evaluate the final solution obtained and analyze its quality and optimality with respect to the objective function. Compare it against known optimal solutions if available.

- Refine and Iterate: If necessary, refine the problem definition, objective function, heuristics, or search strategy based on the insights gained from analyzing the solution. Repeat the process to improve the solution further.

By following these steps, you can approach problems systematically and iteratively improve towards a local optimal solution. Remember that the effectiveness of this approach depends on the problem's nature and the chosen heuristics or search strategy.
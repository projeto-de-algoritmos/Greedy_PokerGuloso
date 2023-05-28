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
onde vai receber o estado do jogo (com as suas cartas) e retornará a jogada, que pode ser uma desistencia, aceitar aumento ou não aumentar nada.

Este jogo segue as regras do [TEXAS HOLD'EM](https://en.wikipedia.org/wiki/Texas_hold_%27em).

Na pasta `estrategias` haverão diversas implementações para se testar.

Todas as cartas são representada como `f(naipe,valor) = "{naipe}{valor}"`, onde `naipe` pode ser `[E,O,P,C]` representando espadas, ouros, paus e copas. O valor pode ser `[A,K,Q,J,10,9,8,7,6,5,4,3,2]` represetando os valores (em ordem decrescente) das cartas do poker. Por exemplo, `E4` significa *4 de paus* ou `OQ` significa *dama de ouros*.

## Screenshots
<!-- Adicione 3 ou mais screenshots do projeto em funcionamento. -->

Um jogo aleatório registrado no `log_jogos.json`:

![](imgs/Screenshot%20from%202023-05-28%2016-20-04.png)

A sequência de ações realizadas em um jogo específico:

![](imgs/Screenshot%20from%202023-05-28%2016-20-04.png)





## Instalação 
**Linguagem**: Python3<br>
**Framework**: *nenhum*<br>

## Uso 



## Outros 
#### Considerações sobre o projeto

A implementação de uma interface gráfica iria demorar demais, detraindo esforço da proposta principal do projeto, então não foi feita.

#### Perguntas interessantes respondidas pela chatgpt

##### How can we mathematically decide that a problem can be solved using a greedy algorithm?

To determine if a problem can be solved using a greedy algorithm, you generally need to evaluate the problem's properties and characteristics. While there is no definitive mathematical test, you can consider the following factors:

- Greedy Choice Property: A greedy algorithm makes locally optimal choices at each step in the hope of finding a global optimum. If the problem exhibits the greedy choice property, meaning that a locally optimal choice always leads to a globally optimal solution, a greedy algorithm may be applicable.

- Optimal Substructure: A problem has optimal substructure if an optimal solution to the problem contains optimal solutions to its subproblems. This property is important because it allows a greedy algorithm to make a series of choices that collectively lead to an optimal solution.

- Proof or Counterexamples: Analyze the problem and try to prove that a greedy algorithm will always yield an optimal solution. Alternatively, look for counterexamples where a greedy approach fails to produce an optimal solution. By examining the problem's specific characteristics, you can gain insight into the applicability of a greedy algorithm.

While these considerations can guide your decision, keep in mind that they do not guarantee the success of a greedy approach. It's crucial to thoroughly understand the problem and analyze its properties to determine the most appropriate algorithmic approach.

##### how can i try to best determine a local optimal solution? what are some analytical steps I should take in a general solution to a problem?

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
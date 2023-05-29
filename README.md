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

Todas as cartas são representada como `f(naipe,valor) = "{naipe}{valor}"`, onde `naipe` pode ser `[E,O,P,C]` representando espadas, ouros, paus e copas. O `valor` pode ser `[A,K,Q,J,10,9,8,7,6,5,4,3,2]` represetando os valores (em ordem decrescente) das cartas do poker. Por exemplo, `E4` significa *4 de paus* ou `OQ` significa *dama de ouros*.

## Screenshots
<!-- Adicione 3 ou mais screenshots do projeto em funcionamento. -->

#### Um jogo aleatório registrado no `log_jogos.json`:

![](imgs/Screenshot%20from%202023-05-28%2016-20-04.png)

#### A sequência de ações realizadas em um jogo específico:

![](imgs/Screenshot%20from%202023-05-28%2016-45-31.png)

Note como nenhum dos jogadores realizou nenhuma aposta. O jogo terminou com o pote que foram forçados a colocar no começo.

#### Uma análise realizada sobre 1000 jogos

![](imgs/Screenshot%20from%202023-05-28%2016-48-45.png)

Note que:
- Assim como a partida na imagem anterior a essa, nenhum jogador realizou nenhuma aposta nessas 1000 partidas, como baseline para desenvolver heurísticas do jogo.
- A carta que trouxe vitórias mais vezes foi a 4.
- A maior quantidade de vitórias foi vencida por pares de cartas.
- Vitórias com `4 of a kind` (4 cartas de mesmo valor) são extremamente raras.
- Houveram empates.

## Instalação 
**Linguagem**: Python3<br>
**Framework**: *nenhum*<br>

## Uso 


Para executar a simulação de jogos, rode: 
```
python sim.py
```
Esse comando vai gerar um arquivo `log_jogos.json` e `logs/log_jogos_<timestamp>.json`
Este arquivo é usado para análise, que gera estatísticas sobre os jogos e permitem o desenvolvimento de um algoritmo melhor.

Para executar a análise de todas as estrategias , rode:
```
python analise.py
```

Para executar uma análise sobre o `log_jogos.json`, rode:
```
python analise.py get_estatisticas
```

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

#### Analises dos algoritimos criados

Descrições:
1. nunca_desiste_nem_aumenta.py
   - Simplesmente paga o valor que precisa pagar pra continuar (inclusive all in)
   - este é um baseline
2. vantagem_simples_v1.py
   - **hipotese**: apostar se suas cartas já forem boas
   - calcula, no conjunto atual de cartas, quais são as chances de ganhar. Se 2 cartas que levam a vitoria forem da sua mão, você tem uma vantagem injusta pro seu adversário, então da all in. Caso contrário faz como o primeiro.
   - **resultado**: surpreendemente, não difere quase nada da estratégia baseline
3. vantagem_fatorada_v1.py
   - **hipotese**: apostar conforme suas chances de ganhar seja grande
   - faz como a 5, mas apenas aceita vitorias melhores que um par (como 2 pares).
   - **resultado:** 
4. vantagem_simples_v2.py
   - faz como a 2, mas desiste de não tiver cartas boas.
5. vantagem_simples_v3.py
   - faz como a 4, mas permance no jogo se tiver 1 carta que representa vantagem injusta.
   - **resultado**
6. vantagem_simples_v4.py
   - **hipotese:** desistir é, em geral, uma jogada ruim. ao invés disso, vamos fatorar apostas.
   - faz como a 5, mas nunca desiste a aposta menos.
   - **resultado:** em comparação com o 5, vai a falência menos vezes

```
os seguintes scripts foram encontrados e serao comparados:
	- nunca_desiste_nem_aumenta.py
	- vantagem_fatorada_v1.py
	- vantagem_simples_v1.py
	- vantagem_simples_v2.py
	- vantagem_simples_v3.py



diff vitorias: [
    {
        "diffApraB": -40,
        "percentualA": 0.48633333333333334,
        "percentualB": 0.49966666666666665,
        "scriptA": "vantagem_fatorada_v1.py",
        "scriptB": "vantagem_fatorada_v1.py"
    },
    {
        "diffApraB": -47,
        "percentualA": 0.4856666666666667,
        "percentualB": 0.5013333333333333,
        "scriptA": "vantagem_fatorada_v1.py",
        "scriptB": "vantagem_simples_v2.py"
    },
    {
        "diffApraB": -50,
        "percentualA": 0.48333333333333334,
        "percentualB": 0.5,
        "scriptA": "nunca_desiste_nem_aumenta.py",
        "scriptB": "vantagem_simples_v4.py"
    },
    {
        "diffApraB": -57,
        "percentualA": 0.48233333333333334,
        "percentualB": 0.5013333333333333,
        "scriptA": "nunca_desiste_nem_aumenta.py",
        "scriptB": "vantagem_simples_v2.py"
    },
    {
        "diffApraB": -59,
        "percentualA": 0.48333333333333334,
        "percentualB": 0.503,
        "scriptA": "vantagem_simples_v1.py",
        "scriptB": "vantagem_simples_v1.py"
    },
    {
        "diffApraB": -61,
        "percentualA": 0.48333333333333334,
        "percentualB": 0.5036666666666667,
        "scriptA": "nunca_desiste_nem_aumenta.py",
        "scriptB": "vantagem_simples_v3.py"
    },
    {
        "diffApraB": -64,
        "percentualA": 0.481,
        "percentualB": 0.5023333333333333,
        "scriptA": "nunca_desiste_nem_aumenta.py",
        "scriptB": "vantagem_fatorada_v1.py"
    },
    {
        "diffApraB": -69,
        "percentualA": 0.4786666666666667,
        "percentualB": 0.5016666666666667,
        "scriptA": "vantagem_fatorada_v1.py",
        "scriptB": "vantagem_simples_v1.py"
    },
    {
        "diffApraB": -72,
        "percentualA": 0.48,
        "percentualB": 0.504,
        "scriptA": "vantagem_fatorada_v1.py",
        "scriptB": "vantagem_simples_v4.py"
    },
    {
        "diffApraB": -78,
        "percentualA": 0.47733333333333333,
        "percentualB": 0.5033333333333333,
        "scriptA": "nunca_desiste_nem_aumenta.py",
        "scriptB": "vantagem_simples_v1.py"
    },
    {
        "diffApraB": -99,
        "percentualA": 0.4786666666666667,
        "percentualB": 0.5116666666666667,
        "scriptA": "vantagem_simples_v4.py",
        "scriptB": "vantagem_simples_v4.py"
    },
    {
        "diffApraB": -119,
        "percentualA": 0.47533333333333333,
        "percentualB": 0.515,
        "scriptA": "vantagem_simples_v2.py",
        "scriptB": "vantagem_simples_v3.py"
    },
    {
        "diffApraB": -122,
        "percentualA": 0.47533333333333333,
        "percentualB": 0.516,
        "scriptA": "vantagem_simples_v2.py",
        "scriptB": "vantagem_simples_v2.py"
    },
    {
        "diffApraB": -134,
        "percentualA": 0.473,
        "percentualB": 0.5176666666666667,
        "scriptA": "vantagem_simples_v2.py",
        "scriptB": "vantagem_simples_v4.py"
    },
    {
        "diffApraB": -145,
        "percentualA": 0.471,
        "percentualB": 0.5193333333333333,
        "scriptA": "vantagem_simples_v3.py",
        "scriptB": "vantagem_simples_v3.py"
    },
    {
        "diffApraB": -160,
        "percentualA": 0.4686666666666667,
        "percentualB": 0.522,
        "scriptA": "vantagem_simples_v3.py",
        "scriptB": "vantagem_simples_v4.py"
    },
    {
        "diffApraB": 236,
        "percentualA": 0.5333333333333333,
        "percentualB": 0.45466666666666666,
        "scriptA": "nunca_desiste_nem_aumenta.py",
        "scriptB": "nunca_desiste_nem_aumenta.py"
    },
    {
        "diffApraB": 254,
        "percentualA": 0.5393333333333333,
        "percentualB": 0.45466666666666666,
        "scriptA": "vantagem_fatorada_v1.py",
        "scriptB": "vantagem_simples_v3.py"
    },
    {
        "diffApraB": 655,
        "percentualA": 0.6026666666666667,
        "percentualB": 0.38433333333333336,
        "scriptA": "vantagem_simples_v1.py",
        "scriptB": "vantagem_simples_v3.py"
    },
    {
        "diffApraB": 673,
        "percentualA": 0.6063333333333333,
        "percentualB": 0.382,
        "scriptA": "vantagem_simples_v1.py",
        "scriptB": "vantagem_simples_v4.py"
    },
    {
        "diffApraB": 901,
        "percentualA": 0.6456666666666667,
        "percentualB": 0.3453333333333333,
        "scriptA": "vantagem_simples_v1.py",
        "scriptB": "vantagem_simples_v2.py"
    }
]
diff falencias: [
    {
        "diffApraB": -40,
        "percentualA": 0.48633333333333334,
        "percentualB": 0.49966666666666665,
        "scriptA": "vantagem_fatorada_v1.py",
        "scriptB": "vantagem_fatorada_v1.py"
    },
    {
        "diffApraB": -47,
        "percentualA": 0.4856666666666667,
        "percentualB": 0.5013333333333333,
        "scriptA": "vantagem_fatorada_v1.py",
        "scriptB": "vantagem_simples_v2.py"
    },
    {
        "diffApraB": -50,
        "percentualA": 0.48333333333333334,
        "percentualB": 0.5,
        "scriptA": "nunca_desiste_nem_aumenta.py",
        "scriptB": "vantagem_simples_v4.py"
    },
    {
        "diffApraB": -57,
        "percentualA": 0.48233333333333334,
        "percentualB": 0.5013333333333333,
        "scriptA": "nunca_desiste_nem_aumenta.py",
        "scriptB": "vantagem_simples_v2.py"
    },
    {
        "diffApraB": -59,
        "percentualA": 0.48333333333333334,
        "percentualB": 0.503,
        "scriptA": "vantagem_simples_v1.py",
        "scriptB": "vantagem_simples_v1.py"
    },
    {
        "diffApraB": -61,
        "percentualA": 0.48333333333333334,
        "percentualB": 0.5036666666666667,
        "scriptA": "nunca_desiste_nem_aumenta.py",
        "scriptB": "vantagem_simples_v3.py"
    },
    {
        "diffApraB": -64,
        "percentualA": 0.481,
        "percentualB": 0.5023333333333333,
        "scriptA": "nunca_desiste_nem_aumenta.py",
        "scriptB": "vantagem_fatorada_v1.py"
    },
    {
        "diffApraB": -69,
        "percentualA": 0.4786666666666667,
        "percentualB": 0.5016666666666667,
        "scriptA": "vantagem_fatorada_v1.py",
        "scriptB": "vantagem_simples_v1.py"
    },
    {
        "diffApraB": -72,
        "percentualA": 0.48,
        "percentualB": 0.504,
        "scriptA": "vantagem_fatorada_v1.py",
        "scriptB": "vantagem_simples_v4.py"
    },
    {
        "diffApraB": -78,
        "percentualA": 0.47733333333333333,
        "percentualB": 0.5033333333333333,
        "scriptA": "nunca_desiste_nem_aumenta.py",
        "scriptB": "vantagem_simples_v1.py"
    },
    {
        "diffApraB": -99,
        "percentualA": 0.4786666666666667,
        "percentualB": 0.5116666666666667,
        "scriptA": "vantagem_simples_v4.py",
        "scriptB": "vantagem_simples_v4.py"
    },
    {
        "diffApraB": -119,
        "percentualA": 0.47533333333333333,
        "percentualB": 0.515,
        "scriptA": "vantagem_simples_v2.py",
        "scriptB": "vantagem_simples_v3.py"
    },
    {
        "diffApraB": -122,
        "percentualA": 0.47533333333333333,
        "percentualB": 0.516,
        "scriptA": "vantagem_simples_v2.py",
        "scriptB": "vantagem_simples_v2.py"
    },
    {
        "diffApraB": -134,
        "percentualA": 0.473,
        "percentualB": 0.5176666666666667,
        "scriptA": "vantagem_simples_v2.py",
        "scriptB": "vantagem_simples_v4.py"
    },
    {
        "diffApraB": -145,
        "percentualA": 0.471,
        "percentualB": 0.5193333333333333,
        "scriptA": "vantagem_simples_v3.py",
        "scriptB": "vantagem_simples_v3.py"
    },
    {
        "diffApraB": -160,
        "percentualA": 0.4686666666666667,
        "percentualB": 0.522,
        "scriptA": "vantagem_simples_v3.py",
        "scriptB": "vantagem_simples_v4.py"
    },
    {
        "diffApraB": 236,
        "percentualA": 0.5333333333333333,
        "percentualB": 0.45466666666666666,
        "scriptA": "nunca_desiste_nem_aumenta.py",
        "scriptB": "nunca_desiste_nem_aumenta.py"
    },
    {
        "diffApraB": 254,
        "percentualA": 0.5393333333333333,
        "percentualB": 0.45466666666666666,
        "scriptA": "vantagem_fatorada_v1.py",
        "scriptB": "vantagem_simples_v3.py"
    },
    {
        "diffApraB": 655,
        "percentualA": 0.6026666666666667,
        "percentualB": 0.38433333333333336,
        "scriptA": "vantagem_simples_v1.py",
        "scriptB": "vantagem_simples_v3.py"
    },
    {
        "diffApraB": 673,
        "percentualA": 0.6063333333333333,
        "percentualB": 0.382,
        "scriptA": "vantagem_simples_v1.py",
        "scriptB": "vantagem_simples_v4.py"
    },
    {
        "diffApraB": 901,
        "percentualA": 0.6456666666666667,
        "percentualB": 0.3453333333333333,
        "scriptA": "vantagem_simples_v1.py",
        "scriptB": "vantagem_simples_v2.py"
    }
]
```
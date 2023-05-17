# Projeto sem Nome

**Número da Lista**: ?
**Conteúdo da Disciplina**: GULOSOS 😏<br>

## Alunos
| Matrícula | Aluno           |
| --------- | --------------- |
| xx/xxxxxx | xxxx xxxx xxxxx |
| xx/xxxxxx | xxxx xxxx xxxxx |

## Sobre 
<!-- Descreva os objetivos do seu projeto e como ele funciona.  -->

A ideia seria montar uma simulação de um jogo estilo pedra papel e tesoura, onde existe "nosso exército" e o "exército deles". O exército deles usará (atacará usando) "armas" contra nós, e nós precisamos retornar (contratacar) cada ataque inimigo utilizando as "armas" que possuímos. Cada arma destroi um conjunto de outras armas:

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

Caso 2:
- X=[1,1,0,0]
- Se arma 1 destroi 3 e 4.
- Se arma 2 destroi 3 e 1.
- Y=[1,0,2,1]
- Qualquer escolha que eu faço reduzirá o vetor Y em mesma proporção, portanto qualquer escolha é correta. 

Portanto, a escolha sempre será definida por: o que causa a menor variação do valor mínimo no vetor Y, e no caso de empate, será o que causa a menor variação dentro do vetor Y (que sempre será negativa).

Como todas as armas representa uma união distinta do conjunto de armas que são contratacadas e contratacam, isso representa a solução da escolha porque é sempre uma escolha ideal dado o cenário apresentado - ela é gulosa.

### Sobre as jogadas e as rodadas



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





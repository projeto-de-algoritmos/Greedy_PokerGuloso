import json
from scriptA import fazer_jogada as fazer_jogadaA
from scriptB import fazer_jogada as fazer_jogadaB
from common import *


class Jogador:
    __fazer_jogada: any
    cartas: list[Carta]
    banca: int  # dinheiro do jogador
    aposta_turno_atual: int
    aposta_total: int

    nome: str
    indice: int

    def __init__(self, fazer_jogada, cartas, banca, indice=0):
        self.__fazer_jogada = fazer_jogada
        self.cartas = cartas
        self.banca = banca

        self.aposta_turno_atual = 0
        self.aposta_total = 0

        self.indice = indice
        self.nome = ['A', 'B', 'C', 'D', 'E', 'F'][indice]

    # retorn a carta jogada, desistencia do jogo ou aumento da aposta
    # se aumento for zero, não tem aposta
    def fazer_jogada(self, estado: EstadoDoJogoParaJogador):
        carta, desistiu, aumento = self.__fazer_jogada(estado)
        if carta not in self.cartas:
            raise ValueError("Carta não está na mão")
        return carta, desistiu, aumento

    def limpar_turno(self):
        self.aposta_turno_atual = 0


class Rodada:
    jogadores: list[Jogador]
    historico_estado: list[str]

    valor_aumento: int
    pote_rodada: int

    indice_jogador_aumento: int
    indice_jogador_atual: int

    turnos_restantes: int
    turnos_jogados: int

    def __init__(self, jogadores: list[Jogador], big_blind_index: int):
        self.jogadores = jogadores
        self.historico_estado = []
        self.indice_jogador_aumento = -1
        self.valor_aumento = -1
        self.indice_jogador_atual = 0
        self.turnos_restantes = len(self.jogadores)
        self.turnos_jogados = 0
        self.pote_rodada = 0

    def remove_jogador(self, indice_jogador=-1, jogador=None):
        if jogador != None:
            indice_jogador = self.jogadores.index(jogador)
        self.jogadores.pop(indice_jogador)
        self.apostas.pop(indice_jogador)
        self.turnos_restantes -= 1

    def jogador_falhou(self, jogador: Jogador, msg: str):
        self.historico_estado.append(f"ERRO! jogador {jogador.nome} {msg}")
        self.remove_jogador(jogador=jogador)

    def log_jogador(self, jogador: Jogador, msg: str):
        self.historico_estado.append(f"jogador {jogador.nome}: {msg}")

    # toda vez que o jogador faz jogada falha, vamos assumir que ele desistiu por W.O.
    def processa_aposta(self, jogador, aumento):
        i = self.jogadores.index(jogador)

        if self.indice_jogador_aumento == i:
            self.jogador_falhou(
                jogador, f"apostou duas vezes")

        valor_adicionado = aumento - jogador.aposta_turno_atual
        if valor_adicionado > jogador.banca:
            self.jogador_falhou(
                jogador, f"não tem dinheiro para igualar")

        if aumento < self.valor_aumento:
            self.jogador_falhou(
                jogador, f"apostou menos que o anterior")

        if aumento > self.valor_aumento:
            if self.valor_aumento * 2 > aumento:
                self.jogador_falhou(
                    jogador, f"apostou menos que o dobro da aposta atual")

            self.indice_jogador_aumento = i
            self.valor_aumento = aumento
            self.turnos_restantes += len(self.jogadores) - 1
            self.log_jogador(
                self.jogadores[i], f"aumentou para {aumento}")

        if aumento == self.valor_aumento:
            self.historico_estado.append(
                f"jogador {jogador.nome} igualou a aposta {aumento}")

        jogador.aposta_turno_atual += valor_adicionado
        jogador.aposta_total += valor_adicionado
        self.pote_rodada += valor_adicionado

    # retorna os jogadores que ainda estão no jogo
    def processar_rodada(self):
        self.historico_estado.append("começando rodada")

        while self.turnos_jogados < self.turnos_restantes:
            i = self.indice_jogador_atual
            jogador = self.jogadores[i]

            self.log_jogador(jogador, f"começando rodada")

            desistiu, aumento = jogador.fazer_jogada(
                self.get_estado_jogo(jogador))

            if desistiu:
                self.log_jogador(jogador, f"desistiu")
                self.remove_jogador(indice_jogador=i)

            self.processa_aposta(jogador, aumento)

            self.indice_jogador_atual = (i + 1) % len(self.jogadores)

        return self.jogadores

    def get_historico(self):
        return self.historico_estado

    def get_estado_jogo(self, jogador: Jogador) -> EstadoDoJogoParaJogador:
        return EstadoDoJogoParaJogador(
            jogador.cartas,
            self.mesa,
            [jogador.aposta_turno_atual for jogador in self.jogadores],
            [jogador.aposta_total for jogador in self.jogadores],
            [jogador.banca for jogador in self.jogadores],
        )


class Partida:

    mesa: list[Carta]
    historico_estado: list[str]
    banca: int
    jogadores: list[Jogador]
    deck: list[Carta]
    valor_inicial: int
    big_blind: int
    small_blind: int

    calculadora: CalculadoraDeVitoria

    def __init__(self, valor_inicial: int = 1000, big_blind: int = 0, small_blind: int = 1):
        self.historico_estado = []
        self.mesa = []
        self.banca = 0
        cartas = faz_permutacao_cartas()
        self.jogadores = [
            Jogador(fazer_jogadaA, cartas[0:2], valor_inicial, 0),
            Jogador(fazer_jogadaB, cartas[2:4], valor_inicial, 1),
        ]
        self.deck = cartas[4:]
        self.valor_inicial = valor_inicial
        self.big_blind = big_blind
        self.small_blind = small_blind
        self.calculadora = CalculadoraDeVitoria()

    def pega_carta_deck(self):
        self.deck, carta_nova = self.deck[1:], self.deck[0]
        self.mesa.append(carta_nova)
        return carta_nova

    def play(self):
        self.historico_estado.append("iniciando partida")
        self.historico_estado.append("MESA: {self.mesa}")
        self.historico_estado.append("processando jogadores")

        jogadores = self.jogadores.copy()

        # pega os blind
        jogadores[self.small_blind].banca -= int(self.valor_inicial / 50)
        jogadores[self.big_blind].banca -= int(self.valor_inicial / 100)
        pote = 0

        # faz as viradas pelo numero de cartas na mesa
        for i in [0, 3, 4, 5]:
            while len(self.mesa) < i:
                self.pega_carta_deck()
            self.historico_estado.append(f"cartas na mesa: {self.mesa}")
            rodada = Rodada(jogadores)
            jogadores = rodada.processar_rodada()
            if len(jogadores) == 1:
                self.historico_estado.append(
                    f"jogador {jogadores[0].nome} ganhou porque todos os outros desistiram")
                vencedores = jogadores
                break
            pote += rodada.pote_rodada

        self.historico_estado.append("fim de jogo")

        self.distribuir_premio_jogadores(jogadores.copy())

        return self.historico_estado

    def distribuir_premio_jogadores(self, jogadores: list[Jogador]) -> list[float]:
        pote_total = self.pote_total
        jogadores = sorted(jogadores, key=lambda jogador: jogador.aposta_total)

        # lista de potes por preço que cada jogador participante do pote pagou. Existe, ao menos, 1 pote.
        # Todos os jogadores que estão em potes menores que o pote máximos estão em all-in, e sua banca é necessariamente 0
        val_potes_pra_cada = list(
            set([jogador.aposta_total for jogador in jogadores]))

        # Exemplo 4 jogadores, onde 2 all in ganharam e 2 empataram no pote final, como exemplo
        # pote_total = 550
        # 50 (all in) (pote max = 50*num_jogadores = 200 = a1)
        # jogador 1 ganha 200
        # pote_total = 350
        # 100 (all in) (pote max = 100*(num_jogadores-1)-a1 = 300 = a2)
        # jogador 2 ganha 100
        # pote_total = 50
        # 200, 200 (pote max = 200*(num_jogadores-2)-a1-a2 = 50; num_vencedores=2; pote_cada=25 = a3)
        # jogador 3 e 4 ganham 25
        # pote_total = 0
        # fim

        valor_distribuido = 0

        for pote in val_potes_pra_cada:
            if len(jogadores) == 0:
                raise Exception("ERRO! Pote sem vencedor??")
            maos = []

            for jogador in jogadores:
                mao = jogador.mao.copy()
                mao = mao + self.mesa.copy()
                maos += mao

            vencedores, cartas = self.calculadora.get_maos_vencedoras(maos)

            self.historico_estado.append(
                f"pote de {pote} vencido por jogador(es) {', '.join([jogadores[i] for i in vencedores])}")

            total_desse_pote = pote * len(jogadores) - valor_distribuido
            if total_desse_pote > pote_total:
                raise Exception("ERRO! Pote maior que o total?")

            for vencedor_i in vencedores:
                vencedor = jogadores[vencedor_i]
                ganho = total_desse_pote / len(vencedores)
                vencedor.banca += ganho
                valor_distribuido += ganho

            pote_total -= total_desse_pote

            while len(jogadores) > 0 and jogadores[0].aposta_total == pote:
                jogadores.pop(0)


def main():
    while True:
        partida = Partida()
        historico_estado = partida.play()
        print(historico_estado)


if __name__ == "__main__":
    main()

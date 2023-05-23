import json
from scriptA import fazer_jogada as fazer_jogadaA
from scriptB import fazer_jogada as fazer_jogadaB
from common import *


class Jogador:
    __fazer_jogada: callable[[EstadoDoJogoParaJogador], Carta]
    cartas: list[Carta]
    banca: int  # dinheiro do jogador

    def __init__(self, fazer_jogada):
        self.__fazer_jogada = fazer_jogada

    # retorn a carta jogada, desistencia do jogo ou aumento da aposta
    # se aumento for zero, não tem aposta
    def fazer_jogada(self, estado: EstadoDoJogoParaJogador):
        carta, desistiu, aumento = self.__fazer_jogada(estado)
        if carta not in self.cartas:
            raise ValueError("Carta não está na mão")
        return carta, desistiu, aumento


class Partida:

    mesa: list[Carta]
    historico_estado: list[str]
    banca: int
    jogadores: list[Jogador]
    deck: list[Carta]

    def __init__(self):
        self.historico_estado = []
        self.mesa = []
        self.banca = 0
        cartas = faz_permutacao_cartas()
        self.jogadores = [
            Jogador(fazer_jogadaA, cartas[0:2]),
            Jogador(fazer_jogadaB, cartas[2:4]),
        ]
        self.deck = cartas[4:]

    def play(self):
        self.historico_estado.append("iniciando partida")
        self.historico_estado.append("MESA: {self.mesa}")
        self.historico_estado.append("processando jogadores")

        self.deck, carta_nova = self.deck[1:]

        self.processar_jogadores()
        self.historico_estado.append("fim de turno")
        return self.historico_estado

    def processar_jogadores(self):
        # novo turno (acabou de descer a mão)
        indice_jogador_aumento = -1
        valor_aumento = -1
        big_blind = 0
        small_blind = 1
        xi = 0
        min_i = len(self.jogadores)

        while xi < min_i:
            i = (xi) % len(self.jogadores)
            jogador = self.jogadores[i]
            if jogador.cartas == None:
                continue

            desistiu, aumento = jogador.fazer_jogada(self.estado)
            if desistiu:
                self.historico_estado.append(f"jogador {i} desistiu")
                jogador.cartas = None

            if aumento > 0:
                if indice_jogador_aumento == i:
                    self.historico_estado.append(
                        f"ERRO! jogador {i} jogou apostou duas vezes")
                    raise ValueError(
                        "Jogador não pode aumentar duas vezes, alguém precisa aumentar antes")
                if aumento < valor_aumento:
                    self.historico_estado.append(
                        f"ERRO! jogador {i} apostou menos que o anterior")
                    raise ValueError(
                        "Aumento não é maior que o anterior")
                if aumento > valor_aumento:
                    if valor_aumento * 2 > aumento:
                        self.historico_estado.append(
                            f"ERRO! jogador {i} apostou menos que o dobro da aposta atual")
                        raise ValueError(
                            "Aumento não é o dobro do anterior")
                    else:
                        indice_jogador_aumento = i
                        valor_aumento = aumento
                        min_i += len(self.jogadores) - 1
                        self.historico_estado.append(
                            f"jogador {i} aumentou para {aumento}")
                else:
                    self.historico_estado.append(
                        f"jogador {i} igualou a aposta {aumento}")
                    if jogador.banca < aumento:
                        self.historico_estado.append(
                            f"ERRO! jogador {i} não tem dinheiro para igualar")
                        raise ValueError(
                            "Jogador não tem dinheiro para igualar")

            xi += 1

        return self.historico_estado


def main():

    while True:
        partida = Partida()
        historico_estado = partida.play()
        print(historico_estado)


if __name__ == "__main__":
    main()

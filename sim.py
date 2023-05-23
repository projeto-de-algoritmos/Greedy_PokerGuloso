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

    def __init__(self):
        self.historico_estado = []
        self.mesa = []
        cartas = faz_permutacao_cartas()
        self.jogadores = [
            Jogador(fazer_jogadaA, cartas[0:2]),
            Jogador(fazer_jogadaB, cartas[2:4]),
        ]
        self.deck = cartas[4:]

    def play(self):
        # novo jogo
        while True:

            # novo turno (acabou de descer a mão)
            indice_jogador_aumento = -1
            valor_aumento = -1
            i = 0
            min_i = len(self.jogadores)

            while i < min_i:
                jogador = self.jogadores[i]
                if jogador.cartas == []:
                    continue

                desistiu, aumento = jogador.fazer_jogada(self.estado)
                if desistiu:
                    jogador.cartas = []

                if aumento > 0:
                    if indice_jogador_aumento == i:
                        raise ValueError(
                            "Jogador não pode aumentar duas vezes, alguém precisa aumentar antes")
                    if aumento > valor_aumento:
                        if valor_aumento * 2 > aumento:
                            raise ValueError(
                                "Aumento não é o dobro do anterior")
                        else:
                            indice_jogador_aumento = i
                            valor_aumento = aumento
                            min_i += len(self.jogadores) - 1
                    if carta != None:
                        raise ValueError(
                            "Jogador não pode aumentar e jogar carta")
                else:

                self.estado.mao.remove(carta)
                self.estado.mesa.append(carta)
                self.historico_estado.append(self)

                i = (i + 1) % len(self.jogadores)

        return self.historico_estado


def main():

    while True:
        partida = Partida()
        historico_estado = partida.play()
        print(historico_estado)


if __name__ == "__main__":
    main()

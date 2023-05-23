import json
from scriptA import fazer_jogada as fazer_jogadaA
from scriptB import fazer_jogada as fazer_jogadaB
from common import *


class Jogador:
    __fazer_jogada: callable[[EstadoDoJogo], Carta]
    cartas: list[Carta]

    def __init__(self, fazer_jogada):
        self.__fazer_jogada = fazer_jogada

    def fazer_jogada(self, estado: EstadoDoJogo):
        carta = self.__fazer_jogada(estado)
        if carta not in self.cartas:
            raise ValueError("Carta não está na mão")
        return carta


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
            # novo turno
            for jogador in self.jogadores:
                carta = jogador.fazer_jogada(self.estado)
                self.estado.mao.remove(carta)
                self.estado.mesa.append(carta)
                self.historico_estado.append(self)

        return self.historico_estado


def main():

    while True:
        partida = Partida()
        historico_estado = partida.play()
        print(historico_estado)


if __name__ == "__main__":
    main()

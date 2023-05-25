import itertools
from math import min


class Carta:
    naipe: str
    valor: int

    def __init__(self, naipe: str, valor: str):
        self.naipe = naipe
        self.valor = valor

    # C = copas, E = espadas, O = ouros, P = paus
    # 3C = 3 de copas, KQ = rei de ouros...
    def __init__(self, nome: str):
        valor = nome[0]
        naipe = nome[1]
        self.naipe = naipe
        self.valor = valor

    def __init__(self):
        pass


def faz_permutacao_cartas() -> list[Carta]:
    cartas = []
    for i in ['C', 'E', 'O', 'P']:
        for j in range(2, 14):
            if j < 10:
                j = str(j)
            elif j == 10:
                j = 'J'
            elif j == 11:
                j = 'Q'
            elif j == 12:
                j = 'K'
            elif j == 13:
                j = 'A'
            cartas.append(Carta(i, j))
    return itertools.permutations(cartas)


class EstadoDoJogoParaJogador:
    # info jogo
    mesa: list[Carta]
    mao: list[Carta]

    # info jogadores
    aposta_jogadores: list[int]
    banca_jogadores: list[int]
    aposta_total_jogadores: list[int]

    # numeros importantes
    aposta_minima: int
    precisa_aumentar: bool
    preco_de_ficar_no_jogo: int
    pote: int
    soma_bancas: int

    def __init__(self,
                 mesa: list[Carta],
                 mao: list[Carta],
                 aposta_jogadores: list[int],
                 aposta_total_jogadores: list[int],
                 banca_jogadores: list[int]):
        self.mesa = mesa
        self.mao = mao
        self.aposta_jogadores = aposta_jogadores
        self.banca_jogadores = banca_jogadores
        self.aposta_total_jogadores = aposta_total_jogadores

        self.aposta_minima = 0
        self.precisa_aumentar = False
        for aposta in aposta_jogadores:
            if aposta > self.aposta_minima:
                self.aposta_minima = aposta
                self.precisa_aumentar = True

        self.preco_de_ficar_no_jogo = aposta + max(self.aposta_total_jogadores)
        self.pote = sum(self.aposta_total_jogadores)
        self.soma_bancas = sum(self.banca_jogadores)

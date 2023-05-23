import itertools


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
    mesa: list[Carta]
    mao: list[Carta]

    def __init__(self):
        self.mesa = []
        self.mao = []

import random


class Carta:
    naipe: str
    valor: str
    nome: str
    valor_i: int

    # VALOR: 2, 3, 4, 5, 6, 7, 8, 9, 10, J = valete, Q = dama, K = rei, A = ás
    # VALOR_I: 2...14
    # NAIPE: C = copas, E = espadas, O = ouros, P = paus
    # NOME: 3C = 3 de copas, KQ = rei de ouros...
    def __init__(self, nome: str = None, naipe: str = None, valor: str = None, valor_i: int = None):
        if naipe is not None and (valor is not None or valor_i is not None):
            self.naipe = naipe
            self.__set_valor(valor=valor, valor_i=valor_i)
        elif nome is not None:
            naipe = nome[0]
            valor = nome[1:]
            self.naipe = naipe
            self.__set_valor(valor=valor, valor_i=valor_i)
        else:
            raise Exception("Precisa de nome ou naipe e valor")

    def __set_valor(self, valor_i: int, valor: str):
        if valor is not None:
            self.valor = valor
            self.valor_i = self.__valor_to_int(valor)
        elif valor_i is not None:
            self.valor_i = valor_i
            self.valor = self.__valor_int_to_str(valor_i)

    def __valor_to_int(self, valor: str):
        if valor.isnumeric():
            self.valor_i = int(valor)
            return self.valor_i
        return {
            'J': 11,
            'Q': 12,
            'K': 13,
            'A': 14,
        }[valor]

    def __valor_int_to_str(self, valor_i: int):
        if valor_i < 11:
            return str(valor_i)
        return {
            11: 'J',
            12: 'Q',
            13: 'K',
            14: 'A',
        }[valor_i]

    def __repr__(self) -> str:
        return f"{self.naipe}{self.valor}"

    def __gt__(self, other) -> bool:
        return self.valor_i >= other.valor_i

    def __lt__(self, other) -> bool:
        return self.valor_i <= other.valor_i

    def to_json(self):
        return {
            'valor_i': self.valor_i,
            'naipe': self.naipe,
            'valor': self.valor,
            'nome': self.nome,
        }

    def from_json(cls, json_data):
        return cls(nome=json_data[0])


def faz_permutacao_cartas(seed=0) -> list[Carta]:
    cartas = []
    for i in ['C', 'E', 'O', 'P']:
        for j in range(2, 15):
            cartas.append(Carta(naipe=i, valor_i=j))
    if seed != 0:
        random.seed(seed)
    random.shuffle(cartas)
    return cartas


class EstadoDoJogoParaJogador:
    # info jogo
    mesa: list[Carta]
    mao: list[Carta]

    # info jogadores
    my_id: int
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
                 my_id: int,
                 mesa: list[Carta],
                 mao: list[Carta],
                 aposta_jogadores: list[int],
                 aposta_total_jogadores: list[int],
                 banca_jogadores: list[int],
                 aposta_minima: int = None):
        self.mesa = mesa
        self.mao = mao
        self.aposta_jogadores = aposta_jogadores
        self.banca_jogadores = banca_jogadores
        self.aposta_total_jogadores = aposta_total_jogadores

        self.aposta_minima = 0
        self.precisa_aumentar = False
        for aposta in aposta_jogadores:
            if aposta > self.aposta_minima:
                if aposta_minima is None:
                    self.aposta_minima = aposta
                else:
                    self.aposta_minima = aposta_minima

                self.precisa_aumentar = True

        self.preco_de_ficar_no_jogo = aposta + max(self.aposta_total_jogadores)
        self.pote = sum(self.aposta_total_jogadores)
        self.soma_bancas = sum(self.banca_jogadores)

        self.my_id = my_id


class CalculadoraDeVitoria:
    ordem_cartas: list[str]
    ordem_jogadas: list[any]
    __count_groups_memo: dict

    def __init__(self):
        self.ordem_cartas = ['A', 'K', 'Q', 'J', '9',
                             '8', '7', '6', '5', '4', '3', '2']
        self.ordem_jogadas = [
            {
                'funcao_verificadora': self.straight_flush,
                'nome': "straight_flush",
            },
            {
                'funcao_verificadora': self.four_of_a_kind,
                'nome': "four_of_a_kind",
            },
            {
                'funcao_verificadora': self.full_house,
                'nome': "full_house",
            },
            {
                'funcao_verificadora': self.flush,
                'nome': "flush",
            },
            {
                'funcao_verificadora': self.straight,
                'nome': "straight",
            },
            {
                'funcao_verificadora': self.three_of_a_kind,
                'nome': "three_of_a_kind",
            },
            {
                'funcao_verificadora': self.two_pairs,
                'nome': "two_pairs",
            },
            {
                'funcao_verificadora': self.pair,
                'nome': "pair",
            },
            {
                'funcao_verificadora': self.high_card,
                'nome': "high_card",
            },
        ]
        self.__count_groups_memo = {}

    def is_mao_A_maior(self, maoA: list[Carta], maoB: list[Carta]):
        sumA = sum([carta.valor_i for carta in maoA])
        sumB = sum([carta.valor_i for carta in maoB])
        return sumA > sumB

    def get_buckets(self, maos: list[list[Carta]]):
        for mao_i in range(len(maos)):
            maos[mao_i] = sorted(
                maos[mao_i], key=lambda carta: carta.valor_i, reverse=True)

        buckets = [[] for _ in range(len(self.ordem_jogadas))]
        cartas = [[] for _ in range(len(self.ordem_jogadas))]
        for mao in maos:
            i = 0
            for jogada in self.ordem_jogadas:
                atende_jogada, c_cartas = jogada['funcao_verificadora'](mao)
                if atende_jogada:
                    buckets[i].append(maos.index(mao))
                    cartas[i].append(c_cartas.copy())
                i += 1

        return buckets, cartas

    def get_labeled_buckets(self, maos: list[list[Carta]]):
        buckets, cartas = self.get_buckets(maos)
        return [
            {
                'tipo': self.ordem_jogadas[i]['nome'],
                'cartas': cartas[i],
            } for i in range(len(buckets))
        ]
        return list(zip(self.ordem_jogadas, buckets, cartas))

    # recebe as maos (mesa + cartas do jogador) pra cada jogador
    # retorna uma lista de vencedores (pelo menos 1) e uma lista de maos vencedoras
    def get_maos_vencedoras(self,
                            maos: list[list[Carta]]) ->\
            tuple[list[int], list[dict]]:
        buckets, cartas = self.get_buckets(maos)

        i = 0
        for bucket in buckets:
            tipo_vitoria = self.ordem_jogadas[i]['nome']
            if len(bucket) > 0:
                if len(bucket) == 1:
                    return [bucket[0]], [{'mao': maos[bucket[0]], 'jogada': tipo_vitoria}]

                highest = 0
                valores_de_maos = []
                for bucket_i in bucket:
                    val = sum([c.valor_i for c in maos[bucket_i]])
                    highest = max(highest, val)
                    valores_de_maos.append(val)

                vencedores = []
                for i in range(len(maos)):
                    if valores_de_maos[i] == highest:
                        vencedores.append(bucket[i])

                return vencedores, [
                    {'mao': maos[item],
                     'jogada': tipo_vitoria,
                     } for item in vencedores]
            i += 1

        raise Exception("ERRO! Não há vencedores! Isso é impossível")

    def straight_flush(self, mao) -> tuple[bool, list[Carta]]:
        is_straight, cartas_straight = self.straight(mao)
        is_flush, cartas_flush = self.flush(mao)
        if is_straight and is_flush:
            return True, list(set(cartas_straight + cartas_flush))
        return False, None

    def four_of_a_kind(self, mao) -> tuple[bool, list[Carta]]:
        groups = self.__count_groups(mao)
        if len(groups) > 0 and len(groups[0]) > 3:
            return True, groups[0]
        return False, None

    def full_house(self, mao) -> tuple[bool, list[Carta]]:
        groups = self.__count_groups(mao)
        if len(groups) > 1 and len(groups[0]) > 2 and len(groups[1]) > 1:
            return True, groups[0] + groups[1]
        return False, None

    def flush(self, mao) -> tuple[bool, list[Carta]]:
        naipes = {'C': [], 'E': [], 'O': [], 'P': []}
        for carta in mao:
            naipe = carta.naipe
            naipes[naipe].append(carta)
        for naipe in naipes:
            if len(naipes[naipe]) >= 5:
                return True, naipes[naipe]
        return False, None

    def straight(self, mao) -> tuple[bool, list[Carta]]:
        last_valor = -1
        sequence_groups = []
        for carta in mao:
            if last_valor == -1:
                last_valor = carta.valor_i
                continue
            elif carta.valor_i == last_valor - 1:
                sequence_groups[-1:].append(carta)
            elif carta.valor_i < last_valor-1:
                last_valor = carta.valor_i
                sequence_groups.append([carta])
        seqs = sorted(sequence_groups, key=lambda seq: len(seq), reverse=True)
        if len(seqs) > 0 and len(seqs[0]) >= 5:
            return True, seqs[0]
        return False, None

    def three_of_a_kind(self, mao) -> tuple[bool, list[Carta]]:
        grupos = self.__count_groups(mao)
        if len(grupos) > 1 and len(grupos[0]) > 2:
            return True, grupos[0]
        return False, None

    def two_pairs(self, mao) -> tuple[bool, list[Carta]]:
        grupos = self.__count_groups(mao)
        if len(grupos) > 1 and len(grupos[0]) > 1 and len(grupos[1]) > 1:
            return True, grupos[0]+grupos[1]
        return False, None

    def pair(self, mao) -> tuple[bool, list[Carta]]:
        grupos = self.__count_groups(mao)
        if len(grupos) > 0 and len(grupos[0]) > 1:
            return True, grupos[0]
        return False, None

    def high_card(self, mao) -> tuple[bool, list[Carta]]:
        return True, [mao[0]]

    # retorna grupos de cartas, sendo cada grupo uma lista de cartas
    # de igual valor. a resposta será ordenada do maior grupo para o menor

    def __count_groups(self, mao) -> list[list[Carta]]:
        memo_nome = ''.join([c.__repr__() for c in mao])
        if memo_nome in self.__count_groups_memo:
            return self.__count_groups_memo[memo_nome]
        valor_last = -1
        grp_index = -1
        grupos = []
        for carta in mao:
            if carta.valor_i == valor_last:
                grupos[grp_index].append(carta)
            else:
                valor_last = carta.valor_i
                grp_index += 1
                grupos.append([carta])
        res = sorted(grupos, key=lambda grupo: len(grupo), reverse=True)
        self.__count_groups_memo[memo_nome] = res
        return res


class CalculadoraChanceVitoria():
    def __init__(self):
        pass

    # retorna valor entre [0.0, 1.0]
    def get_chance_de_vitoria(self, mao: list[Carta]) -> float:

        return 1.0


if __name__ == "__main__":
    calculador = CalculadoraDeVitoria()
    maos, _ = calculador.get_maos_vencedoras(
        [
            [
                Carta('CA'),
                Carta('CQ'),
                Carta('CJ'),
                Carta('C10'),
                Carta('C3'),
                Carta('C2'),
                Carta('C1'),
            ],
            [
                Carta('EA'),
                Carta('EQ'),
                Carta('EJ'),
                Carta('E10'),
                Carta('E3'),
                Carta('E2'),
                Carta('E1'),
            ]
        ]
    )
    print(f"vencedor(es): {maos}")

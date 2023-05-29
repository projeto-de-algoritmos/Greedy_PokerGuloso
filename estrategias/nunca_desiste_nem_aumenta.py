from common import *

CUTOFF = 0.7

# tenta calcular a maior vantagem possível que eu tenho e dá all-in caso
# seja maior que um certo valor


def fazer_jogada(estado: EstadoDoJogoParaJogador) -> tuple[bool, int]:
    # não desiste, nem aposta
    return False, min(estado.aposta_minima, estado.banca_jogadores[estado.my_id])


def test():
    my_id = 0
    mesa = [Carta('E4'), Carta('E5'), Carta('E6')]
    mao = [Carta('E7'), Carta('E8')]
    aposta_jogadores = [0, 0]
    aposta_total_jogadores = [0, 0]
    banca_jogadores = [10, 10]
    aposta_minima = 10

    estado = EstadoDoJogoParaJogador(
        my_id,
        mesa,
        mao,
        aposta_jogadores,
        aposta_total_jogadores,
        banca_jogadores,
        aposta_minima
    )
    desiste, aumenta = fazer_jogada(estado)
    if desiste:
        print("Desistiu")
    elif aumenta > 0:
        print(f"Aumentou {aumenta}")
    else:
        print("Passou")


if __name__ == "__main__":
    test()

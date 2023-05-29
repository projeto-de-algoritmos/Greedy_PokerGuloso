from common import *

CUTOFF = 0.7

# tenta calcular a maior vantagem possível que eu tenho e dá all-in caso
# seja maior que um certo valor


def fazer_jogada(estado: EstadoDoJogoParaJogador) -> tuple[bool, int]:
    mao_completa = estado.mesa + estado.mao
    buckets = CalculadoraDeVitoria(
    ).get_labeled_buckets([mao_completa])

    for bucket in buckets:
        if len(bucket['cartas']) > 0:

            # eu tenho um vantagem injusta?
            # ou seja, eu tenho algum carta que me faz ganhar com facilidade? tipo, tenho uma carta que faz uma trinca?
            cards_only_i_have = [
                card for card in estado.mao if card in bucket['cartas'][0]]
            # print(cards_only_i_have)
            max_aposta = estado.banca_jogadores[estado.my_id]

            if max_aposta < estado.aposta_minima*2:
                max_aposta = estado.aposta_minima

            # all-in
            if max_aposta < estado.banca_jogadores[estado.my_id]:
                max_aposta = estado.banca_jogadores[estado.my_id]
                break

            if len(cards_only_i_have) > 1:
                return False, max_aposta

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

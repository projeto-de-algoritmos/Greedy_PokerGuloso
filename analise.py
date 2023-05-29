import json


def estatisticas():
    jogos = get_last_log()

    cartas_vencedoras = []
    jogadas_vencedoras = []
    empates = []
    vitorias_A = 0
    vitorias_B = 0
    for jogo in jogos:
        if len(jogo["vencedor"]) == 1 and jogo["vencedor"][0] == "A":
            cartas_vencedoras += jogo["jogadorA"]
            jogadas_vencedoras.append(jogo["condicao_vitoria"][0]["jogada"])
            vitorias_A += 1
        elif len(jogo["vencedor"]) == 1 and jogo["vencedor"][0] == "B":
            cartas_vencedoras += jogo["jogadorB"]
            jogadas_vencedoras.append(jogo["condicao_vitoria"][0]["jogada"])
            vitorias_B += 1
        else:
            empates.append(jogo)

    cartas_vencedoras = [c[1:] for c in cartas_vencedoras]

    hist_cartas = build_histogram_from_list(cartas_vencedoras)
    hist_vitoria = build_histogram_from_list(jogadas_vencedoras)

    print(f"jogos: \t{len(jogos)} ")
    print(f"vitorias A: \t{vitorias_A} ")
    print(f"vitorias B: \t{vitorias_B} ")
    print(f"empates: \t{len(empates)} ")
    print_object(hist_cartas, "cartas vencedoras")
    print_object(hist_vitoria, "jogadas vencedoras")
    # print_object(empates, "empates")


def print_object(hist, nome):
    print(f"{nome}: {json.dumps(hist, indent=4)}")


def build_histogram_from_list(lista: list) -> dict:
    hist = {}
    for c in lista:
        if not hist.get(c):
            hist[c] = 1
        else:
            hist[c] += 1

    hist = {k: v for k, v in sorted(
        hist.items(), key=lambda item: item[1], reverse=True)}
    return hist


def get_last_log():
    jogos: dict = None

    with open('log_jogos.json', 'r') as f:
        jogos = json.loads(f.read())
    jogos = jogos["jogos"]
    return jogos


estatisticas()

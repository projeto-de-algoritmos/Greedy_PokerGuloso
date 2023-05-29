import json
import subprocess
import sys


def estatisticas_sobre_log(should_print=False):
    jogos = get_last_log()

    cartas_vencedoras = []
    jogadas_vencedoras = []
    empates = []
    vitorias_A = 0
    vitorias_B = 0
    falencias_A = 0
    falencias_B = 0
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

        for evento in jogo['eventos_partida']:
            if 'faliu' in evento:
                if 'A' in evento:
                    falencias_A += 1
                else:
                    falencias_B += 1

    cartas_vencedoras = [c[1:] for c in cartas_vencedoras]

    hist_cartas = build_histogram_from_list(cartas_vencedoras)
    hist_vitoria = build_histogram_from_list(jogadas_vencedoras)

    if should_print:
        print(f"jogos: \t{len(jogos)} ")
        print(f"vitorias A: \t{vitorias_A} ({vitorias_A/len(jogos)*100:.0f}%)")
        print(f"vitorias B: \t{vitorias_B} ({vitorias_B/len(jogos)*100:.0f}%)")
        print(
            f"empates: \t{len(empates)}  ({len(empates)/len(jogos)*100:.0f}%)")
        print(
            f"falencias A: \t{falencias_A} ({falencias_A/len(jogos)*100:.0f}%)")
        print(
            f"falencias B: \t{falencias_B} ({falencias_B/len(jogos)*100:.0f}%)")
        # print_object(hist_cartas, "cartas vencedoras")
        # print_object(hist_vitoria, "jogadas vencedoras")
        # print_object(empates, "empates")
    else:
        return {
            "jogos": len(jogos),
            "vitorias A": vitorias_A,
            "vitorias B": vitorias_B,
            "empates": len(empates),
            "falencias A": falencias_A,
            "falencias B": falencias_B,
            "cartas vencedoras": hist_cartas,
            "jogadas vencedoras": hist_vitoria,
            "empates": empates,
        }


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


def compara_todas_as_estrategias(should_print=False):

    scripts = subprocess.check_output(["ls", "estrategias/"]).decode("utf-8")
    scripts = scripts.strip().split("\n")

    print("os seguintes scripts foram encontrados e serao comparados:")
    print(*[f"\t- {script}" for script in scripts], sep="\n", end="\n\n")

    for scriptA in scripts:
        index = scripts.index(scriptA)
        for scriptB in scripts[index:]:
            print(f"comparando A='{scriptA}' com B='{scriptB}'")
            subprocess.call(
                ["cp", f"estrategias/{scriptA}", "scriptA.py"])
            subprocess.call(
                ["cp", f"estrategias/{scriptB}", "scriptB.py"])
            subprocess.run(["python3", "sim.py", "-s", "-iter=3000"])
            estatisticas_sobre_log(should_print=should_print)
            print("\n\n")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'get_estatisticas':
        subprocess.run(["python3", "sim.py", "-s", "-iter=3000"])
        estatisticas_sobre_log(should_print=True)
    else:
        compara_todas_as_estrategias(should_print=True)

import json
import copy


class Arma():

    def __init__(self, nome: str, contrataca: list[str]):
        self.nome = nome
        self.contrataca = contrataca

    def __repr__(self):
        return f"Arma({self.nome}, {self.contrataca})"

    def ganha_de(self, arma: "Arma") -> bool:
        return arma.nome in self.contrataca

    def perde_de(self, arma: "Arma") -> bool:
        return self.nome in arma.contrataca


class GeradorDeArmas():

    def gerar_inicial(self) -> list[Arma]:
        raise NotImplementedError

    def gerar_continuo(self, cenario: 'Cenario') -> list[Arma]:
        raise NotImplementedError


class GeradorDeArmasJson(GeradorDeArmas):

    inicial: list[str]

    def __init__(self, file: str) -> None:
        super().__init__()
        self.inicial = []
        with open(file, "r") as f:
            fjson = json.loads(f.read())
            self.inicial = fjson["inicial"]

    def gerar_inicial(self) -> list[Arma]:
        return self.inicial

    def gerar_continuo(cenario: 'Cenario') -> list[Arma]:
        return []


class Cenario():

    last_arma_index: int
    armas_defesa: list[Arma]
    armas_ataque: list[Arma]

    def __init__(self, regras):
        self.last_arma_index = 0

        self.regras = regras
        armas_ataque_str: list[str] = regras.gerador_armas_inimigas.gerar_inicial(
        )
        self.armas_ataque = [copy.copy(regras.armas_index[arma])
                             for arma in armas_ataque_str]

        armas_defesa_str: list[str] = regras.gerador_armas_aliadas.gerar_inicial(
        )
        self.armas_defesa = [copy.copy(regras.armas_index[arma])
                             for arma in armas_defesa_str]

    def is_condicao_de_derrota(self) -> bool:
        return True


class Simulacao():

    def __init__(self):
        pass

    def simular(self, cenario):
        pass


class RegrasDoJogo():
    armas_index: dict[str, Arma]
    gerador_armas_inimigas: GeradorDeArmas
    gerador_armas_aliadas: GeradorDeArmas


class RegrasDoJogo_Versao1(RegrasDoJogo):

    def __init__(self):
        with open("armas.json") as f:
            armas = json.loads(f.read())["armas"]
            armas = [Arma(arma["nome"], arma["contrataca"])
                     for arma in armas]
            self.armas_index = {arma.nome: arma for arma in armas}

        self.gerador_armas_inimigas = GeradorDeArmasJson(
            "armas_inimigas.json")
        self.gerador_armas_aliadas = GeradorDeArmasJson("armas_aliadas.json")


def main():
    regras = RegrasDoJogo_Versao1()

    cenario = Cenario(regras)

    simulacao = Simulacao()

    while not cenario.is_condicao_de_derrota():
        simulacao.simular(cenario)


if __name__ == "__main__":
    main()

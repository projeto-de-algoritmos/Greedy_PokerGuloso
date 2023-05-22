import json


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

    def gerar_inicial() -> list[Arma]:
        raise NotImplementedError

    def gerar_continuo(cenario: 'Cenario') -> list[Arma]:
        raise NotImplementedError


class GeradorDeArmasJson(GeradorDeArmas):

    inicial: list[str]

    def __init__(self, file: str) -> None:
        super().__init__()
        self.inicial = []
        with open(file, "r") as f:
            self.inicial = json.dumps(f.read())["inicial"]

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
        self.armas_ataque = [Arma(arma, regras.arma)
                             for arma in armas_ataque_str]

        armas_defesa_str: list[str] = regras.gerador_armas_aliadas.gerar_inicial(
        )

    def is_condicao_de_derrota(self) -> bool:
        pass


class Simulacao():

    def __init__(self):
        pass

    def simular(self, cenario):
        pass


class RegrasDoJogo():
    armas_index: str[str, Arma]
    gerador_armas_inimigas: GeradorDeArmas
    gerador_armas_aliadas: GeradorDeArmas

    def __init__(self):
        pass


class RegrasDoJogo_Versao1(RegrasDoJogo):

    def __init__(self):
        with open("armas.json") as f:
            armas = json.loads(f.read())
            armas = [Arma(arma["nome"], arma["contrataca"])
                     for arma in self.armas]
            self.armas_index = {arma.nome: arma for arma in armas}

        self.gerador_armas_inimigas = GeradorDeArmasJson(
            "armas_inimigas.json").gerar_inicial()
        self.gerador_armas_aliadas = GeradorDeArmasJson("armas_aliadas.json")


def main():
    regras = RegrasDoJogo_Versao1()

    cenario = Cenario(regras)

    simulacao = Simulacao()

    while not cenario.is_condicao_de_derrota():
        simulacao.simular(cenario)


if __name__ == "__main__":
    main()

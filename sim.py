import json


class Arma():

    def __init__(self, nome: str, contrataca: list[str]):
        self.nome = nome
        self.contrataca = contrataca

    def __repr__(self):
        return f"Arma({self.nome}, {self.contrataca})"


class Cenario():

    armas_defesa: list[Arma]
    armas_ataque: list[Arma]

    def __init__(self, regras, armas_defesa=[], armas_ataque=[]):
        self.regras = regras
        self.armas_defesa = armas_defesa
        self.armas_ataque = armas_ataque

    def is_condicao_de_derrota(self) -> bool:
        pass


# Transformação de cenário
class Ataque():

    def aplicar(self, cenario: Cenario) -> Cenario:
        pass

    def pode_aplicar(self, cenario: Cenario) -> bool:
        # Transformação de cenário
        pass


# Transformação de cenário
class Contrataque():

    def aplicar(self, cenario: Cenario) -> Cenario:
        pass

    def pode_aplicar(self, cenario: Cenario) -> bool:
        pass


class GeradorDeAtaques():

    def __init__(self):
        pass

    def gerar_ataques(cenario: Cenario) -> list[Ataque]:
        raise NotImplementedError


class GeradorDeContrataques():

    def gerar_defesas(cenario: Cenario) -> list[Contrataque]:
        raise NotImplementedError


class Simulacao():
    pass


class RegrasDoJogo_Versao1():
    armas = [
        Arma("Lança míssel terrestre", [
             "Tanque, Antiaéreo, Destruidor, Couraçador"]),
        Arma("Lança míssel aéreo", ["Helicóptero", "Caça"]),
        Arma("Soldado", ["Soldado", "Antiaéreo"]),
        Arma("Tanque", ["Soldado", "Tanque", "Antiaéreo"]),
        Arma("Antiaéreo", ["Caça, Bombardeiro", "Helicóptero"]),
        Arma("Caça", ["Caça", "Bombardeiro"]),
        Arma("Bombardeiro", ["Tanque, Destruidor, Couraçador"]),
        Arma("Helicóptero", ["Soldado, Tanque"]),
        Arma("Destruidor", ["Submarino"]),
        Arma("Submarino", ["Destruidor, Jato"]),
        Arma("Couraçador", ["Destruidor"]),
    ]

    def __init__(self):
        return self


def main():
    regras = RegrasDoJogo_Versao1()

    gerador_de_ataques = GeradorDeAtaques(regras)
    gerador_de_contrataques = GeradorDeContrataques(regras)

    cenario = Cenario(
        regras,
        armas_ataque=[],
        armas_defesa=[],
    )


if __name__ == "__main__":
    main()

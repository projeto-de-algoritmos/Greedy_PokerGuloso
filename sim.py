import json


class Cenario():
    pass


# Transformação de cenário
class Ataque():

    def aplicar(self, cenario: Cenario) -> Cenario:

    def pode_aplicar(self, cenario: Cenario) -> bool:
        # Transformação de cenário


class Contrataque():

    def aplicar(self, cenario: Cenario) -> Cenario:
    def pode_aplicar(self, cenario: Cenario) -> bool:


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


def main():
    gerador_de_ataques =


if __name__ == "__main__":
    main()

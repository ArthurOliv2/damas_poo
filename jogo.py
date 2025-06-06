from tabuleiro import Tabuleiro

class jogo:
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.turno = "branco"
        self.selecionada = None

    def mudar_turno(self):
        self.turno = "preto" if self.turno == "branco" else "branco"
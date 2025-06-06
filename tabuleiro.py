from pecas import Peca

class Tabuleiro:
    def __init__(self):
        self.tabuleiro = self.criar_tabuleiro()

    def criar_tabuleiro(self):
        tab = [[None for _ in range(8)] for _ in range(8)]
        for linha in range(8):
            for col in range(8):
                if (linha + col) % 2 != 0:
                    tab[linha][col] = Peca("preto", linha, col)
                elif linha > 4:
                    tab[linha][col] = Peca("branco", linha, col)
        return tab
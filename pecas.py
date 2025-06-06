class Peca:
    def __init__(self, cor, linha, coluna):
        self.cor = cor
        self.linha = linha
        self.coluna = coluna
        self.dama = False
    
    def virar_dama(self):
        self.dama = True
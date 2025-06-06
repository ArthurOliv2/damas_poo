from interface import Interface
from jogo import Jogo

if __name__ == "__main__":
    jogo = Jogo()
    interface = Interface(jogo)
    interface.iniciar()
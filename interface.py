import tkinter as tk

class Interface:
    def __init__(self, jogo):
        self.jogo = jogo
        self.root = tk.Tk()
        self.root.title = ("Jogo de Damas")
        self.canvas = tk.Canvas(self.root, width=640, height=640)
        self.canvas.pack() 
        self.canvas.bind("<button-1>", self.clique) 
        self.desenhar_tabuleiro() 

    def desenhar_tabuleiro(self):
        self.canvas.delete("all")
        for linha in range(8):
            for col in range(8):
                x1 = col * 80
                y1 = linha * 80
                x2 = x1 + 80
                y2 = y1 + 80
                cor = "white" if (linha + col) % 2 == 0 else "gray"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=cor)

    def clique(self, event):
        col = event.x // 80
        linha = event.y // 80
        print(f"Clicado em: ({linha}, {col})")

    def iniciar(self):
        self.root.mainloop()

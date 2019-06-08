from tkinter import Tk, Frame, Label, TOP
class App:
    def __init__(self, master, anime):
        self.anime = anime
        self.root = master
        self.root.geometry("300x400")
        self.root.title("Status")

        self.frame1 = Frame(self.root)
        self.frame1.pack(side=TOP)

        self.frame2 = Frame(self.root)
        self.frame2.pack()


    def cadastrar(self):
        self.msg = Label(self.frame2, text="{} Status:".format(self.anime))
        self.msg["font"] = ("Arial", "14")
        self.msg.pack()

        self.msg2 = Label(self.frame2, text="Não saiu")
        self.msg2["font"] = ("Arial", "14", "bold")
        self.msg2.pack()

    def clock(self):
        self.root.after(4000, self.clock)
        if self.msg2["text"] == "Não saiu":
            with open("log.txt", "r+") as file:
                linhas = file.readlines()
            print(linhas)
            for linha in linhas:    
                if linha.split(":")[0] == self.anime:
                    if "ON" in linha.split(":")[1].strip("\n"):
                        self.msg2["text"] = "Saiu"

root = Tk()
app = App(root, anime="Kimetsu no yaiba")
app.cadastrar()
app2 = App(root, anime="One punch man")
app2.cadastrar()
app3 = App(root, anime="Senko-san")
app3.cadastrar()
app4 = App(root, anime="Sword Art Online")
app4.cadastrar()
app.clock();app2.clock();app3.clock();app4.clock()
root.mainloop()
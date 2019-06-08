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
                self.linhas = file.readlines()
            print(self.linhas)
            for self.linha in self.linhas:    
                if self.linha.split(":")[0] == self.anime:
                    if "ON" in self.linha.split(":")[1].strip("\n"):
                        self.msg2["text"] = "Saiu"
        else:
            with open("log.txt", "r+") as file:
                self.linhas = file.readlines()
            for self.linha in self.linhas:    
                if self.linha.split(":")[0] == self.anime:
                    if "OFF" in self.linha.split(":")[1].strip("\n"):
                        self.msg2["text"] = "Não saiu"

root = Tk()
app_kny = App(root, anime="Kimetsu no yaiba")
app_kny.cadastrar()
app_opm = App(root, anime="One punch man")
app_opm.cadastrar()
app_sks = App(root, anime="Senko-san")
app_sks.cadastrar()
app_sao = App(root, anime="Sword Art Online")
app_sao.cadastrar()
app_kny.clock();app_opm.clock();app_sks.clock();app_sao.clock()
root.mainloop()
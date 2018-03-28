from Tkinter import *

class Application(Frame):
    
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.button1 = Button(self, text = "Launch WoW")
        self.button1.grid()
        
        self.button2 = Button(self, text = "Close WoW")
        self.button2.grid()
root = Tk()
root.title("WoW Timer")
root.geometry("200x100")#size of gui window

app = Application(root)

#initialize
root.mainloop()

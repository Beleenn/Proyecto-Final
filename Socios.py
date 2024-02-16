import tkinter as tk 
# -------------ESTRUCTURA DE VENTANA --------------- 
window= tk.Tk()
window.title("Futbool Club")
window.geometry("600x400")
icon= tk.PhotoImage(file="jugador.png")
window.iconphoto(True, icon)



window.mainloop()

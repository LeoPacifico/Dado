#construir um dado virtual   ( numeros aleatórios entre 1 a 6)

import tkinter as tk
import random as rd

#definir as funções

def jogarDado():
    numeroSorteado=rd.randint(1,6)
    return numeroSorteado
def atualizar():
    aux=jogarDado()
    lbValorDoNumeroSorteado.config(text=aux)


#criar a tela

tela=tk.Tk()
tela.title("Dado")
tela.resizable(width=False,height=False)

imgDado=tk.PhotoImage(file="dado.png")

#criar label imagem (receber a imagem do dado)
img=tk.Label(tela,image=imgDado)
img.grid(row=0,column=0,rowspan=3,padx=10,pady=10)

#criar o label "Número sorteado"
lbNumeroSorteado=tk.Label(tela,text="Número Sorteado",font="Arial, 30", fg="blue",justify="center")

lbNumeroSorteado.grid(row=0,column=1,padx=10,pady=10)

#criar label do número sorteado
lbValorDoNumeroSorteado=tk.Label(tela,text="---",font="Arial, 50",)
lbValorDoNumeroSorteado.grid(row=1,column=1,pady=10,padx=10,sticky="we")

#criar o botão jogar
btJogar=tk.Button(tela,text="Jogar",font="Arial, 30",bg="#FFF100",relief="raised",
                  command=atualizar)
btJogar.grid(row=2,column=1,sticky="we",padx=10,pady=10)



tela.mainloop()




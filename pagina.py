from tkinter import *

# widgets = guia elementos: botoes, caixas de testo, labels, imagens
# windows = a imagem em si onde fica os widgets 

window = Tk()# intancada a instancia do window


window.geometry("1250x800") # tamanho da imagem

window.title("Hello Word tkinter")

#icon = PhotoImage(file='local_da_imagen') fazer o icone
#window.iconphoto(True,icon) fazer realmente aparecer o icone

window.config(background="blue")



###

photo = PhotoImage(file='c\\users\\coloqueumaimagen')


label = Label(window, 
        text="Hello Word Tkinter", 
        font=('Arial', 40, 'bold', 'italic'), 
        fg='white', 
        bg='black',
        relief=RAISED,
        bd=10,
        padx=20,
        pady=20,
        image=photo,
        compound='bottom'
        )
#label2 = Label(window, photo)


label.pack()

#label.place(x = 0,y = 20)#x a largura y altura



window.mainloop()# faz aparecer a imagem na tela do pc, lista os events 


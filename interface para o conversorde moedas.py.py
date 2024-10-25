def conversor():
    d = int(input('quanto dinheiro você tem na carteira:R$ '))
    print('com',d,'você tem em dolar US$',d/5)

    d ['text'] = 'texto'


from tkinter import *
janela = Tk()
janela.title('conversor de real para dollar')
janela.geometry('200x200')



botão = Button(janela,text ='converta',command = conversor)
botão.grid(column=4,row=4,padx=10,pady=10)

texto = Label(janela,text ='qual valor você quer converter?:R$ ')
texto.grid(column=4,row=2,padx=10,pady=10)

texto = Entry(janela)
texto.grid(column=4,row=3,padx=10,pady=10)


janela.mainloop()
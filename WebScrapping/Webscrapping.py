import requests
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import webbrowser


def web_scrapping():
    """"
    Esta funcion lee el url de una determinada pagina, y crea un objeto que contendra el codigo html
    de nuestra pagina. (Con ayuda de la libreria BeatifulSoup)
    :return None
    """
    while True:
        try:
            url = "https://python-para-impacientes.blogspot.com/2017/02/instalar-python-paso-paso.html"
            page = urlopen(url)
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")

            texto = soup.get_text()

            texto_a_lista = [cadena for cadena in texto.split('\n') if cadena != '']
            cont = 1
            textos_fil = []
            for cadena in texto_a_lista:
                if (str(cont) + ". ") in cadena:
                    cont += 1
                    textos_fil.append(cadena)

            textos = '\n'.join(textos_fil)

            valor = 1
            imagenes = soup.find_all('img', border="0", width="320")
            imagenes = (imagenes[:len(imagenes) - 1])
            for im in imagenes:
                #print(im['src'])
                nombre = valor
                nombre_completo = str(nombre) + ".png"
                urllib.request.urlretrieve((im['src']), nombre_completo)
                valor += 1
            return textos_fil
            break
        except ConnectionResetError:
            print('TimeOut')

def crearpantallaWS():
    """
    Esta funcion crea la pantalla de nuestro programa, en la cual colocaremos la informacion.
    (Esto con ayuda de la libreria Tkinter)
    :return None
    """
    pantalla = tk.Tk()
    pantalla.title('Web Scrapping')
    pantalla.resizable(False, False)
    pantalla.geometry('1280x700')
    pantalla.config(bg='blue')
    pantalla.iconbitmap("icono.ico")

    def cambiar_frame(frame_dest, numero):
        """
        Tiene la funcion de destruir el frame que se esta utilizando y genera uno nuevo.
        :param string frame_dest: representa el frame que vamos a destruir
        :param string numero: representa el numero de la pantalla que nos encontramos
        :param int avance: registra el avande del usuario en el area de aprendizaje de python
        No retorna algun valor
        """
        frame_dest.destroy()
        if numero == 2:
            Frame_2()
        elif numero==3:
            Frame_3()
        elif numero==4:
            Frame_4()
        elif numero==5:
            Frame_5()
        elif numero==6:
            Frame_6()
        elif numero==7:
            Frame_7()
        elif numero==8:
            Frame_8()
        elif numero==9:
            Frame_9()
        elif numero==10:
            Frame_10()
        else:
            exit()

    def pythonlink():
        """
        Esta funcion abre un enlace a determinada pagina. Usa la libreria webbrowser.
        :return None
        """
        new=2
        url = "https://www.python.org/"
        webbrowser.open(url,new=new)
    def enlace0():
        """
        Esta funcion abre un enlace a determinada pagina. Usa la libreria webbrowser.
        :return None
        """
        new=2
        url = "https://www.w3schools.com/python/"
        webbrowser.open(url,new=new)
    def enlace1():
        """
        Esta funcion abre un enlace a determinada pagina. Usa la libreria webbrowser.
        :return None
        """
        new=2
        url = "https://docs.python.org/es/3/tutorial/index.html"
        webbrowser.open(url,new=new)
    def enlace2():
        """
        Esta funcion abre un enlace a determinada pagina. Usa la libreria webbrowser.
        :return None
        """
        new=2
        url = "https://realpython.com/"
        webbrowser.open(url,new=new)


    Frame_1 = Canvas(pantalla, width="1280", height="700")
    Frame_1.pack(expand=True, fill="both")
    Frame_1.config(bg='#87CEFA')
    Frame_1.config(width='1280', height='700')
    Frame_1.config(bd=20)
    Frame_1.config(relief="groove")
    Texto_Titulo = Label(Frame_1, text=' Bienvenido a', bg='#87CEFA', fg='white', font=('Comic Sans', 40)).place(relx=0.5, y=150, anchor=CENTER)
    Texto_imprimir = Label(Frame_1, text='Como instalar Python ', bg='#87CEFA', fg='white',font=('Comic Sans', 50, "bold")).place(relx=0.5, y=300, anchor=CENTER)
    img = ImageTk.PhotoImage(Image.open("pythonbutton.png").resize((280,280)))
    Frame_1.background = img
    bg = Frame_1.create_image(930, 360, anchor=tk.NW, image=img)

    def Frame_2():
        """
        Esta funcion crea el segundo Frame de nuestro programa, esto con ayuda de la libreria Tkinter.
        :return None
        """
        Frame_2 = Canvas(pantalla, width="1280", height="700")
        Frame_2.pack()
        Frame_2.config(bg='#87CEFA')
        Frame_2.config(width='1280', height='700')
        Frame_2.config(bd=20)
        Frame_2.config(relief="groove")
        t = textos_fil[0]
        t = t.split()
        j = 0
        t2 = ''
        for i in range(len(t)):
            if i % 12 == 0:
                t2 += (' '.join(t[j:i]) + '\n')
                j = i
            elif i == len(t) - 1:
                t2 += ' '.join(t[j:])
        Text_titulo_frame_2 = Label(Frame_2, text='Paso 1', bg='#87CEFA', fg='white',font=('Comic Sans', 35, "bold")).place(relx=0.5, y=65, anchor=CENTER)
        Text0_frame_2 = Label(Frame_2, text=t2, bg='#87CEFA', fg='white', font=('Comic Sans', 25)).place(relx=0.5,y=165,anchor=CENTER)
        img = ImageTk.PhotoImage(Image.open("1.png"))
        Frame_2.background = img
        bg = Frame_2.create_image(315, 300, anchor=tk.NW, image=img)
        boton1 = tk.Button(Frame_2, text="Siguiente", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_2,3)).place(x=1090, y=580)
        boton2 = tk.Button(Frame_2, text="Presiona para\n obtener el enlace", font=("Comic Sans", 20), height=5, width=20, bg='#ffd748', fg='white',command=pythonlink).place(x=680, y=310)
    def Frame_3():
        """
        Esta funcion crea el tercer Frame de nuestro programa, esto con ayuda de la libreria Tkinter.
        :return None
        """
        Frame_3 = Canvas(pantalla, width="1280", height="700")
        Frame_3.pack()
        Frame_3.config(bg='#87CEFA')
        Frame_3.config(width='1280', height='700')
        Frame_3.config(bd=20)
        Frame_3.config(relief="groove")
        t = textos_fil[1]
        t = t.split()
        j = 0
        t2 = ''
        for i in range(len(t)):
            if i % 10 == 0:
                t2 += (' '.join(t[j:i]) + '\n')
                j = i
            elif i == len(t) - 1:
                t2 += ' '.join(t[j:])
        Text_titulo_frame_3 = Label(Frame_3, text='Paso 2', bg='#87CEFA', fg='white',font=('Comic Sans', 35, "bold")).place(relx=0.5, y=65, anchor=CENTER)
        Text0_frame_3 = Label(Frame_3, text=t2, bg='#87CEFA', fg='white', font=('Comic Sans', 25)).place(relx=0.5,y=180,anchor=CENTER)
        img = ImageTk.PhotoImage(Image.open("2.png"))
        Frame_3.background = img
        bg = Frame_3.create_image(480, 325, anchor=tk.NW, image=img)
        botonaretroceso = tk.Button(Frame_3, text="Atras", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_3, 2)).place(x=60, y=580)
        botonavance = tk.Button(Frame_3, text="Siguiente", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_3,4)).place(x=1090, y=580)

    def Frame_4():
        """
        Esta funcion crea el cuarto Frame de nuestro programa, esto con ayuda de la libreria Tkinter.
        :return None
        """
        Frame_4 = Canvas(pantalla, width="1280", height="700")
        Frame_4.pack()
        Frame_4.config(bg='#87CEFA')
        Frame_4.config(width='1280', height='700')
        Frame_4.config(bd=20)
        Frame_4.config(relief="groove")
        t = textos_fil[2]
        t = t.split()
        j = 0
        t2 = ''
        for i in range(len(t)):
            if i % 9 == 0:
                t2 += (' '.join(t[j:i]) + '\n')
                j = i
            elif i == len(t) - 1:
                t2 += ' '.join(t[j:])
        Text_titulo_frame_4 = Label(Frame_4, text='Paso 3', bg='#87CEFA', fg='white',font=('Comic Sans', 35, "bold")).place(relx=0.5, y=65, anchor=CENTER)
        Text0_frame_4 = Label(Frame_4, text=t2, bg='#87CEFA', fg='white', font=('Comic Sans', 25)).place(relx=0.5,y=200,anchor=CENTER)
        img = ImageTk.PhotoImage(Image.open("3.png"))
        Frame_4.background = img
        bg = Frame_4.create_image(480, 370, anchor=tk.NW, image=img)
        botonaretroceso = tk.Button(Frame_4, text="Atras", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_4, 3)).place(x=60, y=580)
        boton1 = tk.Button(Frame_4, text="Siguiente", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_4,5)).place(x=1090, y=580)

    def Frame_5():
        """
        Esta funcion crea el quinto Frame de nuestro programa, esto con ayuda de la libreria Tkinter.
        :return None
        """
        Frame_5 = Canvas(pantalla, width="1280", height="700")
        Frame_5.pack()
        Frame_5.config(bg='#87CEFA')
        Frame_5.config(width='1280', height='700')
        Frame_5.config(bd=20)
        Frame_5.config(relief="groove")
        t = textos_fil[3]
        t = t.split()
        j = 0
        t2 = ''
        for i in range(len(t)):
            if i % 9 == 0:
                t2 += (' '.join(t[j:i]) + '\n')
                j = i
            elif i == len(t) - 1:
                t2 += ' '.join(t[j:])
        Text_titulo_frame_5 = Label(Frame_5, text='Paso 4', bg='#87CEFA', fg='white',font=('Comic Sans', 35, "bold")).place(relx=0.5, y=65, anchor=CENTER)
        Text0_frame_5 = Label(Frame_5, text=t2, bg='#87CEFA', fg='white', font=('Comic Sans', 25)).place(relx=0.5,y=185,anchor=CENTER)
        img = ImageTk.PhotoImage(Image.open("4.png"))
        Frame_5.background = img
        bg = Frame_5.create_image(480, 340, anchor=tk.NW, image=img)
        botonaretroceso = tk.Button(Frame_5, text="Atras", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_5, 4)).place(x=60, y=580)
        boton1 = tk.Button(Frame_5, text="Siguiente", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_5,6)).place(x=1090, y=580)

    def Frame_6():
        """
        Esta funcion crea el sexto Frame de nuestro programa, esto con ayuda de la libreria Tkinter.
        :return None
        """
        Frame_6 = Canvas(pantalla, width="1280", height="700")
        Frame_6.pack()
        Frame_6.config(bg='#87CEFA')
        Frame_6.config(width='1280', height='700')
        Frame_6.config(bd=20)
        Frame_6.config(relief="groove")
        t = textos_fil[4]
        t = t.split()
        j = 0
        t2 = ''
        for i in range(len(t)):
            if i % 9 == 0:
                t2 += (' '.join(t[j:i]) + '\n')
                j = i
            elif i == len(t) - 1:
                t2 += ' '.join(t[j:])
        Text_titulo_frame_6 = Label(Frame_6, text='Paso 5', bg='#87CEFA', fg='white',font=('Comic Sans', 35, "bold")).place(relx=0.5, y=65, anchor=CENTER)
        Text0_frame_6 = Label(Frame_6, text=t2, bg='#87CEFA', fg='white', font=('Comic Sans', 25)).place(relx=0.5,y=203,anchor=CENTER)
        img = ImageTk.PhotoImage(Image.open("5.png"))
        Frame_6.background = img
        bg = Frame_6.create_image(480, 375, anchor=tk.NW, image=img)
        botonaretroceso = tk.Button(Frame_6, text="Atras", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_6, 5)).place(x=60, y=580)
        boton1 = tk.Button(Frame_6, text="Siguiente", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_6,7)).place(x=1090, y=580)

    def Frame_7():
        """
        Esta funcion crea el septimo Frame de nuestro programa, esto con ayuda de la libreria Tkinter.
        :return None
        """
        Frame_7 = Canvas(pantalla, width="1280", height="700")
        Frame_7.pack()
        Frame_7.config(bg='#87CEFA')
        Frame_7.config(width='1280', height='700')
        Frame_7.config(bd=20)
        Frame_7.config(relief="groove")
        t = textos_fil[5]
        t = t.split()
        j = 0
        t2 = ''
        for i in range(len(t)):
            if i % 9 == 0:
                t2 += (' '.join(t[j:i]) + '\n')
                j = i
            elif i == len(t) - 1:
                t2 += ' '.join(t[j:])
        Text_titulo_frame_7 = Label(Frame_7, text='Paso 6', bg='#87CEFA', fg='white',font=('Comic Sans', 35, "bold")).place(relx=0.5, y=65, anchor=CENTER)
        Text0_frame_7 = Label(Frame_7, text=t2, bg='#87CEFA', fg='white', font=('Comic Sans', 25)).place(relx=0.5,y=180,anchor=CENTER)
        img = ImageTk.PhotoImage(Image.open("6.png"))
        Frame_7.background = img
        bg = Frame_7.create_image(480, 325, anchor=tk.NW, image=img)
        botonaretroceso = tk.Button(Frame_7, text="Atras", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_7, 6)).place(x=60, y=580)
        boton1 = tk.Button(Frame_7, text="Siguiente", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_7,8)).place(x=1090, y=580)

    def Frame_8():
        """
        Esta funcion crea el octavo Frame de nuestro programa, esto con ayuda de la libreria Tkinter.
        :return None
        """
        Frame_8 = Canvas(pantalla, width="1280", height="700")
        Frame_8.pack()
        Frame_8.config(bg='#87CEFA')
        Frame_8.config(width='1280', height='700')
        Frame_8.config(bd=20)
        Frame_8.config(relief="groove")
        t = textos_fil[6]
        t = t.split()
        j = 0
        t2 = ''
        for i in range(len(t)):
            if i % 9 == 0:
                t2 += (' '.join(t[j:i]) + '\n')
                j = i
            elif i == len(t) - 1:
                t2 += ' '.join(t[j:])
        Text_titulo_frame_8 = Label(Frame_8, text='Paso 7', bg='#87CEFA', fg='white',font=('Comic Sans', 35, "bold")).place(relx=0.5, y=65, anchor=CENTER)
        Text0_frame_8 = Label(Frame_8, text=t2, bg='#87CEFA', fg='white', font=('Comic Sans', 25)).place(relx=0.5,y=225,anchor=CENTER)
        img = ImageTk.PhotoImage(Image.open("7.png"))
        Frame_8.background = img
        bg = Frame_8.create_image(480, 405, anchor=tk.NW, image=img)
        botonaretroceso = tk.Button(Frame_8, text="Atras", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_8, 7)).place(x=60, y=580)
        boton1 = tk.Button(Frame_8, text="Siguiente", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_8,9)).place(x=1090, y=580)

    def Frame_9():
        """
        Esta funcion crea el noveno Frame de nuestro programa, esto con ayuda de la libreria Tkinter.
        :return None
        """
        Frame_9 = Canvas(pantalla, width="1280", height="700")
        Frame_9.pack()
        Frame_9.config(bg='#87CEFA')
        Frame_9.config(width='1280', height='700')
        Frame_9.config(bd=20)
        Frame_9.config(relief="groove")
        t = textos_fil[7]
        t = t.split()
        j = 0
        t2 = ''
        for i in range(len(t)):
            if i % 9 == 0:
                t2 += (' '.join(t[j:i]) + '\n')
                j = i
            elif i == len(t) - 1:
                t2 += ' '.join(t[j:])
        Text_titulo_frame_9 = Label(Frame_9, text='Paso 8', bg='#87CEFA', fg='white',font=('Comic Sans', 35, "bold")).place(relx=0.5, y=65, anchor=CENTER)
        Text0_frame_9 = Label(Frame_9, text=t2, bg='#87CEFA', fg='white', font=('Comic Sans', 25)).place(relx=0.5,y=225,anchor=CENTER)
        img = ImageTk.PhotoImage(Image.open("8.png"))
        Frame_9.background = img
        bg = Frame_9.create_image(480, 405, anchor=tk.NW, image=img)
        botonaretroceso = tk.Button(Frame_9, text="Atras", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_9, 8)).place(x=60, y=580)
        boton1 = tk.Button(Frame_9, text="Siguiente", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_9,10)).place(x=1090, y=580)

    def Frame_10():
        """
        Esta funcion crea el decimo Frame de nuestro programa, esto con ayuda de la libreria Tkinter.
        :return None
        """
        Frame_10 = Canvas(pantalla, width="1280", height="700")
        Frame_10.pack()
        Frame_10.config(bg='#87CEFA')
        Frame_10.config(width='1280', height='700')
        Frame_10.config(bd=20)
        Frame_10.config(relief="groove")
        Text_titulo_frame_10 = Label(Frame_10, text='Enlaces de interes :D', bg='#87CEFA', fg='white',font=('Comic Sans', 35, "bold")).place(relx=0.5, y=65, anchor=CENTER)
        botonaretroceso = tk.Button(Frame_10, text="Atras", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_10, 9)).place(x=60, y=580)
        boton1 = tk.Button(Frame_10, text="Fin", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_10,11)).place(x=1090, y=580)

        boton2 = tk.Button(Frame_10, text="Tutoriales y metodos", font=("Comic Sans", 20), height=4, width=30,bg='#AB7CFF', fg='white', command=enlace0).place(relx=0.5, y=195, anchor=CENTER)
        boton3 = tk.Button(Frame_10, text="Documentancion", font=("Comic Sans", 20), height=4, width=30,bg='#6F7EE3', fg='white', command=enlace1).place(relx=0.5, y=372, anchor=CENTER)
        boton4 = tk.Button(Frame_10, text="De todo un poco", font=("Comic Sans", 20), height=4, width=30,bg='#6FE3D6', fg='white', command=enlace2).place(relx=0.5, y=550, anchor=CENTER)
        img = ImageTk.PhotoImage(Image.open("pythonbutton2.png").resize((280,280)))
        Frame_10.background = img
        bg = Frame_10.create_image(930, 210, anchor=tk.NW, image=img)
    boton0 = tk.Button(Frame_1, text="Click para continuar", font=("comicsansms", 20), height=3, width=30, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_1, 2)).place(relx=0.5, y=500, anchor=CENTER)
    pantalla.mainloop()
def main():
    """
    Esta es la funcion principal del programa. Esta encargada de llamar la funcion de Web Scrapping, y la de
    crear los frames.
    :return None
    """
    global textos_fil
    textos_fil = web_scrapping()
    crearpantallaWS()


main()

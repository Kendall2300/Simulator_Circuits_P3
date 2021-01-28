
from tkinter import *
import os
import pygame
from threading import Thread
from tkinter import messagebox
import random
import numpy as np
import Fuente
import Resistencia
#import matplotlib
#import networkx






class General: #La clase contiene todas las interfaces presentes en el menu, con sus respectivos botones.
    
    def Principal(): #Funcion generadora de la interfaz
        """
*************************************************************************
                    Instituto Tecnológico de Costa Rica
                        Ingeniería en Computadores
        Función: Principal

        Lenguaje y version: Pthon 3.8.2

        Autor: Daniel Montoya Rivera

        Descripcion de la Funcion: 
        La funcion se encarga de la creacion de toda la interfaz gráfica,
        ajusta su tamaño, evita que su tamaño sea editable y le añade un
        ícono a esta. Luego de establecer estos parámetros llama a la
        funcion

*************************************************************************
        """
        global WindGame

        
        WindGame = Tk()

        WindGame.title("Circuit Emulator")
        WindGame.minsize(1300,800)
        WindGame.resizable(width = False , height = False)

        WindGame.iconphoto(False, PhotoImage(file = 'img\icon.png'))

        
        #General.InterfazJuego("hola", 1)
        General.Emulador()
        #General.Menu()
        WindGame.mainloop()
        
    #End Principal


    def cargarImg2(archivo):#Funcion encargada de la creación de imágenes
        ruta = os.path.join('img', archivo)
        imagen = PhotoImage(file=ruta)
        return imagen
    
    #End CargarImg



        
    def Help(): #La funcion muestra los controles y el objetivo del juego

        global Salto, Derecha, Izquierda, Disparo
        
        C_Help = Canvas(WindGame, width = 1300 , height = 800)
        C_Help.place(x=0,y=0)
        
        C_Help.image1 = General.cargarImg2('Menu.png')#Background 
        imgCanvas = C_Help.create_image(0,0, anchor = NW , image =C_Help.image1)


        #Muestreo de las instrucciones del emulador
        
        HelpFile = open("notes\D_Montoya_Rivera_Help.txt", "r", encoding="UTF8").read() #Llamada a un archivo .txt que contiene las instrucciones del juego
        
        lb_Ayuda = Label(C_Help, text = HelpFile, bg='Black', fg= 'Green', font = "Arial 14") #Label que muestra el archivo
        lb_Ayuda.place_forget()
        
        btn_Objetivo = Button(C_Help, text = 'Acerca de', bg = 'black', fg = 'Yellow', height = 1, width = 13, command = lambda: (lb_Ayuda.place(x=300, y = 100)), font =("Goudy Stout", 13))# Se encarga de mostrar el objetivo del juego 
        btn_Objetivo.place(x = 950, y = 600 )
        
        btn_Return = Button(C_Help, text = 'Return', bg = 'black', fg = 'Yellow', height = 1, width = 13,command = lambda:General.Menu(), font =("Goudy Stout", 13)) # Regresa al menu Principal
        btn_Return.place(x = 950, y = 700 )


        #End Help


    def Credits():
        C_Credits = Canvas(WindGame, width = 1300 , height = 800, bg = 'green')
        C_Credits.place(x=0, y=0)
        
        C_Credits.image1 = General.cargarImg2('Menu.png')#Background 
        imgCanvas = C_Credits.create_image(0,0, anchor = NW , image =C_Credits.image1)


        Autor = open("notes\D_Montoya_Rivera_Credits.txt", "r", encoding="UTF8").read() #Llamada a un archivo .txt que contiene al autor del programa.
        
        
        lb_Autor = Label(C_Credits, text = Autor, bg='Black', fg= 'Green', font = "Arial 14") #Label que muestra el archivo
        lb_Autor.place(x=500, y = 100)


        
        btn_Return = Button(C_Credits, text = 'Return', bg = 'black', fg = 'Yellow', height = 1, width = 13,command = lambda:General.Menu(), font =("Goudy Stout", 13)) # Regresa al menu Principal
        btn_Return.place(x = 950, y = 700 )


        
        #End Credits



    
    def Menu(): #Interfaz del menu
        """
*************************************************************************
                    Instituto Tecnológico de Costa Rica
                        Ingeniería en Computadores
        Función: Menu

        Lenguaje y version: Pthon 3.8.2

        Autor: Daniel Montoya Rivera

        Version 1.0

        Descripcion de la Funcion: 
        La funcion crea un canvas que contiene al menu principal del juego
        y dentro de ese mismo canvas añade cuatro botones que realizan llamadas
        a funciones diferentes cuando son presionados, estas funciones
        tienen un botón que les permite regresar al menu principal.

        

*************************************************************************
        """

        C_Game = Canvas(WindGame, width = 1300 , height = 800, bg = 'green')
        C_Game.place(x=0, y=0)
        
        
        C_Game.image1 = General.cargarImg2('Menu.png')#Background 
        imgCanvas = C_Game.create_image(0,0, anchor = NW , image =C_Game.image1)

        #Botones
    
        btn_Play = Button(C_Game, text = 'START', bg = 'black', fg = 'Yellow', height = 1, width = 10, command = lambda:General.Emulador(), font =("Goudy Stout", 13)) 
        btn_Play.place(x = 600, y = 80 )

        btn_Help = Button(C_Game, text = 'HELP', bg = 'black', fg = 'Yellow', height = 1, width = 10, command = lambda:General.Help(), font =("Goudy Stout", 13)) 
        btn_Help.place(x = 600, y = 280 )

        btn_Credits = Button(C_Game, text = 'CREDITS', bg = 'black', fg = 'Yellow', height = 1, width = 10, command = lambda:General.Credits(), font =("Goudy Stout", 13)) 
        btn_Credits.place(x = 600, y = 480 )

        btn_Exit = Button(C_Game, text = 'EXIT', bg = 'black', fg = 'Yellow', height = 1, width = 10, command = lambda:General.Callback(), font =("Goudy Stout", 13)) 
        btn_Exit.place(x = 600 , y = 680 )


        
        #End Menu

    def Callback():
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):
            WindGame.destroy()



        

    def Emulador():
        

        C_Game = Canvas(WindGame, width = 1300 , height = 800, bg = 'white')
        C_Game.place(x=0, y=0)

        global CoordX, source, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, cantResistencias
        
        CoordX = 22
        
        cantResistencias

        #Instancia de objetos del emulador
        
        source = Fuente.Fuente("V1", 5) #Instancia del valor inicial que tendra la fuente de tension.

        r1 = Resistencia.Resistencia("R1", 0)#Instancia de los objetos de resistencias.
        r2 = Resistencia.Resistencia("R2", 0)
        r3 = Resistencia.Resistencia("R3", 0)
        r4 = Resistencia.Resistencia("R4", 0)
        r5 = Resistencia.Resistencia("R5", 0)
        r6 = Resistencia.Resistencia("R6", 0)
        r7 = Resistencia.Resistencia("R7", 0)
        r8 = Resistencia.Resistencia("R8", 0)
        r9 = Resistencia.Resistencia("R9", 0)
        r10 = Resistencia.Resistencia("R10", 0)


        
        #Creacion de botones para la edición del circuito
        

        btn_Return = Button(C_Game, text = 'Return to menu', bg = 'black', fg = 'white', height = 1, width = 13,command = lambda:General.Menu(), font =("Goudy Stout", 10)) # Regresa al menu Principal
        btn_Return.place(x = 1080, y = 759)

        btn_SourceEdit = Button(C_Game, text = 'Editar Fuente', bg = 'black', fg = 'white', height = 1, width = 13,command = lambda:editElements(1), font =("Goudy Stout", 10)) # Regresa al menu Principal
        btn_SourceEdit.place(x = 955, y = 690)

        btn_SR = Button(C_Game, text = 'Resistencia en serie', bg = 'black', fg = 'white', height = 1, width = 20,command = lambda:editElements(2), font =("Goudy Stout", 10)) # Regresa al menu Principal
        btn_SR.place(x = 955, y = 590)

        btn_SR = Button(C_Game, text = 'Resistencia en paralelo', bg = 'black', fg = 'white', height = 1, width = 21,command = lambda:editElements(3), font =("Goudy Stout", 10)) # Regresa al menu Principal
        btn_SR.place(x = 955, y = 490)

        #Creacion de las entradas, labels y botones para la edicion y adicion de los componentes del emulador
 
        en_Name = Entry(C_Game, bg = "light blue") #Entrada para ingresar el nombre
        #en_Name.place(x=900, y=100)
        en_Name.place_forget()
        
        lb_EnName = Label(C_Game, text = "Nombre", bg = "white", fg= 'black', font = "Arial 12") 
        #lb_EnName.place(x=835, y=95)
        lb_EnName.place_forget()
        

        en_Valor = Entry(C_Game, bg = "light blue")#Entrada para ingresar el valor
        #en_Valor.place(x=900, y=150)
        en_Valor.place_forget()

        lb_EnValor = Label(C_Game, text = "Valor", bg = "white", fg= 'black', font = "Arial 12")
        #lb_EnValor.place(x=835, y=145)
        lb_EnValor.place_forget()

        
        btn_Save =  Button(C_Game, text = 'Salvar cambios', bg = 'black', fg = 'white', height = 1, width = 21, font =("Goudy Stout", 10)) # Regresa al menu Principal
        btn_Save.place_forget()


        lB_Error = Label(C_Game, text = "Error en alguna de las entradas", bg = "black", fg= 'red', font = "Arial 12") #Label que muestra errores en alguna de las entradas
        #lB_Error.place(x=835, y=300)
        lB_Error.place_forget()

        lB_Error2 = Label(C_Game, text = "Alcanzada la máxima cantidad de resistencias", bg = "black", fg= 'red', font = "Arial 12") #Label que muestra errores en alguna de las entradas
        #lB_Error2.place(x=835, y=300)
        lB_Error2.place_forget()
        

        #Creacion de los labels a los que corresponde cada componente del emulador

        lb_Fuente = Label(C_Game, text = source.getName() + "\n" + str(source.getTension()) + "V", bg = "white", fg= 'Green', font = "Arial 14") #Label que muestra el archivo
        lb_Fuente.place(x=70, y = 160)
        
        lb_R1 = Label(C_Game, text = r1.getName() + "\n" + str(r1.getResistencia()) + "Ω", bg = "white", fg= 'Green', font = "Arial 14") #Label que muestra el archivo
        lb_R1.place_forget()         

        lb_R2 = Label(C_Game, text = r2.getName() + "\n" + str(r2.getResistencia()) + "Ω", bg = "white", fg= 'Green', font = "Arial 14") #Label que muestra el archivo
        lb_R2.place_forget()         

        lb_R3 = Label(C_Game, text = r3.getName() + "\n" + str(r3.getResistencia()) + "Ω", bg = "white", fg= 'Green', font = "Arial 14") #Label que muestra el archivo
        lb_R3.place_forget()         

        lb_R4 = Label(C_Game, text = r4.getName() + "\n" + str(r4.getResistencia()) + "Ω", bg = "white", fg= 'Green', font = "Arial 14") #Label que muestra el archivo
        lb_R4.place_forget()         

        lb_R5 = Label(C_Game, text = r5.getName() + "\n" + str(r5.getResistencia()) + "Ω", bg = "white", fg= 'Green', font = "Arial 14") #Label que muestra el archivo
        lb_R5.place_forget()         

        lb_R6 = Label(C_Game, text = r6.getName() + "\n" + str(r6.getResistencia()) + "Ω", bg = "white", fg= 'Green', font = "Arial 14") #Label que muestra el archivo
        lb_R6.place_forget()         

        lb_R7 = Label(C_Game, text = r7.getName() + "\n" + str(r7.getResistencia()) + "Ω", bg = "white", fg= 'Green', font = "Arial 14") #Label que muestra el archivo
        lb_R7.place_forget()         

        lb_R8 = Label(C_Game, text = r8.getName() + "\n" + str(r8.getResistencia()) + "Ω", bg = "white", fg= 'Green', font = "Arial 14") #Label que muestra el archivo
        lb_R8.place_forget()         

        lb_R9 = Label(C_Game, text = r9.getName() + "\n" + str(r9.getResistencia()) + "Ω", bg = "white", fg= 'Green', font = "Arial 14") #Label que muestra el archivo
        lb_R9.place_forget()         

        lb_R10 = Label(C_Game, text = r10.getName() + "\n" + str(r10.getResistencia()) + "Ω", bg = "white", fg= 'Green', font = "Arial 14") #Label que muestra el archivo
        lb_R10.place_forget() 

        

            

        #Creación de las imágenes iniciales del emulador

        C_Game.imageParalel = General.cargarImg2('PNode.png')
        imgPara1 = C_Game.create_image(30,55, anchor = NW , image =C_Game.imageParalel)

        C_Game.imageParalel2 = General.cargarImg2('PNode.png')
        imgPara2 = C_Game.create_image(30,238, anchor = NW , image =C_Game.imageParalel2)

        C_Game.imageSupply = General.cargarImg2('Power.png')
        imgSource = C_Game.create_image(0,150, anchor = NW , image =C_Game.imageSupply)

        C_Game.imageSeries = General.cargarImg2('S.png')
        
        C_Game.imageParallel = General.cargarImg2('P.png')
        
        
        
        img2 = C_Game.create_image(122,38, anchor = NW , image =C_Game.imageSeries)

        img3 = C_Game.create_image(222,38, anchor = NW , image =C_Game.imageSeries)

        img4 = C_Game.create_image(322,38, anchor = NW , image =C_Game.imageSeries)

        img5 = C_Game.create_image(422,38, anchor = NW , image =C_Game.imageSeries)

        img6 = C_Game.create_image(522,38, anchor = NW , image =C_Game.imageSeries)

        img7 = C_Game.create_image(622,38, anchor = NW , image =C_Game.imageSeries)

        img8 = C_Game.create_image(722,38, anchor = NW , image =C_Game.imageSeries)

        img9 = C_Game.create_image(822,38, anchor = NW , image =C_Game.imageSeries)

        img10 = C_Game.create_image(922,38, anchor = NW , image =C_Game.imageSeries)


        def editElements(Numero):
            
            en_Name.place(x=900, y=100)
            
            lb_EnName.place(x=835, y=95)
            
            en_Valor.place(x=900, y=150)
            
            lb_EnValor.place(x=835, y=145)

            btn_Save.place(x = 835, y = 200)

            en_Name.delete(0,"end")
            
            en_Valor.delete(0,"end")

            
            if Numero == 1: #Condicion para evaluar si se quiere editar la fuente
                
                btn_Save.config(command=lambda: cambiaFuente(en_Name.get().upper(),en_Valor.get()))
                                
            elif Numero == 2: #Condicion para evaluar si se quiere agregar una resistencia en serie
                
                btn_Save.config(command=lambda: agregaRes(en_Name.get().upper(),en_Valor.get(), 1))
                                
            else: #Condicion para evaluar si se quiere agregar una resistencia en paralelo
                
                btn_Save.config(command=lambda: agregaRes(en_Name.get().upper(),en_Valor.get(), 2))


        #End editElements
                                
        def cambiaFuente(Name, Value):
            
            Value = int(Value)
            
            if not(ValidaEntradas(Name,Value, 1)): #Valida que los parámetros de entrada sean válidos
                lB_Error.place(x=835, y=300)
            else:
                lB_Error.place_forget()
                
                source.setName(Name)
                source.setTension(Value)

                lb_Fuente.config(text = source.getName() + "\n" + str(source.getTension()) + "V")
                
                
            
        def agregaRes(Name, Value, Tipo):

            global cantResistencias, CoordX

            Value = int(Value)
            
            if not (ValidaEntradas(Name,Value, 2)): #Valida que los parámetros de entrada sean válidos
                lB_Error.place(x=835, y=300)
            else:
                lB_Error.place_forget()

                if Tipo == 1: #Condicion para agregar una resistencia en serie

                    if cantResistencias == 10:
                    
                        lB_Error2.place(x=835, y=300)
                        
                    elif cantResistencias == 0:
                        
                        cantResistencias += 1

                        r1.setName(Name)
                        r1.setsetResistencia(Value)

                        if Tipo == 1:

                            img1 = C_Game.create_image(CoordX,38, anchor = NW , image =C_Game.imageSeries1)

                        else:

                            img1 = C_Game.create_image(CoordX,38, anchor = NW , image =C_Game.imageSeries1)
                        

                        

                        

                        


                
                
                



                
                


        def ValidaEntradas(Name,Value, Numero): #Valida las entradas dadas por el usuario


            if Name.strip() != "" and len(Name.strip()) <= 3: #Valida si el nombre dado es nulo o no cumple con la longitud establecida
                
                if Value <= 10 and Value >= 0 and Numero == 1 or Value >= 1 and Numero != 1:
                    
                    btn_Save.place_forget()
                    lb_EnValor.place_forget()
                    en_Valor.place_forget()
                    lb_EnName.place_forget()
                    en_Name.place_forget()
                    en_Name.delete(0,"end")
                    en_Valor.delete(0,"end")
                    return True
                
                else:
                    return False
            else:
                return False
            

            
        #End Emulador


        
#End Class General
      
General.Principal()



















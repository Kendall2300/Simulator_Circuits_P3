
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

        global CoordX, source, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, cantResistencias, LastElement, mouse

        global Tension, Tension1, Tension2, Tension3, Tension4 ,Tension5, Tension6, Tension7, Tension8, Tension9, GroundT

        global Corriente, Corriente1, Corriente2, Corriente3, Corriente4, Corriente5, Corriente6, Corriente7, Corriente8, Corriente9, GroundC

        mouse = [0,0]
        
        Tension = random.uniform(0, 10)
        Tension1 = random.uniform(0, 10)
        Tension2 = random.uniform(0, 10)
        Tension3 = random.uniform(0, 10)
        Tension4 = random.uniform(0, 10)
        Tension5 = random.uniform(0, 10)
        Tension6 = random.uniform(0, 10)
        Tension7 = random.uniform(0, 10)
        Tension8 = random.uniform(0, 10)
        Tension9 = random.uniform(0, 10)

        Corriente = random.uniform(0, 1000)
        Corriente1 = random.uniform(0, 1000)
        Corriente2 = random.uniform(0, 1000)
        Corriente3 = random.uniform(0, 1000)
        Corriente4 = random.uniform(0, 1000)
        Corriente5 = random.uniform(0, 1000)
        Corriente6 = random.uniform(0, 1000)
        Corriente7 = random.uniform(0, 1000)
        Corriente8 = random.uniform(0, 1000)
        Corriente9 = random.uniform(0, 1000)

        GroundT = 0

        GroundC = random.uniform(0, 1000)
        
        CoordX = 22

        LastElement = 0
        
        cantResistencias = 0

        #Instancia de objetos del emulador
        
        source = Fuente.Fuente("V1", 5) #Instancia del valor inicial que tendra la fuente de tension.

        r1 = Resistencia.Resistencia("R1", 0, 1)#Instancia de los objetos de resistencias.
        r2 = Resistencia.Resistencia("R2", 0, 1)
        r3 = Resistencia.Resistencia("R3", 0, 1)
        r4 = Resistencia.Resistencia("R4", 0, 1)
        r5 = Resistencia.Resistencia("R5", 0, 1)
        r6 = Resistencia.Resistencia("R6", 0, 1)
        r7 = Resistencia.Resistencia("R7", 0, 1)
        r8 = Resistencia.Resistencia("R8", 0, 1)
        r9 = Resistencia.Resistencia("R9", 0, 1)
        r10 = Resistencia.Resistencia("R10", 0, 1)


        
        #Creacion de botones para la edición del circuito
        

        btn_Return = Button(C_Game, text = 'Return to menu', bg = 'black', fg = 'white', height = 1, width = 13,command = lambda:General.Menu(), font =("Goudy Stout", 10)) # Regresa al menu Principal
        btn_Return.place(x = 1080, y = 759)

        btn_SourceEdit = Button(C_Game, text = 'Editar Fuente', bg = 'black', fg = 'white', height = 1, width = 13,command = lambda:editElements(1), font =("Goudy Stout", 10)) # Regresa al menu Principal
        btn_SourceEdit.place(x = 955, y = 690)
        

        btn_SR = Button(C_Game, text = 'Resistencia en serie', bg = 'black', fg = 'white', height = 1, width = 20,command = lambda:editElements(2), font =("Goudy Stout", 10)) # Regresa al menu Principal
        btn_SR.place(x = 955, y = 590)

        btn_SR2 = Button(C_Game, text = 'Resistencia en paralelo', bg = 'black', fg = 'white', height = 1, width = 21,command = lambda:editElements(3), font =("Goudy Stout", 10)) # Regresa al menu Principal
        btn_SR2.place(x = 955, y = 490)

        btn_Simulate = Button(C_Game, text = 'Simular', bg = 'Green', fg = 'black', height = 1, width = 10,command = lambda:Simular(), font =("Goudy Stout", 10)) # Regresa al menu Principal
        #btn_Simulate.place(x = 666, y = 590)
        btn_Simulate.place_forget()

        btn_Stop  = Button(C_Game, text = 'Stop', bg = 'Red', fg = 'black', height = 1, width = 10,command = lambda:StopSimular(), font =("Goudy Stout", 10)) # Regresa al menu Principal
        #btn_Stop.place(x = 666, y = 590)
        btn_Stop.place_forget()

        
        #btn_SourceEdit.place_forget()
        #btn_SR.place_forget()
        #btn_SR2.place_forget()
        #btn_Simulate.place_forget()
        
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


        lb_Data = Label(C_Game, bg = "Black", fg= 'White', font = "Arial 14") #Label que muestra el archivo
        lb_Data.place_forget() 
        

            

        #Creación de las imágenes iniciales del emulador

        C_Game.imageParalel = General.cargarImg2('PNode.png')
        imgPara1 = C_Game.create_image(30,55, anchor = NW , image =C_Game.imageParalel)

        C_Game.imageParalel2 = General.cargarImg2('PNode.png')
        imgPara2 = C_Game.create_image(30,238, anchor = NW , image =C_Game.imageParalel2)

        C_Game.imageSupply = General.cargarImg2('Power.png')
        imgSource = C_Game.create_image(0,150, anchor = NW , image =C_Game.imageSupply)

        C_Game.imageSeries = General.cargarImg2('S.png')
        
        C_Game.imageParallel = General.cargarImg2('P.png')

        C_Game.Close = General.cargarImg2('Close.png')
        
        
        
        #img2 = C_Game.create_image(122,38, anchor = NW , image =C_Game.imageSeries)

        #img3 = C_Game.create_image(222,38, anchor = NW , image =C_Game.imageSeries)

        #img4 = C_Game.create_image(322,38, anchor = NW , image =C_Game.imageSeries)

        #img5 = C_Game.create_image(422,38, anchor = NW , image =C_Game.imageSeries)

        #img6 = C_Game.create_image(522,38, anchor = NW , image =C_Game.imageSeries)

        #img7 = C_Game.create_image(622,38, anchor = NW , image =C_Game.imageSeries)

        #img8 = C_Game.create_image(722,38, anchor = NW , image =C_Game.imageSeries)

        #img9 = C_Game.create_image(822,38, anchor = NW , image =C_Game.imageSeries)

        #img10 = C_Game.create_image(922,38, anchor = NW , image =C_Game.imageSeries)

        #img11 = C_Game.create_image(1035,53, anchor = NW , image =C_Game.Close)

        
        def editElements(Numero):
            
            en_Name.place(x=200, y=500)
            
            lb_EnName.place(x=120, y=495)
            
            en_Valor.place(x=200, y=550)
            
            lb_EnValor.place(x=120, y=545)

            btn_Save.place(x = 120, y = 700)

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
                
                
            
        def agregaRes(Name, Value, Tipo): #Funcion encargada de la implementación de resistencias

            global cantResistencias, CoordX, LastElement

            Value = int(Value)
            
            if not (ValidaEntradas(Name,Value, 2)): #Valida que los parámetros de entrada sean válidos
                lB_Error.place(x=100, y=600)
                return
                
            else:
                lB_Error.place_forget()
                

                if cantResistencias == 10:
                
                    lB_Error2.place(x=100, y=600)
                    
                    
                elif cantResistencias == 0:
                    
                    cantResistencias += 1

                    r1.setName(Name)
                    r1.setResistencia(Value)

                    btn_Simulate.place(x = 666, y = 590)

                    
                    
                    lb_R1.config(text = r1.getName() + "\n" + str(r1.getResistencia()) + "Ω")
                    
                    if Tipo == 1:#Condicion para agregar una resistencia en serie

                        r1.setTipo(1)

                        LastElement = 1

                        img1 = C_Game.create_image(CoordX,38, anchor = NW , image =C_Game.imageSeries)

                        lb_R1.place(x= CoordX + 58, y = 70)
                        

                    else:

                        r1.setTipo(2)

                        LastElement = 2

                        img1 = C_Game.create_image(CoordX,38, anchor = NW , image =C_Game.imageParallel)

                        lb_R1.place(x= CoordX + 128, y = 160)
                        
                    CoordX += 100

                elif cantResistencias == 1:
                    
                    cantResistencias += 1

                    r2.setName(Name)
                    r2.setResistencia(Value)

                    

                    lb_R2.config(text = r2.getName() + "\n" + str(r2.getResistencia()) + "Ω")

                    if Tipo == 1:#Condicion para agregar una resistencia en serie

                        r2.setTipo(1)

                        LastElement = 1

                        img2 = C_Game.create_image(CoordX,38, anchor = NW , image =C_Game.imageSeries)

                        lb_R2.place(x= CoordX + 58, y = 70)

                    else:
                        
                        r2.setTipo(2)

                        LastElement = 2

                        img2 = C_Game.create_image(CoordX,38, anchor = NW , image =C_Game.imageParallel)

                        lb_R2.place(x= CoordX + 128, y = 160)
                        
                    CoordX += 100


                elif cantResistencias == 2:
                    
                    cantResistencias += 1

                    r3.setName(Name)
                    r3.setResistencia(Value)
                    

                    lb_R3.config(text = r3.getName() + "\n" + str(r3.getResistencia()) + "Ω")

                    if Tipo == 1:#Condicion para agregar una resistencia en serie

                        r3.setTipo(1)

                        LastElement = 1

                        img3 = C_Game.create_image(CoordX,38, anchor = NW , image =C_Game.imageSeries)

                        lb_R3.place(x= CoordX + 58, y = 70)

                    else:

                        r3.setTipo(2)
                        
                        LastElement = 2

                        img3 = C_Game.create_image(CoordX,38, anchor = NW , image =C_Game.imageParallel)

                        lb_R3.place(x= CoordX + 128, y = 160)
                        
                    CoordX += 100


                elif cantResistencias == 3:
                    
                    cantResistencias += 1

                    r4.setName(Name)
                    r4.setResistencia(Value)

                    lb_R4.config(text = r4.getName() + "\n" + str(r4.getResistencia()) + "Ω")

                    if Tipo == 1:#Condicion para agregar una resistencia en serie

                        r4.setTipo(1)

                        LastElement = 1

                        img4 = C_Game.create_image(CoordX,38, anchor = NW , image =C_Game.imageSeries)

                        lb_R4.place(x= CoordX + 58, y = 70)

                    else:

                        r4.setTipo(2)

                        LastElement = 2

                        img4 = C_Game.create_image(CoordX,38, anchor = NW , image =C_Game.imageParallel)

                        lb_R4.place(x= CoordX + 128, y = 160)
                        
                    CoordX += 100


                elif cantResistencias == 4:
                    
                    cantResistencias += 1

                    r5.setName(Name)
                    r5.setResistencia(Value)

                    lb_R5.config(text = r5.getName() + "\n" + str(r5.getResistencia()) + "Ω")

                    if Tipo == 1:#Condicion para agregar una resistencia en serie

                        r5.setTipo(1)

                        LastElement = 1

                        img5 = C_Game.create_image(CoordX,38, anchor = NW , image =C_Game.imageSeries)

                        lb_R5.place(x= CoordX + 58, y = 70)

                    else:

                        r5.setTipo(2)

                        LastElement = 2

                        img5 = C_Game.create_image(CoordX,38, anchor = NW , image =C_Game.imageParallel)

                        lb_R5.place(x= CoordX + 128, y = 160)
                        
                    CoordX += 100


                elif cantResistencias == 5:
                    
                    cantResistencias += 1

                    r6.setName(Name)
                    r6.setResistencia(Value)

                    lb_R6.config(text = r6.getName() + "\n" + str(r6.getResistencia()) + "Ω")

                    if Tipo == 1:#Condicion para agregar una resistencia en serie

                        r6.setTipo(1)

                        LastElement = 1

                        img6 = C_Game.create_image(CoordX,38, anchor = NW , image =C_Game.imageSeries)

                        lb_R6.place(x= CoordX + 58, y = 70)

                    else:

                        r6.setTipo(2)
                        
                        LastElement = 2

                        img6 = C_Game.create_image(CoordX,38, anchor = NW , image =C_Game.imageParallel)

                        lb_R6.place(x= CoordX + 128, y = 160)
                        
                    CoordX += 100


                elif cantResistencias == 6:
                    
                    cantResistencias += 1

                    r7.setName(Name)
                    r7.setResistencia(Value)

                    lb_R7.config(text = r7.getName() + "\n" + str(r7.getResistencia()) + "Ω")

                    if Tipo == 1:#Condicion para agregar una resistencia en serie

                        r7.setTipo(1)

                        LastElement = 1

                        img7 = C_Game.create_image(CoordX,38, anchor = NW , image =C_Game.imageSeries)

                        lb_R7.place(x= CoordX + 58, y = 70)

                    else:

                        r7.setTipo(2)

                        LastElement = 2

                        img7 = C_Game.create_image(CoordX,38, anchor = NW , image =C_Game.imageParallel)

                        lb_R7.place(x= CoordX + 128, y = 160)
                        
                    CoordX += 100


                elif cantResistencias == 7:
                    
                    cantResistencias += 1

                    r8.setName(Name)
                    r8.setResistencia(Value)

                    lb_R8.config(text = r8.getName() + "\n" + str(r8.getResistencia()) + "Ω")

                    if Tipo == 1:#Condicion para agregar una resistencia en serie

                        r8.setTipo(1)

                        LastElement = 1

                        img8 = C_Game.create_image(CoordX,38, anchor = NW , image =C_Game.imageSeries)

                        lb_R8.place(x= CoordX + 58, y = 70)

                    else:

                        r8.setTipo(2)

                        LastElement = 2

                        img8 = C_Game.create_image(CoordX,38, anchor = NW , image =C_Game.imageParallel)

                        lb_R8.place(x= CoordX + 128, y = 160)
                        
                    CoordX += 100


                elif cantResistencias == 8:
                    
                    cantResistencias += 1

                    r9.setName(Name)
                    r9.setResistencia(Value)

                    lb_R9.config(text = r9.getName() + "\n" + str(r9.getResistencia()) + "Ω")

                    if Tipo == 1:#Condicion para agregar una resistencia en serie

                        r9.setTipo(1)

                        LastElement = 1

                        img9 = C_Game.create_image(CoordX,38, anchor = NW , image =C_Game.imageSeries)

                        lb_R9.place(x= CoordX + 58, y = 70)

                    else:

                        r9.setTipo(2)

                        LastElement = 2

                        img9 = C_Game.create_image(CoordX,38, anchor = NW , image =C_Game.imageParallel)

                        lb_R9.place(x= CoordX + 128, y = 160)
                        
                    CoordX += 100


                elif cantResistencias == 9:
                    
                    cantResistencias += 1

                    r10.setName(Name)
                    r10.setResistencia(Value)

                    lb_R10.config(text = r10.getName() + "\n" + str(r10.getResistencia()) + "Ω")

                    if Tipo == 1:#Condicion para agregar una resistencia en serie

                        r10.setTipo(1)

                        LastElement = 2

                        img10 = C_Game.create_image(CoordX,38, anchor = NW , image =C_Game.imageSeries)

                        
                        img11 = C_Game.create_image(CoordX + 113 ,53, anchor = NW , image =C_Game.Close)


                        lb_R10.place(x= CoordX + 58, y = 70)

                    else:

                        r10.setTipo(2)

                        LastElement = 2

                        img10 = C_Game.create_image(CoordX,38, anchor = NW , image =C_Game.imageParallel)

                        lb_R10.place(x= CoordX + 128, y = 160)
                        
                    CoordX += 100
                


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




        def Simular():
            global LastElement, Condicion

            Condicion = True
            
            btn_SourceEdit.place_forget()
            btn_SR.place_forget()
            btn_SR2.place_forget()
            btn_Simulate.place_forget()
            btn_Stop.place(x = 666, y = 590)

            if LastElement == 1:
                
                img11 = C_Game.create_image(CoordX + 13  ,53, anchor = NW , image =C_Game.Close)

            WindGame.bind('<Motion>', Mouse)

            WindGame.after(1000, lambda:Thread(target=muestraDatos()).start())

            CalculaNodos()


        def CalculaNodos():
            
            global Tension, Tension1, Tension2, Tension3, Tension4 ,Tension5, Tension6, Tension7, Tension8, Tension9, GroundT, Condicion, cantResistencias

            global Corriente, Corriente1, Corriente2, Corriente3, Corriente4, Corriente5, Corriente6, Corriente7, Corriente8, Corriente9, GroundC, mouse
            
            print("hola")


            if cantResistencias == 1:

                Corriente = source.getTension() / r1.getResistencia()
                Tension = source.getTension()

            elif cantResistencias == 2:

                if r1.getTipo() == 1 and r2.getTipo() == 1 or r1.getTipo() == 1 and r2.getTipo() == 2: #Evalua si las 2 resistencias estan en serie
                    R = r1.getResistencia() + r2.getResistencia()

                    Itotal = source.getTension() / R

                    Corriente = Itotal
                    Tension = Itotal * r1.getResistencia()
                    
                    Corriente1 = Itotal
                    Tension1 = Itotal * r2.getResistencia()

                else: #Las dos resistencias están en paralelo

                    Tension = source.getTension()
                    Corriente = Tension / r1.getResistencia()
                    
                    Tension1 = source.getTension()
                    Corriente1 = Tension1 / r2.getResistencia()

            elif cantResistencias == 3:
                
                
                if r1.getTipo() == 1 and r2.getTipo() == 1 and r3.getTipo() == 1 or r1.getTipo() == 1 and r2.getTipo() == 1 and r3.getTipo() == 2: #todas las resistencias en serie

                    R = r1.getResistencia() + r2.getResistencia() + r3.getResistencia()

                    Itotal = source.getTension() / R

                    Corriente = Itotal
                    Tension = Itotal * r1.getResistencia()
                    
                    Corriente1 = Itotal
                    Tension1 = Itotal * r2.getResistencia()
                    
                    Corriente2 = Itotal
                    Tension2 = Itotal * r3.getResistencia()

                elif r1.getTipo() == 2 and r2.getTipo() == 1 and r3.getTipo() == 1 or r1.getTipo() == 2 and r2.getTipo() == 1 and r3.getTipo() == 2: #La ultimas 2 resistencias son serie pero la primera es paralela

                    Tension = source.getTension()
                    Corriente = Tension/r1.getResistencia()


                    R = r2.getResistencia() + r3.getResistencia()

                    Itotal = source.getTension() / R
                    
                    Corriente1 = Itotal
                    Tension1 =  Itotal * r2.getResistencia()
                    
                    Corriente2 = Itotal
                    Tension2 =  Itotal * r3.getResistencia()


                elif r1.getTipo() == 1 and r2.getTipo() == 2 and r3.getTipo() == 2 or r1.getTipo() == 1 and r2.getTipo() == 2 and r3.getTipo() == 1: #Solo la primera res es serie, las otras son paralelas

                    R = r1.getResistencia() + (r2.getResistencia()**-1 + r3.getResistencia()**-1)**-1

                    Itotal = source.getTension() / R

                    Tension = Itotal * r1.getResistencia()
                    Corriente = Itotal

                    Tension1 = source.getTension() - Tension
                    Corriente1 = Tension1/r2.getResistencia()

                    Tension2 = Tension1
                    Corriente2 = Tension2/r3.getResistencia()

                else: #Todas son paralelas

                    Tension = source.getTension()
                    Corriente = Tension/r1.getResistencia()

                    Tension1 = source.getTension()
                    Corriente1 = Tension/r2.getResistencia()

                    Tension2 = source.getTension()
                    Corriente2 = Tension/r3.getResistencia()
                        
            elif cantResistencias == 4:


                if r1.getTipo() == 1 and r2.getTipo() == 1 and r3.getTipo() == 1 and r4.getTipo() == 1  or r1.getTipo() == 1 and r2.getTipo() == 1 and r3.getTipo() == 1 and r4.getTipo() == 2: #Todo en serie

                    R = r1.getResistencia() + r2.getResistencia() + r3.getResistencia() + r4.getResistencia()

                    Itotal = source.getTension() / R

                    Corriente = Itotal
                    Tension = Itotal * r1.getResistencia()
                    
                    Corriente1 = Itotal
                    Tension1 = Itotal * r2.getResistencia()
                    
                    Corriente2 = Itotal
                    Tension2 = Itotal * r3.getResistencia()
                    
                    Corriente3 = Itotal
                    Tension3 = Itotal * r4.getResistencia()

                elif r1.getTipo() == 1 and r2.getTipo() == 2 and r3.getTipo() == 1 and r4.getTipo() == 1 or r1.getTipo() == 1 and r2.getTipo() == 2 and r3.getTipo() == 1 and r4.getTipo() == 2: #R2 en paraelo

                    R = r1.getResistencia() + (r2.getResistencia()**-1 + (r3.getResistencia() + r4.getResistencia())**-1) **-1

                    Itotal = source.getTension() / R

                    Tension = Itotal*r1.getResistencia()
                    Corriente = Itotal

                    Tension1 = source.getTension() - Tension
                    Corriente1 = Tension1 / r2.getResistencia()

                    Corriente2 = Itotal - Corriente1
                    Tension2 = Corriente2 * r3.getResistencia()

                    Corriente3 = Corriente2
                    Tension3 = Corriente3 * r4.getResistencia()

                elif r1.getTipo() == 2 and r2.getTipo() == 1 and r3.getTipo() == 1 and r4.getTipo() == 1: #R1 en paralelo

                    R = (r1.getResistencia()**-1 + (r2.getResistencia()+r3.getResistencia()+r4.getResistencia())**-1)**-1

                    Itotal = source.getTension() / R

                    Tension = source.getTension()
                    Corriente  = Tension/r1.getResistencia()

                    Corriente1 = Itotal - Corriente
                    Corriente2 = Corriente1
                    Corriente3 = Corriente1
                    Corriente4 = Corriente1

                    Tension1 = Corriente1 * r2.getResistencia()
                    Tension2 = Corriente2 * r3.getResistencia()
                    Tension3 = Corriente3 * r4.getResistencia()

                

                elif r1.getTipo() == 1 and r2.getTipo() == 1 and r3.getTipo() == 2 and r4.getTipo() == 1 or r1.getTipo() == 1 and r2.getTipo() == 1 and r3.getTipo() == 2 and r4.getTipo() == 2: #R3 en paralelo

                    R = r1.getResistencia() + r2.getResistencia() + ((r3.getResistencia())**-1 + (r2.getResistencia())**-1)**-1

                    Itotal = source.getTension() / R

                    
                    Corriente = Itotal
                    Tension = Corriente*r1.getResistencia()
                    
                    Corriente1 = Itotal
                    Tension1 = Corriente1*r2.getResistencia()

                    TensionTemp = source.getTension() - Tension - Tension1

                    Tension2 = TensionTemp
                    Corriente2 = Tension2/r3.getResistencia()

                    Tension3 = TensionTemp
                    Corriente3 = Tension3/r4.getResistencia()

                else: #Todas en paralelo

                    Tension = source.getTension()
                    Corriente = Tension/r1.getResistencia()

                    Tension1 = source.getTension()
                    Corriente1 = Tension1/r2.getResistencia()

                    Tension2 = source.getTension()
                    Corriente2 = Tension2/r3.getResistencia()
                    
                    Tension3 = source.getTension()
                    Corriente3 = Tension3/r4.getResistencia()

            elif cantResistencias == 5:

                if r1.getTipo() == 1 and r2.getTipo() == 1 and r3.getTipo() == 1 and r4.getTipo() == 1  and r5.getTipo() == 1 or r1.getTipo() == 1 and r2.getTipo() == 1 and r3.getTipo() == 1 and r4.getTipo() == 1  and r5.getTipo() == 2: #Todo en serie
                    
                    R = r1.getResistencia() + r2.getResistencia() + r3.getResistencia() + r4.getResistencia() + r5.getResistencia()

                    Itotal = source.getTension() / R

                    Corriente = Itotal
                    Tension = Itotal * r1.getResistencia()
                    
                    Corriente1 = Itotal
                    Tension1 = Itotal * r2.getResistencia()
                    
                    Corriente2 = Itotal
                    Tension2 = Itotal * r3.getResistencia()
                    
                    Corriente3 = Itotal
                    Tension3 = Itotal * r4.getResistencia()
                    
                    Corriente4 = Itotal
                    Tension4 = Itotal * r5.getResistencia()

                    
                elif r1.getTipo() == 2 and r2.getTipo() == 2 and r3.getTipo() == 2 and r4.getTipo() == 2  and r5.getTipo() == 2 or  r1.getTipo() == 2 and r2.getTipo() == 2 and r3.getTipo() == 2 and r4.getTipo() == 2  and r5.getTipo() == 1: #Todo en paralelo

                    Tension = source.getTension()
                    Corriente = Tension/r1.getResistencia()

                    Tension1 = source.getTension()
                    Corriente1 = Tension1/r2.getResistencia()

                    Tension2 = source.getTension()
                    Corriente2 = Tension2/r3.getResistencia()
                    
                    Tension3 = source.getTension()
                    Corriente3 = Tension3/r4.getResistencia()

                    Tension4 = source.getTension()
                    Corriente4 = Tension4/r5.getResistencia()

            elif cantResistencias == 6:

                if r1.getTipo() == 1 and r2.getTipo() == 1 and r3.getTipo() == 1 and r4.getTipo() == 1  and r5.getTipo() == 1 and r6.getTipo() == 1 or r1.getTipo() == 1 and r2.getTipo() == 1 and r3.getTipo() == 1 and r4.getTipo() == 1  and r5.getTipo() == 1 and r6.getTipo() == 2:#Todo en serie

                    
                    R = r1.getResistencia() + r2.getResistencia() + r3.getResistencia() + r4.getResistencia() + r5.getResistencia() + r6.getResistencia()

                    Itotal = source.getTension() / R

                    Corriente = Itotal
                    Tension = Itotal * r1.getResistencia()
                    
                    Corriente1 = Itotal
                    Tension1 = Itotal * r2.getResistencia()
                    
                    Corriente2 = Itotal
                    Tension2 = Itotal * r3.getResistencia()
                    
                    Corriente3 = Itotal
                    Tension3 = Itotal * r4.getResistencia()
                    
                    Corriente4 = Itotal
                    Tension4 = Itotal * r5.getResistencia()
                    
                    Corriente5 = Itotal
                    Tension5 = Itotal * r6.getResistencia()


                    
                elif r1.getTipo() == 2 and r2.getTipo() == 2 and r3.getTipo() == 2 and r4.getTipo() == 2  and r5.getTipo() == 2 and r6.getTipo() == 2 or  r1.getTipo() == 2 and r2.getTipo() == 2 and r3.getTipo() == 2 and r4.getTipo() == 2  and r5.getTipo() == 2 and r6.getTipo() == 1:#Todo en paralelo

                    Tension = source.getTension()
                    Corriente = Tension/r1.getResistencia()

                    Tension1 = source.getTension()
                    Corriente1 = Tension1/r2.getResistencia()

                    Tension2 = source.getTension()
                    Corriente2 = Tension2/r3.getResistencia()
                    
                    Tension3 = source.getTension()
                    Corriente3 = Tension3/r4.getResistencia()

                    Tension4 = source.getTension()
                    Corriente4 = Tension4/r5.getResistencia()

                    Tension5 = source.getTension()
                    Corriente5 = Tension5/r6.getResistencia()
                    


            elif cantResistencias == 7:

                if r1.getTipo() == 1 and r2.getTipo() == 1 and r3.getTipo() == 1 and r4.getTipo() == 1  and r5.getTipo() == 1 and r6.getTipo() == 1 and r7.getTipo() == 1 or  r1.getTipo() == 1 and r2.getTipo() == 1 and r3.getTipo() == 1 and r4.getTipo() == 1  and r5.getTipo() == 1 and r6.getTipo() == 1 and r7.getTipo() == 2:#Todo en serie
                    
                    R = r1.getResistencia() + r2.getResistencia() + r3.getResistencia() + r4.getResistencia() + r5.getResistencia() + r6.getResistencia() + r7.getResistencia()

                    Itotal = source.getTension() / R

                    Corriente = Itotal
                    Tension = Itotal * r1.getResistencia()
                    
                    Corriente1 = Itotal
                    Tension1 = Itotal * r2.getResistencia()
                    
                    Corriente2 = Itotal
                    Tension2 = Itotal * r3.getResistencia()
                    
                    Corriente3 = Itotal
                    Tension3 = Itotal * r4.getResistencia()
                    
                    Corriente4 = Itotal
                    Tension4 = Itotal * r5.getResistencia()
                    
                    Corriente5 = Itotal
                    Tension5 = Itotal * r6.getResistencia()
                    
                    Corriente6 = Itotal
                    Tension6 = Itotal * r7.getResistencia()

                
                elif r1.getTipo() == 2 and r2.getTipo() == 2 and r3.getTipo() == 2 and r4.getTipo() == 2  and r5.getTipo() == 2 and r6.getTipo() == 2 and r7.getTipo() == 2  or  r1.getTipo() == 2 and r2.getTipo() == 2 and r3.getTipo() == 2 and r4.getTipo() == 2  and r5.getTipo() == 2 and r6.getTipo() == 2 and r7.getTipo() == 1:#Todo en paralelo
    
                    Tension = source.getTension()
                    Corriente = Tension/r1.getResistencia()

                    Tension1 = source.getTension()
                    Corriente1 = Tension1/r2.getResistencia()

                    Tension2 = source.getTension()
                    Corriente2 = Tension2/r3.getResistencia()
                    
                    Tension3 = source.getTension()
                    Corriente3 = Tension3/r4.getResistencia()

                    Tension4 = source.getTension()
                    Corriente4 = Tension4/r5.getResistencia()

                    Tension5 = source.getTension()
                    Corriente5 = Tension5/r6.getResistencia()
                    
                    Tension6 = source.getTension()
                    Corriente6 = Tension6/r7.getResistencia()

                    


            elif cantResistencias == 8:

                if r1.getTipo() == 1 and r2.getTipo() == 1 and r3.getTipo() == 1 and r4.getTipo() == 1  and r5.getTipo() == 1 and r6.getTipo() == 1 and r7.getTipo() == 1 and r8.getTipo() == 1 or  r1.getTipo() == 1 and r2.getTipo() == 1 and r3.getTipo() == 1 and r4.getTipo() == 1  and r5.getTipo() == 1 and r6.getTipo() == 1 and r7.getTipo() == 1 and r8.getTipo() == 2:#Todo en serie

                                    
                    R = r1.getResistencia() + r2.getResistencia() + r3.getResistencia() + r4.getResistencia() + r5.getResistencia() + r6.getResistencia() + r7.getResistencia() + r8.getResistencia()

                    Itotal = source.getTension() / R

                    Corriente = Itotal
                    Tension = Itotal * r1.getResistencia()
                    
                    Corriente1 = Itotal
                    Tension1 = Itotal * r2.getResistencia()
                    
                    Corriente2 = Itotal
                    Tension2 = Itotal * r3.getResistencia()
                    
                    Corriente3 = Itotal
                    Tension3 = Itotal * r4.getResistencia()
                    
                    Corriente4 = Itotal
                    Tension4 = Itotal * r5.getResistencia()
                    
                    Corriente5 = Itotal
                    Tension5 = Itotal * r6.getResistencia()
                    
                    Corriente6 = Itotal
                    Tension6 = Itotal * r7.getResistencia()
                    
                    Corriente7 = Itotal
                    Tension7 = Itotal * r8.getResistencia()

                elif r1.getTipo() == 2 and r2.getTipo() == 2 and r3.getTipo() == 2 and r4.getTipo() == 2  and r5.getTipo() == 2 and r6.getTipo() == 2 and r7.getTipo() == 2 and r8.getTipo() == 2 or  r1.getTipo() == 2 and r2.getTipo() == 2 and r3.getTipo() == 2 and r4.getTipo() == 2  and r5.getTipo() == 2 and r6.getTipo() == 2 and r7.getTipo() == 2 and r8.getTipo() == 1:#Todo en paralelo
                        
                    Tension = source.getTension()
                    Corriente = Tension/r1.getResistencia()

                    Tension1 = source.getTension()
                    Corriente1 = Tension1/r2.getResistencia()

                    Tension2 = source.getTension()
                    Corriente2 = Tension2/r3.getResistencia()
                    
                    Tension3 = source.getTension()
                    Corriente3 = Tension3/r4.getResistencia()

                    Tension4 = source.getTension()
                    Corriente4 = Tension4/r5.getResistencia()

                    Tension5 = source.getTension()
                    Corriente5 = Tension5/r6.getResistencia()
                    
                    Tension6 = source.getTension()
                    Corriente6 = Tension6/r7.getResistencia()
                    
                    Tension7 = source.getTension()
                    Corriente7 = Tension7/r8.getResistencia()

                



            elif cantResistencias == 9:

                if r1.getTipo() == 1 and r2.getTipo() == 1 and r3.getTipo() == 1 and r4.getTipo() == 1  and r5.getTipo() == 1 and r6.getTipo() == 1 and r7.getTipo() == 1 and r8.getTipo() == 1 and r9.getTipo() == 1 or  r1.getTipo() == 1 and r2.getTipo() == 1 and r3.getTipo() == 1 and r4.getTipo() == 1  and r5.getTipo() == 1 and r6.getTipo() == 1 and r7.getTipo() == 1 and r8.getTipo() == 1 and r9.getTipo() == 2:#Todo en serie

                                    
                    R = r1.getResistencia() + r2.getResistencia() + r3.getResistencia() + r4.getResistencia() + r5.getResistencia() + r6.getResistencia() + r7.getResistencia() + r8.getResistencia() + r9.getResistencia()

                    Itotal = source.getTension() / R

                    Corriente = Itotal
                    Tension = Itotal * r1.getResistencia()
                    
                    Corriente1 = Itotal
                    Tension1 = Itotal * r2.getResistencia()
                    
                    Corriente2 = Itotal
                    Tension2 = Itotal * r3.getResistencia()
                    
                    Corriente3 = Itotal
                    Tension3 = Itotal * r4.getResistencia()
                    
                    Corriente4 = Itotal
                    Tension4 = Itotal * r5.getResistencia()
                    
                    Corriente5 = Itotal
                    Tension5 = Itotal * r6.getResistencia()
                    
                    Corriente6 = Itotal
                    Tension6 = Itotal * r7.getResistencia()
                    
                    Corriente7 = Itotal
                    Tension7 = Itotal * r8.getResistencia()
                    
                    Corriente8 = Itotal
                    Tension8 = Itotal * r9.getResistencia()

                elif r1.getTipo() == 2 and r2.getTipo() == 2 and r3.getTipo() == 2 and r4.getTipo() == 2  and r5.getTipo() == 2 and r6.getTipo() == 2 and r7.getTipo() == 2 and r8.getTipo() == 2  and r9.getTipo() == 2 or r1.getTipo() == 2 and r2.getTipo() == 2 and r3.getTipo() == 2 and r4.getTipo() == 2  and r5.getTipo() == 2 and r6.getTipo() == 2 and r7.getTipo() == 2 and r8.getTipo() == 2  and r9.getTipo() == 1:#Todo en paralelo
                        
                    Tension = source.getTension()
                    Corriente = Tension/r1.getResistencia()

                    Tension1 = source.getTension()
                    Corriente1 = Tension1/r2.getResistencia()

                    Tension2 = source.getTension()
                    Corriente2 = Tension2/r3.getResistencia()
                    
                    Tension3 = source.getTension()
                    Corriente3 = Tension3/r4.getResistencia()

                    Tension4 = source.getTension()
                    Corriente4 = Tension4/r5.getResistencia()

                    Tension5 = source.getTension()
                    Corriente5 = Tension5/r6.getResistencia()
                    
                    Tension6 = source.getTension()
                    Corriente6 = Tension6/r7.getResistencia()
                    
                    Tension7 = source.getTension()
                    Corriente7 = Tension7/r8.getResistencia()
                    
                    Tension8 = source.getTension()
                    Corriente8 = Tension8/r9.getResistencia()

                    



            elif cantResistencias == 10:

                if r1.getTipo() == 1 and r2.getTipo() == 1 and r3.getTipo() == 1 and r4.getTipo() == 1  and r5.getTipo() == 1 and r6.getTipo() == 1 and r7.getTipo() == 1 and r8.getTipo() == 1 and r9.getTipo() == 1 and r10.getTipo() == 1 or  r1.getTipo() == 1 and r2.getTipo() == 1 and r3.getTipo() == 1 and r4.getTipo() == 1  and r5.getTipo() == 1 and r6.getTipo() == 1 and r7.getTipo() == 1 and r8.getTipo() == 1 and r9.getTipo() == 1 and r10.getTipo() == 2:#Todo en serie

                                    
                    R = r1.getResistencia() + r2.getResistencia() + r3.getResistencia() + r4.getResistencia() + r5.getResistencia() + r6.getResistencia() + r7.getResistencia() + r8.getResistencia() + r9.getResistencia() + r10.getResistencia()

                    Itotal = source.getTension() / R

                    Corriente = Itotal
                    Tension = Itotal * r1.getResistencia()
                    
                    Corriente1 = Itotal
                    Tension1 = Itotal * r2.getResistencia()
                    
                    Corriente2 = Itotal
                    Tension2 = Itotal * r3.getResistencia()
                    
                    Corriente3 = Itotal
                    Tension3 = Itotal * r4.getResistencia()
                    
                    Corriente4 = Itotal
                    Tension4 = Itotal * r5.getResistencia()
                    
                    Corriente5 = Itotal
                    Tension5 = Itotal * r6.getResistencia()
                    
                    Corriente6 = Itotal
                    Tension6 = Itotal * r7.getResistencia()
                    
                    Corriente7 = Itotal
                    Tension7 = Itotal * r8.getResistencia()
                    
                    Corriente8 = Itotal
                    Tension8 = Itotal * r9.getResistencia()
                    
                    Corriente9 = Itotal
                    Tension9 = Itotal * r10.getResistencia()

                elif r1.getTipo() == 2 and r2.getTipo() == 2 and r3.getTipo() == 2 and r4.getTipo() == 2  and r5.getTipo() == 2 and r6.getTipo() == 2 and r7.getTipo() == 2 and r8.getTipo() == 2  and r9.getTipo() == 2 and r10.getTipo() == 2 or  r1.getTipo() == 2 and r2.getTipo() == 2 and r3.getTipo() == 2 and r4.getTipo() == 2  and r5.getTipo() == 2 and r6.getTipo() == 2 and r7.getTipo() == 2 and r8.getTipo() == 2  and r9.getTipo() == 2 and r10.getTipo() == 1:#Todo en paralelo
                
                    Tension = source.getTension()
                    Corriente = Tension/r1.getResistencia()

                    Tension1 = source.getTension()
                    Corriente1 = Tension1/r2.getResistencia()

                    Tension2 = source.getTension()
                    Corriente2 = Tension2/r3.getResistencia()
                    
                    Tension3 = source.getTension()
                    Corriente3 = Tension3/r4.getResistencia()

                    Tension4 = source.getTension()
                    Corriente4 = Tension4/r5.getResistencia()

                    Tension5 = source.getTension()
                    Corriente5 = Tension5/r6.getResistencia()
                    
                    Tension6 = source.getTension()
                    Corriente6 = Tension6/r7.getResistencia()
                    
                    Tension7 = source.getTension()
                    Corriente7 = Tension7/r8.getResistencia()
                    
                    Tension8 = source.getTension()
                    Corriente8 = Tension8/r9.getResistencia()
                                        
                    Tension9 = source.getTension()
                    Corriente9 = Tension9/r10.getResistencia()


        def Mouse(event):
            global mouse, Condicion

            if Condicion:

                mouse = (event.x, event.y)

            else:
                return

        def muestraDatos(): #Funcion encargada de colocar labels en los nodos donde el mouse sea posicionado

            
            global Tension, Tension1, Tension2, Tension3, Tension4 ,Tension5, Tension6, Tension7, Tension8, Tension9, GroundT, Condicion, cantResistencias

            global Corriente, Corriente1, Corriente2, Corriente3, Corriente4, Corriente5, Corriente6, Corriente7, Corriente8, Corriente9, GroundC, mouse

            
            if Condicion:

                
                #lb_Data
                
                lb_Data.place_forget()
                
                if mouse[0] > 117 and mouse[0] < 171 and mouse[1] > 40 and mouse[1] < 69 and cantResistencias >= 1: #Evalua la posicion del mouse en el 1 nodo
                    
                        
                    lb_Data.config(text = "Tension = " + str(Tension) + " V\nCorriente = " + str(Corriente) + " A")
                    lb_Data.place(x = mouse[0]+25, y = mouse[1]-25)
                    
                    
                elif mouse[0] > 135 and mouse[0] < 150 and mouse[1] > 230 and mouse[1] < 320 and cantResistencias >= 1: 
                    
                    lb_Data.config(text = "Tension = 0 V\nCorriente = " + str(Corriente) + " A")
                    lb_Data.place(x = mouse[0]+25, y = mouse[1]-25)

                    








                elif mouse[0] > 217 and mouse[0] < 271 and mouse[1] > 40 and mouse[1] < 69 and cantResistencias >= 2:#Evalua la posicion del mouse en el 2 nodo
                    
                    lb_Data.config(text = "Tension = " + str(Tension1) + " V\nCorriente = " + str(Corriente1) + " A")
                    lb_Data.place(x = mouse[0]+25, y = mouse[1]-25)
                    
                elif mouse[0] > 235 and mouse[0] < 250 and mouse[1] > 230 and mouse[1] < 320 and cantResistencias >= 2: 
                    
                    lb_Data.config(text = "Tension = 0 V\nCorriente = " + str(Corriente1) + " A")
                    lb_Data.place(x = mouse[0]+25, y = mouse[1]-25)













                elif mouse[0] > 317 and mouse[0] < 371 and mouse[1] > 40 and mouse[1] < 69 and cantResistencias >= 3:#Evalua la posicion del mouse en el 3 nodo
                    
                    lb_Data.config(text = "Tension = " + str(Tension2) + " V\nCorriente = " + str(Corriente2) + " A")
                    lb_Data.place(x = mouse[0]+25, y = mouse[1]-25)
                    
                elif mouse[0] > 335 and mouse[0] < 350 and mouse[1] > 230 and mouse[1] < 320 and cantResistencias >= 3: 
                    
                    lb_Data.config(text = "Tension = 0 V\nCorriente = " + str(Corriente2) + " A")
                    lb_Data.place(x = mouse[0]+25, y = mouse[1]-25)












                elif mouse[0] > 417 and mouse[0] < 471 and mouse[1] > 40 and mouse[1] < 69 and cantResistencias >= 4:#Evalua la posicion del mouse en el 4 nodo
                    
                    lb_Data.config(text = "Tension = " + str(Tension3) + " V\nCorriente = " + str(Corriente3) + " A")
                    lb_Data.place(x = mouse[0]+25, y = mouse[1]-25)
                    
                elif mouse[0] > 435 and mouse[0] < 450 and mouse[1] > 230 and mouse[1] < 320 and cantResistencias >= 4: 
                    
                    lb_Data.config(text = "Tension = 0 V\nCorriente = " + str(Corriente3) + " A")
                    lb_Data.place(x = mouse[0]+25, y = mouse[1]-25)













                    
                elif mouse[0] > 517 and mouse[0] < 571 and mouse[1] > 40 and mouse[1] < 69 and cantResistencias >= 5:#Evalua la posicion del mouse en el 5 nodo
                    
                    lb_Data.config(text = "Tension = " + str(Tension4) + " V\nCorriente = " + str(Corriente4) + " A")
                    lb_Data.place(x = mouse[0]+25, y = mouse[1]-25)
                    
                elif mouse[0] > 535 and mouse[0] < 550 and mouse[1] > 230 and mouse[1] < 320 and cantResistencias >= 5: 
                    
                    lb_Data.config(text = "Tension = 0 V\nCorriente = " + str(Corriente4) + " A")
                    lb_Data.place(x = mouse[0]+25, y = mouse[1]-25)















                    
                elif mouse[0] > 617 and mouse[0] < 671 and mouse[1] > 40 and mouse[1] < 69 and cantResistencias >= 6:#Evalua la posicion del mouse en el 6 nodo
                    
                    lb_Data.config(text = "Tension = " + str(Tension5) + " V\nCorriente = " + str(Corriente5) + " A")
                    lb_Data.place(x = mouse[0]+25, y = mouse[1]-25)
                    
                elif mouse[0] > 635 and mouse[0] < 650 and mouse[1] > 230 and mouse[1] < 320 and cantResistencias >= 6: 
                    
                    lb_Data.config(text = "Tension = 0 V\nCorriente = " + str(Corriente5) + " A")
                    lb_Data.place(x = mouse[0]+25, y = mouse[1]-25)














                    
                elif mouse[0] > 717 and mouse[0] < 771 and mouse[1] > 40 and mouse[1] < 69 and cantResistencias >= 7:#Evalua la posicion del mouse en el 7 nodo
                    
                    lb_Data.config(text = "Tension = " + str(Tension6) + " V\nCorriente = " + str(Corriente6) + " A")
                    lb_Data.place(x = mouse[0]+25, y = mouse[1]-25)
                    
                elif mouse[0] > 735 and mouse[0] < 750 and mouse[1] > 230 and mouse[1] < 320 and cantResistencias >= 7: 
                    
                    lb_Data.config(text = "Tension = 0 V\nCorriente = " + str(Corriente6) + " A")
                    lb_Data.place(x = mouse[0]+25, y = mouse[1]-25)














                elif mouse[0] > 817 and mouse[0] < 871 and mouse[1] > 40 and mouse[1] < 69 and cantResistencias >= 8:#Evalua la posicion del mouse en el 8 nodo
                    
                    lb_Data.config(text = "Tension = " + str(Tension7) + " V\nCorriente = " + str(Corriente7) + " A")
                    lb_Data.place(x = mouse[0]+25, y = mouse[1]-25)
                    
                elif mouse[0] > 835 and mouse[0] < 850 and mouse[1] > 230 and mouse[1] < 320 and cantResistencias >= 8: 
                    
                    lb_Data.config(text = "Tension = 0 V\nCorriente = " + str(Corriente7) + " A")
                    lb_Data.place(x = mouse[0]+25, y = mouse[1]-25)













                elif mouse[0] > 917 and mouse[0] < 971 and mouse[1] > 40 and mouse[1] < 69 and cantResistencias >= 9:#Evalua la posicion del mouse en el 9 nodo
                    
                    lb_Data.config(text = "Tension = " + str(Tension8) + " V\nCorriente = " + str(Corriente8) + " A")
                    lb_Data.place(x = mouse[0]+25, y = mouse[1]-25)
                    
                elif mouse[0] > 935 and mouse[0] < 950 and mouse[1] > 230 and mouse[1] < 320 and cantResistencias >= 9: 
                    
                    lb_Data.config(text = "Tension = 0 V\nCorriente = " + str(Corriente8) + " A")
                    lb_Data.place(x = mouse[0]+25, y = mouse[1]-25)










                    
                elif mouse[0] > 1017 and mouse[0] < 1071 and mouse[1] > 40 and mouse[1] < 69 and cantResistencias >= 10: #Evalua la posicion del mouse en el 10 nodo
                    
                    lb_Data.config(text = "Tension = " + str(Tension9) + " V\nCorriente = " + str(Corriente9) + " A")
                    lb_Data.place(x = mouse[0]+25, y = mouse[1]-25)
                    
                elif mouse[0] > 1035 and mouse[0] < 1050 and mouse[1] > 230 and mouse[1] < 320 and cantResistencias >= 10:
                    
                    lb_Data.config(text = "Tension = 0 V\nCorriente = " + str(Corriente9) + " A")
                    lb_Data.place(x = mouse[0]+25, y = mouse[1]-25)


                WindGame.after(10,lambda:muestraDatos())



                
            else:
                return

        

                
                

            

        def StopSimular():
            global Condicion

            Condicion = False
            
            btn_Stop.place_forget()
            btn_SourceEdit.place(x = 955, y = 690)
            btn_SR.place(x = 955, y = 590)
            btn_SR2.place(x = 955, y = 490)
            btn_Simulate.place(x = 666, y = 590)

            

            
        #End Emulador


        
#End Class General
      
General.Principal()



















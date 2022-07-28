from math import pi, factorial as fact, sqrt
import tkinter as tk
from pynput import keyboard as kb

operacion=""


def borrar():
	global operacion
	operacion=operacion[:-1]
	if operacion:
		displayCalc.set(operacion)
	else:
		displayCalc.set('0')

def limpiarPantalla():
	global operacion
	operacion=""
	displayCalc.set('0')

def insertar(operador):
	global operacion

	if (operador=="0" and operacion=="") or (operador=="0" and operacion and operacion[-1].isdigit()!=True) : #Impide ingresar ceros a la izquierda
		return

	try:

		if operacion and (operador=="sqrt(" or operador=="fact(") and float(operacion) : #Si hay solo numero ingresado, lo coloca entre los parentesis de estos operadores
			operacion=operador+operacion
		else:
			operacion+=operador

		
	except ValueError:
		operacion+=operador
	finally:
		displayCalc.set(operacion)

def resolver():
	global operacion
	try:
		resultado=eval(operacion)
		displayCalc.set(resultado)
		operacion=str(resultado)
	except ZeroDivisionError:
		displayCalc.set("ERR ZERO DIV")
		operacion=""
	except SyntaxError:
		displayCalc.set("SYNTAX ERR")
		operacion=""

def callback(event):

	tecla=str(event.keysym)
	if tecla.isdigit():
		insertar(str(event.keysym))
	elif tecla=="Return":
		resolver()
	elif tecla=="Delete":
		limpiarPantalla()
	elif tecla=="BackSpace":
		borrar()
	elif tecla=="plus":
		insertar('+')
	elif tecla=="minus":
		insertar('-')
	elif tecla=="slash":
		insertar('/')
	elif tecla=="asterisk":
		insertar('*')
	elif tecla=="parenleft":
		insertar('(')
	elif tecla=="parenright":
		insertar(')')
	elif tecla=="exclam":
		insertar('fact(')
	elif tecla.lower()=="p":
		insertar(str(pi))		

	#print(str(event.keysym))

	return

def pulsa(tecla): #Función para usar con el listener de pynput

	#print(tecla)

	try:
		if 106>int(str(tecla)[1:-1])>95:
			insertar(str(int(str(tecla)[1:-1])-96))
	except Exception as e:
		if str(tecla)[1:-1]=='+' or str(tecla)[1:-1]=='-' or str(tecla)[1:-1]=='*' or str(tecla)[1:-1]=='/' or str(tecla)[1:-1]=='(' or str(tecla)[1:-1]==')':
			insertar(str(tecla)[1:-1])
		elif str(tecla)=='Key.enter':
			resolver()
		elif str(tecla)=='Key.delete':
			limpiarPantalla()
		elif str(tecla)=='Key.backspace':
			borrar()
	else:
		pass
	finally:
		pass


mainWindow=tk.Tk()
mainWindow.config(height=400,width=320)
mainWindow.title("Calculadora")
mainWindow.resizable(0,0)

mainWindow.bind_all('<Key>',callback) #Produce un evento cuando se presiona cualquier tecla y llama a la función callback

displayCalc=tk.StringVar()
displayCalc.set('0')

displayEntry=tk.Entry(bd=20,font=["arial",20,"bold"],state=tk.DISABLED, textvariable=displayCalc,justify='right')
displayEntry.place(height=70,width=300,x=10,y=10)

boton1=tk.Button(height=3,width=5,text="1",command=lambda:insertar("1"))
boton2=tk.Button(height=3,width=5,text="2",command=lambda:insertar("2"))
boton3=tk.Button(height=3,width=5,text="3",command=lambda:insertar("3"))
boton4=tk.Button(height=3,width=5,text="+",command=lambda:insertar("+"))

boton1.place(x=20,y=80)
boton2.place(x=80,y=80)
boton3.place(x=140,y=80)
boton4.place(x=200,y=80)

boton5=tk.Button(height=3,width=5,text="4",command=lambda:insertar("4"))
boton6=tk.Button(height=3,width=5,text="5",command=lambda:insertar("5"))
boton7=tk.Button(height=3,width=5,text="6",command=lambda:insertar("6"))
boton8=tk.Button(height=3,width=5,text="-",command=lambda:insertar("-"))
boton9=tk.Button(height=3,width=5,text="(",command=lambda:insertar("("))

boton5.place(x=20,y=140)
boton6.place(x=80,y=140)
boton7.place(x=140,y=140)
boton8.place(x=200,y=140)
boton9.place(x=260,y=140)

boton10=tk.Button(height=3,width=5,text="7",command=lambda:insertar("7"))
boton11=tk.Button(height=3,width=5,text="8",command=lambda:insertar("8"))
boton12=tk.Button(height=3,width=5,text="9",command=lambda:insertar("9"))
boton13=tk.Button(height=3,width=5,text="X",command=lambda:insertar("*"))
boton14=tk.Button(height=3,width=5,text=")",command=lambda:insertar(")"))

boton10.place(x=20,y=200)
boton11.place(x=80,y=200)
boton12.place(x=140,y=200)
boton13.place(x=200,y=200)
boton14.place(x=260,y=200)

boton15=tk.Button(height=3,width=5,text="<-",command=borrar)
boton16=tk.Button(height=3,width=5,text="0",command=lambda:insertar("0"))
boton17=tk.Button(height=3,width=5,text=".",command=lambda:insertar("."))
boton18=tk.Button(height=3,width=5,text="/",command=lambda:insertar("/"))
boton19=tk.Button(height=3,width=5,text="CLR",command=limpiarPantalla)

boton15.place(x=20,y=260)
boton16.place(x=80,y=260)
boton17.place(x=140,y=260)
boton18.place(x=200,y=260)
boton19.place(x=260,y=260)

boton20=tk.Button(height=3,width=5,text="SQRT",command=lambda:insertar("sqrt("))
boton21=tk.Button(height=3,width=5,text="^",command=lambda:insertar("**"))
boton22=tk.Button(height=3,width=5,text="!",command=lambda:insertar("fact("))
boton23=tk.Button(height=3,width=5,text="PI",command=lambda:insertar(str(pi)))
boton24=tk.Button(height=3,width=5,text="=",command=resolver)

boton20.place(x=20,y=320)
boton21.place(x=80,y=320)
boton22.place(x=140,y=320)
boton23.place(x=200,y=320)
boton24.place(x=260,y=320)

#escuchador = kb.Listener(pulsa)
#escuchador.start()

mainWindow.mainloop()

#escuchador=False


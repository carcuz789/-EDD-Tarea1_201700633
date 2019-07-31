import os
print("RODRIGO EDUARDO CARCUZ ORTEGA 201700633")

print("lista enlazada simple ")
 #lista enlazada en python#
class Nodo:
	
	def init(self,dato):
	    self.siguiente=None
	    self.info=dato

	def verNodo(self):
		return self.info


class Lista:
	def init(self):
	    self.primero=None

	def vacia(self):
		if self.primero==None:
			return True
		else:
			return False


	def InsertarPrimero(self,dato):
		temporal=Nodo(dato)
		temporal.siguiente=self.primero
		self.primero=temporal

	def listar(self):
		print("***********")
		temporal=self.primero
		while temporal!=None:
			print(temporal.verNodo(),end=' ')
			temporal=temporal.siguiente

	def borrarPrimero(self):
		 if self.vacia()	==False:	
		    self.primero=self.primero.siguiente

	def borrarUltimo(self):
		anterior=self.primero
		actual=self.primero
		while actual.siguiente!=None:
			 anterior=actual
			 actual=actual.siguiente
	         anterior.siguiente=None



	def borrarPosicion(self,pos):
        anterior=self.primero
		actual=self.primero
		k=0
		if pos>0:
			while k!= pos and actual.siguiente != None:
				anterior =actual
				actual=self.primero
				k+=1
		    if k==pos:
				anterior.siguiente=actual.siguiente


    def menu():
        os.system('cls')
		print("\t1 - ingresar al nodo")
		print("\t2 - borrar primero")
		print("\t3 -borrar ultimo")
		print("\t4 - borrar posicion")
		print("\t5 - imprimir lista")
		print("\t6 - salir")
listas = Lista()
    while True:
		menu()
		opcionmenu= input("Insertar un numero")
		if opcionmenu=="1":
			print("") 
			in1= input("ingrese lo que contendra el nodo")
			listas.InsertarPrimero(in1) 
			input("pulsa tecla para continuar")

        elif opcionmenu=="2":
			print("")
			listas.borrarPrimero()
            input("pulsa tecla para continuar")

		elif opcionmenu=="3":
			listas.borrarUltimo()
			print("")
			input ("pulsa tecla para continuar")
		elif opcionmenu=="4":
			print("")
			pos=input("ingrese la posicion a borrar")
			listas.borrarPosicion(pos)
		elif opcionmenu=="5":
		    print("")
			listas.listar()
		elif opcionmenu=="6":
			break
		else: 
			print("")
			input("pulsa una opcion valida")


				
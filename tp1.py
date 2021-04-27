const = 123
contContra = 0
contR = 0
contC = 0
contBA = 0
max = 0
x = int(input("1. Empresas 2. Clientes 0. Salir"))
if x == 1:
print("ingrese clave")
while contContra < 3:
	 	 
	   
	y = int(input())
	if y==const:
	print("Oprima 1 para alta de empresa 0. para ir al menú principal")
	c = int(input())
		if c == 1:
			while codEmp != 0:
			print("ingrese nombre")
			nombre = str(input())
			print("ingrese Dirección")
			direccion = str(input())
			print("ingrese Mail")
			mail = str(input())
			print("ingrese COD/CIUDAD")
			codCiudad = str(input())
			print("ingrese Nombre Ciudad")
			nombreCiudad = str(input())
			if codCiudad =="ROS":
				contR = contR + 1
			elif codCiudad == "BA":
				contBA = contBA +1
			else contC = contC + 1

			if contR > max:
			 	max = contR
				nMax = nombreCiudad
			elif contC > max:
				max = contC
				nMax = nombreCiudad

			elif contBA > max:
				max = contBA
				nMax = nombreCiudad
			print("ingrese COD/EMP o 0 para volver al menú principal")
			 codEmp = int(input())
		print("la ciudad que tiene mas empresas desarrolladoras es:",nMax,"y la cantidad es",max)
		
	
	else:
		print("contraseña incorrecta intente nuevamente")
		contContra == contContra + 1 
	if contContra == 3 :

	   print("ha superado el numero maximo de intentos")

				
elif x == 2 :
	print("Programa en proceso")		

else x == 0:
	print("Gracias por su visita")
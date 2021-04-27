const = 123
contContra = 0
contR = 0
contBA = 0
contC = 0
max = 0
x = int(input("1.Empresas 2.Clientes 0.Salir:"))
if x==1:
	print("ingrese clave")
	for contContra in range(3):
		y = int(input())
		if y==const:
			print("oprima 1 para alta de Empresas 0 para ir al menú principal")
			c = int(input())
			if c == 1:
				while codEmp!=0:
					codEmp=int(input("ingrese codigo de empresa o 0 para volver al menú principal"))
					nombre=str(input("ingrese nombre"))
					direccion=str(input("ingrese dirección"))
					mail=str(input("ingrese mail"))
					codCiudad = str(input("ingrese COD/CIUDAD"))
					nombreCiudad=str(input("ingrese el nombre de la ciudad"))
					if codCiudad=="ROS":
						contR==contR+1
					elif codCiudad=="CBA":
						contC==contC+1
					elif codCiudad=="BA":
						contBA==contBA+1

					if contR>max:
						max == contR
						nMax == "Rosario"
					elif contBA>max:
						max == contBA
						nMax == "Buenos Aires"
					elif contC>max:
						max == contC
						nMax == "Córdoba"
							

						

					
				print("la ciudad que tiene más empresas desarrolladoras es",nMax,"y tiene",max)
				print("la ciudad de Rosario tiene ",contR,",la ciudad de Córdoba tiene ",contC,"y la ciudad de Buenos Aires tiene ",contBA)
		else:
			print("contraseña incorrecta intente nuevamente")
			contContra==contContra+1
			if contContra==2:
				print("ha superado el maximo de intentos posibles")

elif x == 2:
	print("programa en proceso")

				

			



   
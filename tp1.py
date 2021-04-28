const = 123
contContra = 0
contR = 0
contBA = 0
contC = 0
codEmp=1
max = 0
x = int(input("1.Empresas 2.Clientes 0.Salir:"))
while x!=0:

	
	if x==1:
		for contContra in range(3):
			y = int(input("ingrese clave: "))
			if y==const:
				print()
				c = int(input("oprima 1 para alta de Empresas 0 para salir: "))
				if c == 1:
					codEmp=int(input("ingrese codigo de empresa: "))
					while codEmp!=0:
						
						nombre=str(input("ingrese nombre: "))
						direccion=str(input("ingrese dirección: "))
						mail=str(input("ingrese mail: "))
						codCiudad = str(input("ingrese COD/CIUDAD (BA,CBA o ROS,)):"))
						while codCiudad != "BA" and codCiudad != "ROS" and codCiudad!= "CBA":
						 	 
							print("el dato ingresado no tiene un formato válido ")
							codCiudad = str(input("ingrese COD/CIUDAD (BA,CBA o ROS,)):"))

						nombreCiudad=str(input("ingrese el nombre de la ciudad:"))
						if codCiudad=="ROS":
							contR=contR+1
						elif codCiudad=="CBA":
							contC=contC+1
						elif codCiudad=="BA":
							contBA=contBA+1

						if contR>max:
							max = contR
							nMax = nombreCiudad
						elif contBA>max:
							max = contBA
							nMax = nombreCiudad
						elif contC>max:
							max = contC
							nMax = nombreCiudad
						codEmp=int(input("ingrese codigo de empresa o 0 para salir"))		

							

						
					print("la ciudad que tiene más empresas desarrolladoras es",nMax,"y tiene",max)
					print("la ciudad de Rosario tiene ",contR,",la ciudad de Córdoba tiene ",contC,"y la ciudad de Buenos Aires tiene ",contBA)
			
				elif c==0:
					print("gracias, vuelva prontos")
					raise SystemExit

			else:
				
				contContra==contContra+1
				if contContra==0:
					print("contraseña incorrecta intente nuevamente")
			
				if contContra==1:
					print("le queda un intento")
					
				if contContra==2:
					print("ha superado el maximo de intentos posibles")
					raise SystemExit
			

	elif x == 2:
		print("programa en proceso")
		raise SystemExit
if x==0:
		print("gracias, vuelva prontos")		

			



   
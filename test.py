#proyectoIntegrador.py
import sqlite3
import subprocess
subprocess.run("python3", "david.py")
#%--------------------------------------%#
def crearTabla():
	
	conexion = sqlite3.connect("INVENTARIO.db")		#se implementarán mayúsculas y doble comillas
	cursor = conexion.cursor()						#para SQLite
	
	cursor.execute("""CREATE TABLE IF NOT EXISTS PRODUCTOS (
	'ID' NOT NULL UNIQUE,
	'MARCA' TEXT NOT NULL,
	'DESCRIPCION' TEXT NOT NULL,
	'PRECIO' REAL,
	'STOCK' INTEGER NOT NULL,
	'UBICACION' INTEGER,
	'PROVEEDOR' TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT))
	""")
	
	conexion.close()
#%--------------------------------------%#
def menuPrincipal():
	
	menuPrincipal	=	[	'|1> Ver inventario.\t\t\t\t|',
							'|2> Añadir producto al inventario.\t\t|',
							'|3> Actualizar producto del inventario.\t\t|',
							'|4> Eliminar producto del inventario.\t\t|',
							'|5> Buscar producto en el inventario.\t\t|',
							'|6> Ayuda/FAQ\t\t\t\t\t|',
							'|7> Salir.\t\t\t\t\t|\n'						]

	print(	'\n\n#################################################\n'
			'|\t\t\t\t\t\t|\n'
			'|Seleccione una de las siguientes opciones:	|\n'
			'|\t\t\t\t\t\t|\n'										)
	
	for i in menuPrincipal:
		print(i)
	
	print(	'|\t\t\t\t\t\t|\n'
			'#################################################'		)	
		
	opcion = controlOpciones(menuPrincipal)
#%--------------------------------------%#
def mostrarProductos():
	
	menuMostrar = [	'1> Mostrar todos los productos.',
					'2> Mostrar productos fuera de stock.',
					'3> Mostrar productos sin precio.',
					'4> Mostrar productos sin ubicar.',
					'5> Volver al menú principal.'			]
	
	print('Seleccione una de las siguientes opciones: ')
	
	for i in menuMostrar:
		print(i)
#%--------------------------------------%#
def controlOpciones(menuActual):
	
	while True:
		
				try:			#verificar ingreso numérico y dentro del rango de opciones dado
					opcion = int(input('\nSeleccione una de las opciones: '))
					if 0 < opcion <= len(menuActual):
						return(opcion)
						break
					else:
						print('\nLa opción ingresada no es válida\n')
						continue
				
				except ValueError:
					print('\nLa opción ingresada no es válida.\n')
					continue
#%--------------------------------------%#
#inicio
crearTabla()
opcion = ''
while opcion != 7:
	menuPrincipal()

	opcion = menuPrincipal()
	
	if opcion == 1:
		mostrarProductos()
		continue
		
	elif opcion == 2:
		añadirProductos()
		continue
		
	elif opcion == 3:
		actualizarProductos()
		continue
		
	elif opcion == 4:
		
	elif opcion == 5:
		
	elif opcion == 6:
		
print('Finalizando...')


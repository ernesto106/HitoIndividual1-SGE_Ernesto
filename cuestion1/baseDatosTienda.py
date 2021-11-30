import sqlite3


# Funciones CRUD para hacer operaciones dentro de la base de datos

def crear_tabla():
    cursor.execute("CREATE TABLE IF NOT EXISTS clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, apellidos TEXT, fechaNacimiento TEXT ,edad INTEGER, telefono TEXT)")
    conexion.commit() # guardamos los cambios hechos dentro de la base de datos

def insert():

    cursor.execute("INSERT INTO clientes (nombre, apellidos, fechaNacimiento, edad, telefono) VALUES('Ernesto', 'Benito García', '1993-10-10', 28, '687238728')")
    conexion.commit()

def update():

 cursor.execute("UPDATE clientes SET nombre = 'Juan' where id = 1")
 conexion.commit()


def select():
 datos=cursor.execute("SELECT * FROM clientes")
 conexion.commit()

 for i in datos:
  print(i)

def delete():
 cursor.execute("DELETE FROM clientes where id=1")
 conexion.commit()



# ============= A continuación utilizamos las diferentes funciones para operar dentro de la base de datos ==============

try:
    conexion = sqlite3.connect('tienda.db') # Conectamos a la base de datos
    cursor = conexion.cursor()
    print("Conexión establecida con éxito") # Si conectamos con éxito, mostramos este mensaje por pantalla

    # Por favor, comente/descomente las diferentes consultas para ejecutarlas una por una y que no haya conflicto

    crear_tabla()
    #insert()
    #update()
    #select()
    #delete()

    cursor.close() #Cerramos el cursor, puesto que ya no vamos a hacer más consultas

except sqlite3.Error as error:
    print("Error", error) # Si ocurre algun error lo capturamos y mostramos la descripcion del error

finally:
    if (conexion):
        conexion.close() # Nos aseguramos siempre de cerrar la conexion con la base de datos
        print("Conexión cerrada")


















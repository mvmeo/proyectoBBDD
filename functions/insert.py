import psycopg2


def insertar_bicicleta():
    try:
        
    #Establecer conexion
        print("Conectando a la base de datos :D")
        print(" ")
        conn = psycopg2.connect(
            database="samuel_proyecto",
            user="insert_user_here",
            password="insert_password_here",
            host="insert_host_here",
            port="5432"
        )

        cursor = conn.cursor()


        print("Listo! Conectado.")
        print(" ")
    #----

        print("Ingresa los siguientes datos a la tabla:")
        print("Numero de serie:")
        numero_serie = input()
        print("Marca:")
        marca = input()
        print("Modelo:")
        modelo = input()
        print("Disciplina:")
        disciplina = input()
        print("Color:")
        color = input()
        print("Precio:")
        precio = input()
        print("Talla:")
        talla = input()
        print("RUT del cliente:")
        rut_cliente = input()
        print("RUT de la tienda:")
        rut_tienda = input()

        insert_query = "INSERT INTO bicicleta (numero_serie, marca, modelo, disciplina, color, precio, talla, rut_cliente, rut_tienda) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
        cursor.execute(insert_query, (numero_serie, marca, modelo, disciplina, color, precio, talla, rut_cliente, rut_tienda))

        print("")
        
        conn.commit()
        print("Datos insertados exitosamente en la tabla bicicleta")
        print("")

    except (Exception, psycopg2.Error) as error:
        print("Error en conectarse a la base de datos :(", error)

    finally:

        if conn:
            cursor.close()
            conn.close()
            print("Conexion a la base de datos finalizada.")


def insertar_cliente():
    try:

    #Establecer conexion
        print("Conectando a la base de datos :D")
        print(" ")
        conn = psycopg2.connect(
            database="samuel_proyecto",
            user="insert_user_here",
            password="insert_password_here",
            host="insert_host_here",
            port="5432"
        )

        cursor = conn.cursor()


        print("Listo! Conectado.")
        print(" ")
    #----

        print("Ingresa los siguientes datos a la tabla:")
        print("RUT:")
        rut = input()
        print("Nombre:")
        nombre = input()
        print("Apellido:")
        apellido = input()
        print("Numero_telefono:")
        numero_telefono = input()
        print("Email:")
        email = input()

        insert_query = '''INSERT INTO cliente (rut, nombre, apellido, numero_telefono, email) VALUES (%s,%s,%s,%s,%s)'''
        cursor.execute(insert_query, (rut, nombre, apellido, numero_telefono, email))
        
        print("")
        
        conn.commit()
        print("Datos insertados exitosamente en la tabla cliente")
        print("")

    except (Exception, psycopg2.Error) as error:
            print("Error en conectarse a la base de datos :(", error)

    finally:

        if conn:
            cursor.close()
            conn.close()
            print("Conexion a la base de datos finalizada.")


def insertar_tienda():

    try:
    #Establecer conexion
        print("Conectando a la base de datos :D")
        print(" ")
        conn = psycopg2.connect(
            user="insert_user_here",
            password="insert_password_here",
            host="insert_host_here",
            port="5432"
        )

        cursor = conn.cursor()


        print("Listo! Conectado.")
        print(" ")
    #----

        print("Ingresa los siguientes datos a la tabla:")
        print("RUT:")
        rut = input()
        print("Nombre:")
        nombre = input()
        print("Dirección:")
        direccion = input()
        print("Comuna:")
        comuna = input()
        print("Región:")
        region = input()

        insert_query = '''INSERT INTO tienda (rut, nombre, direccion, comuna, region) VALUES (%s,%s,%s,%s,%s)'''
        cursor.execute(insert_query, (rut, nombre, direccion, comuna, region))
        
        print("")
        
        conn.commit()
        print("Datos insertados exitosamente en la tabla tienda")
        print("")

    except (Exception, psycopg2.Error) as error:
        print("Error en conectarse a la base de datos :(", error)

    finally:

        if conn:
            cursor.close()
            conn.close()
            print("Conexion a la base de datos finalizada.")

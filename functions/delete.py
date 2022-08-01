import psycopg2

def delete():
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

        print("Ingresa el numero de serie del producto a eliminar de la tabla:")
        numero_serie = input()

        delete_query = '''DELETE FROM bicicleta WHERE numero_serie=%s'''%numero_serie
        cursor.execute(delete_query)
        
        print("")
        
        conn.commit()
        print("Datos eliminados exitosamente en la tabla bicicleta")
        print("")

    except (Exception, psycopg2.Error) as error:
        print("Error en conectarse a la base de datos :(", error)

    finally:

        if conn:
            cursor.close()
            conn.close()
            print("Conexion a la base de datos finalizada.")

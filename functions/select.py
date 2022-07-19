import psycopg2

def select_bicicletas():
    

    try:
        print("Conectando a la base de datos :D")
        print(" ")
        conn = psycopg2.connect(
            database="samuel_proyecto",
            user="alumno",
            password="alumno",
            host="157.245.180.1",
            port="5432"
        )

        cursor = conn.cursor()

        print("Ingresa el nombre a buscar:")
        nombre = input()

        select_query = '''  SELECT modelo 
                            FROM bicicleta JOIN cliente 
                            ON bicicleta.rut_cliente=cliente.rut 
                            WHERE nombre=%s;'''
        cursor.execute(select_query, (nombre,))
        
        rows = cursor.fetchall()
        rows=[i[0] for i in rows]
        
        
        print("--------")
        print("Tiene:")
        
        for bicicleta in rows:

            print("- " + bicicleta)

        print("")

    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse con la base de datos", error)

    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Conexion a la base de datos finalizada.")

def select_disciplinas():

    try:

        print("Conectando a la base de datos :D")
        print(" ")
        conn = psycopg2.connect(
            database="samuel_proyecto",
            user="alumno",
            password="alumno",
            host="157.245.180.1",
            port="5432"
        )

        cursor = conn.cursor()


        print("Listo! Conectado.")
        print(" ")

        #MUESTRA LAS BICICLETAS DEL CLIENTE
        print("Ingresa el nombre a buscar:")
        nombre = input()
        print("--------")

        select_query = '''SELECT disciplina 
                            FROM bicicleta JOIN cliente 
                            ON bicicleta.rut_cliente=cliente.rut 
                            WHERE nombre=%s;'''
        cursor.execute(select_query, (nombre,))
        
        rows = cursor.fetchall()
        rows=[i[0] for i in rows]

        
        print("Practica: ")

        for disciplina in rows:
            print("- " + disciplina)

    except (Exception, psycopg2.Error) as error:
        print("Error en conectarse con la base de datos", error)

    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Conexion a la base de datos finalizada.")
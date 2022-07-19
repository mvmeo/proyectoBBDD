import psycopg2

def talla_s(talla):
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

        select_query = '''  SELECT COUNT(talla) 
                            FROM bicicleta
                            WHERE talla='%s';'''%talla.upper()
        cursor.execute(select_query)
        rows = cursor.fetchall()
        rows=[i[0] for i in rows]

        for talla in rows:

            print(talla)
        

    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse con la base de datos", error)

    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Conexion a la base de datos finalizada.")


def talla_m(talla):
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

        select_query = '''  SELECT COUNT(talla) 
                            FROM bicicleta
                            WHERE talla='%s';'''%talla.upper()
        cursor.execute(select_query)
        rows = cursor.fetchall()
        rows=[i[0] for i in rows]

        for talla in rows:

            print(talla)
        

    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse con la base de datos", error)

    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Conexion a la base de datos finalizada.")

def talla_l(talla):
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

        select_query = '''  SELECT COUNT(talla) 
                            FROM bicicleta
                            WHERE talla='%s';'''%talla.upper()
        cursor.execute(select_query)
        rows = cursor.fetchall()
        rows=[i[0] for i in rows]

        for talla in rows:

            print(talla)
        

    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse con la base de datos", error)

    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Conexion a la base de datos finalizada.")
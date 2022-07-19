import psycopg2


def update():
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

        print("Ingresa los siguientes datos a la tabla:")
        print("Numero de serie:")
        numero_serie = input()
        print("Precio nuevo:")
        precio = input()

        update_query = '''  UPDATE bicicleta
                            SET precio = %s
                            WHERE numero_serie = %s'''
        cursor.execute(update_query, (precio, numero_serie))
        conn.commit()
        print("Precio actualizado.")

    except (Exception, psycopg2.Error) as error:
        print("Error al actualizar el precio", error)

    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Conexion a la base de datos finalizada.")
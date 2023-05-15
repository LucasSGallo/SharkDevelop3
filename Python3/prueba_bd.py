import psycopg2
conexion = psycopg2.connect(
    user='postgres',
    password='*****',
    host=127.0.0.1, #'localhost'
    port=5432,
    dadabase='test_db'
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            cursor = conexion.cursor()
            cursor.execute('SELECT * FROM tb_persona WHERE id_persona = %s',input('Digite el id que necesite')) #place holder (marcador de lugar)
            registros = cursor.fetchone()
            print(registros)
except Exception as e:
        print(f"Ocurrió un error: {e}")
finally:
        #cursor.close() esto ya lo hace el with
        conexion.close() # pero esto no

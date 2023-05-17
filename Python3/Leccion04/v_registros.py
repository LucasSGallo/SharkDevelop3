import psycopg2 # Esto es para poder conectarnos a postgret

conexion = psycopg2.connect(
    user = 'postgres', password= 'admin',host='127.0.0.1',port='5432', database= 'test_bd'

) #creamos variable para conectar con la base de datos

#https://www.psycopg.org/docs/usage.html#with-statement
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona IN (1,2,3,4,5,6,7)' #placeholder
           # id_persona = input('Ingrese un numero para el id_persona: ')
            cursor.execute(sentencia) #de esta manwera ejecutamos la sentencia
            registros = cursor.fetchall() #cupera todos los registros de la sentencia
            for registro in registros:
                print(registro)

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
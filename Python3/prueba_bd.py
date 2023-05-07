import mysql.connector

miConexion=mysql.connector.connect(
    user='',
    host='localhost',
    port= '3306',
    database='test_bd',
)
#print(miConexion)
cur =miConexion.cursor()
sentencia='SELECT * FROM Persona ORDER BY id_persona ASC'
cur.execute(sentencia)
registros=cur.fetchall()
print(registros)

cur.close()
miConexion.close()
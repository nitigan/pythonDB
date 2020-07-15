import psycopg2
try:
    connection = psycopg2.connect(user="postgres",password="INE@2562",host="127.0.0.1",port="5432",database="postgres")
    connection.autocommit = True
    
    cursor = connection.cursor()

    sql = '''CREATE database mydb'''
    cursor.execute(sql)
    print(" Database created successfully....... ")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL",error)

finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
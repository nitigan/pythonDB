import psycopg2

try:
    connection = psycopg2.connect(user="postgres",password="INE@2562",host="127.0.0.1",port="5432",database="mydb")
    connection.autocommit = True
    
    cursor = connection.cursor()

    postgres_insert_query = """ INSERT INTO registration (student_id, subject_id, year, semester, grade) VALUES (%s,%s,%s,%s,%s) """
    record_to_insert = ('6207011956044','060233104','4','1','D')

    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()
    count = cursor.rowcount
    print(count, " Record inserted successfully into registration table ")

except (Exception, psycopg2.Error) as error:
    if(connection):
        print("Failed to insert record into students table",error)

finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
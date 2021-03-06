import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="postgres",password="INE@2562",host="127.0.0.1",port="5432",database="mydb")
    connection.autocommit = True
    
    cursor = connection.cursor()

    create_table_query = '''CREATE TABLE Registration
                            (student_id CHAR(13) NOT NULL,
                             subject_id VARCHAR(15) NOT NULL,
                             year       CHAR(4) NOT NULL,
                             semester   CHAR(1) NOT NULL,
                             grade      CHAR(2) ); '''

    cursor.execute(create_table_query)
    connection.commit()
    print(" Table created successfully in PostgreSQL ")

except (Exception, psycopg2.DatabaseError) as error:
    print("Error while create PostgreSQL table",error)

finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
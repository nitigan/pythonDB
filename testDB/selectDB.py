import psycopg2

def getStudentDetails(name):
    try:
        connection = psycopg2.connect(user="postgres",password="INE@2562",host="127.0.0.1",port="5432",database="mydb")
        
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from students where f_name = %s"

        cursor.execute(postgreSQL_select_Query, (name,))

        print("Selecting rows from students table using cursor.fetchall")
        student_records = cursor.fetchall()

        print("Print each row and it's columns values")
        for row in student_records:
            print("student_id = ", row[0])
            print("f_name = ", row[1])
            print("l_name = ", row[2])
            print("e_mail = ", row[3],"\n")

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL",error)
    
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

getStudentDetails('Nitigan')
getStudentDetails('Kawisara')
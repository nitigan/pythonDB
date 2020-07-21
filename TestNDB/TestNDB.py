import psycopg2
try:
    connection = psycopg2.connect(user="webadmin",
                                password="SPYatb32373",
                                host="node1247-rachpython.th.app.ruk-com.cloud",
                                database="postgres")
    connection.autocommit = True

    cursor = connection.cursor()

    sql = '''CREATE database TestDB'''

    cursor.execute(sql)
    print("Database created successfully.....")

except (Exception, psycopg2.Error) as error:
    print("Error while connection to PostgreSQL",error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
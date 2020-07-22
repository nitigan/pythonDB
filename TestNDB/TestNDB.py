import psycopg2
try:
    connection = psycopg2.connect(user="webadmin",
                                password="IYDdro59112",
                                host="node1418-nitigan.app.ruk-com.cloud",
                                port="11020",
                                database="postgres")
    connection.autocommit = True

    cursor = connection.cursor()

    sql = '''CREATE database TestDB4'''

    cursor.execute(sql)
    print("Database created successfully.....")

except (Exception, psycopg2.Error) as error:
    print("Error while connection to PostgreSQL",error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
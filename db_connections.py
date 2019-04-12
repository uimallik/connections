import cx_Oracle
import psycopg2

def oracle_connection_query(query):
    connection = db.pool.aquire()
    cursor = connection.cursor()
    cursor.execute(query)
    response = cursor.fetchall()
    cursor.close()
    db_pool.release(connection)
    return response

db_pool = cx_Oracle.SessionPool('username','password','db_server')

result = oracle_connection_query('Select * from ...')
print(result)


def postgres_connection_query(query):
    try:
        conn = psycopg2.connect("dbname='template1' user='dbuser' host='localhost' password='dbpass'")
    except:
        print "I am unable to connect to the database"
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()
    return "Success"

inserting = postgres_connection_query('Insert into..',result)

print(inserting)


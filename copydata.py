import psycopg2
import requests


# Add the URL of the file which has select query
query_to_get_data = requests.get("URL for storage")



# DB Server connection
def postgres_connection_query(query):
    try:
        conn = psycopg2.connect(dbname='template1', user='dbuser', host='localhost', password='dbpass')
    except:
        print "I am unable to connect to the database"
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()
    return "Success"

# Adding target tablename 
query_to_insert_data = "insert into table_name  "+query_to_get_data  


postgres_connection_query(query_to_insert_data)

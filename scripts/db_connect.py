import psycopg2

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="conversations",
            user="gpts",
            password="ai!25",
            host="localhost"
        )
        return conn
    except psycopg2.Error as e:
        print("Unable to connect to the database")
        print(e)
        return None

def test_db_connection():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT 1;")
        result = cursor.fetchone()
        print("Connection Test Passed: ", result)
        cursor.close()
        conn.close()
    except Exception as e:
        print("Connection Test Failed: ", e)

test_db_connection()

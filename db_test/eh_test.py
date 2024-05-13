def test_error_handling():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        # Intentional SQL error
        cursor.execute("SELECT from non_existent_table;")
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error Handling Test Passed: ", e)

test_error_handling()

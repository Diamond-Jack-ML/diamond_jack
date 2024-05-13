def test_data_integrity():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT question, answer FROM conversations ORDER BY id DESC LIMIT 1;")
    question, answer = cursor.fetchone()
    cursor.close()
    conn.close()
    assert question == "What is AI?" and answer == "Artificial Intelligence is the branch of computer sciences that emphasizes the development of intelligence machines, thinking and working like humans.", "Data Integrity Test Failed"
    print("Data Integrity Test Passed")

test_data_integrity()

class StudentRepo:

    @staticmethod
    def insert(mydb, cursor, data):
        sql = "INSERT INTO students (code, first_name, last_name, dob, math, physics, chemistry) VALUES (%s, %s, %s, %s,%s,%s,%s)"
        cursor.execute(sql, data)
        mydb.commit()
        print(cursor.rowcount, "inserted")

    @staticmethod
    def find_all(mydb, cursor):
        cursor.execute("SELECT * FROM students")
        results = cursor.fetchall()
        return results if len(results) else []

    @staticmethod
    def update(mydb, cursor, id, data):
        sql = "UPDATE students SET code=%s, first_name=%s, last_name=%s, dob=%s, math=%s, physics=%s, chemistry=%s WHERE id=%s"
        cursor.execute(sql, (*data, id))
        mydb.commit()
        print(cursor.rowcount, "updated")

    @staticmethod
    def delete(mydb, cursor, id):
        sql = "DELETE FROM students WHERE id=%s"
        cursor.execute(sql, (id,))
        mydb.commit()
        print(cursor.rowcount, "deleted")

    @staticmethod
    def find_by_id(mydb, cursor, id):
        sql = "SELECT * FROM students WHERE id=%s"
        cursor.execute(sql, (id,))
        result = cursor.fetchone()
        return result if result else None
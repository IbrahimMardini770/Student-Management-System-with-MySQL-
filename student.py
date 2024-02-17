import mysql.connector

class Student:
    
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",    
            database="CRUD_DB"
        )
        self.mycursor = self.mydb.cursor()

    def create_tables(self):
        self.mycursor.execute('''
            CREATE TABLE IF NOT EXISTS student (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL
            )
        ''')
        self.mycursor.execute('''
             CREATE TABLE IF NOT EXISTS mark (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            degree FLOAT NOT NULL,
            student_id INT,
            FOREIGN KEY (student_id) REFERENCES student (id)
            )
        ''')
        self.mycursor.execute('''
           CREATE TABLE IF NOT EXISTS teacher (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
            )
        ''')
        self.mydb.commit()

    def insert_student(self, st_name):
        sql = "INSERT INTO student (name) values (%s)"
        val = (st_name,)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print(self.mycursor.rowcount, "record inserted")

    def update_student(self, o_st_id, n_st_name):
        sql = '''
            UPDATE student SET      
            name = %(N_name)s
            WHERE id = %(O_id)s
        '''
        val = {"N_name": n_st_name, "O_id": o_st_id}
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def show_students(self):
        self.mycursor.execute('SELECT id, name FROM student')
        myresult = self.mycursor.fetchall()
        for x in myresult:
            print('id: ' + str(x[0]) + ' name: ' + x[1])

    def delete_student(self, st_id):
        sql = 'DELETE FROM student WHERE id = %(id)s'
        val = {"id": st_id}
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def search_student(self, st_name):
        sql = 'SELECT id, name FROM student WHERE name = %s'
        val = (st_name,)
        self.mycursor.execute(sql, val)
        myresult = self.mycursor.fetchone()
        if myresult:
            print(f"The Id Is: {myresult[0]}, The Name Is: {myresult[1]}")
        else:
            print("Student not found with the given name")



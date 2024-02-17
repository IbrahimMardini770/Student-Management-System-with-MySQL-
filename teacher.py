import mysql.connector

class Teacher:
    password="Te1234"

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="CRUD_DB"
        )
        self.mycursor = self.mydb.cursor()
        

    def Insert_Teacher(self,St_Name):
        sql="INSERT INTO teacher (name) values (%s)"
        val=(St_Name,)
        self.mycursor.execute(sql,val)
        self.mydb.commit()
        print(self.mycursor.rowcount, "record inserted")

    def Show_Teacher(self):
        self.mycursor.execute('''
                SELECT id,name FROM teacher
                    ''')
        myresult=self.mycursor.fetchall()
        for x in myresult:
            print(f"the id is: {x[0]} and the naem is: {x[1]}")

    def Update_Teacher(self,O_id,N_Name):
        sql=('''
            UPDATE teacher SET 
                name=%(N_Name)s
                where id=%(O_id)s
            ''')
        val={"N_Name":N_Name,"O_id":O_id}
        self.mycursor.execute(sql,val)
        self.mydb.commit()

    def Delete_Teacher(self,O_id):
        sql='''
                Delete From teacher 
                where id=%s 
            '''
        val=(O_id,)
        self.mycursor.execute(sql,val)
        self.mydb.commit()

    def Search_Teacher(self,name):
        sql='''
            SELECT id, name FROM teacher
            WHERE name = %s
                '''
        val=(name,)
        self.mycursor.execute(sql,val)
        myresult=self.mycursor.fetchall()
        if myresult:
            for x in myresult:
                print(f"the id is: {x[0]} , The Name Is : {x[1]}")        
        else:
            print("teacher not found with the given name !?")



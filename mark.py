import mysql.connector

class Mark:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="CRUD_DB"
        )
        self.mycursor = self.mydb.cursor()

    def Insert_Mark(self, M_Name,M_Degree,St_Name):
        find_student_id_sql="SELECT id FROM student WHERE name=%s"
        find_student_id_val=(St_Name,)
        self.mycursor.execute(find_student_id_sql,find_student_id_val)
        student_id_result=self.mycursor.fetchone()
        if student_id_result:
            student_id=student_id_result[0]
            insert_mark_sql="INSERT INTO mark (name,degree,student_id) VALUES (%s,%s,%s)"
            insert_mark_va1=(M_Name,M_Degree,student_id)
            self.mycursor.execute(insert_mark_sql,insert_mark_va1)
            self.mydb.commit()

            print(self.mycursor.rowcount, "recod inserted into mark table")

        else:
            print("Student not found with the givent name.")


    def Update_Mark(self, O_M_id, N_M_name, N_M_Degree, N_St_Name):
        # Validate whether the record with the given ID exists
        select_query = "SELECT id FROM mark WHERE id = %s"
        select_values = (O_M_id,)

        try:
            self.mycursor.execute(select_query, select_values)
            existing_record = self.mycursor.fetchone()

            if existing_record:
                # Check if the student name exists
                select_student_query = "SELECT id FROM student WHERE name = %s"
                select_student_values = (N_St_Name,)
                self.mycursor.execute(select_student_query, select_student_values)
                student_result = self.mycursor.fetchone()

                if student_result:
                    # Update the record
                    update_query = '''
                        UPDATE mark
                        SET name = %s, degree = %s, student_id = %s
                        WHERE id = %s
                    '''
                    update_values = (N_M_name, N_M_Degree, student_result[0], O_M_id)
                    
                    self.mycursor.execute(update_query, update_values)
                    self.mydb.commit()
                    print(f"Record with Id {O_M_id} updated successfully.")
                else:
                    print("The student name does not exist.")
            else:
                print(f"Record with Id {O_M_id} not found. Update failed.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def View_Mark(self,St_Name):
        find_Student_id_sql="SELECT id FROM student WHERE name=%s"
        find_Student_id_val=(St_Name,)
        self.mycursor.execute(find_Student_id_sql,find_Student_id_val)
        student_id_result=self.mycursor.fetchone()

        if student_id_result:
            student_id=student_id_result[0]

            view_marks_sql="SELECT name,degree FROM mark where student_id=%s"
            view_marks_val=(student_id,)
            self.mycursor.execute(view_marks_sql,view_marks_val)
            marks=self.mycursor.fetchall()

            if marks:
                print(f"Marks for {St_Name}")
                for mark in marks:
                    print(f"Subject:{mark[0]}, Degree:{mark[1]}")
            else:
                print(f"No marks found for {St_Name} ")
        else:
            print("Student not found with the given name .")


    def Delete_Mark(self,m_id):
        find_mark_id_sql="Select id from mark where id=%s"
        find_mark_id_val=(m_id,)

        try:
            self.mycursor.execute(find_mark_id_sql,find_mark_id_val)
            find_id=self.mycursor.fetchone()
            if find_id:
                delete_mark_sql="delete from mark where id=%s"
                delete_mark_val=(m_id,)
                self.mycursor.execute(delete_mark_sql,delete_mark_val)
                self.mydb.commit()
                print(f"Mark ID {m_id} has been deleted.")
            else:
                print(f"The mark id :{m_id} not found. Deleted failed. ")
        except mysql.connector.Error as err:
            print(f"Error:{err}")

    def Search_Mark(self, keyword):
        # Search for marks by mark name or student name
        search_sql = "SELECT m.name AS mark_name, m.degree, s.name AS student_name \
                    FROM mark m \
                    JOIN student s ON m.student_id = s.id \
                    WHERE m.name LIKE %s OR s.name LIKE %s"
        search_val = ('%' + keyword + '%', '%' + keyword + '%')
        self.mycursor.execute(search_sql, search_val)
        search_results = self.mycursor.fetchall()

        if search_results:
            print(f"Search results for '{keyword}':")
            for result in search_results:
                print(f"Mark Name: {result[0]}, Degree: {result[1]}, Student Name: {result[2]}")
        else:
            print(f"No results found for '{keyword}'.")





   
    


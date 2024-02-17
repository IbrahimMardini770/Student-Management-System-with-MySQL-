import mysql.connector
import student as St
import teacher as Te
import mark as Ma

class Program:
    def main_menu(self): 
            
            while True: 
                print("\n1- Am a Teacher")
                print("2- Am a Student")
                S_T_chice=input("Enter 1 or 2: ")   
                            
                if S_T_chice=="1":
                    techer_pasword=input("\nInput your password: ")
                    if techer_pasword == teacher_manager.password:
 
                        print("\n1- Manage Students")
                        print("\n2- Manage Teachers")
                        print("\n3- Manage Marks")
                        S_T_M_Mange_chice=input("\nEnter 1 or 2 or 3: ")

                        if S_T_M_Mange_chice=="1":
                            while True:
                                print("\n1. Add Student")
                                print("2. View Students")
                                print("3. Delete Student")
                                print("4. Update Student")
                                print("5. Search Student")
                                print("6. Exit")

                                choice = input("Enter Your Choice: ")

                                if choice == "1":
                                    st_name = input("Insert the student name: ")
                                    student_manager.insert_student(st_name)
                                elif choice == "2":
                                    student_manager.show_students()
                                elif choice == "3":
                                    st_id = input("Input the student id: ")
                                    student_manager.delete_student(st_id)
                                elif choice == "4":
                                    o_st_id = input("Input the student id you want to change: ")
                                    n_st_name = input("Input the NEW student Name: ")
                                    student_manager.update_student(o_st_id, n_st_name)
                                elif choice == "5":
                                    st_name = input("Input the Student Name: ")
                                    student_manager.search_student(st_name)
                                elif choice == "6":
                                    print("Thanks for using the Student Management System!")
                                    break
                                else:
                                    print("Invalid choice. Please enter a valid option.")
    #---------------------------------------------------------------------------------------------------                                
                        elif S_T_M_Mange_chice=="2":
                            while True:
                                print("\n1. Add Teacher")
                                print("2. View Teacher")
                                print("3. Delete Teacher")
                                print("4. Update Teacher")
                                print("5. Search Teacher")
                                print("6. Exit")

                                choice = input("Enter Your Choice: ")

                                if choice == "1":
                                    tea_name = input("Insert the Teacher name: ")
                                    teacher_manager.Insert_Teacher(tea_name)
                                elif choice == "2":
                                    teacher_manager.Show_Teacher()
                                elif choice == "3":
                                    tea_id = input("Input the Teacher id: ")
                                    teacher_manager.Delete_Teacher(tea_id)
                                elif choice == "4":
                                    o_tea_id = input("Input the Teacher id you want to change: ")
                                    n_tea_name = input("Input the NEW Teacher Name: ")
                                    teacher_manager.Update_Teacher(o_tea_id, n_tea_name)
                                elif choice == "5":
                                    tea_name = input("Input the Teacher Name: ")
                                    teacher_manager.Search_Teacher(tea_name)
                                elif choice == "6":
                                    print("Thanks for using the Teacher Management System!")
                                    break
                                else:
                                    print("Invalid choice. Please enter a valid option.")
    #-----------------------------------------------------------------------------------------------------------------                      
                        elif S_T_M_Mange_chice=="3":
                            while True:
                                print("\n1. Add Mark")
                                print("2. View Marks")
                                print("3. Delete Mark")
                                print("4. Update Mark")
                                print("5. Search Mark")
                                print("6. Exit")

                                choice = input("Enter Your Choice: ")

                                if choice == "1":
                                    mar_name = input("Insert the Mark name: ")
                                    mar_degree = input("Insert the degree: ")
                                    mar_st_name = input("Insert the student name: ")
                                    mark_manager.Insert_Mark(mar_name, mar_degree , mar_st_name )
                                elif choice == "2":
                                    mar_view=input("Input the student name you want his mark: ")
                                    mark_manager.View_Mark(mar_view)
                                elif choice == "3":
                                    m_id = input("Input the Mark id: ")
                                    mark_manager.Delete_Mark(m_id)
                                elif choice == "4":
                                    m_id = input("Input the Mark id you want to change: ")
                                    m_name = input("Input the NEW Mark Name: ")
                                    m_degree = input("Input the NEW degree: ")
                                    m_s_name = input("Input the  student name: ")
                                    mark_manager.Update_Mark(m_id, m_name , m_degree , m_s_name)
                                elif choice == "5":
                                    m_s_name = input("Input the Student Name or the Mark name: ")
                                    mark_manager.Search_Mark(m_s_name)
                                elif choice == "6":
                                    print("Thanks for using the Mark Management System!")
                                    break
                                else:
                                    print("Invalid choice. Please enter a valid option.")

                    else:
                        print("The password is wrong")
#--------------------------------------student--------------------------------------------------------
                if S_T_chice=="2":
                    student_name = input("\n1- Enter Your Name To see your Marks ")
                    mark_manager.Search_Mark(student_name)
                    break
                



                        


if __name__ == "__main__":
    student_manager =St.Student()
    teacher_manager =Te.Teacher()
    mark_manager =Ma.Mark()
    program_object=Program()
    student_manager.create_tables()
    program_object.main_menu()
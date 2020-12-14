import sqlite3

conn = sqlite3.connect('studatabase.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS student(sid VARCHAR(10), firstname TEXT, lastname TEXT, birthyear INT)')


class Student():
    def __init__(self, student_id, fname, lname, birth_year):
        self.Student_id = student_id
        self.Fname = fname
        self.Lname = lname
        self.birth_year = birth_year

    def print_details(self):
        print(
            f"The student you want to add has the following details\nStudent ID: {self.Student_id}\nFirst Name: {self.Fname}\nLastName: {self.Lname}\nBirth Year: {self.birth_year} ")

    def insert_table(self):
        c.execute("INSERT INTO  student VALUES(?,?,?,?)", (self.Student_id, self.Fname, self.Lname, self.birth_year))
        conn.commit()
        print("======Student added======")


# def check_text(a):
#     if a.isalpha():
#         return(True)
#     else:
#         return (False)
#
#
# def check_int(a):
#     if a.isnumeric():
#         return(True)
#     else:
#         return (False)


print("Welcome to the student database app!")
print("================================")
run = True
while run:
    try:
        student_id = int(input("Please enter a student id: "))
        fname = input("Please enter the student First Name: ").upper()
        lname = input("Please enter the student Last Name: ").upper()
        b_year = int(input("Please enter the student birth year: "))
    except:
        print("Please enter correct data types")
        continue


    # print(check_int(b_year))

    new_student = Student(student_id, fname, lname, b_year)

    new_student.print_details()
    confirm = input("Is this information correct? (y or n): ").lower()
    if confirm == 'n':
        print("you will need to re-enter the information")
        continue
    elif confirm == 'y':
        new_student.insert_table()

    rerun = input("Do you want to add another student? (y or n)").lower()
    if rerun == 'n':
        run = False

from people import *

acceptable_values = {'1','2','3','4','5'}
x = 0
faculty_list = []
student_list = []

while x != 5:
    print("""  
    *** TUFFY TITAN STUDENT/FACULTY MAIN MENU
1. Add faculty
2. Print faculty
3. Add student
4. Print student
9. Exit the program
    """)
    x= 0
    while (x in acceptable_values) == False:
        # ask for valid input
        x = input("Enter menu choice: ")
    x = int(x)
    if x == 1:
        a = str(input("Enter first name: "))
        b = str(input("Enter last name: "))
        c = str(input("Enter department: "))
        a = Faculty(a, b, c)
        faculty_list.append(a)
    elif x == 2:
        print(
        """
======================= FACLUTY =======================
Record Name                 Department
====== ==================== =========================
"""
        )
        for i, obj in enumerate(faculty_list):
            name = obj.firstname + " " + obj.lastname
            print(f'{str(i):7}{name:21}{obj.department:7}')
    elif x == 3:
        a = str(input("Enter first name: "))
        b = str(input("Enter last name: "))
        c = str(input("Enter class year: "))
        d = str(input("Enter major: "))
        e = int(input("Enter faculty advisor: "))
        while (e > (len(faculty_list) - 1)) or (e < 0):
            # ask for valid input
            try:
                e = int(input("Enter faculty advisor: "))
            except ValueError:
                pass
            
        e = str(e)
        a = Student(a, b)
        a.set_class(c)
        a.set_major(d)
        a.set_advisor(e)
        student_list.append(a)
    elif x == 4:
        print(
        """
===================================== STUDENTS ======================================
Name                 Class    Major                     Advisor
==================== ======== ========================= =========================
"""
        )
        for i, obj in enumerate(student_list):
            stu_name = obj.firstname + " " + obj.lastname
            tea_name = faculty_list[i].firstname + " " + faculty_list[i].lastname
            print(f'{stu_name:21}{str(obj.classyear):9}{obj.major:26}{tea_name}')
    else:
        break

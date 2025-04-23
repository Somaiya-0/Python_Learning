class Students:

    def __init__(self):
        self.record = []

    def add_student(self):
        print("\n")
        print("-"*8,"Adding student's information to the record","-"*8)
        name = input("Enter student name : ")
        ID = int(input(f"Enter {name}'s id : "))
        if any(rec["ID"] == ID for rec in self.record):
            print(f"Id conflicted!")
            return


        dept = input(f"Emter {name}'s department: ")
        cg = input(f"Enter {name}'s cg : ")
        Student={
            "name":name,
            "ID": ID,
            "dept":dept,
            "cg":cg
        }
        self.record.append(Student)
        print(f"Record for {name} has been added.")
        while True:
            add_more=input("Add more student?(y/n) : ")
            if add_more=='y':
                name = input("Enter student name : ")
                ID = int(input(f"Enter {name}'s id : "))
                if any(rec["ID"] == ID for rec in self.record):
                    print(f"Id conflicted!")
                    return
                dept = input(f"Emter {name}'s department: ")
                cg = input(f"Enter {name}'s cg : ")
                Student={
                    "name":name,
                    "ID": ID,
                    "dept":dept,
                    "cg":cg
                }
                self.record.append(Student)
                print(f"Record for {name} has been added.")
            elif add_more == 'n':
                break
            else:
                print("inavlid choice")
    def show_record(self):
        print("\n")
        print("-"*8,"Showing Record","-"*8)
        border = "+---------+-------+-------+------+"
        header = "| Name    | ID    | Dept  | CGPA |"
        print(border)
        print(header)
        print(border)
        for i,s in enumerate(self.record,1):
            

            
            print(f'| {s["name"]:<8}| {s["ID"]:<6}| {s["dept"]:<6}| {s["cg"]:<5}|')

            print(border)
    
    def search_by_id(self):
        search = int(input("Enter student's Id to update: "))
        found=0
        for i,s in enumerate(self.record,1):
            if s["ID"]==search:
                found=1
                border = "+---------+-------+-------+------+"
                header = "| Name    | ID    | Dept  | CGPA |"

                print(border)
                print(header)
                print(border)
                print(f'| {s["name"]:<8}| {s["ID"]:<6}| {s["dept"]:<6}| {s["cg"]:<5}|')
                print(border)
        if found==0:
            print("ID not found!")

    def update_student(self):
        print("-"*8,"Updating Record","-"*8)

        search = int(input("Enter student's Id to update: "))
        for i,s in enumerate(self.record,1):
            found=0
            if s["ID"]==search:
                found=1
                print(f"\n{s["name"]}'s information :")
                border = "+---------+-------+-------+------+"
                header = "| Name    | ID    | Dept  | CGPA |"

                print(border)
                print(header)
                print(border)
                print(f'| {s["name"]:<8}| {s["ID"]:<6}| {s["dept"]:<6}| {s["cg"]:<5}|')

                print(border)
                print(f'''Select what you want to update:
                            1. Name
                            2. ID
                            3. Department
                            4. CGPA''')
                choice = input("\nEnter your choice (1-4): ")
                if choice == "1":
                    name = input("Enter students name: ")
                    s["name"]=name
                elif choice == "2":
                    ID = int(input(f"Enter {s["name"]}'s id : "))
                    s["ID"]=ID
                        
                elif choice == "3":
                    dept = input(f"Emter {s["name"]}'s department: ")
                    s["dept"] = dept

                elif choice == "4":
                    cg = input(f"Enter {s["name"]}'s cg : ")
                    s["cg"] = cg
        if found==0:
            print("ID not found!")
            
        print("Record has been updated.")
    
    def delete_student(self):
        print("-"*8,"Deleting Record","-"*8)
        search = int(input("Enter student's Id to delete: "))
        for i,s in enumerate(self.record,0):
            if s["ID"]==search:
                self.record.pop(i)
                print("Successfully Deleted.")
                

def main():
    student = Students()
    
    print("\n")
    print("="*8, "Student Record Management System", "="*8)
    print("1. Add Student Record")
    print("2. Show Students Record")
    print("3. Show specific student's record")
    print("4. Update record of a student")
    print("5. Delete rocord of a student")
    print("6. Exit")
    while True:
        

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            student.add_student()
        elif choice == "2":
            student.show_record()
        elif choice == "3":
            student.search_by_id()
        elif choice == "4":
            student.update_student()   
        elif choice == "5":
            student.delete_student()
        elif choice == "6":
            print("Program Finished!")
            break

        else:
            print("\nInvadlid choice")

if __name__ == "__main__":
    main()
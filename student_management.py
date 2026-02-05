import json

class Student_management:
    def __init__(self):
        self.student_datas = []
        self.load_std()

    def print_header(self):
        print("ID | Name       | Age   | Course            | Marks")
        print("----------------------------------------------------")

    def print_student(self,stds):
        
        print(f"{stds['std_id']:<2} | "
                    f"{stds['std_name']:<10} | "
                    f"{stds['std_age']:<5} | "
                    f"{stds['std_course']:<17} | "
                    f"{stds['std_marks']:<5}")

    def add_std(self):
        try :
            id = input("Enter Student ID :")
            if any(s["std_id"] == id for s in self.student_datas):
                print("Studend Id alredy exists")
                return
            name = input("Enter Student Name : ")
            age = int(input("Enter student age : "))
            course = input("Enter Student course : ")
            marks = float(input("Enter student Marks : "))

            student_records = {
                "std_id" : id,
                "std_name" : name,
                "std_age" : age,
                "std_course" : course,
                "std_marks" : marks
            }

            self.student_datas.append(student_records)
            print("student data successfully added in Record Book")
        
        except ValueError :
            print("Age must be integer and Marks should be number in float")
        
    def view_std(self):
        if not self.student_datas:
            print("No student records found")
            return
        self.print_header()
        for stds in self.student_datas:
            self.print_student(stds)
            # print(f"{stds['std_id']:<2} | "
            #         f"{stds['std_name']:<10} | "
            #         f"{stds['std_age']:<5} | "
            #         f"{stds['std_course']:<17} | "
            #         f"{stds['std_marks']:<5}")

    def search_std(self):
        u_id = input("Please enter the student id which you want to find : ")
        found = False

        for stds in self.student_datas:
            if stds["std_id"] == u_id:
                print("Data is found")
                self.print_header()
                # print("ID | Name       | Age   | Course            | Marks")
                # print("----------------------------------------------------")
                self.print_student(stds)
                # print(f"{item['std_id']:<2} | "
                #     f"{item['std_name']:<10} | "
                #     f"{item['std_age']:<5} | "
                #     f"{item['std_course']:<17} | "
                #     f"{item['std_marks']:<5}")
                found = True
                break

        if not found:
            print("Data not found with this student id")


    def print_menu(self):
        
        print("A: Update  Student Id")
        print("B: Update  Student Name")
        print("C: Update  Student Age")
        print("D: Update  Student Course")
        print("E: Update  Student Marks")
        print("F: Save & exit")
        print("\n")

    def update_field(self,item,key,message, data_type=str):
        old_value = item[key]
        new_value = data_type(input(f"{message} "))
        item[key] = new_value
        
        print("\nField updated successfully")
        print(f"{message} {old_value} → {new_value}")
        self.print_student(item)
    
    def update_std(self):

        std_id = input("enter Student id number to update :")
        found = False

        for item in self.student_datas:
            if item["std_id"] == std_id :
                print("\ndata found")
                # self.view_std()
                found = True

                while True:
                        self.print_menu()
                        choose = input("Choose option between A - F : ").upper()
        
                        if choose == "A":
                            self.update_field(item, "std_id","enter student new id : ")
                        elif choose == "B":
                            self.update_field(item, "std_name","enter student new Name : ")
                        elif choose == "C":
                            self.update_field(item, "std_age","enter student new age :",int)
                        elif choose == "D":
                            self.update_field(item, "std_course","enter student new course :")
                        elif choose == "E":
                            self.update_field(item, "std_marks","enter student new marks :",float)
                        elif choose == "F":
                            break
                        else : 
                            print("Invalid option. Please choose between A - F")

        if not found:
            print("Data not found with this id ")



    def delete_std(self):
        delete_id = input("enter the student id which you want to delete : ")

        for item in self.student_datas :
            if item["std_id"] == delete_id:
                check = input("Are you sure to delete this Entery (Y/N) : ").upper()
                if check == 'Y':
                    self.student_datas.remove(item)
                    print("Entry deleted")
                    self.view_std()
                    break
                else:
                    print("Entery not deleted because you are not sure")
                return

    def save_std(self):
        with open("student_recods.json","w") as file:
            json.dump(self.student_datas,file,indent=2)
        print("student record saved")
        

    def load_std(self):
        try :
            with open("student_recods.json","r") as file:
                self.student_datas = json.load(file)
            
        except FileNotFoundError:
            self.student_datas = []

student_data = Student_management()
while True :
    print("\n")
    print(" 1. Add Student")
    print(" 2. View Students") 
    print(" 3. Search Student")
    print(" 4. Update Student")
    print(" 5. Delete Student")
    print(" 6. Save & Exit")
    print("\n")
    choose = input("Please choose the option from above : ")

    if choose == "1":
        student_data.add_std()
    elif choose == "2":
        student_data.view_std()
    elif choose == "3" :
        student_data.search_std()
    elif choose == "4":
        student_data.update_std()
    elif choose == "5":
        student_data.delete_std()
    elif choose == "6":
        student_data.save_std()
        break        
    else :
        print("Please enter valid option number between 1-6")
    
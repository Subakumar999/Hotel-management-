print("my name is Subalakshmi K")
print("my emailid is subalakshmimonika@gmail.com")
print("python batch74")

print("***** welcome to GOVT hospital adminsitration****")
print("**HAPPINESS IS THE HIGHEST FORM OF HEALTH***")

class patient:
    def __init__(self,name,department,ward,room):
        name=["patient1","patient2","patient3"]
        self.name=input("enter patient name:")
        if self.name=="patient1":
            print(f"patient1 is in the faculty ward")
        
        elif self.name=="patient2":
            print(f"patient2 is in the normal ward2 in the 2nd floor")
        elif self.name=="patient3":
            print(f"patient3 is in the normal ward3 in the 1st floor")
       
        department=["faculty","normal ward2","normal ward3"]
        self.department=input(f"enter your patient department:")

        if self.department=="faculty":
            print(f"patient1 is in the faculty ward ")
        elif self.department=="normal ward2":
            print(f"patient2 is in the normal ward2 in the 2nd floor")
        elif self.department=="normal ward3":
            print(f"patient3 is in the normal ward3 in the 1st floor")

        ward=["1","2","3"]
        self.ward= int(input("enter your ward:"))
        if self.ward=="1":
            print(f"patient1 is in the faculty ward ")
        elif self.ward=="2":
            print(f"patient2 is in the  ward2 in the 2nd floor")
        elif self.ward=="3":
            print(f"patient3 is in the ward3 in the 1st floor")
        
        room=["a","b","c"]
        self.room=input("enter your room:")
        if self.room=="a":
            print(f"patient1 is in a room the faculty ward ")
        elif self.room=="2":
            print(f"patient2 is in b room in the  normal ward2 in the 2nd floor")
        elif self.room=="3":
            print(f"patient3 is inc room in the normal ward3 in the 1st floor")

    def get_patient_data(self):
        print(f"the patinet name is {self.name}")
        print(f"the patient department is {self.department}")
        print(f"the patient ward is in {self.ward}")
        print(f"the patient room is {self.room}")
        
class doctor(patient):
    def __init__(self,d_name,d_department,d_ward,d_room,name,department,ward,room):
        d_name=["doctor1","doctor2","doctor3"]
        self.d_name=input("enter doctor name:")
        if self.d_name=="doctor1":
            print(f"doctor1 is in the faculty ward")
        elif self.d_name=="doctor2":
            print(f"doctor is in the normal ward2 in the 2nd floor")
        elif self.d_name=="doctor3":
            print(f"doctor3 is in the normal ward3 in the 1st floor")
        else:
            print(f"the doctor is absent")

        d_department=["faculty","normal ward2","normal ward3"]
        self.d_department=input(f"enter your working department:")

        if self.d_department=="faculty":
            print(f"doctor1 is in the faculty ward ")
        elif self.d_department=="normal ward2":
            print(f"doctor2 is in the normal ward2 in the 2nd floor")
        elif self.d_department=="normal ward3":
            print(f"doctor3 is in the normal ward3 in the 1st floor")
        else:
            print(f"the doctor is absent")
        d_ward=["1","2","3"]
        self.d_ward= int(input("enter your ward:"))
        if self.d_ward=="1":
            print(f"doctor1 is in the faculty ward ")
        elif self.d_ward=="2":
            print(f"doctor2 is in the  ward2 in the 2nd floor")
        elif self.d_ward=="3":
            print(f"doctor3 is in the ward3 in the 1st floor")
        
        d_room=["a","b","c"]
        self.d_room=input("enter your room:")
        if self.d_room=="a":
            print(f"doctor1 is visting the patient1 in a room the faculty ward ")
        elif self.d_room=="2":
            print(f"doctor2 is visting the patient2 is in b room in the  normal ward2 in the 2nd floor")
        elif self.d_room=="3":
            print(f"doctor3 is visitng the patient3 is inc room in the normal ward3 in the 1st floor")


        patient.__init__(self,name,department,ward,room)
                 
    def get_doctor_data(self):
        print(f"the patinet name is {self.name}")
        print(f"the patient department is {self.department}")
        print(f"the doctor work is {self.d_ward}")
        print(f"the doctor is the {self.d_room}")


   
obj1=doctor("self.d_name","self.d_department","self.d_ward","self.d_room","self.name","self.department","self.ward","self.room")
obj1.get_patient_data()
obj1.get_doctor_data()

print("health is wealth")
        
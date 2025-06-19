class Student:
    id=""
    gpa=""
    dep=""
    def set_value(self,id,gpa,dep):
        self.id=id
        self.gpa=gpa
        self.dep=dep

    def display(self):
        print(f"ID:{self.id},GPA:{self.gpa},Department:{self.dep}")
    
sakib = Student()
sakib.set_value(960,3.20,"cse")
sakib.display()

Nahid = Student()
Nahid.set_value(988,2.90,"cse")
Nahid.display()

# class university:
#     def say_my_name(self,name):
#         self.university_name = name

# class AdmissionCell(university):
#     def collect_my_data(self,name,reg):
#         self.name=name
#         self.reg=reg   
#     def display_data(self):
#         print(self.name,self.reg)

# class Debart_cell(AdmissionCell):
#     def debart_list(self):
#         print("Debart list Generated>>>>>>>>>")

# obj=Debart_cell()
# obj.say_my_name("VIT")
# obj.collect_my_data("Simran","23mca10063")



class university:
    def say_my_name(self,name):
        self.university_name = name

class AdmissionCell(university):
    def collect_my_data(self,name,reg):
        self.name = name
        self.reg = reg
    def display_data(self):
        print(self.name, self.reg)

class debard_cell(AdmissionCell):
    def debard_list(self):
        print("Debard list Generated....")

obj=debard_cell()
obj.say_my_name("VIT")
obj.collect_my_data("Simran","230493083")

obj.display_data()
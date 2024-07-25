# class university:
#     def IPR(self):
#         print("information process resources")
#     def IT(self):
#         print("Department of Information Technology")

#     def Exam(self):
#         print("Department of examination")

# VIT= university()
# NIT= university()
# IIT= university()
# VIT.Exam()


#create the class that display functional units of any university present in india .Call this class with various university available in india to display 
# the working of various department.

#Q.2 create a class for the bikers.every biker is having some unit     in following points:-
# total no of fails
# engine type
# engine number/chasase number
# create the objects for this class for 2 wheelers and 3 wheelers .execute various functions with various objects.

# class Vehicles:
#     def __init__ (self, wheels,  engine_number,engine_type):

#         self.wheels = wheels
#         self.engine_number = engine_number
#         self.engine_type = engine_type
#     def features(self):
#         print(self.wheels," ",self.engine_number," ",self.engine_type)

# bike=Vehicles(2,"HDFC56694","BS6")
# car=Vehicles(3,"asdf959595","BS4")
# bike.features()
# car.features()


#create a class for mobiles every mobile is having some features.write total number of camera.
# 2. processing speed
# 3.recording 
# 4.create a model of mobile classes,
# take the feature from users for each object and display them

# class Mobile():
#     def self_camera(self,number_of_camera):
#         self.no_of_camera = no_of_camera
#     def processing_speed(self,processing_speed):
#         self.processing_speed = processing_speed
#     def recording_feature(self,recording_feature):
#         self.recording_feature = recording_feature


#     def get_features(self):
#         print(self.no_of_camera, self.processing_speed, self.recording_feature)


# oppo = Mobile()

# oppo.set_camera(4)
# oppo.processing_speed()




# create a constant inside a class in python .any constant    value can be declared directly inside a class just like a normal variable
# that constat value can be called directly with the object of that class




#create a class library having 2 different section :-
# first mca section in which alll the book code starts with Mca101
# onl y 3 books is available in mca  section that are :- java  , python and c+

# the another section is physics where the code starts from PHY101
# only 3 biooks are avaialble in that section that ate:- thermodynamics, optics , quantum physics

# ask the user which section he wants to visit and display all the books available in that sections.


class library:
    def constant_section(self):
        section= input("Selection")
        match section:
            case "mca":print("Java\nPython\nc++")
            case "physics":print("thermodynamics\nQuantum physics\nOptics")
            case_:print()


#create a class bank . every bank should have some name and every bank should provide loan facility.
# for home loan a bank should provide 12% interest 
# for education loan bank provides 10 % of interedt with principal amount of 15,000 rupee
# there are 2 banks from where we can the loan facility .provide the date and time for any specific type of loan and do compare
# which particular bank is better to avail the loan facility.


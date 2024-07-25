

class Vehicle:
    def __init__(self,wheels,engine_number,engine_type):
        # self.vehicle_type = vehicle_type
        self.wheels = wheels
        self.engine_number = engine_number
        self.engine_type = engine_type

    def set_wheel(self,wheels):
        self.wheels=wheels

    def set_engine(self,engine_number):
        self.engine_number = engine_number

    def set_engine_type(self,engine_type):
        self.engine_type = engine_type

    def features(self):
        print(self.wheels," ",self.engine_number," ",self.engine_type)

bike=Vehicle(2,"HDOW56870","BS6")
car=Vehicle(4,"RG5684570","BG7")
bike.features()
car.features()

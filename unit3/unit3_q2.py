class Mobile:
    def total_no_camera(self,total_no_camera):
        self.total_no_camera=total_no_camera

    def processing_system(self,processing_system):
        self.processing_system=processing_system

    def Recording_facility(self,recording_facility):
        self.Recording_facility=recording_facility

    def get_feature(self):
        print(self.total_no_camera," ",self.processing_system," ",self.Recording_facility)

oppo=Mobile()
oppo.total_no_camera(3)
oppo.processing_system("3.2 Gbps")
oppo.Recording_facility("4k 30 fps")
oppo.get_feature()
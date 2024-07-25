class FeesCollection:
    def pay_fees(self): print("Fees paid."); return True

class Examination:
    def clear_exams(self): print("Exams cleared."); return True

class Placement:
    def get_placed(self): print("Placement done."); return True

class ResearchPaperPublishing:
    def publish_paper(self): print("Paper published."); return True

class Student(FeesCollection, Examination, Placement, ResearchPaperPublishing):
    def fulfill_requirements(self):
        return all([self.pay_fees(), self.clear_exams(), self.get_placed(), self.publish_paper()])

    def get_professional_job(self):
        if self.fulfill_requirements():
            print("Eligible for a professional job.")
        else:
            print("Not eligible for a professional job.")

# Example usage
student = Student()
student.get_professional_job()

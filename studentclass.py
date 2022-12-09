class student:
    def __init__(self, name, major, gpa, is_on_probation):  # constructor
        self.name = name  # name of student is equal to name that we passed and not some function of that
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honour_roll(self):  # additional function. self is a compulsory argument.
        if self.gpa >= 9:
            return True
        else:
            return False


student1 = student(
    "Manish", "Econ", 9.78, False
)  # parameters get passed in the constructor

student2 = student("Garima", "Fashion Technology", 7.832, True)

print(student1.gpa)
print(student1.on_honour_roll())
print(student2.on_honour_roll())

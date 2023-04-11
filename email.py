import re
class Email:

    def __init__(self, email:str):
        self.email = email
        self.isStudent=False
        self.isMale=True

        if "student.wat.edu.pl" in email:
            self.isStudent = True
        match = re.match(r"([a-z]+)\.([a-z]+)", email)
        if match:
            self.first_name = match.group(1)
            self.last_name = match.group(2)

        if re.search(r"[a-z]*a$", self.first_name):
            self.isMale = False


    def get_first_name(self):
            return self.first_name

    def get_last_name(self):
            return self.last_name

    def is_student(self):
            return self.isStudent

    def is_male(self):
            return self.isMale





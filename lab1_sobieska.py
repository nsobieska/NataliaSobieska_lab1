from email import Email
import unittest

class EmailTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.data = [
        ["natalia.sobieska@student.wat.edu.pl", "natalia", "sobieska", True, False],
        ["agnieszka.zalewska01@student.wat.edu.pl", "agnieszka", "zalewska", True, False],
        ["jan.kowalski@student.wat.edu.pl", "jan", "kowalski", True, True],
        ["anna.nowak@wat.edu.pl", "anna", "nowak", False, False],
        ["piotr.wozniak@wat.edu.pl", "piotr", "wozniak", False, True],
        ["anna.lewandowska01@student.wat.edu.pl", "anna", "lewandowska", True, False],
        ["andrzej.kowalski@student.wat.edu.pl", "andrzej", "kowalski", True, True],
        ["adam.malysz02@wat.edu.pl", "adam", "malysz", False, True],
        ["tomasz.kot@wat.edu.pl", "tomasz", "kot", False, True],
        ["malgorzata.rozenek05@wat.edu.pl", "malgorzata", "rozenek", False, False],
        ]

    def test_name(self):
        for temp in self.data:
            mail = temp[0]
            first_name = temp[1]
            extracted = Email(mail)
            self.assertEqual(first_name, extracted.first_name)

    def test_surnname(self):
        for temp in self.data:
            mail = temp[0]
            last_name = temp[2]
            extracted = Email(mail)
            self.assertEqual(last_name, extracted.last_name)

    def test_is_student(self):
        for temp in self.data:
            mail=temp[0]
            isStudent=temp[3]
            extracted=Email(mail)
            self.assertEqual(isStudent, extracted.isStudent)

    def test_is_male(self):
        for temp in self.data:
            mail = temp[0]
            isMale = temp[4]
            extracted = Email(mail)
            self.assertEqual(isMale, extracted.isMale)

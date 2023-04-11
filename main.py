# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from email import Email


e1 = Email("norbert.waszkowiak01@wat.edu.pl")
print("imie: " + e1.get_first_name())
print("nazwisko: " + e1.get_last_name())
if e1.isStudent==True:
    print("Jest studentem.")
else:
    print("Nie jest studentem.")
if e1.isMale==True:
    print("Jest mezczyzna.")
else:
    print("Jest kobieta.")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

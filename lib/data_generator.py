# This module contains functions to lazily generate student data.

def student_generator(student_list, major):
    for student in student_list:
        if student[2].lower() == major.lower():
            yield student
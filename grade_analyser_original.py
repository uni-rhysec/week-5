'''
Portfolio Task - Grade Analyser

In order to decide student's overall classification, the university needs to take an overall mean average of their grades across all modules.
The classifications and boundaries are as follows:
>= 70 : 1
>=60 : 2:1
>=50 : 2:2
>=40 : 3
<40 : F

Each student's data is stored in a row in a csv file (4 sample files have been provided).
Students can have between 1 - 12 modules, for example:
203982,73,42,55,83,,,,,,,, # 4 modules
203742,55,97,57,37,76,68,,,,,, # 6 modules
You should ensure that you consider the number of modules when calculating your mean.

Your code needs to:
- ask for the filename of the student file
- read in the data, and for each student calculate their average grade and classification
- write out this calculated data in the format:
     student_id,average_grade,classification
     The average grade should be given to 2 decimal places
     this can be achieved by using the following in an fstring: {variable_name:.2f}
- write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

Your output files must be structured exactly as described - output files for all the test files have been provided so you can compare and ensure they are identical.

Note:
Your code will only be tested on valid files in the format shown in the 4 example files in this folder - you do not need to validate any data.
'''

def convert_to_classification(mean):
     if mean >= 70:
          return "1"
     if mean >= 60:
          return "2:1"
     if mean >= 50:
          return "2:2"
     if mean >= 40:
          return "3"
     return "F"

file_name = input("Enter file name: ")
with open(f"/workspaces/week-5/{file_name}", "r") as read_from:
     with open(f"/workspaces/week-5/{file_name}_out.csv", "w") as write_to:
          line_1 = True
          for student in read_from:
               if line_1:
                    line_1 = False
                    write_to.write("student_id,average_grade,classification\n")
               else:
                    student_grades = student.strip().split(',')
                    print(student_grades)
                    total_score = 0
                    total_modules = 0
                    for module in range(1,13):
                         if student_grades[module] != '':
                              total_score += int(student_grades[module])
                              total_modules += 1
                    mean = total_score / total_modules
                    print(mean)
                    classification = convert_to_classification(mean)
                    string = f"{student_grades[0]},{mean:.2f},{classification}\n"
                    write_to.write(string)

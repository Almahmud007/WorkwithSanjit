'''
students = { 'uid-1': {"name": "John", "surname": "Doe", "email": "john@gmail.com"}, 'uid-2': {"name": "Jane", "surname": "Doe", "email": "jane@gmail.com"}, 'uid-3': {"name": "John", "surname": "Smith", "email": None}, 'uid-4': {"name": "Jane", "surname": "Smith", "email": "jane@gmail.com"}, }

students_attendance = { 'uid-1': [True, True, True, True, True, True, True, True, False, True], 'uid-2': [False, False, False, True, True, False, True, True, False, True], 'uid-3': [True, True, False, False, True, True, True, True, True, True], 'uid-4': [False, False, False, False, True, False, True, True, False, True], }

students_grades = { 'uid-1': {"hw1": 10, "hw2": 8, "hw3": 9}, 'uid-2': {"hw1": 9, "hw2": 8, "hw3": 10}, 'uid-3': {"hw1": 8, "hw2": 9, "hw3": 10}, 'uid-4': {"hw1": 10, "hw2": 8, "hw3": 10}, } Based on the Data Build a report for each student. The report should include the following information:

Write a function which calculate the average of the grades for each student. The function should return a dictionary with the key "uid" and the value is the average of the grades for each student with student First and Surname combined.

write a function which calculate the percentage of the attendance for each student. The function should return a dictionary with the key "uid" and the value is the percentage of the attendance for each student with student First and Surname combined.

Write a function which calculate a summay of the grades and attendence for each student. The function should return a dictionary with the key "uid" and the value is a dictionary with the Name and Surname conbined, Total percentage of present in the class and average grade from homework.

Write a function which calculate overall peformance of students based on their grades and attendance. The function should return a dictionary with the key "uid" and the value is the overall performance of the student. The overall performance is calculated as the average of the grades and the attendance. The weight of the grades is 0.7 and the weight of the attendance is 0.3. Ex. The overall performance of student 1 is calculated as follows: (0.7 * 0.8) + (0.3 * 0.75) = 0.765 , where 0.8 is the average of the grades and 0.75 is the percentage of the attendance.

Bonus Task: Write a function which will rank the studens by their overall peformance on the class. The function should return a dictionary with the key "uid" and the value is the rank of the student. The rank of the student is calculated based on the overall performance of the student. The student with the highest overall performance should get the rank 1. The student with the lowest overall performance should get the rank n, where n is the number of students in the class.

'''


students = {
    'uid-1': {"name": "John", "surname": "Doe", "email": "john@gmail.com"},
    'uid-2': {"name": "Jane", "surname": "Doe", "email": "jane@gmail.com"},
    'uid-3': {"name": "John", "surname": "Smith", "email": None},
    'uid-4': {"name": "Jane", "surname": "Smith", "email": "jane@gmail.com"},
}

students_attendance = {
    'uid-1': [True, True, True, True, True, True, True, True, False, True],
    'uid-2': [False, False, False, True, True, False, True, True, False, True],
    'uid-3': [True, True, False, False, True, True, True, True, True, True],
    'uid-4': [False, False, False, False, True, False, True, True, False, True],
}

students_grades = {
    'uid-1': {"hw1": 10, "hw2": 8, "hw3": 9},
    'uid-2': {"hw1": 9, "hw2": 8, "hw3": 10},
    'uid-3': {"hw1": 8, "hw2": 9, "hw3": 10},
    'uid-4': {"hw1": 10, "hw2": 8, "hw3": 10},
}

class Student:
    
    def __init__(self,students,students_attendance,students_grades):
        self.student = students
        self.students_attendance = students_attendance
        self.students_grades = students_grades
           
    def merged_data(self):
        merged_data = {}

        for uid, student_data in students.items():
            if uid in students_attendance and uid in students_grades:
                merged_data[uid] = {
                    **student_data,
                    "attendance": students_attendance[uid],
                    "grades": students_grades[uid]
                }

        return merged_data
        
    def uid(self):
        all_data = self.merged_data()
        all_uid = []
        for uid,val in all_data.items():
            all_uid.append(uid)
        return all_uid
        
    def name(self):
        all_data = self.merged_data()
        all_name = []
        
        for uid,val in all_data.items():
            all_name.append(val["name"])
        return all_name
        
    def surname(self):
        all_data = self.merged_data()
        all_surname = []
        for uid,val in all_data.items():
            all_surname.append(val["surname"])
        return all_surname  
    
    def student_avg(self):
        
        all_data = self.merged_data()
        all_uid = self.uid()
        all_name = self.name()
        all_surname = self.surname()
        
        averages = []

        for uid,val in all_data.items():
            grades = val['grades'].values()
            average = sum(grades)/len(grades)
            averages.append(average)
        
        result_dict = {}
        for uid, name, surname, average in zip(all_uid, all_name, all_surname, averages):
            rounded_average = round(average, 2)
            result_dict[uid] = {"name": name, "surname": surname, "Average": rounded_average}
            
        return result_dict
        
    def percentage(self):
        
        main_val = self.students_attendance
        
        all_uid = self.uid()
        all_name = self.name()
        all_surname = self.surname()
    
        attendence = []
        for uid, attend in main_val.items():
            attend_val = (attend.count(True) / len(attend))*100
            attend_round = round(attend_val)
            attendence.append(attend_round)

            
        percentage_dict = {}
        for uid, name, surname, attendence in zip(all_uid, all_name, all_surname, attendence):
            percentage_dict[uid] = {"name": name, "surname": surname, "Attendence(%)": attendence}
            
        return percentage_dict
    
if __name__ == "__main__":
    main_out = Student(students, students_attendance, students_grades)
    print(main_out.student_avg())
    main_out.percentage()
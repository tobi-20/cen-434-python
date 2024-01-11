import numpy as np

def generate_random_names(n):
    first_names = ['Chijioke', 'Ngozi', 'Obinna', 'Aisha', 'Emeka']
    last_names = ['Eze', 'Okafor', 'Onwuka', 'Abubakar', 'Ugwu']
    
    return np.random.choice(first_names, size=n) + ' ' + np.random.choice(last_names, size=n)

def calculate_cgpa(exam_scores):
    percentage_marks = (exam_scores / 100) * 100
    cgpa = np.where(percentage_marks >= 90, 5.0,
                    np.where(percentage_marks >= 80, 4.5,
                             np.where(percentage_marks >= 70, 4.0,
                                      np.where(percentage_marks >= 60, 3.5, 3.0))))
    return cgpa

num_students = 5

names = generate_random_names(num_students)
ages = np.random.randint(18, 25, size=num_students)
exam_scores = np.random.uniform(60, 100, size=num_students)

cgpa = calculate_cgpa(exam_scores)

print("Simulated Data:")
print("Names:", names)
print("Ages:", ages)
print("Exam Scores:", exam_scores)
print("CGPA:", cgpa)

selected_data = {'Name': names, 'Age': ages, 'ExamScore': exam_scores, 'CGPA': cgpa}
print("\nSelected Data:")
print(selected_data)

passed_indices = np.where(exam_scores >= 70)[0]
passed_data = {'Name': names[passed_indices], 'ExamScore': exam_scores[passed_indices], 'CGPA': cgpa[passed_indices]}
print("\nStudents who passed:")
print(passed_data

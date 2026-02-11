import pandas as pd

student_data_frame = pd.read_csv("student.csv")
# Create a data frame with the student data

filtered_student_data_frame = student_data_frame[
    (student_data_frame["studytime"] >= 3) &
    (student_data_frame["internet"] == 1) &
    (student_data_frame["absences"] <= 5)
]
# Filters the data to match the requirements of high-engagement students

filtered_student_data_frame.to_csv("high_engagement.csv")
# Creates a csv file with the new filtered data set
number_of_students = len(filtered_student_data_frame)
# Find the total number of students

average_grade_of_students = filtered_student_data_frame["grade"].mean()
#Find the average grade using the .mean() method
print(f"Number of high-engagement students: {number_of_students}")
print(f"Average garde of high-engagement students: {average_grade_of_students}")
# Print the number and average grade of the high-engagement students

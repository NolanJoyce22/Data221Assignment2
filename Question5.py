import pandas as pd


student_data_frame = pd.read_csv("student.csv")
#Create a data frame from the student data

def assign_band(grade):
    if grade <= 9:
        return "Low"

    elif grade <= 14:
        return "Medium"

    else:
        return "High"
# Assign grades to 3 different categorical variables (Low,Medium,High)

student_data_frame["grade_band"] = student_data_frame["grade"].apply(assign_band)
# Create new data column by passing grade values into the assign_band function

grade_band_summary_data = (student_data_frame.groupby("grade_band")
.agg(
    number_of_students_summarized = ("grade", "count"),
    average_absences = ("absences", "mean"),
    internet_usage_percentage = ("internet", "mean")
    )

)
# Split the data into 3 groups of high, low, and medium grades
# for each group using .agg calculate number students, average absences, and mean internet usage for each grade band

grade_band_summary_data["internet_usage_percentage"] *= 100
# Convert the internet proportion to a percentage

grade_band_summary_data.to_csv("student_bands.csv")
# Create a csv file from the data set
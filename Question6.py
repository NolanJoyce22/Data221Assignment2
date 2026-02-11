import pandas as pd

crime_data_frame = pd.read_csv("crime.csv")
# Create the data set from the csv

def assign_risk(violent_crime_per_population):
    if violent_crime_per_population >= 0.50:
        return "HighCrime"

    else:
        return "LowCrime"
# Create two different risk groups based off of violent_crime_per_population

crime_data_frame["risk"]  = crime_data_frame["ViolentCrimesPerPop"].apply(assign_risk)
# Create the new column with the HighCrime and LowCrime categories using assign_risk function

risk_summary = (
    crime_data_frame.groupby("risk")
    .agg(
        average_unemployment = ("PctUnemployed", "mean")
    )
)
# Calculate the average unemployment rate based off of crime rate and store it in a new column average_unemployment

print("Average Unemployment Rate by Crime Risk")

for risk_level, row in risk_summary.iterrows():
    print(f"{risk_level}: {row['average_unemployment']}")
# Print the average unemployment rate based off of drime risk

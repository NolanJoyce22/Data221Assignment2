# Data221Assignment2

# Question 1
Takes "sample-file.txt" and counts the number of times tokens with more than 2 characters appear in the file. The output is the top 10 most frequently occurring tokens in the file.

# Question 2
Takes "sample-file.txt" and splits the file into tokens, and then bigrams. The frequency of each bigram is then counted, and the top 5 most frequently occurring bigrams are output.

# Question 3
Uses "sample-file.txt" to find nearly duplicate lines. The file is split into lines and then sets of duplicate lines. The file outputs the number of near duplicate sets and the first two near duplicate sets that occur in the file, along with their corresponding line numbers.

# Question 4
Takes the "student.csv" file and creates a new file "high_engagement.csv", with a new data set containg the high engagement students. Students with more the 3 hours of studying, 1 hour of internet, and 5 or less absences are considered high engagement. The code also outputs the number of high engagement students and the group's grade average.

# Question 5
Uses the "student.csv" file to create a new categorical variable and grouped summary table. The variable is grade band, and the summary table containins the number of students, avearge absences, and percentage of students with internet access in each grade band. The data is saved to a new file "student_bands.csv".

# Question 6
Uses "crime.csv" to create a new column called "risk based on ViolentCrimesPerPop". The column either contains "High-Crime" or "Low-Crime". For each group the average unemployment rate is calculated and printed.

# Question 7
Uses the Wikipedia page "https://en.wikipedia.org/wiki/Data_science" to scrape the first paragraph from the main content area that contains more than 50 characters. The code outputs the page title along with the scraped paragraph.

# Question 8
Uses the webpage "https://en.wikipedia.org/wiki/Data_science". The code extracts all the "h2" section headings from the main content area, and writes them in order to a text file called "headings.txt".

# Question 9
Uses the webpage "https://en.wikipedia.org/wiki/Machine_learning". The code parses the first data table from the main content area that contains at least 3 rows, and saves the extracted table to "Wiki_table.csv".

# Question 10
Uses a function that takes in a file name and keyword as parameters and returns the line and line numbers that contain the specified keyword. The number of matching lines, as well as the first 3 matching lines are output. The code uses the file "sample-file.txt" and the keyword "lorem".


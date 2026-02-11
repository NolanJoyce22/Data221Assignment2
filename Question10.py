def find_lines_containing(filename, keyword):
# Function takes in a filename and key word
# It will return a list of lines that contain the key word
    matches_of_line_and_keyword = []
# Create a list to store the line_number, and the matching_line
    with open(filename, "r", encoding = "utf-8") as file:
# Open the file in read mode
        for line_number, line in enumerate(file, start=1):
            if keyword.lower() in line.lower():
                matches_of_line_and_keyword.append((line_number, line.strip()))
# Loop through each line while tracking line number, converting all characters to lowercase, and
# append the line_number and line that contains the keyword
    return matches_of_line_and_keyword
# return the list

lorem_in_sample_file = find_lines_containing("sample-file.txt", "lorem")
# call the function with file name "sample-file.txt" and key word "lorem"

print(f"Number of matching lines: {len(lorem_in_sample_file)}")

print("\nFirst 3 matching lines")


for line_number, line_text in lorem_in_sample_file[:3]:
    print(f"Line{line_number}: {line_text}")
# Print how many matches were found and the first 3 matching lines
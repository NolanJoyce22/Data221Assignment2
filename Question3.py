import string

with open("sample-file.txt", "r") as file:
    lines = file.readlines()
# Read the file

groups_of_lines = {}
# Create a dictionary with the key as the normalized line and
# the value as the list of (line_number, original line)

for index, line in enumerate(lines, start=1):
# Loop though each line keeping track of its line number
    original_line = line.strip()
# Remove whitespaces from line

    normalized_line = original_line.lower()
# Convert line to all lowercase characters

    normalized_line = normalized_line.replace(" ", "")
# Remove spacing so space differences don't affect results

    for ch in string.punctuation:
        normalized_line = normalized_line.replace(ch, "")

    if normalized_line == "":
        continue
# Remove punctuation and skip empty lines


    if normalized_line not in groups_of_lines:
        groups_of_lines[normalized_line] = []
# If the normalized line hasn't been seen yet create a new list for it

    groups_of_lines[normalized_line].append((index, original_line))
# Add the current line number and original line to the list

duplicate_sets = []
# Create a list to store only duplicate sets
for key in groups_of_lines:
    if len(groups_of_lines[key]) > 1:
        duplicate_sets.append(groups_of_lines[key])
# Only append to list if the group contains more than one line meaning the lines are near duplicate

print("Number of near-duplicate sets:", len(duplicate_sets))

print("\nFirst two sets\n")

for duplicate_group in duplicate_sets[:2]:
    for line_number, text in duplicate_group:
        print(f"Line {line_number}: {text}")
# Print only the first two duplicate sets

    print()
# Print a blank line between the two pairs













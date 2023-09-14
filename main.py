"""
Module for reversing the order of markdown headers ## on a .md file
"""

FILE_NAME = input("Enter file name with extension: ")
section_list = []

# Extract sections
with open(f"{FILE_NAME}", 'r', encoding="UTF-8") as file:
    current_section = ""

    for line in file:
        if ("##" in line) and ("###" not in line):
            section_list.append(current_section)
            current_section = line
            continue

        current_section += line

    section_list.append(current_section + '\n')

# Write sections in reverse order
with open(f"reversed-{FILE_NAME}", 'w', encoding="UTF-8") as file:
    section_list.reverse()

    for line in section_list:
        file.write(line)
        
print("Reversion Completed!")

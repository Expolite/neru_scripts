# Script for renaming folders: replaces spaces with underscores
import os

# Config
find = " "
replace = "_"

# Text Colors
txt_green = "\033[32m"
txt_red = "\033[31m"
txt_yellow = "\033[33m"
txt_colorEnd = "\033[0m"

# Track results
renamed_count = 0
skipped_count = 0

# Get current directory
current_dir = os.getcwd()
print(f"Current path : {current_dir}")

# Get all entries in current directory
all_entries = os.listdir(current_dir)
print(f"All Items : {all_entries}")
print()

for name in all_entries:
    full_path = os.path.join(current_dir, name)
    print(f"Full Path of Item :  {full_path}")

    if os.path.isdir(full_path):                                        # Only handle folders
        print(f"Original Folder : {txt_yellow}{name}{txt_colorEnd}")

        if find in name:
            new_name = name.replace(find, replace)
            new_full_path = os.path.join(current_dir, new_name)     # new path

            # rename folder
            os.rename(full_path, new_full_path)
            print(f"Folder renamed to {txt_green}{new_name}{txt_colorEnd}")
            
            renamed_count += 1
        else:
            print(f"Folder remain: {txt_red}{name}{txt_colorEnd}")
            skipped_count += 1

        print()     # Spacer 

# Final Summary
print(f"{txt_green}[Script Completed!]{txt_colorEnd}")
print(f"Folder Renamed: {txt_green}{renamed_count}{txt_colorEnd}")
print(f"Folder Skipped (No Match): {txt_red}{skipped_count}{txt_colorEnd}")

input("Press Enter to exit...")

# Coded_by_Ronnel_Macompas_-_2025-7-26
import os

# Get the directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))
print(f"[DEBUG] current dir: {current_dir}")

# Loop through items in the same directory as the script
for name in os.listdir(current_dir):
    full_path = os.path.join(current_dir, name)

    # Check if it's a folder (not a file)
    if os.path.isdir(full_path):
        # Create new name by replacing spaces with underscores
        new_name = name.replace(" ", "_")

        # Only rename if there's actually a change
        if new_name != name:
            new_full_path = os.path.join(current_dir, new_name)
            os.rename(full_path, new_full_path)
            print(f'Renamed: "{name}" → "{new_name}"')

# Rename Folder: Replace spaces to underscores
# Coded by Ronnel Macompas 
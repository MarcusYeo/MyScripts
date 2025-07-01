import os

def rename_files(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".srt"):
                # Construct the full path to the file
                file_path = os.path.join(root, filename)
                # Split the filename into name and extension
                name, extension = os.path.splitext(filename)
                
                # Check if the filename contains '_vi' and delete the file if it does
                # if '_vi' in name:
                    # os.remove(file_path)
                    # print(f"Deleted '{file_path}'")
                    # continue  # Skip to the next file
                
                # Check if the filename contains 'English'
                if 'English' in name:
                    # Remove 'English' from the filename
                    new_name = name.replace('English', '').strip()
                    # Construct the new filename
                    new_filename = f"{new_name}{extension}"
                    # Construct the full path to the new file
                    new_file_path = os.path.join(root, new_filename)
                    # Rename the file
                    os.rename(file_path, new_file_path)
                    print(f"Renamed '{file_path}' to '{new_file_path}'")
                
                if '_en' in name:
                    # Remove 'English' from the filename
                    new_name = name.replace('_en', '').strip()
                    # Construct the new filename
                    new_filename = f"{new_name}{extension}"
                    # Construct the full path to the new file
                    new_file_path = os.path.join(root, new_filename)
                    # Rename the file
                    os.rename(file_path, new_file_path)
                    print(f"Renamed '{file_path}' to '{new_file_path}'")

# Replace 'directory_path' with the path to your main directory containing the subfolders
directory_path = r"C:\Users\marcus.yeo\Downloads\myfolder"
rename_files(directory_path)

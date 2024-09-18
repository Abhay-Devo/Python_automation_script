import os
import shutil

# Define folder paths
unorganized_folder = r"C:\\Users\\HP\\OneDrive\\Desktop\\temp1"  # Replace with your directory
organized_folder = r"C:\\Users\\HP\\OneDrive\\Desktop\\temp2"    # Replace with your directory


# File type categories and corresponding file extensions
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Compressed': ['.zip', '.rar', '.7z'],
    'Scripts': ['.py', '.sh', '.bat'],
}


# Create folders for each file type if they don't exist
for folder in file_types.keys():
    folder_path = os.path.join(organized_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


# Iterate over files in the downloads folder and organize them
for filename in os.listdir(unorganized_folder):
    file_path = os.path.join(unorganized_folder, filename)
    

    if os.path.isfile(file_path):           # Check if it's a file

        # Get file extension
        file_extension = os.path.splitext(filename)[1].lower()


        # Move the file to its respective folder based on extension
        moved = False
        for category, extensions in file_types.items():
            if file_extension in extensions:
                dest_folder = os.path.join(organized_folder, category)
                shutil.move(file_path, os.path.join(dest_folder, filename))
                moved = True
                print(f"Moved: {filename} -> {category}")
                break

        # If the file type doesn't match any category, move it to 'Others'
        if not moved:
            other_folder = os.path.join(organized_folder, 'Others')
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"Moved: {filename} -> Others")


print("Task completed: All files organized!")

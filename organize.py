import os
import shutil

# Define the source (Downloads) and destination folders
downloads_folder = "/path/to/Downloads"
destination_folder = "/path/to/organized_folder"

# Ensure the destination folder exists; create it if it doesn't
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# List of common document file extensions to be moved
document_extensions = [".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx"]

# Iterate through files in the Downloads folder
for root, dirs, files in os.walk(downloads_folder):
    for file in files:
        # Check if the file has one of the document extensions
        if any(file.lower().endswith(ext) for ext in document_extensions):
            # Construct the full path of the source file
            source_file_path = os.path.join(root, file)
            
            # Construct the full path of the destination file
            destination_file_path = os.path.join(destination_folder, file)
            
            # Move the file to the destination folder
            try:
                shutil.move(source_file_path, destination_file_path)
                print(f"Moved: {file}")
            except Exception as e:
                print(f"Error moving {file}: {str(e)}")

#print("Organizing complete.")

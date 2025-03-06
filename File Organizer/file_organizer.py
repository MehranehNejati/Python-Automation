import os
import shutil
from datetime import datetime

def organize_files(folder="test_folder"):
    # Map file extensions to folder names
    file_types = {
        ".txt": "text",
        ".jpg": "images",
        ".jpeg": "images",
        ".png": "images",
        ".pdf": "documents"
    }
    
    # Create log file
    log_file = "organize_log.txt"
    with open(log_file, "a") as log:
        log.write(f"\nRun started at {datetime.now()}\n")
    
    # Create folders if they don’t exist
    for folder_name in file_types.values():
        os.makedirs(f"{folder}/{folder_name}", exist_ok=True)
    
    # Sort files
    for file in os.listdir(folder):
        try:
            for ext, folder_name in file_types.items():
                if file.lower().endswith(ext):
                    old_path = os.path.join(folder, file)
                    new_path = os.path.join(folder, folder_name, file)
                    shutil.move(old_path, new_path)
                    msg = f"Moved {file} to {folder_name}"
                    print(msg)
                    with open(log_file, "a") as log:
                        log.write(f"{msg}\n")
        except Exception as e:
            error_msg = f"Error moving {file}: {e}"
            print(error_msg)
            with open(log_file, "a") as log:
                log.write(f"{error_msg}\n")
    
    print("File organization complete! Check organize_log.txt for details.")

# Run it
if __name__ == "__main__":
    organize_files()
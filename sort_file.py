import os
import shutil

def sort_files(folder):
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt'],
        'Others': ['.tar', '.exe', '.zip'],
    }

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()

            if file_extension:
                for category, extensions in file_types.items():
                    if file_extension in extensions:
                        destination_dir = os.path.join(folder, category)
                        if not os.path.exists(destination_dir):
                            os.makedirs(destination_dir)
                        shutil.move(file_path, destination_dir)
                        break
            else:
                destination_dir = os.path.join(folder, 'Folders')
                if not os.path.exists(destination_dir):
                    os.makedirs(destination_dir)
                shutil.move(file_path, destination_dir)

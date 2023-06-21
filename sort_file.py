import os
import shutil
import platform

def sort_files(source_dir):
    pictures_found = False
    videos_found = False
    documents_found = False

    for file_name in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file_name)
        if os.path.isfile(file_path) and not is_system_file(file_path):
            try:
                if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
                    move_to_pictures_directory(file_path)
                    pictures_found = True
                elif file_name.lower().endswith(('.mp4', '.mov', '.avi')):
                    move_to_videos_directory(file_path)
                    videos_found = True
                else:
                    move_to_documents_directory(file_path)
                    documents_found = True
            except Exception as e:
                return f"Failed to move {file_path}: {str(e)}"

    if not (pictures_found or videos_found or documents_found):
        return "There are no files here to sort."
    else:
        return"Files sorted successfully."

def move_to_pictures_directory(file_path):
    destination_dir = get_pictures_directory()
    if destination_dir:
        new_folder_name = 'VA-Pictures'
        create_new_folder(destination_dir, new_folder_name)

        destination_file_path = os.path.join(destination_dir, new_folder_name, os.path.basename(file_path))
        shutil.move(file_path, destination_file_path)
        # print(f"Moved {file_path} to {destination_file_path}")
    else:
        return "Failed to determine Pictures directory."

def move_to_videos_directory(file_path):
    destination_dir = get_videos_directory()
    if destination_dir:
        new_folder_name = 'VA-Videos'
        create_new_folder(destination_dir, new_folder_name)

        destination_file_path = os.path.join(destination_dir, new_folder_name, os.path.basename(file_path))
        shutil.move(file_path, destination_file_path)
        # print(f"Moved {file_path} to {destination_file_path}")
    else:
        return "Failed to determine Videos directory."

def move_to_documents_directory(file_path):
    destination_dir = get_documents_directory()
    if destination_dir:
        new_folder_name = 'VA-Documents'
        create_new_folder(destination_dir, new_folder_name)

        destination_file_path = os.path.join(destination_dir, new_folder_name, os.path.basename(file_path))
        shutil.move(file_path, destination_file_path)
        # print(f"Moved {file_path} to {destination_file_path}")
    else:
        return "Failed to determine Documents directory."

def create_new_folder(destination_dir, folder_name):
    new_folder_path = os.path.join(destination_dir, folder_name)
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)

def get_pictures_directory():
    if platform.system() == 'Windows':
        return os.path.expanduser("~/Pictures")
    elif platform.system() == 'Darwin':
        return os.path.expanduser("~/Pictures")
    elif platform.system() == 'Linux':
        return os.path.expanduser("~/Pictures")
    else:
        return None

def get_videos_directory():
    if platform.system() == 'Windows':
        return os.path.expanduser("~/Videos")
    elif platform.system() == 'Darwin':
        return os.path.expanduser("~/Movies")
    elif platform.system() == 'Linux':
        return os.path.expanduser("~/Videos")
    else:
        return None

def get_documents_directory():
    if platform.system() == 'Windows':
        return os.path.expanduser("~/Documents")
    elif platform.system() == 'Darwin':
        return os.path.expanduser("~/Documents")
    elif platform.system() == 'Linux':
        return os.path.expanduser("~/Documents")
    else:
        return None

def is_system_file(file_path):
    if platform.system() == 'Windows':
        return bool(os.path.basename(file_path).startswith('.') or os.path.splitext(file_path)[0].startswith('.'))
    else:
        return False
import os
import platform
import subprocess
import concurrent
import asyncio

async def find_files_and_folders(directory, name):
    found_items = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for root, dirs, files in os.walk(directory):
            for dir_name in dirs:
                if name.lower() in dir_name.lower():
                    found_items.append(os.path.join(root, dir_name))
            for file_name in files:
                if name.lower() in file_name.lower():
                    found_items.append(os.path.join(root, file_name))
    return found_items


def open_directory(path):
    # Check the OS platform
    if platform.system() == 'Darwin':  # macOS
        subprocess.run(['open', '-R', path])
    elif platform.system() == 'Windows':
        subprocess.run(['explorer', os.path.normpath(path)])
    elif platform.system() == 'Linux':
        subprocess.run(['xdg-open', os.path.normpath(path)])
    else:
        return "Unsupported operating system."
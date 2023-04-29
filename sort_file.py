import os
import shutil

download_folder = os.path.expanduser('~/Desktop')
photo_folder = os.path.expanduser('~/Pictures/pythonVA-images')
video_folder = os.path.expanduser('~/Videos/pythonVA-videos')

def sort_images(dir):

    if not os.path.exists(photo_folder):
        os.makedirs(photo_folder)

    if dir == "desktop":
        from_dir = os.path.expanduser('~/Desktop')

    if dir == "download":
        from_dir = os.path.expanduser('~/Downloads')

    files = os.listdir(from_dir)
    image_files = [f for f in files if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    for f in image_files:
        shutil.move(os.path.join(from_dir, f), os.path.join(photo_folder, f))

def sort_videos(dir):

    if not os.path.exists(video_folder):
        os.makedirs(video_folder)
    
    if dir == "1":
        from_dir = os.path.expanduser('~/Desktop')

    if dir == "2":
        from_dir = os.path.expanduser('~/Downloads')

    files = os.listdir(from_dir)
    image_files = [f for f in files if f.endswith(('.mp4', '.mov', '.mkv', '.gif'))]

    for f in image_files:
        shutil.move(os.path.join(from_dir, f), os.path.join(video_folder, f))


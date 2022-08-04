from fileinput import filename
import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


from_dir = "/Users/aaravshah/Downloads"
to_dir = "/Users/aaravshah/Desktop/Classes/Coding/PYTHON/Projects/PRO103Test"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
       name,ext=os.path.splitext(event.src_path)
       time.sleep(1)
       for key,value in dir_tree.items():
            time.sleep(1)
            if ext in value:
                filename=os.path.basename(event.src_path)
                print("downloaded--" + filename)

                path1=from_dir+'/'+ filename
                path2=to_dir+'/' + key
                path3=to_dir+'/' + key + '/' + filename

                if os.path.exists(path2):
                    print("directory exists")
                    print("moving--" + filename)
                    shutil.move(path1,path3)
                    time.sleep(1)
                
                else:
                    print("making directory--")
                    os.makedirs(path2)
                    print("moving--" + filename)
                    shutil.move(path1,path3)
                    time.sleep(1)


# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


while True:
    time.sleep(2)
    print("running...")

    
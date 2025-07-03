import shutil
import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#PATHS
sourceDirectory = "C:/Users/alfar/Downloads"
dir_images = "C:/Users/alfar/Downloads/Downloaded Images"
dir_zip = "C:/Users/alfar/Downloads/Downloaded Zip Files"
dir_videos = "C:/Users/alfar/Downloads/Downloaded Videos"
dir_documents = "C:/Users/alfar/Downloads/Downloaded Documents"

#CREATE UNIQUE FILE NAME IF NEEDED
def makeUnique(destination, name):
    filename, extension = os.path.splitext(name)
    counter = 1
    new_name = name

    while os.path.exists(os.path.join(destination, new_name)):
        new_name = f"{filename}({counter}){extension}"
        counter += 1

    return new_name

#MOVE FILE TO DESTINATION
def moveFile(destination, entry, name):

    if os.path.exists(os.path.join(destination, name)):
        name = makeUnique(destination, name)

    shutil.move(entry.path, os.path.join(destination, name))
    logging.info(f"Moved {entry.name} to {destination}")

#FILE EVENT HANDLER
class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(sourceDirectory) as entries:
            for entry in entries:

                if entry.is_file():

                    name = entry.name.lower()
                    if name.endswith((".png", ".jpg", ".jpeg")):
                        moveFile(dir_images, entry, entry.name)

                    elif name.endswith(".zip"):
                        moveFile(dir_zip, entry, entry.name)

                    elif name.endswith((".mp4", ".mov")):
                        moveFile(dir_videos, entry, entry.name)

                    elif name.endswith((".pdf",".docx",".xlsx")):
                        moveFile(dir_documents, entry, entry.name)

#MAIN SCRIPT
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, sourceDirectory, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

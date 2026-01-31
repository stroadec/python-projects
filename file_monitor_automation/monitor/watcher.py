import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileHandler(FileSystemEventHandler):
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def on_created(self, event):
        if event.is_directory:
            return

        time.sleep(1)
        shutil.move(event.src_path, f"{self.destination}/{event.src_path.split('/')[-1]}")
        print(f"📁 File processed: {event.src_path}")

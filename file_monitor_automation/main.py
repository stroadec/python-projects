import os
import yaml
from watchdog.observers import Observer
from monitor.watcher import FileHandler

def main():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    source = config["watch_folder"]
    destination = config["processed_folder"]

    os.makedirs(source, exist_ok=True)
    os.makedirs(destination, exist_ok=True)

    event_handler = FileHandler(source, destination)
    observer = Observer()
    observer.schedule(event_handler, source, recursive=False)
    observer.start()

    print(f"👀 Monitoring folder: {source}")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    main()

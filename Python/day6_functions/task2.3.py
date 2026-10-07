import os

def list_directory(path):
    for item in os.listdir(path):
        print(item)

        full_path = os.path.join(path, item)

        if os.path.isdir(full_path):
            list_directory(full_path)

list_directory(".")
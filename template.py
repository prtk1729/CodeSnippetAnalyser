import os
from pathlib import Path # '/' in linux/mac interconversion to Windows
import logging


logging.basicConfig( level=logging.INFO,
                    format= '[%(asctime)s]: %(message)s:' ) # Trap


list_of_dir = [
                "src/__init__.py",
                "src/helper.py",
                "requirements.txt",
                "setup.py",
                "research/trials.ipynb",
                ".env",
                "app.py"
              ]



def create_folder(filedir):
    # create directory
    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # Creates if didnt exist only
        logging.info(f"Creating a new Directory: {filedir}") # Trap: logging.info not logging 
    return


def create_file(filename):
    # create file -> Only if not existing before or Existed before but 0-content
    # 0-content i.e wont overwrite by creating new file
    if (not os.path.exists(filename)) or ( os.path.getsize(filename) == 0):
        with open(file, "w"):
            pass # trick creates  the file
            logging.info(f"Created a new file: {filename}")
    else:
        logging.info(f"File already existed Before")
    return


for file in list_of_dir:
    # interconversion b/w os
    dir = Path(file) # Windows(files_string)
    # split to filedir, filename
    filedir, filename = os.path.split(dir)  
    create_folder(filedir)
    create_file(filename)




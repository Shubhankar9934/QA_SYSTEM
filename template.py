import os
from pathlib import Path
import logging

# list all files in the current directory
list_of_files =[
    "QA_WithPDF/__init__.py",
    "QA_WithPDF/data_ingention.py",
    "QA_WithPDF/embedding.py",
    "QA_WithPDF/model_api.py",
    "notebook/experiments.ipynb",
    "StramlitApp.py",
    "logger.py",
    "exception.py",
    "setup.py"
]

# create a directory

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Directory created: {filedir} for the file: {filename}")

        if (not os.path.exists(filepath) or (os.path.getsize(filepath) == 0)):
            with open(filepath, 'w') as f:
                pass
                logging.info(f"Creating empty file: {filepath}")
        
        else:
            logging.info(f"File already exists: {filepath}")
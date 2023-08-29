import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'TextSummarizer'

list_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init.py__",
    f"src/{project_name}/components/__init.py__",
    f"src/{project_name}/utils/__init.py__",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init.py__",
    f"src/{project_name}/config/__init.py__",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init.py__",
    f"src/{project_name}/entity/__init.py__",
    f"src/{project_name}/constants/__init.py__",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
]

for file in list_files:
    file = Path(file)
    filedir, filename = os.path.split(file)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory: {filedir} for the file {filename}")
    if(not os.path.exists(file)) or (os.path.getsize(file) == 0):
        with open(file, "w") as f:
            pass
            logging.info(f"creating empty file: {filename}")
    else:
        logging.info(f"{filename} already exists")
import os
from pathlib import Path  
import logging
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s')

project_name = 'textSummarization'
list_of_files = [".github/workflow/.gitkeep",
                f"src/{project_name}/__init__.py",
                f"src/{project_name}/utils/__init__.py",
                f"src/{project_name}/components/common.py",
                f"src/{project_name}/logging/__init__.py",
                f"src/{project_name}/config/__init__.py",
                f"src/{project_name}/config/configuration.py",
                f"src/{project_name}/pipeline/__init__.py",
                f"src/{project_name}/entity/__init__.py",
                f"src/{project_name}/constants/__init__.py",
                "config/config.yml",
                "param.yml",
                "app.py",
                "Dockerfile",
                "requirements.txt",
                "setup.py",
                'research/trials.ipnyb'
                ]


for pathfile in list_of_files:
    pathfile = Path(pathfile)
    filedir,filename = os.path.split(pathfile)
    
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Created directory:{filedir} for the file name {filename}")
        
    if (not os.path.exists(pathfile)) or (os.path.getsize(pathfile)==0):
        with open(pathfile,'w') as f:
            pass 
            logging.info(f"Creating empty file:{pathfile}")
    
    else:
        logging.info(f"{pathfile} already exists")
        
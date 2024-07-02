
#chack if the file exsist or not in python

import os

file_path="E:\python_in_one_folder\olevel_python_practis_set\Q4.py"

if os.path.exists(file_path):
    print(f"the file path {file_path} exsist")
else:
    print(f"the file path {file_path} not exsist")
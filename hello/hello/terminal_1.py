import subprocess
import os

command = "python manage.py runserver 192.168.1.40:8000"
#result = subprocess.run(command, shell=True, capture_output=True, text=True)

os.system(command)
input("Enter to close")
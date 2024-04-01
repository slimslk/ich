import os
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-file", help="Path to python file")
arg = parser.parse_args()

file_name = os.path.basename(arg.file)
if not os.path.exists(file_name):
    print(f"File {file_name} not found!")
elif not file_name.endswith(".py"):
    print(f"File {file_name} couldn't be executed!")
else:
    print(f"Файл {file_name} успешно запущен")

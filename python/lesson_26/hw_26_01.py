from os import path, system
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-file", help="Path to python file")
arg = parser.parse_args()

file_name = path.basename(arg.file)
if not path.isfile(arg.file):
    print(f"Not a file or file {file_name} doesn't exist")
else:
    if len(file_name) < 3 or not file_name.endswith(".py"):
        print(f"File {file_name} couldn't be executed!")
    else:
        system(f"python {arg.file}")
        print(f"Файл {file_name} успешно запущен")




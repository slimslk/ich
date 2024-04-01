from os import walk, path
from argparse import ArgumentParser


def get_files_and_sub_dirs_list(dir_path: str) -> list[str]:
    elements = walk(dir_path)
    files_sub_dirs_list = []
    for cur_path, sub_dirs, files in elements:
        for file in files:
            file_path = path.join(cur_path, file)
            files_sub_dirs_list.append(file_path)
        for sub_dir in sub_dirs:
            subdir_path = path.join(cur_path, sub_dir)
            files_sub_dirs_list.append(subdir_path)
    return files_sub_dirs_list


parser = ArgumentParser()
parser.add_argument("-path", help="Path to directory")
arg = parser.parse_args()
dir_path = arg.path
if not path.exists(dir_path):
    print(f"Directory {dir_path} not found!")
else:
    for item in get_files_and_sub_dirs_list(dir_path):
        print(f"{item}")

import os
import pathlib

# print(os.path.exists(r"D:\SteamLibrary"))


# print(type(path))


# for i in path.iterdir():
#     print(i.name)


def parse_folder(path):
    files = []
    folders = []
    for i in pathlib.Path.iterdir(path):
        if i.is_file():
            files.append(i.name)
        if i.is_dir():
            folders.append(i.name)

    return files, folders


os.path.exists(r"D:\SteamLibrary")
path = pathlib.Path(r"D:\SteamLibrary")
parse_folder(path)

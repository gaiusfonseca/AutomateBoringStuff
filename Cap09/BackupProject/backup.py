#! /usr/bin/python
# Usage: backup a folder to a zip file and increment version each time itś used.

import re, os, zipfile

# set working directory
def set_working_directory():
    working_directory = os.path.join(os.getcwd(), "Cap09", "BackupProject")
    os.chdir(working_directory)
    print(f"working directory set to: {working_directory}")

# returns the highest index in an array
def get_highest_index(indexes):
    indexes.sort(reverse=True)
    return indexes[0] + 1

# get the index for the next backup
def get_next_index():
    basename = os.path.basename(os.getcwd())
    extension = "\\.zip"
    filename_regex = re.compile(basename + "_" + "(?P<index>\\d+)" + extension)
    indexes = [0]

    for filename in os.listdir("."):
        print(f"testing a match against {filename} with {filename_regex}")
        match = filename_regex.match(filename)
        print(f"found a match? {"no" if match == None else "yes"}")
        if match:
            indexes.append(int(match.group("index")))

    return get_highest_index(indexes)

# generate the new backup name
def generate_backup_name():
    basename = os.path.basename(os.getcwd())
    index = get_next_index()
    extension = ".zip"
    return f"{basename}_{index}{extension}"

# create backup file
def backup_to_zip(folder):
    archive_name = generate_backup_name()
    print(f"creatting zip archive: {archive_name}")
    zip_archive = zipfile.ZipFile(archive_name, "w")
    for file in os.listdir(folder):
        zip_archive.write(file, compress_type=zipfile.ZIP_DEFLATED)
        print(f"{file} added to ziparchive.")
    zip_archive.close()
    print("backup created!")

set_working_directory()
backup_to_zip(".")

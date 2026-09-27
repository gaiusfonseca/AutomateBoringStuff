#! /usr/bin/python
# Usage: generate sample files for the project and rename 
# switching american date style for european date style.

import os
import re

def generate_basename(text_before, date, text_after, extension):
    name = " ".join([text_before, date, text_after])
    basename = ".".join([name, extension])
    return basename

def create_file(folder_path, basename):
    file_path = os.path.join(folder_path, basename)
    file = open(file_path, 'w')
    file.write("tips about beating the game.")
    file.close()

def generate_samples(target_folder, games):
    for game, release in games.items():
        file_name = generate_basename(game, release, "notes","txt")
        create_file(target_folder, file_name)

def match_file_name(file_name):
    regex = re.compile(r"""
    ^(?P<text_before>.*?)                                           # text before
    (?P<month>[01]\d)-(?P<day>[0123]\d)-(?P<year>(?:19|20)\d{2})    # date
    (?P<text_after>.*?)$                                            # text after 
    """, re.VERBOSE)

    matching_object = regex.search(file_name)
    return matching_object

def rename_file(folder_path, old_name, new_name):
    old = os.path.join(folder_path, old_name)
    new = os.path.join(folder_path, new_name)
    os.rename(old, new)

games = {
    "castlevania": "09-26-1986",
    "castlevania II simon's quest": "12-01-1988",
    "castlevania III dracula's curse": "10-25-1990"
}

project_directory = os.path.join(os.getcwd(), "Cap09", "RenameProject")
generate_samples(project_directory, games)
files = os.listdir(project_directory)

for file_name in files:
    matching_object = match_file_name(file_name)
    if matching_object != None:
        european_basename = f"{matching_object.group("text_before")} " \
            f"{matching_object.group("day")}-{matching_object.group("month")}-{matching_object.group("year")} " \
            f"{matching_object.group("text_after")}"
        rename_file(project_directory, file_name, european_basename)
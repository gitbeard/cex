import os
import shutil
import time
import functions_excel


def get_full_path_files(source_dir):
    filenames = []
    files = os.listdir(source_dir)
    #print(files)
    i = 0
    while i < len(files):
        thisfilename = os.path.abspath(source_dir + files[i])
        filenames.append(thisfilename)
        i = i + 1
    return filenames

def old_get_files(source_dir):
    filenames = []
    files = os.listdir(source_dir)
    #print(files)
    i = 0
    while i < len(files):
        thisfilename = os.path.join(source_dir, files[i])
        filenames.append(thisfilename)
        i = i + 1
    return filenames


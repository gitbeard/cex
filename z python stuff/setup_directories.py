import os

def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)

def setup_dirs():
    # Creates these directories inside the directory this file is located.
    dir_list = []
    dir_list.append("DATA\\RAW\\")  # Don't forget to use \\
    dir_list.append("DATA\\PROCESSED\\")
    dir_list.append("DATA\\OUTPUT\\")
    for d in dir_list:
        print(d)
        ensure_dir(d)

#setup_dirs()

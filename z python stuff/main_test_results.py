import datetime
import time
import os
from functions_db import *
from functions_excel import *
from functions_files import *

################################################################################
def main():
    files = get_files()
    print(files)

    for f in files:
        #first_file.excel_to_db(f)
        #move_file(destin_dir, f)
        
        file_info = importing_file_info(f)
        file_info_insert(file_info)

        table = "file_info"
        where = "`filename` = '" + file_info['filename'] + "'"
        this_file_db = dbselect(table, where)
        #print(this_file_db)
        file_id = this_file_db[0]['id']
        
        
        
        raw_file_content = get_raw_excel(f)
        y = raw_file_content.get()
        
        #print(file_info)
        #print(raw_file_content)
        
        for z in y:
            raw_opto = to_raw_db(z, file_id)

            #print(raw_opto)
            raw_data_insert(raw_opto)




################################################################################
def get_files():
    source_dir = "DATA\\RAW\\"
    destin_dir = "DATA\\PROCESSED\\"
    output_dir = "DATA\\OUTPUT\\"
    
    #files = get_files(source_dir)
    #print(files)

    files = get_full_path_files(source_dir)
    # print(files)
    return files
    
################################################################################
def to_raw_db(z, file_id):
    raw_opto = {'file_id':file_id,
                'row_id':0,
                'A':'','B':'','C':'','D':'','E':'','F':'','G':'',
                'H':'','I':'','J':'','K':'','L':'','M':'','N':'',
                'O':'','P':'','Q':'','R':'','S':'','T':''}

    columns = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']

    i = 0
    while i < len(z):
        if type(z[i]) is datetime.datetime:
            # Convert this cell and next column to proper datetime.
            date = z[i]
            i = i + 1
            time = z[i]

            time = excel_dec_to_time(time)
            date_time = add_time_to_datetime(date, time)

            raw_opto[columns[i]] = str(date_time)

        else:
            raw_opto[columns[i]] = str(z[i])
        i = i + 1

    return raw_opto

################################################################################
def importing_file_info(f):
    file_info = {'id':0,
                 'filename':'',
                 'date_modified':'',
                 'date_uploaded':'',
                 'parsed':0,
                 'printed':0,
                 'unit_id':0}

    mod_time = os.path.getmtime(f) # File's Date Modified time in seconds.
    fn = f.split('\\')
        
    file_info['filename'] = fn[len(fn)-1]
    file_info['date_modified'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(mod_time))  # Date Modified of file
    file_info['date_uploaded'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))  # Time right now
    file_info['unit_id'] = 1  # fn[len(fn)-2] Probably use folder name to figure out unit id later.

    return file_info



main()

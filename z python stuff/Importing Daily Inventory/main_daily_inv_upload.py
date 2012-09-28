import datetime
import time
import os
from functions_db import *
from functions_excel import *
from functions_files import *

################################################################################
def main():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) + "\n")
    files = get_files()
    print(files)

    for f in files:
        #first_file.excel_to_db(f)
        #move_file(destin_dir, f)
        
        file_info = importing_file_info(f)
        file_info_insert_inv(file_info)



        ## Get the file_id for the file being uploaded (id in file_info table)
        ## Put this id into the daily_inventory table for tracking info
        table = "file_infos"
        where = "`filename` = '" + file_info['filename'] + "'"
        this_file_db = dbselect(table, where)
        file_id = this_file_db[0]['id']
        
        
        wb = xl.Workbook(f)                     # Open this Excel File
        ws = wb.worksheets                      # Get a list of worksheets for this file
        ws_names = get_worksheet_names(ws)      # Get the names and indexes of the worksheets
        ws_ind = ws_names["NC INV"]             # Get the index of this worksheet name
        ws[ws_ind].xlWorksheet.Activate()       # Activate this worksheet

        content = wb.get("A2:L5000")            # Select data in this range
        actual_content = content.get()          # Actually get the data


        # For each row, format it for insertion into database
        # Then insert it
        source_dir = "DATA\\OUTPUT\\"
        the_filename = file_info['filename'].split('.')[0]
        filename = source_dir + the_filename + '.csv'
        thisfile = open(filename, 'a')
                
        for a in actual_content:
            if a[0] is None:
                break
            else:
                inv_row = make_inv_record(a, file_info['date_modified'], int(file_id))
                #inv_row_insert(inv_row)
                v = inv_row
                
                msg = str(v['item_number']) + ',' + str(v['location_id']) + ',' + str(v['datetime']) + ',' + str(v['quantity']) + ',' + str(v['file_id']) + '\n'
                thisfile.writelines(msg)
        thisfile.close()
        print(the_filename)
        up_filename = "DATA\/OUTPUT\/" + the_filename + ".csv"
        print(up_filename)
        upload_csv(up_filename)
                
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) + "\n")
    return

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
def make_inv_record(a, date_modified, file_id):
    inv_row = {'item_number':0,
               'location_id':2,
               'datetime':date_modified,
               'quantity':0,
               'file_id':file_id}

    inv_row['item_number'] = int(a[0])
    inv_row['quantity'] = int(a[4])

    return inv_row

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
                 'date_uploaded':''}

    mod_time = os.path.getmtime(f) # File's Date Modified time in seconds.
    fn = f.split('\\')
        
    file_info['filename'] = fn[len(fn)-1]
    file_info['date_modified'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(mod_time))  # Date Modified of file
    file_info['date_uploaded'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))  # Time right now

    return file_info



main()

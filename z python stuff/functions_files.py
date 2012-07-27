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
        thisfilename = os.path.abspath(files[i])
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

def get_files_paths(source_dir):
    filenames = []
    files = os.listdir(source_dir)
    i = 0
    while i < len(files):
        thisfilename = os.path.join(source_dir, files[i])
        filenames.append(thisfilename)
        i = i + 1
    return filenames


        








##def process_messages():
##    try:
##        source_dir = "DATA\\RAW\\"
##        destin_dir = "DATA\\PROCESSED\\"
##        output_dir = "DATA\\OUTPUT\\"
##        files = os.listdir(source_dir)
##        print(files)
##        i = 0
##        while i < len(files):
##            thisfilename = os.path.join(source_dir, files[i])
##            #print(thisfilename)
##            thisfile = open(thisfilename, 'r')
##            thisdata = thisfile.readlines()
##            thisfile.close()
##            #print(thisdata)
##            phone_number = ''
##            x = 0
##            while x < len(thisdata):
##                thisline = thisdata[x]
##                #print(thisline)
##
##                ####################################
##                # CMGR Line
##                
##                if(thisline.find("(") >= 0):
##                    #print(thisline
##                    thisline = thisline.split('(')[1]
##                    if(thisline.find("-") >= 0):
##                        thisline = thisline.split('-')[0]
##                    if(thisline.find('\"') >= 0):
##                        thisline = thisline.split('\"')[0]
##                    if(thisline.find(')') >= 0):
##                        thisline = thisline.split(')')[0]
## 
##                    print(thisline)
##                    
##                x = x + 1
##
##            #shutil.move(source_dir + files[i], destin_dir + files[i])
##            i = i + 1
##
##        return
##    
##    except Exception(exception):
##               #ser.close()
##               print("Error in transfer()\n")
##               print('Error Message:' + str(exception) + "\n")
##               destin_dir = "DATA\\ERRORS\\"
##               shutil.move(source_dir + files[i], destin_dir + files[i])
##               return


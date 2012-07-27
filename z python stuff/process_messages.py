from db_functions import *
#from dbselect import *
#from get_roster import *
#from alarms import *
#from sendsms import *
from parse_messages import *

import os
import shutil
import time

def process_messages():
    try:
        source_dir = "DATA\\RAW\\"
        destin_dir = "DATA\\PROCESSED\\"
        files = os.listdir(source_dir)
        print files
        i = 0
        while i < len(files):
            thisfilename = os.path.join(source_dir, files[i])
            print thisfilename
            thisfile = open(thisfilename, 'r')
            thisdata = thisfile.readlines()
            thisfile.close()
            print thisdata
            phone_number = ''
            x = 0
            while x < len(thisdata):
                thisline = thisdata[x]
                print thisline

                ####################################
                # CMGR Line
                
                if(thisline.find("+CMGR:") >= 0):
                    #print thisline
                    thisline = thisline.split('\",\"')
                    phone_number = thisline[1]
                    timestamp = thisline[3]
                    if(phone_number.find('+') >=0):
                        phone_number = phone_number.split('+')[1]
                    if(timestamp.find(':') >= 0):
                        if(timestamp.find('-') >= 0):
                            timestamp = timestamp.split('-')[0]
                        elif(timestamp.find('+') >= 0):
                            timestamp = timestamp.split('+')[0]
                        timestamp = time.mktime(time.strptime(timestamp.strip(), "%y/%m/%d,%H:%M:%S"))
                        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))

                # End CMGR Line
                ####################################

                elif(thisline.find("AT+CMGR=") >= 0 or thisline.find("OK\r\n") >= 0):
                    thisline = thisline # This is junk, don't do anything.

                # Insert all messages into the all_messages table.
                elif(thisline.find("\r\n") >= 0):
                    insert_message = {'time_sent':"",
                                      'time_inserted':"",
                                      'phone_number':0,
                                      'message':''}
                    
                    thisline = thisline.split("\r\n")[0]
                    if (len(thisline) > 0):
                        print thisline
                        insert_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))  # Time right now
                        insert_message['time_sent'] = timestamp
                        insert_message['time_inserted'] = insert_time
                        insert_message['phone_number'] = int(phone_number)
                        insert_message['message'] = thisline

                        all_messages_insert(insert_message)

                        if(thisline.find("Cmd") >= 0):
                            parse_radio_feedback(thisline, phone_number, timestamp)
                        else:
                            parse_dau_data(thisline, phone_number, timestamp)

                    # Then Process each message.
                    # DTI X4
                    #if(thisline.find("<u") >= 0):
                        #print "X4"
                        #parse_dti_x4(thisline)


##                # MAXBOTIX                
##                elif(thisline.find("000:") >= 0):
##                    print "Maxbotix"
##                    parse_maxbotix(thisline, phone_number, timestamp)
                x = x + 1

            shutil.move(source_dir + files[i], destin_dir + files[i])
            i = i + 1

        return
    
    except Exception, exception:
               #ser.close()
               print("Error in process_messages()\n")
               print('Error Message:' + str(exception) + "\n")
               destin_dir = "DATA\\ERRORS\\"
               shutil.move(source_dir + files[i], destin_dir + files[i])
               return


from db_functions import *
from parse_alarm import *
from event_logger import *
import os
import shutil
import time


def parse_dau_data(thisline, phone_number, timestamp):
    try:
        # Example messages:
        # 90147 011711:1032 lowBattery_warning 476,480
        # 90147 011711:1044 heartbeat 478,479
        # 89048 011711:1302 overflow_warning 1800,1632
        # 89048 011611:1307 164,1635
        # 90147 010100:0002  1625,837,61,87,61,84,64,85/010680:0003 0000.0000N,00000.0000E,M,0,00,0.0
        # 90147 010100:0002 heartbeat 1629,827,63,90,61,89,71,96/010680:0003 0000.0000N,00000.0000E,M,0,00,0.0
        # 90147 010100:0002 info+info+info+info+info+info+heartbeat 1643,865,51,75,50,76,51,78/010680:0003 0000.0000N,00000.0000E,M,0,00,0.0
        # 93628 041211:2156 lowBattery_warning+info+heartbeat 482,483,0,0,0,0,0,0/045716.000,3346.5741N,11823.7314W,299.4M,2,08,0.9
        # 14626 011812:1558 heartbeat 287,2,3,2,2,2,2,2,2,2,2,2,3,2,87,758/010680:0003 0000.0000N,00000.0000E,M,0,00,0.0

        data_info = {'time_sent':timestamp,
                     'time_data':"",
                     'phone_number':int(phone_number),
                     'unit_serial':0,
                     'alert_message':''}

        gps_present = 0
        if(thisline.find('/') > 0):
            gps_present = 1

        this_line = thisline.split(" ")

        # First test if the first value is 5 digits
        if(len(this_line[0]) == 5):
            try:
                # Then make sure no letters in first value
                if(int(this_line[0])):
                    # Serial number for that unit
                    data_info['unit_serial'] = int(this_line[0])

                    # Timestamp of the data
                    ts = time.strptime(this_line[1],"%m%d%y:%H%M") # Convert DayMonthYear:HourMin to a struct_time
                    #mk_ts = time.mktime(ts) # Converts to seconds
                    #ts = time.localtime(mk_ts) # Convert back to struct_time
                    data_info['time_data'] = time.strftime("%Y-%m-%d %H:%M:00", ts)



                # Sort out Data and GPS
                x = len(this_line)
                if(gps_present == 0):
                    if(x == 3):  # No alert message
                        data_line = this_line[2]
                    elif(x == 4): # Alert message
                        data_info['alert_message'] = this_line[2]
                        data_line = this_line[3]

                elif(gps_present == 1):
                    if(x == 3):  # No alert message AND no space in gps
                        data_line = this_line[2]
                        data_gps = data_line.split('/')
                        data_line = data_gps[0]
                        gps_line = data_gps[1]
                    elif(x == 4):  # Alert message OR space in gps
                        if(this_line[2].find(',') == -1): # Alert message
                            data_info['alert_message'] = this_line[2]
                            data_line = this_line[3]
                            data_gps = data_line.split('/')
                            data_line = data_gps[0]
                            gps_line = data_gps[1]
                        else:  # Space in gps
                            data_line = this_line[2]
                            gps_line = this_line[3]
                            
                    elif(x == 5):  # Alert message AND space in gps
                        data_info['alert_message'] = this_line[2]
                        data_line = this_line[3]
                        gps_line = this_line[4]

                    # Parse GPS Portion
                    gps = gps_line.split(',')
                    if(len(gps) > 6):
                        gps.pop(0)
                    parse_gps_portion(gps, data_info)

                # Parse Data Portion
                data = data_line.split('/')[0]
                data = data.split(',')
                parse_data_portion(data, data_info)

                return

            except Exception, exception:
               print("Error, not a data message\n")
               print('Error Message:' + str(exception) + "\n")
               return

        return # If len(this_line[0]) != 5

    except Exception, exception:
       print("Error in parse_dau_data()\n")
       print('Error Message:' + str(exception) + "\n")
       log_error("Error in parse_dau_data. Detail: " + str(exception) + "\n")
       return


def parse_data_portion(data, data_info):
    try:
        dau_data = {'time_sent':data_info['time_sent'],
                    'time_inserted':"",
                    'time_data':data_info['time_data'],
                    'phone_number':data_info['phone_number'],
                    'unit_serial':data_info['unit_serial'],
                    'sensor_1':0,
                    'sensor_2':0,
                    'sensor_3':0,
                    'sensor_4':0,
                    'sensor_5':0,
                    'sensor_6':0,
                    'sensor_7':0,
                    'sensor_8':0,
                    'sensor_9':0,
                    'sensor_10':0,
                    'sensor_11':0,
                    'sensor_12':0,
                    'sensor_13':0,
                    'sensor_14':0,
                    'sensor_15':0,
                    'sensor_16':0,
                    'alert_message':data_info['alert_message']}
        
        dau_data['sensor_1'] = int(data[0])
        dau_data['sensor_2'] = int(data[1])
        if(len(data) > 2):
            dau_data['sensor_3'] = int(data[2])
            dau_data['sensor_4'] = int(data[3])
            dau_data['sensor_5'] = int(data[4])
            dau_data['sensor_6'] = int(data[5])
            dau_data['sensor_7'] = int(data[6])
            dau_data['sensor_8'] = int(data[7])
        if(len(data) > 8):
            dau_data['sensor_9'] = int(data[8])
            dau_data['sensor_10'] = int(data[9])
            dau_data['sensor_11'] = int(data[10])
            dau_data['sensor_12'] = int(data[11])
            dau_data['sensor_13'] = int(data[12])
            dau_data['sensor_14'] = int(data[13])
            dau_data['sensor_15'] = int(data[14])
            dau_data['sensor_16'] = int(data[15])

        insert_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))  # Time right now
        dau_data['time_inserted'] = insert_time

        print dau_data

        dau_data_insert(dau_data)
        parse_alarm(dau_data)

        return

    except Exception, exception:
       print("Error in parse_data_portion()\n")
       print('Error Message:' + str(exception) + "\n")
       log_error("Error in parse_data_portion. Detail: " + str(exception) + "\n")
       return


def parse_gps_portion(gps, data_info):
    try:
        gps_data = {'time_inserted':"",
                    'time_data':data_info['time_data'],
                    'phone_number':data_info['phone_number'],
                    'unit_serial':data_info['unit_serial'],
                    'north':0.0,
                    'west':0.0,
                    'raw_north':0.0,
                    'raw_west':0.0,
                    'altitude':0.0,
                    'num_satellites':0,
                    'gps_differential':0,
                    'accuracy_meters':0.0}

        north_p = '0.0'
        west_p = '0.0'
        if(gps[0].find('N') >= 0):
            north_p = gps[0].split('N')[0]
        elif(gps[0].find('S') >= 0):
            north_p = gps[0].split('S')[0]
        if(gps[1].find('W') >= 0):
            west_p = gps[1].split('W')[0]
        elif(gps[1].find('E') >= 0):
            west_p = gps[1].split('E')[0]
        gps_data['raw_north'] = float(north_p)
        gps_data['raw_west'] = float(west_p)
        altitude_var = 0
        if(gps[2].find('M') >= 0):
            altitude_var = gps[2].split('M')[0]
            if(altitude_var == ''):
                altitude_var = 0
        gps_data['altitude'] = float(altitude_var)
        gps_data['num_satellites'] = int(gps[3])
        gps_data['gps_differential'] = int(gps[4])
        gps_data['accuracy_meters'] = float(gps[5])

        n_pt = north_p.split('.') # North point
        w_pt = west_p.split('.') # West point


        n_deg = n_pt[0][0] + n_pt[0][1] # First 2 digits make the degrees
        n_min = n_pt[0][2] + n_pt[0][3] # Last 2 digits make the minutes
        if(len(w_pt[0]) == 4):
            w_deg = w_pt[0][0] + w_pt[0][1] # First 2 digits make the degrees
            w_min = w_pt[0][2] + w_pt[0][3] # Last 2 digits make the minutes
        else:
            w_deg = w_pt[0][0] + w_pt[0][1] + w_pt[0][2] # First 3 digits make the degrees
            w_min = w_pt[0][3] + w_pt[0][4] # Last 2 digits make the minutes

        n_time = float(n_min + '.' + n_pt[1]) / 60 # Put min and seconds together, divide by 60
        w_time = float(w_min + '.' + w_pt[1]) / 60

        n_gps = str(int(n_deg) + n_time) # Put the degrees, minutes, seconds together
        w_gps = str(int(w_deg) + w_time)

        n_gps = n_gps[:10] # Just keep the first 10 characters of the string
        w_gps = '-' + w_gps[:10]
        
        gps_data['north'] = float(n_gps)
        gps_data['west'] = float(w_gps)


        insert_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))  # Time right now
        gps_data['time_inserted'] = insert_time

        print gps_data
        dau_gps_insert(gps_data)

        return

    except Exception, exception:
       print("Error in parse_gps_portion()\n")
       print('Error Message:' + str(exception) + "\n")
       log_error("Error in parse_gps_portion. Detail: " + str(exception) + "\n")
       return


def parse_radio_feedback(thisline, phone_number, timestamp):
    try:
        feedback = {'time_sent':timestamp,
                    'time_inserted':"",
                    'time_data':"",
                    'successful':0,
                    'phone_number':int(phone_number),
                    'message':thisline,
                    'unit_id':0,
                    'parameter_id':0,
                    'parameter_value':0}

        current = {'unit_id':0,
                   'parameter_id':0,
                   'parameter_value':0}

        # Example
        # thisline = 'Good Cmd received: timestamp=11/10/13,13:13:47-16 cmd=STAYAWAKE=1'

        this_line = thisline.split("=")
        
        # Time Inserted #
        time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time()))

        # Time Data #
        timestamp_data = this_line[1].split(' cmd')[0]
        if(timestamp_data.find('-') >= 0):
            timestamp_data = timestamp_data.split('-')[0]
        elif(timestamp_data.find('+') >= 0):
            timestamp_data = timestamp_data.split('+')[0]
        timestamp_data = time.mktime(time.strptime(timestamp_data.strip(), "%y/%m/%d,%H:%M:%S"))
        timestamp_data = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp_data))
        time_data = timestamp_data
        
        # Successful #
        if(this_line[0].find('Good') >=0):
            successful = 1
        
        # Unit Id #
        # Look up phone number in view_unit_sim_ldink
        table = 'view_unit_sim_link'
        where = '`view_unit_sim_link`.`phone_number` = ' + str(phone_number)
        unit_sim_info = dbselect(table, where)
        unit_sim_info = unit_sim_info[0]
        unit_id = int(unit_sim_info['unit_id'])
        
        # Parameter Id #
        # Look up parameter_name in radio_parameter_description table
        parameter_name = this_line[2]
        table = 'radio_parameter_description'
        where = '`radio_parameter_description`.`parameter_name` = \'' + parameter_name + '\''
        parameter_info = dbselect(table, where)
        parameter_info = parameter_info[0]
        parameter_id = int(parameter_info['parameter_id'])

        # Parameter Value #
        parameter_value = int(this_line[3])

        # Set values feedback #
        feedback['time_inserted'] = time_now
        feedback['time_data'] = time_data
        feedback['successful'] = successful
        feedback['unit_id'] = unit_id
        feedback['parameter_id'] = parameter_id
        feedback['parameter_value'] = parameter_value

        # Set values for current #
        current['unit_id'] = unit_id
        current['parameter_id'] = parameter_id
        current['parameter_value'] = parameter_value

        radio_feedback_insert(feedback)

        radio_current_insert_update(current)

        return
    
    except Exception, exception:
       print("Error in parse_radio_feedback()\n")
       print('Error Message:' + str(exception) + "\n")
       log_error("Error in parse_radio_feedback. Detail: " + str(exception) + "\n")
       return   




### Testing
##x = []
##x.append('90147 011711:1032 lowBattery_warning 476,480')
##x.append('90147 011711:1044 heartbeat 478,479')
##x.append('89048 011711:1302 overflow_warning 1800,1632')
##x.append('89048 011611:1307 164,1635')
##x.append('90147 010100:0002  1625,837,61,87,61,84,64,85/010680:0003 0000.0000N,00000.0000E,M,0,00,0.0')
##x.append('90147 010100:0002 heartbeat 1629,827,63,90,61,89,71,96/010680:0003 0000.0000N,00000.0000E,M,0,00,0.0')
##x.append('90147 010100:0002 info+info+info+info+info+info+heartbeat 1643,865,51,75,50,76,51,78/010680:0003 0000.0000N,00000.0000E,M,0,00,0.0')
##x.append('93628 041211:2156 lowBattery_warning+info+heartbeat 482,483,0,0,0,0,0,0/045716.000,3346.5741N,11823.7314W,299.4M,2,08,0.9')
##x.append('14626 011812:1558 heartbeat 287,2,3,2,2,2,2,2,2,2,2,2,3,2,87,758/010680:0003 0000.0000N,00000.0000E,M,0,00,0.0')
##
##phone_number = '1111111111'
##timestamp = '9999-12-31 23:59:59'
##y = 0
##while y < len(x):
##    print ""
##    print "####################################"
##    print "Test " + str(y) + " x=" + str(len(x))
##    parse_dau_data(x[y], phone_number, timestamp)
##    y = y + 1
##
##    

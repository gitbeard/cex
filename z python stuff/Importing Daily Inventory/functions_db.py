"#! /usr/bin/env python"

import MySQLdb

########################################################

def dbinsert(sql):
    try:
        DBSERVER        = "box703.bluehost.com" #localhost"
        DBUSER          = "uziemacc_dti"
        DBPASSW         = "[DTidata!1]"
        DBNAME          = "uziemacc_CEX_DAILY_INV"

        db = MySQLdb.connect (host = DBSERVER, user = DBUSER, passwd = DBPASSW, db = DBNAME)
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        db.close()
        
    except Exception as exception:
        print("Database Error\n")
        print("Detail: " + str(exception) + "\n")
        db.close()

########################################################
        
def dbquery(sql):
    try:
        DBSERVER        = "box703.bluehost.com" #localhost"
        DBUSER          = "uziemacc_dti"
        DBPASSW         = "[DTidata!1]"
        DBNAME          = "uziemacc_CEX_DAILY_INV"

        db = MySQLdb.connect(host = DBSERVER, user = DBUSER, passwd = DBPASSW, db = DBNAME) #cursorclass = MySQLdb.CursorDictRowsMixIn not working.
        cursor = db.cursor(MySQLdb.cursors.DictCursor) #CursorDictRowsMixIn MixIn not working.
        y = cursor.execute(sql)
        z = cursor.fetchall()
        #desc = cursor.description returns info about columns.
        db.commit()
        db.close()
        return z

    except Exception as exception:
        print("Database Error\n")
        print("Detail: " + str(exception) + "\n")
        db.close()

#########################################################

def dbselect(table, where):
    sql = 'SELECT * FROM `' + table + '`'
    if(where != ''):
        sql = sql + ' WHERE ' + where
    #print(sql)
    return dbquery(sql)


def dbselect_distinct(table, where, distinct):
    sql = 'SELECT DISTINCT `'+ distinct +'` FROM `' + table + '`'
    if(where != ''):
        sql = sql + ' WHERE ' + where
    #print(sql)
    return dbquery(sql)

def raw_data_insert(data):
    #sql = 'INSERT INTO `data_opto_raw` (`file_id`, `row_id`, `A`, `B`, `C`, `D`, `E`, `F`, `G`, `H`) \
    #        VALUES (%(file_id)s, %(row_id)s, %(A)s, %(B)s, %(C)s, %(D)s, %(E)s, %(F)s, %(G)s, %(H)s)' % data

    sql = 'INSERT INTO `data_opto_raw` (`file_id`, `row_id`, `A`, `B`, `C`, `D`, `E`, `F`, `G`, `H`, `I`, `J`, `K`, `L`, `M`, `N`, `O`, `P`, `Q`, `R`, `S`, `T` ) \
            VALUES (\'%(file_id)s\', \'%(row_id)s\', \'%(A)s\', \'%(B)s\', \'%(C)s\', \'%(D)s\', \'%(E)s\', \'%(F)s\', \'%(G)s\', \'%(H)s\', \'%(I)s\', \'%(J)s\', \'%(K)s\', \'%(L)s\', \'%(M)s\', \'%(N)s\', \'%(O)s\', \'%(P)s\', \'%(Q)s\', \'%(R)s\', \'%(S)s\', \'%(T)s\')' % data
        
    #print(sql)
    dbinsert(sql)

def file_info_insert_inv(data):
    sql = 'INSERT INTO `file_infos` (`id`, `filename`, `date_modified`, `date_uploaded`) \
            VALUES (\'%(id)d\', \'%(filename)s\', \'%(date_modified)s\', \'%(date_uploaded)s\')' % data
    dbinsert(sql)

def inv_row_insert(data):
    sql = 'INSERT INTO `daily_inventories` (`item_number`, `location_id`, `datetime`, `quantity`, `file_id`) \
            VALUES (\'%(item_number)d\', \'%(location_id)d\', \'%(datetime)s\', \'%(quantity)d\', \'%(file_id)d\')' % data    
    dbinsert(sql)


def upload_csv(datafile):
    sql = 'LOAD DATA LOCAL INFILE \'' + datafile + '\' IGNORE INTO TABLE `daily_inventories` FIELDS TERMINATED BY \',\' OPTIONALLY ENCLOSED BY \'"\' LINES TERMINATED BY \'\\n\''
    print(sql)
    dbinsert(sql)
    
#def file_info_insert(data):
#    sql = 'INSERT INTO `file_info` (`id`, `filename`, `date_modified`, `date_uploaded`, `parsed`, `printed`, `unit_id`) \
#            VALUES (\'%(id)d\', \'%(filename)s\', \'%(date_modified)s\', \'%(date_uploaded)s\', \'%(parsed)d\', \'%(printed)d\', \'%(unit_id)d\')' % data
#    dbinsert(sql)


    

#########################################################
##def all_messages_insert(data):
##    sql = 'INSERT INTO `all_messages` (`time_sent`, `time_inserted`, `phone_number`, `message`) VALUES (\'%(time_sent)s\', \'%(time_inserted)s\', %(phone_number)d, \'%(message)s\')' % data
##    dbinsert(sql)
##    
##def dau_data_insert(data):
##    sql = 'INSERT INTO `data_dau` (`time_sent`, `time_inserted`, `time_data`, `phone_number`, `unit_serial`, `sensor_1`, `sensor_2`, `sensor_3`, `sensor_4`, `sensor_5`, `sensor_6`, `sensor_7`, `sensor_8`, `sensor_9`, `sensor_10`, `sensor_11`, `sensor_12`, `sensor_13`, `sensor_14`, `sensor_15`, `sensor_16`, `alert_message`) VALUES (\'%(time_sent)s\', \'%(time_inserted)s\', \'%(time_data)s\', %(phone_number)d, %(unit_serial)d, %(sensor_1)d, %(sensor_2)d, %(sensor_3)d, %(sensor_4)d, %(sensor_5)d, %(sensor_6)d, %(sensor_7)d, %(sensor_8)d, %(sensor_9)d, %(sensor_10)d, %(sensor_11)d, %(sensor_12)d, %(sensor_13)d, %(sensor_14)d, %(sensor_15)d, %(sensor_16)d, \'%(alert_message)s\')' % data
##    dbinsert(sql)
##    
##def dau_gps_insert(data):
##    sql = 'INSERT INTO `data_gps` (`time_inserted`, `time_data`, `phone_number`, `unit_serial`, `north`, `west`, `raw_north`, `raw_west`, `altitude`, `num_satellites`, `gps_differential`, `accuracy_meters`)VALUES (\'%(time_inserted)s\', \'%(time_data)s\', %(phone_number)d, %(unit_serial)d, %(north)f, %(west)f, %(raw_north)f, %(raw_west)f, %(altitude)f, %(num_satellites)d, %(gps_differential)d, %(accuracy_meters)f)' % data
##    dbinsert(sql)
##
##def alarm_queue_insert(data):
##    sql = 'INSERT INTO `alarm_queue` (`unit_serial`, `time_data`, `time_inserted`, `send_to_phone`,`message`) VALUES (%(unit_serial)d, \'%(time_data)s\', \'%(time_inserted)s\', %(send_to_phone)d,  \'%(message)s\')' % data
##    dbinsert(sql)
##
##def alarm_history_insert(data):
##    sql = 'INSERT INTO `alarm_history` (`alarm_id`, `unit_serial`, `time_data`, `time_inserted`, `time_sent`, `sent_to_phone`,`message`) VALUES (%(alarm_id)d, %(unit_serial)d, \'%(time_data)s\', \'%(time_inserted)s\', \'%(time_sent)s\', %(sent_to_phone)d,  \'%(message)s\')' % data
##    dbinsert(sql)
##
##def radio_program_history_insert(data):
##    sql = 'INSERT INTO `radio_program_history` (`msg_id`, `time_inserted`, `time_to_send`, `phone_number`, `message`, `time_sent`, `unit_id`, `parameter_id`, `parameter_value`) VALUES ( %(msg_id)d, \'%(time_inserted)s\', \'%(time_to_send)s\', %(phone_number)d, \'%(message)s\', \'%(time_sent)s\', %(unit_id)d, %(parameter_id)d, \'%(parameter_value)s\' )' % data
##    dbinsert(sql)
##
##def radio_feedback_insert(data):
##    sql = 'INSERT INTO `radio_program_feedback` (`time_sent`, `time_inserted`, `time_data`, `successful`, `phone_number`, `message`,  `unit_id`, `parameter_id`, `parameter_value`) VALUES ( \'%(time_sent)s\', \'%(time_inserted)s\', \'%(time_data)s\', %(successful)d, %(phone_number)d, \'%(message)s\',  %(unit_id)d, %(parameter_id)d, \'%(parameter_value)s\' )' % data
##    dbinsert(sql)
##
##def radio_current_update(data):
##    sql = 'UPDATE `radio_parameter_current` SET `parameter_value` = %(parameter_value)d WHERE `radio_parameter_current`.`unit_id` = %(unit_id)d AND `radio_parameter_current`.`parameter_id` = %(parameter_id)d' % data
##    dbinsert(sql)
##
##def delete_queue(table_name, record_name, record_id):
##    # table_name = alarm_queue or radio_program_queue
##    # record_name = alarm_id or msg_id
##    # record_id = alarm_id or msg_id
##    sql = 'DELETE FROM `' + table_name + '` WHERE `' + table_name + '`.`' + record_name + '` = ' + str(record_id)
##    dbinsert(sql)
##
##def update_settings_alarm(data, new_state):
##    sql = 'UPDATE `settings_alarm` SET `last_state` = ' + str(new_state) + ' WHERE `settings_alarm`.`unit_serial` = %(unit_serial)d' % data
##    dbinsert(sql)
##    
##def update_settings_alarm_NEW(unit_id, sen_number, new_state):
##    sql = 'UPDATE `settings_alarm` SET `last_state` = ' + str(new_state) + ' WHERE `settings_alarm`.`unit_id` = \'' + str(unit_id) + '\' AND `settings_alarm`.`sensor_number` = \'' + str(sen_number) + '\'' 
##    dbinsert(sql)
##    
##        
###########################################################

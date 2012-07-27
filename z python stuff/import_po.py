import datetime
import time
import os
from functions_db import *
from functions_excel import *
from functions_files import *

# This is for importing PO information that was exported from AccPac to CEX web app

################################################################################
def main():
    files = get_files()
    print(files)

    for f in files:
        print(f)
        thisfile = open(f, 'r')
        thisdata = thisfile.readlines()
        thisfile.close()
        
        x = 0

        # Import the first line to purchase_orders
        thisline = thisdata[x]
        thisline = thisline.split(',')
        po_data = parse_po(thisline) # Parse first line
        db_insert_po(po_data) # Insert into DB
        po_id = int(get_po_id(po_data['po_number'])) # Get po_id

        # Import all lines to purchase_order_items
        while x < len(thisdata):
            thisline = thisdata[x]
            if(thisline == ''):
                break
            thisline = thisline.split(',')
            po_item_data = parse_po_items(thisline) # Parse item
            po_item_data['po_id'] = po_id
            db_insert_po_items(po_item_data) # Insert item info into database
            x = x + 1


################################################################################
def parse_po(thisline):
    po_data = {'po_number':0,
               'company_id':0,
               'line_items':0,
               'total_items':0,
               'total_price':0,
               'status':0,
               'date_placed':'',
               'date_ready':'',
               'date_shipped':'',
               'date_received':''}
    print(thisline)
    po_data['po_number'] = int(thisline[2].split('PO-')[1])
    #company_id = get_company_id(thisline[7])
    #company_id= 0
    #po_data['company_id'] = company_id   # Need a better way to do this...
    #po_data['line_items'] = thisline[]  # Upadate after import items
    #po_data['total_items'] = thisline[] # Upadate after import items
    #po_data['total_price'] = thisline[] # Upadate after import items
    #po_data['status'] = thisline[]      # Upadate after something happens
    po_data['date_placed'] = thisline[0]
    po_data['date_ready'] = thisline[0]    # Start same as placed, need to update later
    po_data['date_shipped'] = thisline[0]  # Start same as placed, need to update later
    po_data['date_received'] = thisline[0] # Start same as placed, need to update later

    return po_data
    
################################################################################
def parse_po_items(thisline):
    po_item_data = {'po_id':0,
                    'line_number':0,
                    'item_number':0,
                    'part_number':'',
                    'part_description':'',
                    'quantity':0,
                    'unit_price':0.0,
                    'extended_price':0.0,
                    'status':0}

    
    #po_item_data['po_id'] = thisline[] # Updated outside this function
    po_item_data['line_number'] = int(thisline[11])
    #po_item_data['item_number'] = thisline[] # Need a good way to do this
    po_item_data['part_number'] = thisline[13]
    po_item_data['part_description'] = thisline[14]
    po_item_data['quantity'] = int(thisline[12])
    po_item_data['unit_price'] = float(thisline[18])
    po_item_data['extended_price'] = float(thisline[20])
    #po_item_data['status'] = thisline[] # Update after something happens

    return po_item_data


################################################################################
def get_po_id(po_number):

    table = "purchase_orders"
    where = "`po_number` = '" + str(po_number) + "'"
    po_id = dbselect_inv(table, where)

    return po_id[0]['id']

################################################################################
def get_files():
    source_dir = "DATA\\PURCHASE_ORDERS\\RAW\\"
    destin_dir = "DATA\\PURCHASE_ORDERS\\PROCESSED\\"
    
    #files = get_files(source_dir)
    #print(files)

    files = get_files_paths(source_dir)
    # print(files)
    return files



main()

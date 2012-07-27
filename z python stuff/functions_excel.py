
import xl
import math
import datetime


################################################################################
def get_raw_excel(file):
    # Return the entire excel worksheet, to be printed or inserted into db

    wb = xl.Workbook(file)
    x = wb.get("A1:Z255")
    
    return x

################################################################################
def excel_dec_to_time(t):
    t = math.modf(t)            # Split whole and fraction portions of t
    h = math.modf(t[0] * 24)    # Mult frac by hours in day
    m = math.modf(h[0] * 60)    # Mult frac by minutes in hour
    s = math.modf(m[0] * 60)    # Mult frac by seconds in minute
 
    h = int(h[1])
    m = int(m[1])
    s = int(s[1])

    time = {"H":h, "M":m, "S":s}

    return time

################################################################################
def add_time_to_datetime(d, t):
    d = d.replace(hour=t["H"], minute=t["M"], second=t["S"])
    return d

################################################################################




### TESTING ###

## Tests for get_raw_excel()
# wb = xl.Workbook(r"C:\Jimmy\CableX\TestResults\Python\raw_file_1")
#file = "\raw_file_1"
#x = get_raw_excel(file)
#print(x)



## Tests for add_time_to_datetime() and excel_dec_to_time()

#d = 0.552604167
##d = 0.751377315
##
##
##time = excel_dec_to_time(d)
##print(time)
##
##d = datetime.datetime(2012, 3, 29, 0, 0)
##print(d)
##new_d = add_time_to_datetime(d, time)
##print(new_d)


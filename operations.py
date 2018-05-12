import table_manger
import os
import datetime
import time
from accounting import total_charge

def assign_table(tables):
    try:
        active_table = int(input("Select table Number: "))
        i = active_table - 1
        if tables[i].table_status == ' NOT OCCUPIED ':
            tables[i].table_status = '   OCCUPIED   '
            tables[i].session.start_time =  datetime.datetime.now()
            tables[i].session.display_start = tables[i].session.start_time.strftime('%H:%M')
        else:
            print("Table is Occupied.  Please select another table")
            input("Hit enter to continue")
    except:
        print("Invailid table number")
        input("Press enter to continue")

def check_out_table(tables):
    try:
        active_table = int(input("Select table Number: "))
        i = active_table - 1
        if tables[i].table_status == '   OCCUPIED   ':
            total_charge(tables,i)
            tables[i].table_status = ' NOT OCCUPIED '
            tables[i].session.display_start = '     '
        else:
            print("Table is Unoccupied.  Please assign the table first.")
            input("Hit enter to continue")
    except:
        print("Invailid table number")
        input("Press enter to continue")

def edit_table_start_time(tables):
    try:
        active_table = int(input("Select table Number: "))
        i = active_table - 1
    except:
        print("Invailid table number")
        input("Press enter to continue")
    try:
        if tables[i].table_status =='   OCCUPIED   ':
            new_time = datetime.datetime.strptime(input('specify time in HH:MM 24h format: '), '%H:%M' ).time()
            tables[i].session.start_time = datetime.datetime.combine(datetime.date.today(), new_time)
            if tables[i].session.start_time > datetime.datetime.now():
                print("Please enter a time in the past.")
                input("Press enter to continue")
                edit_table_start_time(tables)
            tables[i].session.display_start = str(tables[i].session.start_time.hour).zfill(2) + ":" + str(tables[i].session.start_time.minute).zfill(2)
        else:
            print("Table is Unoccupied.  Please assign the table first.")
            input("Press enter to continue")
    except:
        print("Invailid enter")
        input("Press enter to continue")
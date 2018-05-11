import os
import datetime
import time
from colorama import Fore, Style
import colorama


os.system('clear')

tables = []
rate = 30.00
cell = 18

class Table:
    def __init__(self,table_number):
        self.table_number = table_number
        self.table_status = (f'{Fore.GREEN} NOT OCCUPIED{Style.RESET_ALL} ')
        self.start_time = '     '
        self.table_start = '     '
        self.display_start = '     '
        self.table_end = '     '
        self.display_end = '     '
        self.time_played = '      '
        self.time_played_hours = '  '
        self.time_played_minutes = '  '
        self.display_played = '      '
        self.charge = 0.0

    def __repr__(self):
        return (f" {self.table_number} \n {self.table_status}\n")

#def pool_hall_setup():
#    table_setup = ['01','02','03','04','05','06','07','08','09','10','11','12']
#    i=0
#    while i < len(table_setup):
#        tables.append(Table(table_setup[i]))
#        i+=1

def pool_hall_setup():
    for index in range (1,13):
       pool_table = Table(index)
       tables.append(pool_table)

def assign_table():
    try:
        active_table = int(input("Select table Number: "))
        i = active_table - 1
        if tables[i].table_status == (f'{Fore.GREEN} NOT OCCUPIED{Style.RESET_ALL} '):
            tables[i].table_status = (f'{Fore.RED}   OCCUPIED   {Style.RESET_ALL}')
            tables[i].start_time =  datetime.datetime.now()
            tables[i].display_start = tables[i].start_time.strftime('%H:%M')
            #new_time = datetime.datetime.strptime(input('specify time in HH:MM 24h format: '), '%H:%M' ).time()
            #tables[i].start_time = datetime.datetime.combine(datetime.date.today(), new_time)
            #tables[i].display_start = str(tables[i].start_time.hour).zfill(2) + ":" + str(tables[i].start_time.minute).zfill(2)
        else:
            print("Table is Occupied.  Please select another table")
            input("Hit enter to continue")
    except:
        print("Invailid table number")
        input("Press enter to continue")

def check_out_table():
    try:
        active_table = int(input("Select table Number: "))
        i = active_table - 1
        if tables[i].table_status == (f'{Fore.RED}   OCCUPIED   {Style.RESET_ALL}'):
            total_charge(i)
            tables[i].table_status = (f'{Fore.GREEN} NOT OCCUPIED{Style.RESET_ALL} ')
            tables[i].display_start = '     '
        else:
            print("Table is Unoccupied.  Please assign the table first.")
            input("Hit enter to continue")
    except:
        print("Invailid table number")
        input("Press enter to continue")

def total_charge(i):
    tables[i].table_end = datetime.datetime.now()
    tables[i].display_start = str(tables[i].start_time.hour).zfill(2) + ":" + str(tables[i].start_time.minute).zfill(2)
    tables[i].display_end = str(tables[i].table_end.hour).zfill(2) + ":" + str(tables[i].table_end.minute).zfill(2)
    tables[i].time_played =  datetime.datetime.now() - tables[i].start_time
    charge = tables[i].time_played.seconds * (rate/60/60) 
    tables[i].display_played = tables[i].time_played.seconds
    tables[i].time_played_hours,  remainder = divmod(tables[i].display_played, 3600)
    tables[i].time_played_minutes = round(remainder / 60)
    

    os.system('clear')
        
    print('\n\n\n\n')
    print('_________________________________________')
    print('')
    print(f'Pool Table Number:     {tables[i].table_number}') 
    print('')
    print(f'Start Time:            {tables[i].display_start}')
    print('')
    print(f'End Time:              {tables[i].display_end}')
    print('')
    print(f'Total Time Played:     {tables[i].time_played_hours}:{tables[i].time_played_minutes}')
    print('')
    print(f'Total cost:            ${charge:,.2f}')
    print('_________________________________________')
    input("Press enter to continue")

    daily_report = str(datetime.datetime.now().month).zfill(2) + "-" + str(datetime.datetime.now().day).zfill(2) + "-" + str(datetime.datetime.now().year) + '.txt'
    with open(daily_report, 'a') as file:
        file.write(
    '\n\n\n\n'
    '_________________________________________\n'
    '\n'
    f'Pool Table Number:     {tables[i].table_number}\n'
    '\n'
    f'Start Time:            {tables[i].display_start}\n'
    '\n'
    f'End Time:              {tables[i].display_end}\n'
    '\n'
    f'Total Time Played:     {tables[i].time_played_hours}:{tables[i].time_played_minutes}\n'
    '\n'
    f'Total cost:            ${charge:,.2f}\n'
    '_________________________________________\n'
    )

def edit_table_start_time():
    try:
        active_table = int(input("Select table Number: "))
        i = active_table - 1
    except(IndexError):
        print("Invailid table number")
        input("Press enter to continue")
    try:
        if tables[i].table_status ==(f'{Fore.RED}   OCCUPIED   {Style.RESET_ALL}'):
            new_time = datetime.datetime.strptime(input('specify time in HH:MM 24h format: '), '%H:%M' ).time()
            tables[i].start_time = datetime.datetime.combine(datetime.date.today(), new_time)
            if tables[i].start_time > datetime.datetime.now():
                print("Please enter a time in the past.")
                input("Press enter to continue")
                edit_table_start_time()
                #table_status_display()
            tables[i].display_start = str(tables[i].start_time.hour).zfill(2) + ":" + str(tables[i].start_time.minute).zfill(2)
        else:
            print("Table is Unoccupied.  Please assign the table first.")
            input("Press enter to continue")
    except:
        print("Invailid enter")
        input("Press enter to continue")

def submit_daily_report():

    #daily_report = str(datetime.datetime.now().month).zfill(2) + "-" + str(datetime.datetime.now().day).zfill(2) + "-" + str(datetime.datetime.now().year) + '.txt'
    #with open(daily_report) as email:
    pass




def change_rate():
    try:
        global rate
        rate = float(input("Enter the new hourly rate: "))
        print(f"The current rate is: ${rate:,.2f} per hour.")
        return(rate)
    except(ValueError):
        print("Please enter a Dollar value")
        input("Press enter to continue")
        change_rate()

def upper_frame():
    print(" " *5 + "#" * cell + " " *5 + "#" * cell + " " *5 + "#" * cell + " " *5 + "#" *cell)

def table_status_display():
    os.system('clear')
    print()
    print(f"The current rate is: ${rate:,.2f} per hour.")
    print()
    print()
    print()
    upper_frame()
    print(" " * 5 + "#    Table 01    #" +" " * 5 + "#    Table 02    #" +" " * 5 + "#    Table 03    #" +" " * 5 + "#    Table 04    #")
    print(" " * 5 + f"# {tables[0].table_status} #" +" " * 5 + f"# {tables[1].table_status} #" +" " * 5 + f"# {tables[2].table_status} #" +" " * 5 + f"# {tables[3].table_status} #")
    print(" " * 5 + f'# Start: {tables[0].display_start}   #' +" " * 5 + f'# Start: {tables[1].display_start}   #' +" " * 5 + f'# Start: {tables[2].display_start}   #' +" " * 5 + f'# Start: {tables[3].display_start}   #')
#    print(" " * 5 + f'# Played:{tables[0].time_played_hours}:{tables[0].time_played_minutes}   #' +" " * 5 + f'# Played:{tables[1].time_played_hours}:{tables[1].time_played_minutes}   #' +" " * 5 + f'# Played:{tables[2].time_played_hours}:{tables[2].time_played_minutes}   #' +" " * 5 + f'# Played:{tables[3].time_played_hours}:{tables[3].time_played_minutes}   #')    
    upper_frame()
    print()
    print()
    upper_frame()
    print(" " * 5 + "#    Table 05    #" +" " * 5 + "#    Table 06    #" +" " * 5 + "#    Table 07    #" +" " * 5 + "#    Table 08    #")
    print(" " * 5 + f"# {tables[4].table_status} #" +" " * 5 + f"# {tables[5].table_status} #" +" " * 5 + f"# {tables[6].table_status} #" +" " * 5 + f"# {tables[7].table_status} #")
    print(" " * 5 + f'# Start: {tables[4].display_start}   #' +" " * 5 + f'# Start: {tables[5].display_start}   #' +" " * 5 + f'# Start: {tables[6].display_start}   #' +" " * 5 + f'# Start: {tables[7].display_start}   #')
#    print(" " * 5 + f'# Played:{tables[4].time_played_hours}:{tables[4].time_played_minutes}   #' +" " * 5 + f'# Played:{tables[5].time_played_hours}:{tables[5].time_played_minutes}   #' +" " * 5 + f'# Played:{tables[6].time_played_hours}:{tables[6].time_played_minutes}   #' +" " * 5 + f'# Played:{tables[7].time_played_hours}:{tables[7].time_played_minutes}   #')
    upper_frame()
    print() 
    print()
    upper_frame()
    print(" " * 5 + "#    Table 09    #" +" " * 5 + "#    Table 10    #" +" " * 5 + "#    Table 11    #" +" " * 5 + "#    Table 12    #")
    print(" " * 5 + f"# {tables[8].table_status} #" +" " * 5 + f"# {tables[9].table_status} #" +" " * 5 + f"# {tables[10].table_status} #" +" " * 5 + f"# {tables[11].table_status} #")
    print(" " * 5 + f'# Start: {tables[8].display_start}   #' +" " * 5 + f'# Start: {tables[9].display_start}   #' +" " * 5 + f'# Start: {tables[10].display_start}   #' +" " * 5 + f'# Start: {tables[11].display_start}   #')    
#    print(" " * 5 + f'# Played:{tables[8].time_played_hours}:{tables[8].time_played_minutes}   #' +" " * 5 + f'# Played:{tables[9].time_played_hours}:{tables[9].time_played_minutes}   #' +" " * 5 + f'# Played:{tables[10].time_played_hours}:{tables[10].time_played_minutes}   #' +" " * 5 + f'# Played:{tables[11].time_played_hours}:{tables[11].time_played_minutes}   #')
    upper_frame()
    print()
    print()
    menu()

def menu():
    print('\n \n')
    print(" ")
    print("What action would you like to preform?")
    print('\n')
    print(' 1) Assign Table ')
    print(' 2) Checkout Table ')
    print(' 3) Edit Start time')
 #   print(' 4) Submit Daily report NOT WORKING')
    print(' 4) Change Hourly Rate')
    print('\n')
#    print(' R) Refresh')
    print('\n')
    print(' Q) EXIT')
    action = input()

    if action == '1':
        assign_table()
        table_status_display()
    elif action == '2':
        check_out_table()
        table_status_display()
    elif action == '3':
        edit_table_start_time()
        table_status_display()
 #   elif action == '4':
 #       pass
    elif action == '4':
        change_rate()
        table_status_display()
#    elif action.casefold() == 'r':
#        table_status_display() 
    elif action.casefold() == 'q':
        exit
    else:
        table_status_display()

pool_hall_setup()
table_status_display()




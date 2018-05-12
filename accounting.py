import table_manger
import os
import datetime
import time
rate = 30.00

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

def total_charge(tables,i):
    tables[i].session.table_end = datetime.datetime.now()
    tables[i].session.display_start = str(tables[i].session.start_time.hour).zfill(2) + ":" + str(tables[i].session.start_time.minute).zfill(2)
    tables[i].session.display_end = str(tables[i].session.table_end.hour).zfill(2) + ":" + str(tables[i].session.table_end.minute).zfill(2)
    tables[i].session.time_played =  datetime.datetime.now() - tables[i].session.start_time
    charge = tables[i].session.time_played.seconds * (rate/60/60) 
    tables[i].session.display_played = tables[i].session.time_played.seconds
    tables[i].session.time_played_hours,  remainder = divmod(tables[i].session.display_played, 3600)
    tables[i].session.time_played_minutes = round(remainder / 60)

    os.system('clear')
    print('\n\n\n\n')
    print('_________________________________________')
    print('')
    print(f'Pool Table Number:     {tables[i].table_number}') 
    print('')
    print(f'Start Time:            {tables[i].session.display_start}')
    print('')
    print(f'End Time:              {tables[i].session.display_end}')
    print('')
    print(f'Total Time Played:     {tables[i].session.time_played_hours}:{tables[i].session.time_played_minutes}')
    print('')
    print(f'Rate charged:          ${rate}  per hour')
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
    f'Start Time:            {tables[i].session.display_start}\n'
    '\n'
    f'End Time:              {tables[i].session.display_end}\n'
    '\n'
    f'Total Time Played:     {tables[i].session.time_played_hours}:{tables[i].session.time_played_minutes}\n'
    '\n'
    f'Rate charged:          ${rate}  per hour\n'
    '\n'
    f'Total cost:            ${charge:,.2f}\n'
    '_________________________________________\n'
    )
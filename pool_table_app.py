import os
import datetime
import time
from colorama import Fore, Style, Back
import colorama
import table_manger
from operations import assign_table, check_out_table, edit_table_start_time
from accounting import total_charge, change_rate, rate



os.system('clear')
tables = []
cell = 6

def pool_hall_setup():
    for index in range (1,13):
       pool_table = table_manger.Table(index)
       tables.append(pool_table)
       tables[index-1].session = table_manger.Session()



def upper_frame():
    print(f" " *5 + f'{Back.GREEN}'"██" + "-"  * cell + '██' +"-"  * cell +'██'  f'{Style.RESET_ALL}' + f" " *5 + f'{Back.GREEN}'"██" + "-"  * cell + '██' +"-"  * cell +'██'  f'{Style.RESET_ALL}' + f" " *5 + f'{Back.GREEN}'"██" + "-"  * cell + '██' +"-"  * cell +'██'  f'{Style.RESET_ALL}' + f" " *5 + f'{Back.GREEN}'"██" + "-"  * cell + '██' +"-"  * cell +'██'  f'{Style.RESET_ALL}')

def status_display(tables):
    os.system('clear')
    print('')
    print(f"The current rate is: ${rate:,.2f} per hour.")
    print()
    print()
    print('')
    upper_frame()
    print(" " * 5 + f"{Back.GREEN}|    Table 01    |{Style.RESET_ALL}" +" " * 5 + f"{Back.GREEN}|    Table 02    |{Style.RESET_ALL}" +" " * 5 + f"{Back.GREEN}|    Table 03    |{Style.RESET_ALL}" +" " * 5 + f"{Back.GREEN}|    Table 04    |{Style.RESET_ALL}")
    print(" " * 5 + f"{Back.GREEN}| {tables[0].table_status} |{Style.RESET_ALL}" +" " * 5 + f"{Back.GREEN}| {tables[1].table_status} |{Style.RESET_ALL}" +" " * 5 + f"{Back.GREEN}| {tables[2].table_status} |{Style.RESET_ALL}" +" " * 5 + f"{Back.GREEN}| {tables[3].table_status} |{Style.RESET_ALL}")
    print(" " * 5 + f'{Back.GREEN}|  Start: {tables[0].session.display_start}  |{Style.RESET_ALL}' +" " * 5 + f"{Back.GREEN}|  Start: {tables[1].session.display_start}  |{Style.RESET_ALL}" +" " * 5 + f"{Back.GREEN}|  Start: {tables[2].session.display_start}  |{Style.RESET_ALL}" +" " * 5 + f"{Back.GREEN}|  Start: {tables[3].session.display_start}  |{Style.RESET_ALL}")
    upper_frame()
    print()
    print()
    upper_frame()
    print(" " * 5 + f"{Back.GREEN}|    Table 05    |{Style.RESET_ALL}" +" " * 5 + f"{Back.GREEN}|    Table 06    |{Style.RESET_ALL}" +" " * 5 + f"{Back.GREEN}|    Table 07    |{Style.RESET_ALL}" +" " * 5 + f"{Back.GREEN}|    Table 08    |{Style.RESET_ALL}")
    print(" " * 5 + f"{Back.GREEN}| {tables[4].table_status} |{Style.RESET_ALL}" +" " * 5 + f"{Back.GREEN}| {tables[5].table_status} |{Style.RESET_ALL}" +" " * 5 + f"{Back.GREEN}| {tables[6].table_status} |{Style.RESET_ALL}" +" " * 5 + f"{Back.GREEN}| {tables[7].table_status} |{Style.RESET_ALL}")
    print(" " * 5 + f'{Back.GREEN}|  Start: {tables[4].session.display_start}  |{Style.RESET_ALL}' +" " * 5 + f'{Back.GREEN}|  Start: {tables[5].session.display_start}  |{Style.RESET_ALL}' +" " * 5 + f'{Back.GREEN}|  Start: {tables[6].session.display_start}  |{Style.RESET_ALL}' +" " * 5 + f'{Back.GREEN}|  Start: {tables[7].session.display_start}  |{Style.RESET_ALL}')
    upper_frame()
    print() 
    print()
    upper_frame()
    print(" " * 5 + f"{Back.GREEN}|    Table 09    |{Style.RESET_ALL}" +" " * 5 + f"{Back.GREEN}|    Table 10    |{Style.RESET_ALL}" +" " * 5 + f"{Back.GREEN}|    Table 11    |{Style.RESET_ALL}" +" " * 5 + f"{Back.GREEN}|    Table 12    |{Style.RESET_ALL}")    
    print(" " * 5 + f'{Back.GREEN}| {tables[8].table_status} |{Style.RESET_ALL}' +" " * 5 + f'{Back.GREEN}| {tables[9].table_status} |{Style.RESET_ALL}' +" " * 5 + f'{Back.GREEN}| {tables[10].table_status} |{Style.RESET_ALL}' +" " * 5 + f'{Back.GREEN}| {tables[11].table_status} |{Style.RESET_ALL}')
    print(" " * 5 + f'{Back.GREEN}|  Start: {tables[8].session.display_start}  |{Style.RESET_ALL}' +" " * 5 + f'{Back.GREEN}|  Start: {tables[9].session.display_start}  |{Style.RESET_ALL}' +" " * 5 + f'{Back.GREEN}|  Start: {tables[10].session.display_start}  |{Style.RESET_ALL}' +" " * 5 + f'{Back.GREEN}|  Start: {tables[11].session.display_start}  |{Style.RESET_ALL}')    
    upper_frame()
    print()
    print('')
    menu()

def menu():
    global rate
    print('\n \n')
    print(" ")
    print("What action would you like to preform?")
    print('\n')
    print(' 1) Assign Table ')
    print(' 2) Checkout Table ')
    print(' 3) Edit Start time')
    print(' 4) Change Hourly Rate')
    print('\n')
    print('\n')
    print(' Q) EXIT')
    action = input()

    if action == '1':
        assign_table(tables)
        status_display(tables)
    elif action == '2':
        check_out_table(tables)
        status_display(tables)
    elif action == '3':
        edit_table_start_time(tables)
        status_display(tables)
    elif action == '4':
        rate = change_rate()
        status_display(tables)
    elif action.casefold() == 'q':
        exit
    else:
        status_display(tables)

pool_hall_setup()
status_display(tables)




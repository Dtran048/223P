#Dylan Tran
# 3/11/2024
# holds all the functions that will be called by main

import json 
import calendar 


def read_data(*, filename):
   try:
      with open(filename, 'r') as f:
         x = json.load(f)
         return x
   except FileNotFoundError:
      return {}    

def write_data(*, filename, data):
    with open(filename, "w") as outfile:
        json.dump(data, outfile)
    return()

def max_temperature(*, data, date):
    x = 0
    for k in data.keys():
        if k[:8] == date and data[k]['t'] > x:
            x = data[k]['t']
    return(x)

def min_temperature(*, data, date):
    x = 9999
    for k in data.keys():
        if k[:8] == date and data[k]['t'] < x:
            x = data[k]['t']
    return(x)

def max_humidity(*, data, date):
    x = 0
    for k in data.keys():
        if k[:8] == date and data[k]['h'] > x:
            x = data[k]['h']
    return(x)

def min_humidity(*, data, date):
    x = 9999
    for k in data.keys():
        if k[:8] == date and data[k]['h'] < x:
            x = data[k]['h']
    return(x)

def tot_rain(*, data, date):
    x = 0
    for k in data.keys():
        if k[:8] == date:
            x += data[k]['r']
    return(x)

def report_daily(*, data, date):
    print(
        """
========================= DAILY REPORT ========================
Date                     Time Temperature Humidity Rainfall
==================== ======== =========== ======== ========"""
    )
    for k in data.keys():
        if k[:8] == date:
            myd = f'{calendar.month_name[int(k[5:6])]} {int(k[6:8])}, {k[:4]:4}'
            time = f'{k[8:10]}:{k[10:12]}:{k[12:14]}'
            print(f'{myd:20} {time:7} {int(data[k]['t']):11d} {int(data[k]['h']):8d} {format(format(data[k]['r'], '.2f'),'>8')}')

def report_historical(*, data):
    days = []
    print(
        """
============================== HISTORICAL REPORT ===========================
                         Minimum     Maximum  Minumum  Maximum    Total
Date                 Temperature Temperature Humidity Humidity Rainfall
==================== =========== =========== ======== ======== ========"""
    )
    for k in data.keys():
        if k[:8] not in days:
            days.append(k[:8])
    days.sort()
    for i in days:
        date = f'{calendar.month_name[int(i[5:6])]} {int(i[6:8])}, {i[:4]}'
        print(f'{date:21}  {min_temperature(data = data, date = i):9d} {max_temperature(data = data, date = i):11d}  {min_humidity(data = data, date = i):7d}  {max_humidity(data = data, date = i):7d}  {format(tot_rain(data = data, date = i), ".2f"):>7} ')





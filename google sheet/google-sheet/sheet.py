#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on May 23, 2018

Course work: 

@author: 

Source:

'''
import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('Mine.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Copy of Legislators 2017").sheet1

list_of_hashes = sheet.get_all_records()
print(list_of_hashes)    

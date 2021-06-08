#!/usr/bin/python
# -*- coding: utf-8 -*-
import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials
 
#変更してください
key_name = 'dashboard-315508-eeb646ebb75c.json'
sheet_name = 'Dashboard'
 
#APIにログイン
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(key_name, scope)
gc = gspread.authorize(credentials)
 
#セル'A1'に'TEST'と入力
cell_number = 1
input_value = 'TEST'
wks = gc.open(sheet_name).sheet1

while True:
  wks.update_acell("A" + str(cell_number), input_value + str(cell_number))
  cell_number = cell_number + 1
  time.sleep(10)

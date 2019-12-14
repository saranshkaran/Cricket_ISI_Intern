# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 19:56:45 2019

@author: LENOVO
"""

import numpy as np
import pandas as pd
pd.set_option('precision', 2)
import os


import yaml

def read_data(filepath):
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor, Loader=yaml.FullLoader)
    return data    

filepath = os.getcwd()
files_list = os.listdir()
for file in files_list:
    if file.endswith('py'):
        continue
    data = read_data(filepath + "\\" + file )
    if len(data['innings']) != 2 :
        continue
    
    
    balls_1st = data['innings'][0]['1st innings']['deliveries']
    
    balls_2nd = data['innings'][1]['2nd innings']['deliveries']
    
    team_batting_1st = data['innings'][0]['1st innings']['team']
    
    team_batting_2nd = data['innings'][1]['2nd innings']['team']
    
    date = data['info']['dates']
     
    gender = data['info']['gender']
    
    match_type = data['info']['match_type']
    
    if gender != 'male' or match_type!= 'ODI':
        continue
    

    total_runs = 0 
    column_names = ['date','team_batting_1st','team_batting_2nd', 'overs', 'runs'] 
    df1 = pd.DataFrame(columns = column_names)
    
    df1['date'] = date
    df1['team_batting_1st'] = team_batting_1st
    df1['team-batting_2nd'] =team_batting_2nd
    
    for ball in balls_1st:
        for ball_no, outcome in  ball.items():
            df2 = pd.DataFrame({'overs': [ball_no,] , 'runs':[outcome['runs']['total']],})
            df1 = df1.append(df2, ignore_index = True)
            #total_runs += outcome['runs']['total']
    #total_runs += ball[ball_no]['runs']['total']

    for ball in balls_2nd:
        for ball_no, outcome in  ball.items():
            df2 = pd.DataFrame({'overs': [ball_no,] , 'runs':[outcome['runs']['total']],})
            df1 = df1.append(df2, ignore_index = True)
    CSV_dir = filepath + '\\CSV_MatchWise'
    if not os.path.exists(CSV_dir):
        os.makedirs(CSV_dir)
    df1.to_csv(CSV_dir + "\\" + (str(date[0]) + team_batting_1st + '_' + team_batting_2nd )+ '.csv',index=True)
    
    
    
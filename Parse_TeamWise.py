# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 01:11:01 2019

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
    if not file.endswith('yaml'):
        continue
    data = read_data(filepath + "\\" + file)
    if len(data['innings']) != 2 :
        continue
    
    
    balls_1st = data['innings'][0]['1st innings']['deliveries']
    
    balls_2nd = data['innings'][1]['2nd innings']['deliveries']
    
    team_batting_1st = data['innings'][0]['1st innings']['team']
    
    team_batting_2nd = data['innings'][1]['2nd innings']['team']
    
    date = data['info']['dates']
     
    gender = data['info']['gender']
    
    winner = data['info']['gender']
    
    match_type = data['info']['match_type']
    
    if gender != 'male' or match_type!= 'ODI':
        continue
    

    final_score = 0
    no_of_balls = 0
    wickets = 0
    column_names = ['date','team_batting_1st','team_batting_2nd', 'overs','batsman','bowler', 'non striker','runs by batsman','extras','total runs this ball','runs','wickets down'] 
    df_1st_inn = pd.DataFrame(columns = column_names)
    
    df_1st_inn['date'] = date
    df_1st_inn['team_batting_1st'] = team_batting_1st
    df_1st_inn['team_batting_2nd'] =team_batting_2nd
    
    for ball in balls_1st:
        for ball_no, outcome in  ball.items():
            if 'wicket' in outcome.keys():
                wickets +=1
            no_of_balls += 1
            df2 = pd.DataFrame({'overs': [ball_no,] , 'batsman':outcome['batsman'], 'bowler': outcome['bowler'], 'non striker': outcome['non_striker'],'runs by batsman': [outcome['runs']['batsman'],], 'extras':[outcome['runs']['extras'],],'total runs this ball':[outcome['runs']['total'],],'runs':[final_score,], 'wickets down': [wickets,] })
            df_1st_inn = df_1st_inn.append(df2, ignore_index = True)
            final_score += outcome['runs']['total']
            
    #total_runs += ball[ball_no]['runs']['total']
    
    
    target = final_score + 1
    final_score = 0
    wickets = 0
    df_2nd_inn = pd.DataFrame(columns = column_names)
    df_2nd_inn['date'] = date
    df_2nd_inn['team_batting_1st'] = team_batting_1st
    df_2nd_inn['team_batting_2nd'] = team_batting_2nd
    for ball in balls_2nd:
        for ball_no, outcome in  ball.items():
            if 'wicket' in outcome.keys():
                wickets +=1
            df2 = pd.DataFrame({'overs': [ball_no,] , 'batsman':outcome['batsman'], 'bowler': outcome['bowler'], 'non striker': outcome['non_striker'],'runs by batsman': [outcome['runs']['batsman'],], 'extras':[outcome['runs']['extras'],],'total runs this ball':[outcome['runs']['total'],],'runs':[final_score,], 'wickets down': [wickets,]})
            df_2nd_inn = df_2nd_inn.append(df2, ignore_index = True)
            final_score += outcome['runs']['total']

    
    CSV_dir = filepath + '\\CSV_TeamWise'
    if not os.path.exists(CSV_dir):
        os.makedirs(CSV_dir)
        
    df_1st_inn.to_csv(CSV_dir + "\\" + str(date[0]) + team_batting_1st + '1st_inn.csv',index=True, header = True, columns = column_names)
    df_2nd_inn.to_csv(CSV_dir + "\\" + str(date[0]) + team_batting_2nd + '2nd_inn.csv',index=True, header = True, columns = column_names)
    
    
    
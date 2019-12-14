# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 17:56:48 2019

@author: LENOVO
"""

import os
import pandas as pd

filepath = os.getcwd()
top_4 = 'India Australia New Zealand England'
files = os.listdir()

column =  ['date','team_batting_1st','team_batting_2nd', 'overs', 'runs']
team_df_NZ =   pd.DataFrame(columns=column)

team_df_Aus =   pd.DataFrame(columns=column)
team_df_Ind =   pd.DataFrame(columns=column)
team_df_Eng =   pd.DataFrame(columns=column)


for file in files:
    if file[10:-11] not in top_4:
        continue
    elif file == "2019-07-09India2nd_inn":
        continue
    else:
        if 'New Zealand' in file and '1st' in file:
            df1 = pd.read_csv(filepath+'\\'+file)
            team_df_NZ = team_df_NZ.append(df1.iloc[1:,:],ignore_index = True)
        elif 'India' in file and '2nd' in file:
            df1 = pd.read_csv(filepath+'\\'+file)
            team_df_Ind = team_df_Ind.append(df1.iloc[1:,:],ignore_index = True)
        elif 'Australia' in file and '1st' in file:
            df1 = pd.read_csv(filepath+'\\'+file)
            team_df_Aus = team_df_Aus.append(df1.iloc[1:,:],ignore_index = True)
        elif 'England' in file and '2nd' in file:
            df1 = pd.read_csv(filepath+'\\'+file)
            team_df_Eng = team_df_Eng.append(df1.iloc[1:,:],ignore_index = True)
CSV_dir = filepath + '\\CSV_Top4\\'
if not os.path.exists(CSV_dir):
    os.makedirs(CSV_dir)
team_df_NZ.to_csv(CSV_dir  +'NZ_1st_inn_test.csv',index=True)
team_df_Ind.to_csv(CSV_dir  +'Ind_2nd_inn_test.csv',index=True)
team_df_Aus.to_csv(CSV_dir  +'Aus_1st_inn_test.csv',index=True)
team_df_Eng.to_csv(CSV_dir  +'Eng_2nd_inn_test.csv',index=True)
#%%
import pandas as pd
import numpy as np

df = pd.read_csv('../data/raw/LAIS_public.csv')

df['dinn'] = 0
df.dinnpd = df.dinnpd.astype('Int32')
df.dinnpc = df.dinnpc.astype('Int32')
df.loc[(df.dinnpd==1) | (df.dinnpc==1),'dinn']=1

target = 'dinn'

features = ['country','fucode','exp_f','year','isic3_1d','isic3_2d','sales_us_Y1','sales_us_Y2','sales_us_Y3',
'export_us_Y1','export_us_Y2','export_us_Y3','dexport','empl_Y1','empl_Y2','empl_Y3','phd_Y1','phd_Y2','phd_Y3',
'master_Y1','master_Y2','master_Y3','postgrad_Y1','postgrad_Y2','postgrad_Y3','undergrad_Y1','undergrad_Y2','undergrad_Y3',
'unidegree_Y1','unidegree_Y2','unidegree_Y3','degree_nesc','degree_et','degree_ingnesc','degree_ssc','degree_medsc','degree_agrsc','degree_hum',
'nontert_Y1','nontert_Y2','nontert_Y3','second_Y1','second_Y2','second_Y3',
'RD_empl','ict_mach_us_Y1','IPexp_us_Y1','ict_mach_us_Y2','IPexp_us_Y2','drdintexp',
'drdextexp','dictexp','dmachexp','dict_mach','dTTexp','dconexp','dIPexp','dtrainexp','dIDexp','dmktexp','dongoingia','dabandia']


target_index = df[target].dropna().index
#df_target = df.drop(target_index)
df_target = df[[*features, target]]

#%%
df_target.to_csv('../data/processed/dinn_dataset.csv',index=False)
# %%

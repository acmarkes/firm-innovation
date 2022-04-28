#%%
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', 500)

features = {'country': 'str',
 'fucode': 'int',
 'exp_f': 'float',
 'year': 'int',
 'isic3_1d': 'str',
 'isic3_2d': 'float',
 'sales_us_Y1': 'float',
 'sales_us_Y2': 'float',
 'sales_us_Y3': 'float',
 'export_us_Y1': 'float',
 'export_us_Y2': 'float',
 'export_us_Y3': 'float',
 'dexport': 'bool',
 'empl_Y1': 'int',
 'empl_Y2': 'int',
 'empl_Y3': 'int',
 'phd_Y1': 'float',
 'phd_Y2': 'float',
 'phd_Y3': 'float',
 'master_Y1': 'float',
 'master_Y2': 'float',
 'master_Y3': 'float',
 'postgrad_Y1': 'float',
 'postgrad_Y2': 'float',
 'postgrad_Y3': 'float',
 'undergrad_Y1': 'float',
 'undergrad_Y2': 'float',
 'undergrad_Y3': 'float',
 'unidegree_Y1': 'float',
 'unidegree_Y2': 'float',
 'unidegree_Y3': 'float',
 'degree_nesc': 'float',
 'degree_et': 'float',
 'degree_ingnesc': 'float',
 'degree_ssc': 'float',
 'degree_medsc': 'float',
 'degree_agrsc': 'float',
 'degree_hum': 'float',
 'nontert_Y1': 'float',
 'nontert_Y2': 'float',
 'nontert_Y3': 'float',
 'second_Y1': 'float',
 'second_Y2': 'float',
 'second_Y3': 'float',
 'RD_empl': 'int',
 'ict_mach_us_Y1': 'float',
 'IPexp_us_Y1': 'float',
 'ict_mach_us_Y2': 'float',
 'IPexp_us_Y2': 'float',
 'drdintexp': 'int',
 'drdextexp': 'float',
 'dictexp': 'float',
 'dmachexp': 'float',
 'dict_mach': 'int',
 'dTTexp': 'int',
 'dconexp': 'int',
 'dIPexp': 'int',
 'dtrainexp': 'int',
 'dIDexp': 'int',
 'dmktexp': 'int',
 'dongoingia': 'int',
 'dabandia': 'int',
 'dinnpd': 'int',
 'dinnpc': 'int'}

df = pd.read_csv('../data/raw/LAIS_public.csv',usecols=features.keys())#, dtype=features)

df['dinn'] = 0
df.dinnpd = df.dinnpd.astype('Int32')
df.dinnpc = df.dinnpc.astype('Int32')
df.loc[(df.dinnpd==1) | (df.dinnpc==1),'dinn']=1

target = 'dinn'

target_index = df[target].dropna().index
#df_target = df.drop(target_index)
df_target = df[[*features, target]]

#%%
df_target.to_csv('../data/processed/dinn_dataset.csv',index=False)
# %%

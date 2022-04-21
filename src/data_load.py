#%%
import pandas as pd 
df_og = pd.read_csv('https://media.githubusercontent.com/media/acmarkes/datasets/main/LAIS_public.csv')
df_og.to_csv('../data/raw/LAIS_public.csv')
# %%

#%%
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', 500)

df = pd.read_csv('../data/processed/dinn_dataset.csv')
#%%
#df['fucode'] = df.fucode.astype(int)
df['unique_id'] = df.index.astype(str)+df['fucode'].astype(str).str.slice(0,-2)+df['country'].str.slice(0,2).str.upper()+df['year'].astype(str).str.slice(2)
#df.set_index('unique_id',inplace=True,drop=True)

#%%
df['unique_id'].value_counts(ascending=False)

#%%


# %%

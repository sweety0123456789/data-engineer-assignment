

import pandas as pd
df =  pd.read_csv("/content/sample - Sheet1.csv")   # reading the csv file
df.loc[pd.isnull(df[['county']]).any(axis=1)].to_csv('Table_county_null')   # creating a table for null value in county column as it is not mandatory field
counties  = df['county'].unique().tolist()  # collecting all the counties name in dataset
counties = [x for x in counties if pd.notnull(x)] # removing  np.nan from this list
for county in counties:
  df.loc[df['county']==county].to_csv('Table_'+county+'.csv') # creating separate tables for each county



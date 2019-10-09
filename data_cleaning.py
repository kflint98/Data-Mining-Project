import pandas as pd
import numpy as np

df = pd.read_csv('project_dataset.csv')
#print(df.head())
print(df.shape)
df.query('MODIFIED_FILE.str.contains("[a-zA-Z]\.[a-zA-Z]+$") == True', inplace = True)

print(df.shape)

insecure_df = df[df['SECU_FLAG']=='INSECURE']
neutral_df = df[df['SECU_FLAG']=='NEUTRAL']

print(insecure_df.shape)
print(neutral_df.shape)

df.to_csv('modified_dataset.csv')
insecure_df.to_csv('insecure_dataset.csv')
neutral_df.to_csv('neutral_dataset.csv')

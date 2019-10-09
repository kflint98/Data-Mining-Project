import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/krisf/OneDrive/Documents/Coding/4220/Term Project/project_dataset.csv')
#print(df.head())
print(df.shape)
df.query('MODIFIED_FILE.str.contains("[a-zA-Z]\.[a-zA-Z]+$") == True', inplace = True)

print(df.shape)

insecure_df = df[df['SECU_FLAG']=='INSECURE']
neutral_df = df[df['SECU_FLAG']=='NEUTRAL']

print(insecure_df.shape)
print(neutral_df.shape)

df.to_csv('C:/Users/krisf/OneDrive/Documents/Coding/4220/Term Project/modified_dataset.csv')
insecure_df.to_csv('C:/Users/krisf/OneDrive/Documents/Coding/4220/Term Project/insecure_dataset.csv')
neutral_df.to_csv('C:/Users/krisf/OneDrive/Documents/Coding/4220/Term Project/neutral_dataset.csv')
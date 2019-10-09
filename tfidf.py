import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

import progressbar
from time import sleep

keylist = list()
valuelist = list()

neutral_df = pd.read_csv('C:/Users/krisf/OneDrive/Documents/Coding/4220/Term Project/neutral_dataset.csv')
insecure_df = pd.read_csv('C:/Users/krisf/OneDrive/Documents/Coding/4220/Term Project/insecure_dataset.csv')

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(neutral_df['MODIFIED_FILE'])

d = dict()
sorted_list = list()

feature_names = vectorizer.get_feature_names()
numcols = X.shape[0]
doc = 0

bar = progressbar.ProgressBar(maxval=numcols, \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()


for doc in range(numcols):
    feature_index = X[doc,:].nonzero()[1]
    scores = zip(feature_index, [X[doc, x] for x in feature_index])
    for w, s in [(feature_names[i], s) for (i, s) in scores]:
        if w not in keylist:
            if s != 0.0:
                keylist.append(w)
                d.update({w: s})
                #print(w, s)
    doc += 1
    bar.update(doc)
bar.finish()
sorted = sorted(d.items(), key=lambda x: x[1], reverse=True)

sorted = sorted[:1000]

print(len(sorted))
print(sorted)



#var.to_txt('C:/Users/krisf/OneDrive/Documents/Coding/4220/Term Project/vector.txt')


#df = pd.DataFrame(X.toarray(), columns = vectorizer.get_feature_names())

#print(df)


#print(X.shape)
#print(X)

#print(X.head())
#print(neutral_df.head())




#vectorizer.fit(neutral_df['MODIFIED_FILE'])
#print(vectorizer.vocabulary_)
#print(vectorizer.idf_)

#vector = vectorizer.transform([neutral_df['MODIFIED_FILE']])

#print(vector.shape)
#print(vector.toarray())
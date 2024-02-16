# -*- coding: utf-8 -*-
"""Customer Churn Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S8xUGQT7MEQSSDaQ2j987vWBwEB-KpHD
"""

import pandas as pd, numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('/content/Churn_Modelling.csv')
data

# EDA

data.info()

data.describe()

data.shape

data.nunique()

data.isna().sum()

exit = pd.Series(data['Exited'])

exit_values_count = exit.value_counts()

legends = ['0','1']
plt.pie(exit_values_count, autopct='%.2f',labels=legends)
plt.show()

data = data.dropna()
x = data.drop('Exited', axis = 1)
y = data.Exited
for col in x.select_dtypes(['object','float']):
  x[col], _ = x[col].factorize()
x.info()

from sklearn.feature_selection import mutual_info_classif
miscore = mutual_info_classif(x,y)
miscore = pd.Series(miscore, name = 'MiScore', index = x.columns)
miscore = miscore.sort_values(ascending = False)
miscore

def plot_miscore(scores):
  scores = scores.sort_values(ascending = True)
  width = np.arange(len(scores))
  ticks = list(scores.index)
  plt.barh(width, scores)
  plt.yticks(width, ticks)
  plt.title('Mutual Info Score')
  plt.figure(dpi = 100, figsize=(9,6))

plot_miscore(miscore)

x = x.drop(['EstimatedSalary','CustomerId','RowNumber','Tenure','Surname'],axis=1)

x
# y

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import GradientBoostingRegressor

x_train,x_test, y_train, y_test = train_test_split(x,y, test_size=0.3)

rf_model = RandomForestClassifier(n_estimators=100,criterion='gini')
rf_model.fit(x_train, y_train)

y_pred = rf_model.predict(x_test)

print(accuracy_score(y_test,y_pred))

inp = np.array(['600','1','1','35','3500','5','1','1'])
inp = np.reshape(inp, (1,-1))
rf_model.predict(inp)

gb_model = GradientBoostingClassifier()

gb_model.fit(x_train, y_train)

y_gb_pred = gb_model.predict(x_test)

print(accuracy_score(y_test,y_gb_pred))

inp = np.array(['600','1','1','35','3500','5','1','1'])
inp = np.reshape(inp, (1,-1))
gb_model.predict(inp)

gb_r_model = GradientBoostingRegressor()

gb_r_model.fit(x_train,y_train)

y_gb_r_pred = gb_r_model.predict(x_test)

print(gb_r_model.score(x_train,y_train))
print(gb_r_model.score(x_test,y_test))

inp = np.array(['600','1','1','35','3500','5','1','1'])
inp = np.reshape(inp, (1,-1))
gb_r_model.predict(inp)


import os

#data analysis and wrangling
"""
Data wrangling, sometimes referred to as data munging, is the process of 
transforming and mapping data from one "raw" data form into another format
 with the intent of making it more appropriate and valuable for a variety 
 of downstream purposes such as analytics.
"""	
import pandas as pd
import numpy as np
import random as rnd

#visualization
import seaborn as sns
import matplotlib.pyplot as plt
'exec(%matplotlib inline)'

#machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier

#load data as pandas dataframe
train_df = pd.read_csv(os.getcwd()+"\\train.csv")
test_df = pd.read_csv(os.getcwd()+"\\test.csv")
combine = [train_df, test_df]

#displays features of the dataset
print(train_df.columns.values)

#preview data
print(train_df.head())
print(train_df.tail())
print("-"*40)
print(train_df.info())
print("-"*40)
#by default The result will include all numeric columns.
print(train_df.describe())
print("-"*40)
#Including only string columns in a DataFrame description.
print(train_df.describe(include=[np.object]))
print("-"*40)
print(train_df[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean().sort_values(by="Survived", ascending=False))
print("-"*40)
print(train_df[['Sex', 'Survived']].groupby(['Sex'], as_index=False).mean().sort_values(by="Survived", ascending=False))
print("-"*40)
print(train_df[['SibSp', 'Survived']].groupby(['SibSp'], as_index=False).mean().sort_values(by="Survived", ascending=False))
print("-"*40)
print(train_df[['Parch', 'Survived']].groupby(['Parch'], as_index=False).mean().sort_values(by="Survived", ascending=False))

"""
g = sns.FacetGrid(train_df, col='Survived', row='Embarked')
g.map(plt.hist, 'Age', bins=20)
grid = sns.FacetGrid(train_df, row='Embarked', col='Survived')
grid.map(sns.barplot, 'Sex', 'Fare')
grid.add_legend()
plt.show()
"""
train_df = train_df.drop(['Ticket', 'Cabin'], axis=1)
test_df = test_df.drop(['Ticket', 'Cabin'], axis=1)
combine = [train_df, test_df]
print(train_df.shape)

for dataset in combine:
	dataset['Title'] = dataset.Name.str.extract(' ([A-Za-z]+)\.', expand=False)

"""
Compute a simple cross-tabulation of two (or more) factors. By default 
computes a frequency table of the factors unless an array of values 
and an aggregation function are passed
"""
print(pd.crosstab(train_df['Title'], train_df['Sex']))	

for dataset in combine:
	dataset['Title'] = dataset['Title'].replace(['Lady', 'Countess', 'Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'],  'Rare')
	
	dataset['Title'] = dataset['Title'].replace('Mlle', 'Miss')
	dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
	dataset['Title'] = dataset['Title'].replace('Mme', 'Mrs')
	
print(train_df[['Title', 'Survived']].groupby(['Title'], as_index=False).mean())

title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Rare": 5}

for dataset in combine:
	dataset['Title'] = dataset['Title'].map(title_mapping)
	dataset['Title'] = dataset['Title'].fillna(0)
	
print(train_df.head())

train_df = train_df.drop(['Name', 'PassengerId'], axis=1)
test_df = test_df.drop(['Name'], axis=1)
combine = [train_df, test_df]

for dataset in combine:
	dataset['Sex'] = dataset['Sex'].map({'female': 1, 'male': 0}).astype(int)
	
print(train_df.head())


guess_ages = np.zeros((2,3))

for dataset in combine:
	for i in range(0,2):
		for j in range(0,3):
			guess_df = dataset[(dataset['Sex']==1) & 






















print("End of Program")
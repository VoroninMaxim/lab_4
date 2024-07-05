import pandas as pd

#Load
titanic_train = pd.read_csv('datasets/titanic_train.csv', sep=',')

mean_age = titanic_train['Age'].mean()

titanic_train['Age'] = titanic_train['Age'].apply(lambda x: mean_age if pd.isna(x) else x)

titanic_train.to_csv('datasets/titanic_train.csv', index=False)
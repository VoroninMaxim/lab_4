from catboost.datasets import titanic

# load
titanic_train, titanic_test = titanic()

titanic_train = titanic_train[['Pclass', 'Sex', 'Age']]

#Save
titanic_train.to_csv('datasets/titanic_train.csv', index=False)
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

titanic_train = pd.read_csv('datasets/titanic_train.csv', sep=',')

encoder = OneHotEncoder(drop='if_binary', sparse_output=False)

sex_encoded = encoder.fit_transform(titanic_train[['Sex']])

sex_encoded_df = pd.DataFrame(sex_encoded, columns=encoder.get_feature_names_out(['Sex']))
titanic_train = pd.concat([titanic_train.drop(columns=['Sex']), sex_encoded_df], axis=1)

# Обновить датасет
titanic_train.to_csv('datasets/titanic_train.csv', index=False)
# loading library with iris dataset
from sklearn.datasets import load_iris
# loading scikit scrandom forest classifier library
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
np.random.seed(0)

# creating object called iris with iris data
iris=load_iris()
# creating a dataframe with four feature variables
df=pd.DataFrame(iris.data,columns=iris.feature_names)
# viewing top 5 rows
df.head()

iris=load_iris()
df=pd.DataFrame(iris.data,columns=iris.feature_names)
# viewing first five rows
print(iris)

# Use Case Implementation
#adding new column for namezz
df['species']=pd.Categorical.from_codes(iris.target,iris.target_names)
df.head()

# Creating test and training data
df['is_train']=np.random.uniform(0,1,len(df))<=.75
df.head()

# creating dataframes with test_rows and training_rows
train,test=df[df['is_train']==True],df[df['is_train']==False]
# showing no of observations for testing and training dataframes
print('No. of observations in training data are:',len(train))
print('No. of observations in testing data are:',len(test))

# Creating list of feature column's namezz
features=df.columns[:4]
# Viewing all features
features

# Converting species names into digits
y=pd.factorize(train['species'])[0]
# Now viewing target
y

# Creating random forest classifier
clf=RandomForestClassifier(n_jobs=2,random_state=0)
# Training your classifier
clf.fit(train[features],y)

# applying trained classifier to the test
clf.predict(test[features])

# maping names for plants for each predicted plant class
preds=iris.target_names[clf.predict(test[features])]
# viewing predicted species
preds[0:5]

# viewing actual species
test['species'].head()

# creating matrix
pd.crosstab(test['species'],preds,rownames=['Actual Species'],colnames=['Predicted Species'])

preds=iris.target_names[clf.predict([[3.6,5.0,2.0,1.4],[5.0,3.6,1.4,2.0]])]
preds

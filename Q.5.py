import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.metrics import classification_report 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import precision_score, recall_score, f1_score

df = pd.read_csv("heart.csv", header="infer")

X=df.iloc[:,:-1] #input data
y=df.iloc[:,-1] #target data

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,stratify=y)

k=int(input("Enter the number of nearest neighbours to be used, i.e. k:"))

#creating instance of a class
model=KNeighborsClassifier(n_neighbors=k, weights='distance')

#training the classifier
model.fit(X_train,y_train)

#predicting from the trained classifier
pred=model.predict(X_test)

from sklearn.metrics import accuracy_score, classification_report
#performance metrics
accuracy=accuracy_score(y_test,pred)
print("Accuracy:", accuracy)
print("Precision:", precision_score(y_test, pred, average='weighted'))
print("Recall:", recall_score(y_test, pred, average='weighted'))
print("F1-score:", f1_score(y_test, pred, average='weighted'))

print("\nClassification Report:\n")
print(classification_report(y_test,pred))



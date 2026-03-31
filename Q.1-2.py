import pandas as pd
import numpy as np
import math # for flooring operation later
import time # for calculating time taken to execute the code

df = pd.read_csv("test_Y3wMUE5_7gLdaTN.csv", header='infer')
print(df)
df.info() # information about the data set
print(df.describe()) # statistical summary of the data set

df2=df.dropna(axis=0) # drop rows with missing values
print(df2)

df3=df.dropna(axis=1) # drop columns with missing values
print(df3)

mean_value = np.mean(df.loc[~df["LoanAmount"].isna() & (df["Education"]=="Graduate"), "LoanAmount"].values)
print(mean_value)
df.loc[df["LoanAmount"].isna() & (df["Education"]=="Graduate"), "LoanAmount"] = mean_value
print(df["LoanAmount"])
df.info() # information about the data set after filling missing values

mean_value1 = np.mean(df.loc[~df["LoanAmount"].isna() & (df["Education"]=="Not Graduate"), "LoanAmount"].values)
print(mean_value1)
df.loc[df["LoanAmount"].isna() & (df["Education"]=="Not Graduate"), "LoanAmount"] = mean_value1
print(df["LoanAmount"])
df.info() # information about the data set after filling missing values

mean_value2 = np.mean(df.loc[~df["Loan_Amount_Term"].isna() & (df["Education"]=="Graduate"), "Loan_Amount_Term"].values)
print(mean_value2)
df.loc[df["Loan_Amount_Term"].isna() & (df["Education"]=="Graduate"), "Loan_Amount_Term"] = mean_value2
print(df["Loan_Amount_Term"])
df.info() # information about the data set after filling missing values

mean_value3 = np.mean(df.loc[~df["Loan_Amount_Term"].isna() & (df["Education"]=="Not Graduate"), "Loan_Amount_Term"].values)
print(mean_value3)
df.loc[df["Loan_Amount_Term"].isna() & (df["Education"]=="Not Graduate"), "Loan_Amount_Term"] = mean_value3
print(df["Loan_Amount_Term"])
df.info() # information about the data set after filling missing values

mean_value4 = np.mean(df.loc[~df["Loan_Amount_Term"].isna() & (df["Education"]=="Graduate"), "Loan_Amount_Term"].values)
print(mean_value4)
df.loc[df["Loan_Amount_Term"].isna() & (df["Education"]=="Graduate"), "Loan_Amount_Term"] = mean_value4
print(df["Loan_Amount_Term"])
df.info() # information about the data set after filling missing values

mean_value5 = np.mean(df.loc[~df["Credit_History"].isna() & (df["Education"]=="Graduate"), "Credit_History"].values)
print(mean_value5)
df.loc[df["Credit_History"].isna() & (df["Education"]=="Graduate"), "Credit_History"] = mean_value5
print(df["Credit_History"])
df.info() # information about the data set after filling missing values

mean_value6 = np.mean(df.loc[~df["Credit_History"].isna() & (df["Education"]=="Not Graduate"), "Credit_History"].values)
print(mean_value6)
df.loc[df["Credit_History"].isna() & (df["Education"]=="Not Graduate"), "Credit_History"] = mean_value6
print(df["Credit_History"])
df.info() # information about the data set after filling missing values

mode1 = df.loc[df["Education"]=="Graduate","Gender"].mode()[0]
print(mode1)
df.loc[df["Gender"].isna() & (df["Education"]=="Graduate"), "Gender"] = mode1
print(df["Gender"])
df.info() # information about the data set after filling missing values

mode2 = df.loc[df["Education"]=="Not Graduate","Gender"].mode()[0]
print(mode2)
df.loc[df["Gender"].isna() & (df["Education"]=="Not Graduate"), "Gender"] = mode2
print(df["Gender"])
df.info() # information about the data set after filling missing values

mode3 = df.loc[df["Education"]=="Graduate","Dependents"].mode()[0]
print(mode3)
df.loc[df["Dependents"].isna() & (df["Education"]=="Graduate"), "Dependents"] = mode3
print(df["Dependents"])
df.info() # information about the data set after filling missing values

mode4 = df.loc[df["Education"]=="Not Graduate","Dependents"].mode()[0]
print(mode4)
df.loc[df["Dependents"].isna() & (df["Education"]=="Not Graduate"), "Dependents"] = mode4
print(df["Dependents"])
df.info() # information about the data set after filling missing values

mode5 = df.loc[df["Education"]=="Graduate","Self_Employed"].mode()[0]
print(mode5)
df.loc[df["Self_Employed"].isna() & (df["Education"]=="Graduate"), "Self_Employed"] = mode5
print(df["Self_Employed"])
df.info() # information about the data set after filling missing values

mode6 = df.loc[df["Education"]=="Not Graduate","Self_Employed"].mode()[0]
print(mode6)
df.loc[df["Self_Employed"].isna() & (df["Education"]=="Not Graduate"), "Self_Employed"] = mode6
print(df["Self_Employed"])
df.info() # information about the data set after filling missing values

df1 = df.to_csv("filled_test.csv")

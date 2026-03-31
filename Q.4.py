import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("filled_test.csv")

plt.suptitle("Different Types of Plots")

# 1. Histogram
plt.subplot(2,3,1)
plt.hist(df["ApplicantIncome"], color="red", label="Income")
plt.title("Histogram - Applicant Income")
plt.xlabel("Applicant Income")
plt.ylabel("Frequency")
plt.legend()

# 2. Scatter Plot
plt.subplot(2,3,2)
plt.scatter(df["ApplicantIncome"][df["Gender"]=="Male"],
            df["LoanAmount"][df["Gender"]=="Male"],
            color='blue', label='Male')
plt.scatter(df["ApplicantIncome"][df["Gender"]=="Female"],
            df["LoanAmount"][df["Gender"]=="Female"],
            color='pink', label='Female')
plt.title("Scatter Plot - Income vs LoanAmount")
plt.xlabel("Applicant Income")
plt.ylabel("Loan Amount")
plt.legend()

# 3. Bar Chart
plt.subplot(2,3,3)
counts = df["Gender"].value_counts()
plt.bar(counts.index, counts.values, color=['blue', 'pink'], label=counts.index)
plt.title("Bar Chart - Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.legend()

# 4. Box Plot
plt.subplot(2,3,4)
plt.boxplot(df["LoanAmount"].dropna(), labels=["Loan Amount"])
plt.title("Box Plot - LoanAmount")
plt.ylabel("Loan Amount")
plt.legend(["Loan Amount"])

# 5. Line Plot
plt.subplot(2,3,5)
plt.plot(df["ApplicantIncome"], label="Applicant Income", color="green")
plt.title("Line Plot - Applicant Income")
plt.xlabel("Index")
plt.ylabel("Income")
plt.legend()

plt.subplots_adjust(hspace=0.5, wspace=0.5)
plt.show()
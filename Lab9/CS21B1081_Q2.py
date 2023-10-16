
# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv('diabetes.csv')

X = df.iloc[:, :-2]
y = df.iloc[:, -2]

mean = X.mean()
median = X.median()
mode = X.mode()
minimum = X.min()
maximum = X.max()
std = X.std()

print("Mean: \n", mean)
print("Median: \n", median)
print("Mode: \n", mode)
print("Minimum: \n", minimum)
print("Maximum: \n", maximum)
print("Standard Deviation: \n", std)


# In[3]:


def correlation_coeff(x, y):
    x_mean, y_mean = x.mean(), y.mean()
    x_std, y_std = x.std(), y.std()
    n = len(x)
    return np.sum((x-x_mean)*(y-y_mean)) / (n*x_std*y_std)


# In[6]:


age_corr = []
for i in X.columns:
    age_corr.append(correlation_coeff(X['Age'], X[i]))

bmi_corr = []
for i in X.columns:
    bmi_corr.append(correlation_coeff(X['BMI'], X[i]))


# In[7]:


plt.bar(X.columns, age_corr)
plt.xlabel('Features')
plt.ylabel('Correlation Coefficient')
plt.title('Correlation Coefficient with Age')
plt.show()


# In[8]:


plt.bar(X.columns, bmi_corr)
plt.xlabel('Features')
plt.ylabel('Correlation Coefficient')
plt.title('Correlation Coefficient with BMI')
plt.show()


---
title: "Loan Default Project"
excerpt: "Predicting loan default from bank data"
collection: portfolio
---

# Business Objective
A bank has given us a data set and would like us to find which potential customers will likely repay a bank loan and what questions to ask on future applications based off of previous loan data.
1. Data set of Loans and if they were paid or defaulted. 
2. Look for the Customers who have paid and predict if future customers will pay back or default loan.
3. Come up with questions for customer when they are applying for loan


```python
import pandas as pd
```


```python
df = pd.read_csv('1533148983_LoansTrainingSet.csv')
```

## Taking a Look at the Data

```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 256984 entries, 0 to 256983
    Data columns (total 19 columns):
    Loan ID                         256984 non-null object
    Customer ID                     256984 non-null object
    Loan Status                     256984 non-null object
    Current Loan Amount             256984 non-null int64
    Term                            256984 non-null object
    Credit Score                    195308 non-null float64
    Years in current job            245508 non-null object
    Home Ownership                  256984 non-null object
    Annual Income                   195308 non-null float64
    Purpose                         256984 non-null object
    Monthly Debt                    256984 non-null object
    Years of Credit History         256984 non-null float64
    Months since last delinquent    116601 non-null float64
    Number of Open Accounts         256984 non-null int64
    Number of Credit Problems       256984 non-null int64
    Current Credit Balance          256984 non-null int64
    Maximum Open Credit             256984 non-null object
    Bankruptcies                    256455 non-null float64
    Tax Liens                       256961 non-null float64
    dtypes: float64(6), int64(4), object(9)
    memory usage: 37.3+ MB



```python
df.head()
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Loan ID</th>
      <th>Customer ID</th>
      <th>Loan Status</th>
      <th>Current Loan Amount</th>
      <th>Term</th>
      <th>Credit Score</th>
      <th>Years in current job</th>
      <th>Home Ownership</th>
      <th>Annual Income</th>
      <th>Purpose</th>
      <th>Monthly Debt</th>
      <th>Years of Credit History</th>
      <th>Months since last delinquent</th>
      <th>Number of Open Accounts</th>
      <th>Number of Credit Problems</th>
      <th>Current Credit Balance</th>
      <th>Maximum Open Credit</th>
      <th>Bankruptcies</th>
      <th>Tax Liens</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>000025bb-5694-4cff-b17d-192b1a98ba44</td>
      <td>5ebc8bb1-5eb9-4404-b11b-a6eebc401a19</td>
      <td>Fully Paid</td>
      <td>11520</td>
      <td>Short Term</td>
      <td>741.0</td>
      <td>10+ years</td>
      <td>Home Mortgage</td>
      <td>33694.0</td>
      <td>Debt Consolidation</td>
      <td>$584.03</td>
      <td>12.3</td>
      <td>41.0</td>
      <td>10</td>
      <td>0</td>
      <td>6760</td>
      <td>16056</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>1</td>
      <td>00002c49-3a29-4bd4-8f67-c8f8fbc1048c</td>
      <td>927b388d-2e01-423f-a8dc-f7e42d668f46</td>
      <td>Fully Paid</td>
      <td>3441</td>
      <td>Short Term</td>
      <td>734.0</td>
      <td>4 years</td>
      <td>Home Mortgage</td>
      <td>42269.0</td>
      <td>other</td>
      <td>$1,106.04</td>
      <td>26.3</td>
      <td>NaN</td>
      <td>17</td>
      <td>0</td>
      <td>6262</td>
      <td>19149</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>2</td>
      <td>00002d89-27f3-409b-aa76-90834f359a65</td>
      <td>defce609-c631-447d-aad6-1270615e89c4</td>
      <td>Fully Paid</td>
      <td>21029</td>
      <td>Short Term</td>
      <td>747.0</td>
      <td>10+ years</td>
      <td>Home Mortgage</td>
      <td>90126.0</td>
      <td>Debt Consolidation</td>
      <td>$1,321.85</td>
      <td>28.8</td>
      <td>NaN</td>
      <td>5</td>
      <td>0</td>
      <td>20967</td>
      <td>28335</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>3</td>
      <td>00005222-b4d8-45a4-ad8c-186057e24233</td>
      <td>070bcecb-aae7-4485-a26a-e0403e7bb6c5</td>
      <td>Fully Paid</td>
      <td>18743</td>
      <td>Short Term</td>
      <td>747.0</td>
      <td>10+ years</td>
      <td>Own Home</td>
      <td>38072.0</td>
      <td>Debt Consolidation</td>
      <td>$751.92</td>
      <td>26.2</td>
      <td>NaN</td>
      <td>9</td>
      <td>0</td>
      <td>22529</td>
      <td>43915</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>4</td>
      <td>0000757f-a121-41ed-b17b-162e76647c1f</td>
      <td>dde79588-12f0-4811-bab0-e2b07f633fcd</td>
      <td>Fully Paid</td>
      <td>11731</td>
      <td>Short Term</td>
      <td>746.0</td>
      <td>4 years</td>
      <td>Rent</td>
      <td>50025.0</td>
      <td>Debt Consolidation</td>
      <td>$355.18</td>
      <td>11.5</td>
      <td>NaN</td>
      <td>12</td>
      <td>0</td>
      <td>17391</td>
      <td>37081</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



Going through each column, duplicate values have been recorded, missing information needs to be filled in multiple columns and object columns need to be convereted to numbers. Also, the 'credit score' column has a recording error. The column most important column we need for analysis is 'Loan Status'. Which is our column that shows if a loan was paid off or defaulted.


```python
# drop exact duplicate rows 
df.drop_duplicates(keep='first', inplace=True)
```


```python
# Split Columns between numbers and objects to groupby 'Loan ID' so we can fill in missing values
df_obj = df.select_dtypes(include='object')
df_num = df.select_dtypes(exclude='object')
```

```python
# Loan ID to numbers data frame so can use groupby
df_num['Loan ID'] = df['Loan ID']
```
```python
# groupby Loan ID and takes the max of each loan
df_num = df_num.groupby('Loan ID').max().reset_index()
df_obj = df_obj.drop_duplicates(subset='Loan ID')
df = df_obj.merge(df_num) 
```


```python
# grabbing Loan and Customer ID
loan_cust_id = df[['Loan ID', 'Customer ID']]
df.drop(['Loan ID', 'Customer ID'], axis=1, inplace=True)
```

## Filling in Missing Data
Columns with NaN values were filled with values similar to data in the row


```python
# BANKRUPTCIES
df['Bankruptcies'].fillna(0.0, inplace=True)
df['Tax Liens'].fillna(0.0, inplace=True)
# Months since last delinquent
df['Months since last delinquent'].fillna(0.0, inplace = True)
# Replace Column Years in current job == < 1 Year to .5 integer
df['Years in current job'].replace('< 1 year', 0.5, inplace=True)
# Replace Column Years in current job == 10+ Year to 15 year
df['Years in current job'].replace('10+ years', '15 year', inplace=True)
# Fill NaN Values in Years in current job column to '0 year' string
df['Years in current job'] = df['Years in current job'].fillna(value='0 years')
# Extracts digit from Years in current job and changes Years in current job to int
df['Years in current job'] = df['Years in current job'].str.extract('(\d+)').astype(float)
# Fill NaN Values in Years to 0.5 for < 1 year
df['Years in current job'] = df['Years in current job'].fillna(value=0.5)
```

### CORRECTING DATA INPUT ERRORS


```python
# replace other to Other
df.replace('other', 'Other', inplace=True)
# Changes #VALUE! in Maximum Open Credit to 0
df.loc[df['Maximum Open Credit'] == '#VALUE!', 'Maximum Open Credit'] = df['Current Loan Amount'].median()
# found median of Loan Amount without the 99999999 values
loan_median = df[df['Current Loan Amount'] < 99999999]['Current Loan Amount'].median()
# Change the 9999999 Loan Amount Values to loan median
df.loc[df['Current Loan Amount'] == 99999999, 'Current Loan Amount'] = loan_median
# replace HaveMortgage to Home Mortgage
df.replace('HaveMortgage', 'Home Mortgage', inplace=True)
```

### For a score with a range between 300-850, a credit score of 700 or above is generally considered good. A score of 800 or above on the same range is considered to be excellent. Most credit scores fall between 600 and 750


```python
df['Credit Score'].describe()
```




    count    171202.000000
    mean       1261.776013
    std        1775.229972
    min         585.000000
    25%         716.000000
    50%         735.000000
    75%         745.000000
    max        7510.000000
    Name: Credit Score, dtype: float64




```python
df['Credit Score'] = df['Credit Score'].apply(lambda x : x / 10 if x > 1000 else x)
```


```python
df['Credit Score'].describe()
```




    count    171202.000000
    mean        722.755698
    std          26.827283
    min         585.000000
    25%         712.000000
    50%         732.000000
    75%         742.000000
    max         751.000000
    Name: Credit Score, dtype: float64


### Changing Object Columns to numeric 
Many of the columns have object data types including: Term, Home Ownership, Purpose, Loan Status, Monthly Debt and Maximum Open Credit. Those that will be changed to nonordinal datatype include Term, Home Ownership, Purpose. The other columns will be changed to numerical. Loan Status, which is our target, will be converted to 0 based on being paid off and 1 being unpaid.


```python
d = {'Fully Paid': 0, 'Charged Off': 1}
df['Loan Status'] = df['Loan Status'].map(d)
```


```python
# removing , and $ from Monthly Debt and changing to float
df['Monthly Debt'] = df['Monthly Debt'].str.replace(',','')
df['Monthly Debt'] = df['Monthly Debt'].str.replace('$','')
df['Monthly Debt'] = df['Monthly Debt'].astype(float)
```


```python
df['Maximum Open Credit'] = df['Maximum Open Credit'].astype(float)
```

### Creating Dummies for the Columns: Term, Home Ownership and Purpose


```python
df = pd.get_dummies(df, drop_first=True)
```

```python
loan = df.corr()['Loan Status']
```

```python
sns.countplot(x='Loan Status', data=df)
```

![png](/images/output_29_1.png)



```python
sns.scatterplot(x='Credit Score', y='Annual Income', data=df)
```


![png](/images/output_30_1.png)



```python
# Take out Loan Status and Annual Income to predict them
loan_status = df['Loan Status']
income = df['Annual Income']
df.drop(['Loan Status', 'Annual Income'], axis=1, inplace=True)
```

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
```

```python
filled = df[df['Credit Score'].notnull()]
missing = df[df['Credit Score'].isnull()]
```

```python
X_train, X_test, y_train, y_test = train_test_split(filled.drop('Credit Score', axis=1), 
                                                    filled['Credit Score'], test_size=0.4, random_state=101)
```

```python
L = LinearRegression()
```

```python
L.fit(X_train, y_train)
```

```python
r2_score(y_train, L.predict(X_train))
```
    0.28462988125672517


```python
mean_squared_error(y_train, L.predict(X_train))**.5
```

    22.740334260998736



```python
predict = L.predict(X_test)
```


```python
predictions = L.predict(missing.drop('Credit Score', axis=1))
```


```python
missing['Credit Score'] = predictions
df = pd.concat([missing, filled])
```

```python
# Adding Annual Income Column back
df['Annual Income'] = income
```


```python
filled = df[df['Annual Income'].notnull()]
missing = df[df['Annual Income'].isnull()]
```


```python
X_train, X_test, y_train, y_test = train_test_split(filled.drop('Annual Income', axis=1), 
                                                    filled['Annual Income'], test_size=0.4, random_state=101)
```


```python
L.fit(X_train, y_train)
```

```python
print(r2_score(y_test, L.predict(X_test)))
print(mean_squared_error(y_test, L.predict(X_test))**.5)
```

    0.3833735024596715
    38215.97609792463



```python
prediction = L.predict(missing.drop('Annual Income', axis=1))
missing['Annual Income'] = prediction
```


```python
df = pd.concat([missing, filled])
```


```python
df['Loan Status'] = loan_status
```


```python
sns.countplot(x='Loan Status', data=df)
```

![png](/images/output_52_1.png)


## Imbalanced Data


Using undersampling to balance out the number of Loans that were paid off and unpaid. The under sampled 'Loan Status' which is the charged off loans will match the number of  paid off loans.


```python
# Shuffle the Dataset.
shuffled_df = df.sample(frac=1,random_state=4)

# Put all the charged off loan class in a separate dataset.
upaid_df = shuffled_df.loc[shuffled_df['Loan Status'] == 1]

#Randomly select 492 observations from the paid off (majority class)
paid_df = shuffled_df.loc[shuffled_df['Loan Status'] == 0].sample(n=39509,random_state=42)

# Concatenate both dataframes again
normalized_df = pd.concat([upaid_df, paid_df])
```


```python
#plot the dataset after the undersampling
plt.figure(figsize=(8, 8))
sns.countplot('Loan Status', data=normalized_df)
plt.title('Balanced Classes')
plt.show()
```


![png](/images/output_56_0.png)



```python
X = normalized_df.drop('Loan Status', axis=1)
y = normalized_df['Loan Status']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101, 
                                                    stratify=normalized_df['Loan Status'])
```


```python
from sklearn.linear_model import LogisticRegression
log = LogisticRegression()
```


```python
log.fit(X_train, y_train)
```




    LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
                       intercept_scaling=1, l1_ratio=None, max_iter=100,
                       multi_class='auto', n_jobs=None, penalty='l2',
                       random_state=None, solver='lbfgs', tol=0.0001, verbose=0,
                       warm_start=False)




```python
predictions = log.predict(X_test)
```


```python
from sklearn.metrics import classification_report, confusion_matrix
```


```python
print(classification_report(y_test, predictions))
```

                  precision    recall  f1-score   support
    
               0       0.59      0.60      0.60     15804
               1       0.60      0.59      0.59     15804
    
        accuracy                           0.59     31608
       macro avg       0.59      0.59      0.59     31608
    weighted avg       0.59      0.59      0.59     31608
    


Based off the classification report, we scored about 60% accuracy that people will both pay back their loans and if they will default on their loans. 


```python
import numpy as np   
```

```python
feature_importance = abs(log.coef_[0])
feature_importance = 100.0 * (feature_importance / feature_importance.max())
sorted_idx = np.argsort(feature_importance)
pos = np.arange(sorted_idx.shape[0]) + .5

featfig = plt.figure()
featax = featfig.add_subplot(1, 1, 1)
featax.barh(pos, feature_importance[sorted_idx], align='center')
featax.set_yticks(pos)
featax.set_yticklabels(np.array(X.columns)[sorted_idx], fontsize=8)
featax.set_xlabel('Relative Feature Importance')

plt.tight_layout()   
plt.show()
```


![png](/images/output_65_0.png)


## Conclusion

After looking at the chart above which feature importance that is based off of the column coefficients, the most important questions to ask future loan applicants are:
1. How much is their monthly debt?
2. What is their credit score?
3. How much is their current loan amount?
4. What is their annual income?

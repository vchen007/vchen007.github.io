# Business Objective
A bank has given us a data set and would like us to find which potential customers will likely repay a bank loan and what questions to ask on future applications based off of previous loan data.
1. Data set of Loans and if they were paid or defaulted. 
2. Look for the Customers who have paid and predict if future customers will pay back or default loan.
3. Come up with questions for customer when they are applying for loan


```python
import pandas as pd
```


```python
!pip install tabulate
```

    Collecting tabulate
    [?25l  Downloading https://files.pythonhosted.org/packages/c4/41/523f6a05e6dc3329a5660f6a81254c6cd87e5cfb5b7482bae3391d86ec3a/tabulate-0.8.6.tar.gz (45kB)
    [K     |████████████████████████████████| 51kB 2.9MB/s eta 0:00:01
    [?25hBuilding wheels for collected packages: tabulate
      Building wheel for tabulate (setup.py) ... [?25ldone
    [?25h  Created wheel for tabulate: filename=tabulate-0.8.6-cp37-none-any.whl size=23274 sha256=41a7d96eef8677f6d418b89feb38e7d047ffd13bab2493c416fe9bc4a79e61c0
      Stored in directory: /Users/vchen123/Library/Caches/pip/wheels/9c/9b/f4/eb243fdb89676ec00588e8c54bb54360724c06e7fafe95278e
    Successfully built tabulate
    Installing collected packages: tabulate
    Successfully installed tabulate-0.8.6



```python

```


```python
df = pd.read_csv('1533148983_LoansTrainingSet.csv')
```

    /Applications/anaconda3/lib/python3.7/site-packages/IPython/core/interactiveshell.py:3058: DtypeWarning: Columns (16) have mixed types. Specify dtype option on import or set low_memory=False.
      interactivity=interactivity, compiler=compiler, result=result)


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
df.describe()
```

    |       |   Current Loan Amount |   Credit Score |    Annual Income |   Years of Credit History |   Months since last delinquent |   Number of Open Accounts |   Number of Credit Problems |   Current Credit Balance |   Bankruptcies |      Tax Liens |
    |:------|----------------------:|---------------:|-----------------:|--------------------------:|-------------------------------:|--------------------------:|----------------------------:|-------------------------:|---------------:|---------------:|
    | count |      256984           |      195308    | 195308           |              256984       |                    116601      |              256984       |               256984        |         256984           |  256455        | 256961         |
    | mean  |           1.37133e+07 |        1251.12 |  71952.7         |                  18.2902  |                        34.8815 |                  11.1063  |                    0.156628 |          15406.6         |       0.110316 |      0.0272026 |
    | std   |           3.43813e+07 |        1762.02 |  58877.6         |                   7.07575 |                        21.8542 |                   4.98298 |                    0.460731 |          19665.1         |       0.336229 |      0.24595   |
    | min   |         505           |         585    |      0           |                   3.4     |                         0      |                   0       |                    0        |              0           |       0        |      0         |
    | 25%   |        8299           |         714    |  44321           |                  13.5     |                        16      |                   8       |                    0        |           5974           |       0        |      0         |
    | 50%   |       14298           |         733    |  61242           |                  17       |                        32      |                  10       |                    0        |          11078           |       0        |      0         |
    | 75%   |       24367           |         744    |  86462           |                  21.7     |                        51      |                  14       |                    0        |          19319           |       0        |      0         |
    | max   |           1e+08       |        7510    |      8.71355e+06 |                  70.5     |                       176      |                  76       |                   11        |              1.73141e+06 |       7        |     11         |


```python
df.head(10)
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
    <tr>
      <td>5</td>
      <td>0000a149-b055-4a57-b762-280783ccc25e</td>
      <td>62ddc017-7023-4ba7-af23-1a7cd16c1ce5</td>
      <td>Fully Paid</td>
      <td>10208</td>
      <td>Short Term</td>
      <td>716.0</td>
      <td>10+ years</td>
      <td>Rent</td>
      <td>41853.0</td>
      <td>Business Loan</td>
      <td>$561.52</td>
      <td>13.2</td>
      <td>NaN</td>
      <td>4</td>
      <td>1</td>
      <td>2289</td>
      <td>4671</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>6</td>
      <td>0000afa6-8902-4f8f-b870-25a8fdad0aeb</td>
      <td>e49c1a82-a0f7-45e8-9f46-2f75c43f9fbc</td>
      <td>Charged Off</td>
      <td>24613</td>
      <td>Long Term</td>
      <td>6640.0</td>
      <td>6 years</td>
      <td>Rent</td>
      <td>49225.0</td>
      <td>Business Loan</td>
      <td>$542.29</td>
      <td>17.6</td>
      <td>73.0</td>
      <td>7</td>
      <td>0</td>
      <td>14123</td>
      <td>16954</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>7</td>
      <td>0000afa6-8902-4f8f-b870-25a8fdad0aeb</td>
      <td>e49c1a82-a0f7-45e8-9f46-2f75c43f9fbc</td>
      <td>Charged Off</td>
      <td>24613</td>
      <td>Long Term</td>
      <td>NaN</td>
      <td>6 years</td>
      <td>Rent</td>
      <td>NaN</td>
      <td>Business Loan</td>
      <td>$542.29</td>
      <td>17.6</td>
      <td>73.0</td>
      <td>7</td>
      <td>0</td>
      <td>14123</td>
      <td>16954</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>8</td>
      <td>00011dfc-31c1-4178-932a-fbeb3f341efb</td>
      <td>ef6e098c-6c83-4752-8d00-ff793e476b8c</td>
      <td>Fully Paid</td>
      <td>10036</td>
      <td>Short Term</td>
      <td>NaN</td>
      <td>5 years</td>
      <td>Rent</td>
      <td>NaN</td>
      <td>Debt Consolidation</td>
      <td>$386.36</td>
      <td>17.7</td>
      <td>NaN</td>
      <td>7</td>
      <td>0</td>
      <td>11970</td>
      <td>16579</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0001cb86-af28-4011-bb86-183786e473ae</td>
      <td>4aae67bb-d54b-41ae-8bce-1d62022ed8dd</td>
      <td>Fully Paid</td>
      <td>2036</td>
      <td>Short Term</td>
      <td>733.0</td>
      <td>NaN</td>
      <td>Home Mortgage</td>
      <td>55985.0</td>
      <td>Debt Consolidation</td>
      <td>$741.79</td>
      <td>19.8</td>
      <td>29.0</td>
      <td>7</td>
      <td>0</td>
      <td>10926</td>
      <td>15676</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
print(tabulate(df.head(10), headers="keys", tablefmt="pipe"))
```
    |    | Loan ID                              | Customer ID                          | Loan Status   |   Current Loan Amount | Term       |   Credit Score | Years in current job   | Home Ownership   |   Annual Income | Purpose            | Monthly Debt   |   Years of Credit History |   Months since last delinquent |   Number of Open Accounts |   Number of Credit Problems |   Current Credit Balance |   Maximum Open Credit |   Bankruptcies |   Tax Liens |
    |----|--------------------------------------|--------------------------------------|---------------|-----------------------|------------|----------------|------------------------|------------------|-----------------|--------------------|----------------|---------------------------|--------------------------------|---------------------------|-----------------------------|--------------------------|-----------------------|----------------|-------------|
    |  0 | 000025bb-5694-4cff-b17d-192b1a98ba44 | 5ebc8bb1-5eb9-4404-b11b-a6eebc401a19 | Fully Paid    |                 11520 | Short Term |            741 | 10+ years              | Home Mortgage    |           33694 | Debt Consolidation | $584.03        |                      12.3 |                             41 |                        10 |                           0 |                     6760 |                 16056 |              0 |           0 |
    |  1 | 00002c49-3a29-4bd4-8f67-c8f8fbc1048c | 927b388d-2e01-423f-a8dc-f7e42d668f46 | Fully Paid    |                  3441 | Short Term |            734 | 4 years                | Home Mortgage    |           42269 | other              | $1,106.04      |                      26.3 |                            nan |                        17 |                           0 |                     6262 |                 19149 |              0 |           0 |
    |  2 | 00002d89-27f3-409b-aa76-90834f359a65 | defce609-c631-447d-aad6-1270615e89c4 | Fully Paid    |                 21029 | Short Term |            747 | 10+ years              | Home Mortgage    |           90126 | Debt Consolidation | $1,321.85      |                      28.8 |                            nan |                         5 |                           0 |                    20967 |                 28335 |              0 |           0 |
    |  3 | 00005222-b4d8-45a4-ad8c-186057e24233 | 070bcecb-aae7-4485-a26a-e0403e7bb6c5 | Fully Paid    |                 18743 | Short Term |            747 | 10+ years              | Own Home         |           38072 | Debt Consolidation | $751.92        |                      26.2 |                            nan |                         9 |                           0 |                    22529 |                 43915 |              0 |           0 |
    |  4 | 0000757f-a121-41ed-b17b-162e76647c1f | dde79588-12f0-4811-bab0-e2b07f633fcd | Fully Paid    |                 11731 | Short Term |            746 | 4 years                | Rent             |           50025 | Debt Consolidation | $355.18        |                      11.5 |                            nan |                        12 |                           0 |                    17391 |                 37081 |              0 |           0 |
    |  5 | 0000a149-b055-4a57-b762-280783ccc25e | 62ddc017-7023-4ba7-af23-1a7cd16c1ce5 | Fully Paid    |                 10208 | Short Term |            716 | 10+ years              | Rent             |           41853 | Business Loan      | $561.52        |                      13.2 |                            nan |                         4 |                           1 |                     2289 |                  4671 |              1 |           0 |
    |  6 | 0000afa6-8902-4f8f-b870-25a8fdad0aeb | e49c1a82-a0f7-45e8-9f46-2f75c43f9fbc | Charged Off   |                 24613 | Long Term  |           6640 | 6 years                | Rent             |           49225 | Business Loan      | $542.29        |                      17.6 |                             73 |                         7 |                           0 |                    14123 |                 16954 |              0 |           0 |
    |  7 | 0000afa6-8902-4f8f-b870-25a8fdad0aeb | e49c1a82-a0f7-45e8-9f46-2f75c43f9fbc | Charged Off   |                 24613 | Long Term  |            nan | 6 years                | Rent             |             nan | Business Loan      | $542.29        |                      17.6 |                             73 |                         7 |                           0 |                    14123 |                 16954 |              0 |           0 |
    |  8 | 00011dfc-31c1-4178-932a-fbeb3f341efb | ef6e098c-6c83-4752-8d00-ff793e476b8c | Fully Paid    |                 10036 | Short Term |            nan | 5 years                | Rent             |             nan | Debt Consolidation | $386.36        |                      17.7 |                            nan |                         7 |                           0 |                    11970 |                 16579 |              0 |           0 |
    |  9 | 0001cb86-af28-4011-bb86-183786e473ae | 4aae67bb-d54b-41ae-8bce-1d62022ed8dd | Fully Paid    |                  2036 | Short Term |            733 | nan                    | Home Mortgage    |           55985 | Debt Consolidation | $741.79        |                      19.8 |                             29 |                         7 |                           0 |                    10926 |                 15676 |              0 |           0 |


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

    /Applications/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:2: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      



```python
# groupby Loan ID and takes the max of each loan
df_num = df_num.groupby('Loan ID').max().reset_index()
df_obj = df_obj.drop_duplicates(subset='Loan ID')
df = df_obj.merge(df_num) 
```


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 215700 entries, 0 to 215699
    Data columns (total 19 columns):
    Loan ID                         215700 non-null object
    Customer ID                     215700 non-null object
    Loan Status                     215700 non-null object
    Term                            215700 non-null object
    Years in current job            206710 non-null object
    Home Ownership                  215700 non-null object
    Purpose                         215700 non-null object
    Monthly Debt                    215700 non-null object
    Maximum Open Credit             215700 non-null object
    Current Loan Amount             215700 non-null int64
    Credit Score                    171202 non-null float64
    Annual Income                   171202 non-null float64
    Years of Credit History         215700 non-null float64
    Months since last delinquent    97438 non-null float64
    Number of Open Accounts         215700 non-null int64
    Number of Credit Problems       215700 non-null int64
    Current Credit Balance          215700 non-null int64
    Bankruptcies                    215248 non-null float64
    Tax Liens                       215678 non-null float64
    dtypes: float64(6), int64(4), object(9)
    memory usage: 32.9+ MB



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


```python
df['Years in current job'].value_counts(dropna=False)
```




    15.0    66711
    2.0     19831
    0.5     17544
    3.0     17428
    5.0     14987
    1.0     14130
    4.0     13632
    6.0     12230
    7.0     11713
    8.0     10232
    0.0      8990
    9.0      8272
    Name: Years in current job, dtype: int64



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
```


```python
df.replace('HaveMortgage', 'Home Mortgage', inplace=True)
```


```python

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


```python
# Change Loan Status to 0,1 based on being paid off 
# 1 is the more important feature we are looking for
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


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 215700 entries, 0 to 215699
    Data columns (total 17 columns):
    Loan Status                     215700 non-null int64
    Term                            215700 non-null object
    Years in current job            215700 non-null float64
    Home Ownership                  215700 non-null object
    Purpose                         215700 non-null object
    Monthly Debt                    215700 non-null float64
    Maximum Open Credit             215700 non-null float64
    Current Loan Amount             215700 non-null float64
    Credit Score                    171202 non-null float64
    Annual Income                   171202 non-null float64
    Years of Credit History         215700 non-null float64
    Months since last delinquent    215700 non-null float64
    Number of Open Accounts         215700 non-null int64
    Number of Credit Problems       215700 non-null int64
    Current Credit Balance          215700 non-null int64
    Bankruptcies                    215700 non-null float64
    Tax Liens                       215700 non-null float64
    dtypes: float64(10), int64(4), object(3)
    memory usage: 29.6+ MB


### Creating Dummies for the Columns: Term, Home Ownership and Purpose


```python
df = pd.get_dummies(df, drop_first=True)
```


```python

```


```python
import seaborn as sns
%matplotlib inline
```


```python
loan = df.corr()['Loan Status']
```


```python
sns.jointplot(x='Loan Status', y='Annual Income', data=df)
```




    <seaborn.axisgrid.JointGrid at 0x11e89dc10>




![png](output_40_1.png)



```python
sns.countplot(x='Loan Status', data=df)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x11b72a290>




![png](output_41_1.png)



```python
df.corr()['Credit Score']
```




    Loan Status                    -0.245848
    Years in current job           -0.015201
    Monthly Debt                   -0.088133
    Maximum Open Credit             0.010205
    Current Loan Amount            -0.208047
    Credit Score                    1.000000
    Annual Income                   0.014844
    Years of Credit History         0.085461
    Months since last delinquent   -0.057957
    Number of Open Accounts        -0.038642
    Number of Credit Problems      -0.062030
    Current Credit Balance         -0.014965
    Bankruptcies                   -0.048236
    Tax Liens                      -0.027479
    Term_Short Term                 0.483576
    Home Ownership_Own Home        -0.013158
    Home Ownership_Rent            -0.048028
    Purpose_Buy House              -0.033435
    Purpose_Buy a Car               0.038942
    Purpose_Debt Consolidation      0.062105
    Purpose_Educational Expenses    0.008310
    Purpose_Home Improvements       0.018612
    Purpose_Medical Bills          -0.029543
    Purpose_Other                  -0.064317
    Purpose_Take a Trip            -0.009580
    Name: Credit Score, dtype: float64




```python
sns.scatterplot(x='Credit Score', y='Annual Income', data=df)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x11b7eb150>




![png](output_43_1.png)



```python
df.corr()['Annual Income']
```




    Loan Status                    -0.064451
    Years in current job            0.096976
    Monthly Debt                    0.471019
    Maximum Open Credit             0.031687
    Current Loan Amount             0.304788
    Credit Score                    0.014844
    Annual Income                   1.000000
    Years of Credit History         0.155115
    Months since last delinquent    0.018211
    Number of Open Accounts         0.145422
    Number of Credit Problems      -0.017196
    Current Credit Balance          0.305022
    Bankruptcies                   -0.047194
    Tax Liens                       0.036210
    Term_Short Term                -0.066624
    Home Ownership_Own Home        -0.037248
    Home Ownership_Rent            -0.158150
    Purpose_Buy House               0.008664
    Purpose_Buy a Car              -0.015555
    Purpose_Debt Consolidation     -0.034359
    Purpose_Educational Expenses   -0.009857
    Purpose_Home Improvements       0.076374
    Purpose_Medical Bills          -0.002762
    Purpose_Other                  -0.017304
    Purpose_Take a Trip            -0.011203
    Name: Annual Income, dtype: float64




```python
df.corr()['Loan Status']
```




    Loan Status                     1.000000
    Years in current job           -0.016711
    Monthly Debt                    0.014033
    Maximum Open Credit            -0.006031
    Current Loan Amount             0.078167
    Credit Score                   -0.245848
    Annual Income                  -0.064451
    Years of Credit History        -0.030149
    Months since last delinquent    0.000327
    Number of Open Accounts         0.017602
    Number of Credit Problems       0.009090
    Current Credit Balance         -0.007107
    Bankruptcies                   -0.000100
    Tax Liens                       0.010739
    Term_Short Term                -0.158569
    Home Ownership_Own Home         0.006862
    Home Ownership_Rent             0.052967
    Purpose_Buy House              -0.002251
    Purpose_Buy a Car              -0.019681
    Purpose_Debt Consolidation      0.001182
    Purpose_Educational Expenses   -0.000450
    Purpose_Home Improvements      -0.018178
    Purpose_Medical Bills           0.004362
    Purpose_Other                   0.003693
    Purpose_Take a Trip            -0.000357
    Name: Loan Status, dtype: float64




```python
# Take out Loan Status and Annual Income
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
X_train, X_test, y_train, y_test = train_test_split(filled.drop('Credit Score', axis=1), filled['Credit Score'], test_size=0.4, random_state=101)
```


```python
L = LinearRegression()
```


```python
L.fit(X_train, y_train)
```




    LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)




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
import matplotlib.pyplot as plt
```


```python
plt.scatter(y_test, predict)
```




    <matplotlib.collections.PathCollection at 0x12221ee10>




![png](output_56_1.png)



```python

```


```python
predictions = L.predict(missing.drop('Credit Score', axis=1))
```


```python
missing['Credit Score'] = predictions
df = pd.concat([missing, filled])
```

    /Applications/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:1: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      """Entry point for launching an IPython kernel.



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




    LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)




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

    /Applications/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:2: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      



```python
df = pd.concat([missing, filled])
```


```python
df['Loan Status'] = loan_status
```


```python
sns.countplot(x='Loan Status', data=df)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x122501190>




![png](output_68_1.png)



```python
df['Loan Status'].value_counts()
```




    0    176191
    1     39509
    Name: Loan Status, dtype: int64



## Imbalanced Data


Using undersampling to balance out the number of Loans that were paid off and unpai


```python
# Shuffle the Dataset.
shuffled_df = df.sample(frac=1,random_state=4)

# Put all the fraud class in a separate dataset.
fraud_df = shuffled_df.loc[shuffled_df['Loan Status'] == 1]

#Randomly select 492 observations from the non-fraud (majority class)
non_fraud_df = shuffled_df.loc[shuffled_df['Loan Status'] == 0].sample(n=39509,random_state=42)

# Concatenate both dataframes again
normalized_df = pd.concat([fraud_df, non_fraud_df])
```


```python
#plot the dataset after the undersampling
plt.figure(figsize=(8, 8))
sns.countplot('Loan Status', data=normalized_df)
plt.title('Balanced Classes')
plt.show()
```


![png](output_73_0.png)



```python
X = normalized_df.drop('Loan Status', axis=1)
y = normalized_df['Loan Status']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101, stratify=normalized_df['Loan Status'])
```


```python
from sklearn.linear_model import LogisticRegression
log = LogisticRegression()
```


```python
log.fit(X_train, y_train)
```

    /Applications/anaconda3/lib/python3.7/site-packages/sklearn/linear_model/logistic.py:432: FutureWarning: Default solver will be changed to 'lbfgs' in 0.22. Specify a solver to silence this warning.
      FutureWarning)





    LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
                       intercept_scaling=1, l1_ratio=None, max_iter=100,
                       multi_class='warn', n_jobs=None, penalty='l2',
                       random_state=None, solver='warn', tol=0.0001, verbose=0,
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
    


Based off the classification report, we scored about 60% accuracy that people will pay back their loans. 


```python
print(confusion_matrix(y_test, predictions))
```

    [[9495 6309]
     [6521 9283]]



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


![png](output_83_0.png)


## Conclusion

After seeing the feature importance based off of the column coefficients, the most important questions to ask future loan applicants are:
1. How much is their monthly debt?
2. What is their credit score?
3. How much is their current loan amount?
4. What is their annual income?


```python

```

# Business Objective
A delivery based company has daily, telementary data on it's fleet of devices and wants to save costs on maintenence. A predictive model will be design to determine the condition of the devices and when repairs should performed instead of routine or reactive repairs. Thus, saving the company costs in maintence and allowing devices to be kept in the field longer.


```python
import pandas as pd
import numpy as np
```


```python
df = pd.read_csv('1533148882_failures.csv')
```

## Looking at the data
The data given is in time series format with each column being a date and specific device ID. The other columns are not named and give nondescriptive information.


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
      <th>date</th>
      <th>device</th>
      <th>failure</th>
      <th>attribute1</th>
      <th>attribute2</th>
      <th>attribute3</th>
      <th>attribute4</th>
      <th>attribute5</th>
      <th>attribute6</th>
      <th>attribute7</th>
      <th>attribute8</th>
      <th>attribute9</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>2015-01-01</td>
      <td>S1F01085</td>
      <td>0</td>
      <td>215630672</td>
      <td>56</td>
      <td>0</td>
      <td>52</td>
      <td>6</td>
      <td>407438</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2015-01-01</td>
      <td>S1F0166B</td>
      <td>0</td>
      <td>61370680</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>6</td>
      <td>403174</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>2</td>
      <td>2015-01-01</td>
      <td>S1F01E6Y</td>
      <td>0</td>
      <td>173295968</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>12</td>
      <td>237394</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>3</td>
      <td>2015-01-01</td>
      <td>S1F01JE0</td>
      <td>0</td>
      <td>79694024</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>410186</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>4</td>
      <td>2015-01-01</td>
      <td>S1F01R2B</td>
      <td>0</td>
      <td>135970480</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>15</td>
      <td>313173</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.describe()
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
      <th>failure</th>
      <th>attribute1</th>
      <th>attribute2</th>
      <th>attribute3</th>
      <th>attribute4</th>
      <th>attribute5</th>
      <th>attribute6</th>
      <th>attribute7</th>
      <th>attribute8</th>
      <th>attribute9</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>count</td>
      <td>124494.000000</td>
      <td>1.244940e+05</td>
      <td>124494.000000</td>
      <td>124494.000000</td>
      <td>124494.000000</td>
      <td>124494.000000</td>
      <td>124494.000000</td>
      <td>124494.000000</td>
      <td>124494.000000</td>
      <td>124494.000000</td>
    </tr>
    <tr>
      <td>mean</td>
      <td>0.000851</td>
      <td>1.223868e+08</td>
      <td>159.484762</td>
      <td>9.940455</td>
      <td>1.741120</td>
      <td>14.222693</td>
      <td>260172.858025</td>
      <td>0.292528</td>
      <td>0.292528</td>
      <td>12.451524</td>
    </tr>
    <tr>
      <td>std</td>
      <td>0.029167</td>
      <td>7.045960e+07</td>
      <td>2179.657730</td>
      <td>185.747321</td>
      <td>22.908507</td>
      <td>15.943021</td>
      <td>99151.009852</td>
      <td>7.436924</td>
      <td>7.436924</td>
      <td>191.425623</td>
    </tr>
    <tr>
      <td>min</td>
      <td>0.000000</td>
      <td>0.000000e+00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>8.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <td>25%</td>
      <td>0.000000</td>
      <td>6.127675e+07</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>8.000000</td>
      <td>221452.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <td>50%</td>
      <td>0.000000</td>
      <td>1.227957e+08</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>10.000000</td>
      <td>249799.500000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <td>75%</td>
      <td>0.000000</td>
      <td>1.833084e+08</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>12.000000</td>
      <td>310266.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <td>max</td>
      <td>1.000000</td>
      <td>2.441405e+08</td>
      <td>64968.000000</td>
      <td>24929.000000</td>
      <td>1666.000000</td>
      <td>98.000000</td>
      <td>689161.000000</td>
      <td>832.000000</td>
      <td>832.000000</td>
      <td>18701.000000</td>
    </tr>
  </tbody>
</table>
</div>



### After reviewing histograms of each column:
- Attribute2, Attribute3, Attribute4, Attribute7, Attribute8, Attribute9 all seem to have a code with the majority of those values being 0. These columns will be updated to be either a 0 or 1.
- Attribute7 and Attribute8 have the same values. Attribute8 will be dropped.


```python
import matplotlib.pyplot as plt
%matplotlib inline
```


```python
n_bins = 10

fig, axes = plt.subplots(nrows=3, ncols=3)
fig.set_figheight(15)
fig.set_figwidth(15)
ax0, ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, = axes.flatten()

ax0.hist(df['attribute1'], n_bins, density=True, histtype='bar')
ax0.set_title('attribute1')

ax1.hist(df['attribute2'], n_bins, density=True, histtype='bar')
ax1.set_title('attribute2')

ax2.hist(df['attribute3'], n_bins, density=True, histtype='bar')
ax2.set_title('attribute3')

ax3.hist(df['attribute4'], n_bins, density=True, histtype='bar')
ax3.set_title('attribute4')

ax4.hist(df['attribute5'], n_bins, density=True, histtype='bar')
ax4.set_title('attribute5')

ax5.hist(df['attribute6'], n_bins, density=True, histtype='bar')
ax5.set_title('attribute6')

ax6.hist(df['attribute7'], n_bins, density=True, histtype='bar')
ax6.set_title('attribute7')

ax7.hist(df['attribute8'], n_bins, density=True, histtype='bar')
ax7.set_title('attribute8')

ax8.hist(df['attribute9'], n_bins, density=True, histtype='bar')
ax8.set_title('attribute9')

fig.tight_layout()
plt.show()
```


![png](output_8_0.png)


### Target Column


```python
df['failure'].value_counts()
```




    0    124388
    1       106
    Name: failure, dtype: int64




```python
import seaborn as sns
sns.set(style="whitegrid")
plt.figure(figsize=(8, 8))
sns.countplot('failure', data=df)
plt.title('Failure Count')
plt.show()
```


![png](output_11_0.png)


### Due to the highly imbalanced data, using an oversampling of the devices that have failure will help the predictive model. The oversampling will occur after the test, train and split process.


```python
df.drop(columns=['attribute8'], inplace=True)
```


```python
# drop the duplicate rows that are entirely the same
df.drop_duplicates(keep='first', inplace=True)
```


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 124494 entries, 0 to 124493
    Data columns (total 11 columns):
    date          124494 non-null object
    device        124494 non-null object
    failure       124494 non-null int64
    attribute1    124494 non-null int64
    attribute2    124494 non-null int64
    attribute3    124494 non-null int64
    attribute4    124494 non-null int64
    attribute5    124494 non-null int64
    attribute6    124494 non-null int64
    attribute7    124494 non-null int64
    attribute9    124494 non-null int64
    dtypes: int64(9), object(2)
    memory usage: 11.4+ MB


### Extracting Information from the Date
By creating columns for day of week, day of the month, months and seasons will give better idea of when devices fail and the kind of data that was given.


```python
from datetime import datetime
from datetime import date

date = df['date']
df['date'] = pd.to_datetime(date)

# Get day of the week 
df['day_of_week'] = df['date'].dt.day_name()

# Get season
df['season'] = df['date'].apply(lambda dt: (dt.month%12 + 3)//3)

# Name seasons
season_dict = {1 : 'winter', 2: 'spring', 3: 'summer', 4: 'fall'}
df['season'] = df['season'].map(season_dict)

# Get month
df['month'] = df['date'].dt.month 
```


```python
df['month'].value_counts()
```




    1     25032
    3     19833
    2     19500
    4     12012
    5     11330
    7     10531
    6     10469
    8      8346
    9      4470
    10     2940
    11       31
    Name: month, dtype: int64



- Notice the number of data points decreases by each month and December not having any observations.


```python
import matplotlib.pyplot as plt
%matplotlib inline

import seaborn as sns
sns.set(style="whitegrid")
```


```python
df_fail = df.loc[(df['failure']==1)]
```


```python
import seaborn as sns
sns.set(style="whitegrid")
g = sns.catplot(x="season", y="failure", data=df,
                height=6, kind="bar", palette="muted").set(title = "Rate of Failure by Season")
```


![png](output_22_0.png)



```python
season =  sns.countplot(x="season", data=df_fail).set(title = "Number of Failures by Season")
```


![png](output_23_0.png)



```python
g = sns.catplot(x="month", y="failure", data=df,
                height=6, kind="bar", palette="muted").set(title = "Rate of Failure by Month")
```


![png](output_24_0.png)



```python
month = sns.countplot(x='month', data=df_fail).set(title = "Number of Failures by Month")
```


![png](output_25_0.png)



```python
plt.figure(figsize=(20,5))
ax = sns.lineplot(x="date", y="failure", data=df).set(title = "Mean Failures by Month")
```

    /Applications/anaconda3/lib/python3.7/site-packages/pandas/plotting/_matplotlib/converter.py:103: FutureWarning: Using an implicitly registered datetime converter for a matplotlib plotting method. The converter was registered by pandas on import. Future versions of pandas will require you to explicitly register matplotlib converters.
    
    To register the converters:
    	>>> from pandas.plotting import register_matplotlib_converters
    	>>> register_matplotlib_converters()
      warnings.warn(msg, FutureWarning)



![png](output_26_1.png)



```python
# Groupby Day of the week by failures
df.groupby(['day_of_week'])['failure'].value_counts()
```




    day_of_week  failure
    Friday       0          18029
                 1             12
    Monday       0          17859
                 1             27
    Saturday     0          17889
                 1              8
    Sunday       0          17855
                 1              4
    Thursday     0          18119
                 1             22
    Tuesday      0          17516
                 1             18
    Wednesday    0          17121
                 1             15
    Name: failure, dtype: int64




```python
df_fail['day_of_week'].value_counts()
```




    Monday       27
    Thursday     22
    Tuesday      18
    Wednesday    15
    Friday       12
    Saturday      8
    Sunday        4
    Name: day_of_week, dtype: int64




```python
order = ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
```


```python
day = sns.countplot(x='day_of_week', data=df_fail, order=order).set(title = "Number of Failures by Day of week")
```


![png](output_30_0.png)



```python
g = sns.catplot(x='day_of_week', y="failure", data=df,
                height=6, kind="bar", palette="muted", order=order).set(title = "Rate of Failure by Day of Week")
```


![png](output_31_0.png)



```python
# Groupby Season by failures
df.groupby(['season'])['failure'].value_counts()
```




    season  failure
    fall    0           7438
            1              3
    spring  0          43136
            1             39
    summer  0          29320
            1             26
    winter  0          44494
            1             38
    Name: failure, dtype: int64




```python
df['day'] = df['date'].dt.day
```


```python
df['day'].value_counts()
```




    1     4742
    2     4742
    5     4706
    4     4705
    3     4677
    6     4641
    7     4345
    8     4263
    9     4263
    10    4262
    11    4261
    12    4217
    13    4154
    14    4110
    15    4076
    16    4076
    17    4033
    18    3989
    19    3981
    20    3939
    21    3894
    22    3893
    23    3850
    24    3812
    25    3806
    26    3728
    27    3726
    28    3622
    29    2948
    30    2945
    31    2088
    Name: day, dtype: int64




```python
plt.figure(figsize=(20,5))
ax = sns.lineplot(x="day", y="failure", data=df).set(title = "Rate of Failure by day of the Month")
```


![png](output_35_0.png)


### Changing columns to either 0 or 1


```python
df['attribute2'] = np.where(df['attribute2'] > 0, 1, df['attribute2'])
df['attribute3'] = np.where(df['attribute3'] > 0, 1, df['attribute3'])
df['attribute4'] = np.where(df['attribute4'] > 0, 1, df['attribute4'])
df['attribute7'] = np.where(df['attribute7'] > 0, 1, df['attribute7'])
df['attribute9'] = np.where(df['attribute9'] > 0, 1, df['attribute9'])
```


```python
failed_devices = df[df['failure'] == 1]
working_devices = df[df['failure'] == 0]
```


```python
dummies = pd.get_dummies(df[['day_of_week', 'season']], drop_first=True)
df.drop(df[['day_of_week', 'season', 'date']], axis=1, inplace=True)
df = pd.concat([df, dummies], axis=1)
```


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 124494 entries, 0 to 124493
    Data columns (total 21 columns):
    device                   124494 non-null object
    failure                  124494 non-null int64
    attribute1               124494 non-null int64
    attribute2               124494 non-null int64
    attribute3               124494 non-null int64
    attribute4               124494 non-null int64
    attribute5               124494 non-null int64
    attribute6               124494 non-null int64
    attribute7               124494 non-null int64
    attribute9               124494 non-null int64
    month                    124494 non-null int64
    day                      124494 non-null int64
    day_of_week_Monday       124494 non-null uint8
    day_of_week_Saturday     124494 non-null uint8
    day_of_week_Sunday       124494 non-null uint8
    day_of_week_Thursday     124494 non-null uint8
    day_of_week_Tuesday      124494 non-null uint8
    day_of_week_Wednesday    124494 non-null uint8
    season_spring            124494 non-null uint8
    season_summer            124494 non-null uint8
    season_winter            124494 non-null uint8
    dtypes: int64(11), object(1), uint8(9)
    memory usage: 18.4+ MB



```python
df.describe()
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
      <th>failure</th>
      <th>attribute1</th>
      <th>attribute2</th>
      <th>attribute3</th>
      <th>attribute4</th>
      <th>attribute5</th>
      <th>attribute6</th>
      <th>attribute7</th>
      <th>attribute9</th>
      <th>month</th>
      <th>day</th>
      <th>day_of_week_Monday</th>
      <th>day_of_week_Saturday</th>
      <th>day_of_week_Sunday</th>
      <th>day_of_week_Thursday</th>
      <th>day_of_week_Tuesday</th>
      <th>day_of_week_Wednesday</th>
      <th>season_spring</th>
      <th>season_summer</th>
      <th>season_winter</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>count</td>
      <td>124494.000000</td>
      <td>1.244940e+05</td>
      <td>124494.000000</td>
      <td>124494.000000</td>
      <td>124494.000000</td>
      <td>124494.000000</td>
      <td>124494.000000</td>
      <td>124494.000000</td>
      <td>124494.000000</td>
      <td>124494.000000</td>
      <td>124494.000000</td>
      <td>124494.000000</td>
      <td>124494.000000</td>
      <td>124494.000000</td>
      <td>124494.000000</td>
      <td>124494.000000</td>
      <td>124494.000000</td>
      <td>124494.000000</td>
      <td>124494.000000</td>
      <td>124494.000000</td>
    </tr>
    <tr>
      <td>mean</td>
      <td>0.000851</td>
      <td>1.223868e+08</td>
      <td>0.051280</td>
      <td>0.073377</td>
      <td>0.075008</td>
      <td>14.222693</td>
      <td>260172.858025</td>
      <td>0.011711</td>
      <td>0.217970</td>
      <td>4.028299</td>
      <td>14.894196</td>
      <td>0.143670</td>
      <td>0.143758</td>
      <td>0.143453</td>
      <td>0.145718</td>
      <td>0.140842</td>
      <td>0.137645</td>
      <td>0.346804</td>
      <td>0.235722</td>
      <td>0.357704</td>
    </tr>
    <tr>
      <td>std</td>
      <td>0.029167</td>
      <td>7.045960e+07</td>
      <td>0.220568</td>
      <td>0.260755</td>
      <td>0.263405</td>
      <td>15.943021</td>
      <td>99151.009852</td>
      <td>0.107584</td>
      <td>0.412869</td>
      <td>2.572167</td>
      <td>8.759542</td>
      <td>0.350756</td>
      <td>0.350846</td>
      <td>0.350535</td>
      <td>0.352825</td>
      <td>0.347860</td>
      <td>0.344529</td>
      <td>0.475955</td>
      <td>0.424451</td>
      <td>0.479326</td>
    </tr>
    <tr>
      <td>min</td>
      <td>0.000000</td>
      <td>0.000000e+00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>8.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <td>25%</td>
      <td>0.000000</td>
      <td>6.127675e+07</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>8.000000</td>
      <td>221452.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>2.000000</td>
      <td>7.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <td>50%</td>
      <td>0.000000</td>
      <td>1.227957e+08</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>10.000000</td>
      <td>249799.500000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>3.000000</td>
      <td>15.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <td>75%</td>
      <td>0.000000</td>
      <td>1.833084e+08</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>12.000000</td>
      <td>310266.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>6.000000</td>
      <td>22.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <td>max</td>
      <td>1.000000</td>
      <td>2.441405e+08</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>98.000000</td>
      <td>689161.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>11.000000</td>
      <td>31.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.columns
```




    Index(['device', 'failure', 'attribute1', 'attribute2', 'attribute3',
           'attribute4', 'attribute5', 'attribute6', 'attribute7', 'attribute9',
           'month', 'day', 'day_of_week_Monday', 'day_of_week_Saturday',
           'day_of_week_Sunday', 'day_of_week_Thursday', 'day_of_week_Tuesday',
           'day_of_week_Wednesday', 'season_spring', 'season_summer',
           'season_winter'],
          dtype='object')




```python
device_group = df.groupby('device').agg({'failure': 'sum', 'attribute1' : 'mean', 'attribute2': 'max',
                                           'attribute3': 'max', 'attribute4': 'max', 'attribute5': 'mean',
                                           'attribute6': 'mean', 'attribute7': 'max', 'attribute9': 'max',
                                        'month': 'max', 'day': 'max', 'day_of_week_Monday': 'max', 'day_of_week_Saturday': 'max',
                                        'day_of_week_Sunday' : 'max', 'day_of_week_Thursday': 'max', 'day_of_week_Tuesday': 'max',
                                        'day_of_week_Wednesday': 'max', 'season_spring': 'max', 'season_summer': 'max',
                                        'season_winter': 'max'})

device_columns = ['failure', 'attribute1', 'attribute2', 'attribute3',
                   'attribute4', 'attribute5', 'attribute6', 'attribute7', 'attribute9',
                   'month', 'day', 'day_of_week_Monday', 'day_of_week_Saturday',
                   'day_of_week_Sunday', 'day_of_week_Thursday', 'day_of_week_Tuesday',
                   'day_of_week_Wednesday', 'season_spring', 'season_summer',
                   'season_winter']

device_group = pd.DataFrame(device_group, index = device_group.index)
device_group.columns = device_columns

#Creating the sent_after_failure column
sent_after_failure = ['S1F0GPFZ', 'S1F136J0', 'W1F0KCP2', 'W1F0M35B', 'W1F11ZG9']

device_group['sent_after_failure'] = 0
device_group.loc[sent_after_failure, 'sent_after_failure'] = 1
```


```python
device_group['failure'].value_counts()
```




    0    1062
    1     106
    Name: failure, dtype: int64




```python
device_group.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Index: 1168 entries, S1F01085 to Z1F2PBHX
    Data columns (total 21 columns):
    failure                  1168 non-null int64
    attribute1               1168 non-null float64
    attribute2               1168 non-null int64
    attribute3               1168 non-null int64
    attribute4               1168 non-null int64
    attribute5               1168 non-null float64
    attribute6               1168 non-null float64
    attribute7               1168 non-null int64
    attribute9               1168 non-null int64
    month                    1168 non-null int64
    day                      1168 non-null int64
    day_of_week_Monday       1168 non-null uint8
    day_of_week_Saturday     1168 non-null uint8
    day_of_week_Sunday       1168 non-null uint8
    day_of_week_Thursday     1168 non-null uint8
    day_of_week_Tuesday      1168 non-null uint8
    day_of_week_Wednesday    1168 non-null uint8
    season_spring            1168 non-null uint8
    season_summer            1168 non-null uint8
    season_winter            1168 non-null uint8
    sent_after_failure       1168 non-null int64
    dtypes: float64(3), int64(9), uint8(9)
    memory usage: 168.9+ KB



```python
myBasicCorr = device_group.corr()
fig, ax = plt.subplots(figsize=(10,10)) 
sns.heatmap(myBasicCorr, ax= ax)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x1a1ff3bcd0>




![png](output_46_1.png)



```python
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
```


```python
X_train, X_test, y_train, y_test = train_test_split(device_group.drop('failure', axis=1), device_group['failure'], 
                                                    test_size=0.4, random_state=42, stratify=device_group['failure'])
```

## SMOTE over sampling 


```python
from imblearn.over_sampling import SMOTE
sm = SMOTE(sampling_strategy='auto', random_state=42)
x_train_res, y_train_res = sm.fit_sample(X_train, y_train)
```


```python
y_train_res.value_counts()
```




    1    636
    0    636
    Name: failure, dtype: int64




```python
np.bincount(y_train_res)
```




    array([636, 636])




```python
from sklearn.ensemble import GradientBoostingClassifier
gbc = GradientBoostingClassifier()
```


```python
gbc.fit(x_train_res, y_train_res)
```




    GradientBoostingClassifier(ccp_alpha=0.0, criterion='friedman_mse', init=None,
                               learning_rate=0.1, loss='deviance', max_depth=3,
                               max_features=None, max_leaf_nodes=None,
                               min_impurity_decrease=0.0, min_impurity_split=None,
                               min_samples_leaf=1, min_samples_split=2,
                               min_weight_fraction_leaf=0.0, n_estimators=100,
                               n_iter_no_change=None, presort='deprecated',
                               random_state=None, subsample=1.0, tol=0.0001,
                               validation_fraction=0.1, verbose=0,
                               warm_start=False)




```python
y_pred = gbc.predict(X_test)
print(classification_report(y_test, y_pred))
```

                  precision    recall  f1-score   support
    
               0       0.97      0.97      0.97       426
               1       0.70      0.74      0.72        42
    
        accuracy                           0.95       468
       macro avg       0.84      0.85      0.85       468
    weighted avg       0.95      0.95      0.95       468
    


## Conclusion

Looking at the classification report, with the recall as the most important metric to accurately predict which devices will fail about 74% on the next trip. The model will help to increase the company's ability to save money on preventative maintenance  the amount of time devices are out in the field.

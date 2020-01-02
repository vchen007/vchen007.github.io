# Business Objective
1. Data set of Loans and if they were paid or defaulted. 
2. Look for the Customers who have paid and predict if future customers will pay back or default loan.
3. Come up with questions for customer when they are applying for loan


```python
import pandas as pd
```


```python
df = pd.read_csv('1533148983_LoansTrainingSet.csv')
```

    /Applications/anaconda3/lib/python3.7/site-packages/IPython/core/interactiveshell.py:3058: DtypeWarning: Columns (16) have mixed types. Specify dtype option on import or set low_memory=False.
      interactivity=interactivity, compiler=compiler, result=result)



```python
import pandas_profiling
```


```python
pandas_profiling.ProfileReport(df)
```




<meta charset="UTF-8">

<style>

        .variablerow {
            border: 1px solid #e1e1e8;
            border-top: hidden;
            padding-top: 2em;
            padding-bottom: 2em;
            padding-left: 1em;
            padding-right: 1em;
        }

        .headerrow {
            border: 1px solid #e1e1e8;
            background-color: #f5f5f5;
            padding: 2em;
        }
        .namecol {
            margin-top: -1em;
            overflow-x: auto;
        }

        .dl-horizontal dt {
            text-align: left;
            padding-right: 1em;
            white-space: normal;
        }

        .dl-horizontal dd {
            margin-left: 0;
        }

        .ignore {
            opacity: 0.4;
        }

        .container.pandas-profiling {
            max-width:975px;
        }

        .col-md-12 {
            padding-left: 2em;
        }

        .indent {
            margin-left: 1em;
        }

        .center-img {
            margin-left: auto !important;
            margin-right: auto !important;
            display: block;
        }

        /* Table example_values */
            table.example_values {
                border: 0;
            }

            .example_values th {
                border: 0;
                padding: 0 ;
                color: #555;
                font-weight: 600;
            }

            .example_values tr, .example_values td{
                border: 0;
                padding: 0;
                color: #555;
            }

        /* STATS */
            table.stats {
                border: 0;
            }

            .stats th {
                border: 0;
                padding: 0 2em 0 0;
                color: #555;
                font-weight: 600;
            }

            .stats tr {
                border: 0;
            }

            .stats td{
                color: #555;
                padding: 1px;
                border: 0;
            }


        /* Sample table */
            table.sample {
                border: 0;
                margin-bottom: 2em;
                margin-left:1em;
            }
            .sample tr {
                border:0;
            }
            .sample td, .sample th{
                padding: 0.5em;
                white-space: nowrap;
                border: none;

            }

            .sample thead {
                border-top: 0;
                border-bottom: 2px solid #ddd;
            }

            .sample td {
                width:100%;
            }


        /* There is no good solution available to make the divs equal height and then center ... */
            .histogram {
                margin-top: 3em;
            }
        /* Freq table */

            table.freq {
                margin-bottom: 2em;
                border: 0;
            }
            table.freq th, table.freq tr, table.freq td {
                border: 0;
                padding: 0;
            }

            .freq thead {
                font-weight: 600;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;

            }

            td.fillremaining{
                width:auto;
                max-width: none;
            }

            td.number, th.number {
                text-align:right ;
            }

        /* Freq mini */
            .freq.mini td{
                width: 50%;
                padding: 1px;
                font-size: 12px;

            }
            table.freq.mini {
                 width:100%;
            }
            .freq.mini th {
                overflow: hidden;
                text-overflow: ellipsis;
                white-space: nowrap;
                max-width: 5em;
                font-weight: 400;
                text-align:right;
                padding-right: 0.5em;
            }

            .missing {
                color: #a94442;
            }
            .alert, .alert > th, .alert > td {
                color: #a94442;
            }


        /* Bars in tables */
            .freq .bar{
                float: left;
                width: 0;
                height: 100%;
                line-height: 20px;
                color: #fff;
                text-align: center;
                background-color: #337ab7;
                border-radius: 3px;
                margin-right: 4px;
            }
            .other .bar {
                background-color: #999;
            }
            .missing .bar{
                background-color: #a94442;
            }
            .tooltip-inner {
                width: 100%;
                white-space: nowrap;
                text-align:left;
            }

            .extrapadding{
                padding: 2em;
            }

            .pp-anchor{

            }

</style>

<div class="container pandas-profiling">
    <div class="row headerrow highlight">
        <h1>Overview</h1>
    </div>
    <div class="row variablerow">
    <div class="col-md-6 namecol">
        <p class="h4">Dataset info</p>
        <table class="stats" style="margin-left: 1em;">
            <tbody>
            <tr>
                <th>Number of variables</th>
                <td>19 </td>
            </tr>
            <tr>
                <th>Number of observations</th>
                <td>256984 </td>
            </tr>
            <tr>
                <th>Total Missing (%)</th>
                <td>5.6% </td>
            </tr>
            <tr>
                <th>Total size in memory</th>
                <td>37.3 MiB </td>
            </tr>
            <tr>
                <th>Average record size in memory</th>
                <td>152.0 B </td>
            </tr>
            </tbody>
        </table>
    </div>
    <div class="col-md-6 namecol">
        <p class="h4">Variables types</p>
        <table class="stats" style="margin-left: 1em;">
            <tbody>
            <tr>
                <th>Numeric</th>
                <td>10 </td>
            </tr>
            <tr>
                <th>Categorical</th>
                <td>9 </td>
            </tr>
            <tr>
                <th>Boolean</th>
                <td>0 </td>
            </tr>
            <tr>
                <th>Date</th>
                <td>0 </td>
            </tr>
            <tr>
                <th>Text (Unique)</th>
                <td>0 </td>
            </tr>
            <tr>
                <th>Rejected</th>
                <td>0 </td>
            </tr>
            <tr>
                <th>Unsupported</th>
                <td>0 </td>
            </tr>
            </tbody>
        </table>
    </div>
    <div class="col-md-12" style="padding-left: 1em;">

        <p class="h4">Warnings</p>
        <ul class="list-unstyled"><li><a href="#pp_var_Annual Income"><code>Annual Income</code></a> is highly skewed (γ1 = 50.982)  <span class="label label-info">Skewed</span></li><li><a href="#pp_var_Annual Income"><code>Annual Income</code></a> has 61676 / 24.0% missing values <span class="label label-default">Missing</span></li><li><a href="#pp_var_Bankruptcies"><code>Bankruptcies</code></a> has 229661 / 89.4% zeros <span class="label label-info">Zeros</span></li><li><a href="#pp_var_Credit Score"><code>Credit Score</code></a> has 61676 / 24.0% missing values <span class="label label-default">Missing</span></li><li><a href="#pp_var_Customer ID"><code>Customer ID</code></a> has a high cardinality: 215700 distinct values  <span class="label label-warning">Warning</span></li><li><a href="#pp_var_Loan ID"><code>Loan ID</code></a> has a high cardinality: 215700 distinct values  <span class="label label-warning">Warning</span></li><li><a href="#pp_var_Maximum Open Credit"><code>Maximum Open Credit</code></a> has a high cardinality: 87188 distinct values  <span class="label label-warning">Warning</span></li><li><a href="#pp_var_Monthly Debt"><code>Monthly Debt</code></a> has a high cardinality: 129115 distinct values  <span class="label label-warning">Warning</span></li><li><a href="#pp_var_Months since last delinquent"><code>Months since last delinquent</code></a> has 140383 / 54.6% missing values <span class="label label-default">Missing</span></li><li><a href="#pp_var_Number of Credit Problems"><code>Number of Credit Problems</code></a> has 223171 / 86.8% zeros <span class="label label-info">Zeros</span></li><li><a href="#pp_var_Tax Liens"><code>Tax Liens</code></a> has 252322 / 98.2% zeros <span class="label label-info">Zeros</span></li><li><a href="#pp_var_Years in current job"><code>Years in current job</code></a> has 11476 / 4.5% missing values <span class="label label-default">Missing</span></li><li>Dataset has 16610 duplicate rows <span class="label label-warning">Warning</span></li> </ul>
    </div>
</div>
    <div class="row headerrow highlight">
        <h1>Variables</h1>
    </div>
    <div class="row variablerow">
    <div class="col-md-3 namecol">
        <p class="h4 pp-anchor" id="pp_var_Annual Income">Annual Income<br/>
            <small>Numeric</small>
        </p>
    </div><div class="col-md-6">
    <div class="row">
        <div class="col-sm-6">
            <table class="stats ">
                <tr>
                    <th>Distinct count</th>
                    <td>60559</td>
                </tr>
                <tr>
                    <th>Unique (%)</th>
                    <td>23.6%</td>
                </tr>
                <tr class="alert">
                    <th>Missing (%)</th>
                    <td>24.0%</td>
                </tr>
                <tr class="alert">
                    <th>Missing (n)</th>
                    <td>61676</td>
                </tr>
                <tr class="ignore">
                    <th>Infinite (%)</th>
                    <td>0.0%</td>
                </tr>
                <tr class="ignore">
                    <th>Infinite (n)</th>
                    <td>0</td>
                </tr>
            </table>

        </div>
        <div class="col-sm-6">
            <table class="stats ">

                <tr>
                    <th>Mean</th>
                    <td>71953</td>
                </tr>
                <tr>
                    <th>Minimum</th>
                    <td>0</td>
                </tr>
                <tr>
                    <th>Maximum</th>
                    <td>8713500</td>
                </tr>
                <tr class="ignore">
                    <th>Zeros (%)</th>
                    <td>0.0%</td>
                </tr>
            </table>
        </div>
    </div>
</div>
<div class="col-md-3 collapse in" id="minihistogram8569089068023125674">
    <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAABLCAYAAAA1fMjoAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAPYQAAD2EBqD%2BnaQAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAArhJREFUeJzt2jtLY1EYheHlmEKx9tJoqZ2iBPwBYhiIjRC0Cf4FUSyE6YQpbELaNIKFIDaCFxg7EZEjTNLaimITxNLG6DddmIxhoZCLDO8DKXKyT/I1L3sHTk9EhAA09a3bAwBfWarbA/wr/ePXp%2B/5/fN7GyYB2EEAi0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAg0AAoyciottDAF8VOwhgEAhgEAhgEAja4unpSfPz87q%2Bvv7Q%2Bmw2q%2Bnp6YbXxMSESqVSmyf1Ul39dfyXyuWyNjc3dXd39%2BF7Tk9PG94Xi0Wdn58rn8%2B3erxPYQdBSx0eHmpjY0Nra2vvPru6ulIul1M6nVY2m9XR0VHT70iSRLu7uyoWixoYGGj3yF4ALVStVuPl5SUiIsbHxyNJkoiIuLm5icnJyTg7O4tarRblcjlmZ2fj4uKi4f5arRaZTCZKpVLHZ2%2BGHQQtNTg4qFTq/cl9f39fc3NzymQy6u3t1czMjJaWlrS3t9ew7vj4WM/Pz1pZWenUyBb/QdARDw8PSpJE6XS6fu319VVjY2MN6w4ODrS8vKy%2Bvr5Oj9gUgaAjRkZGtLi4qK2trfq1arWq%2BOtBjsfHR1UqFW1vb3djxKY4YqEjcrmcTk5OdHl5qbe3N93e3iqfz2tnZ6e%2BplKpaGhoSKOjo12ctBE7CDpiampKhUJBhUJBq6ur6u/v18LCgtbX1%2Btr7u/vNTw83MUp3%2BNhRcDgiAUYBAIYBAIYBAIYBAIYBAIYBAIYBAIYBAIYBAIYBAIYBAIYfwC5Yo0qLjuR8AAAAABJRU5ErkJggg%3D%3D">

</div>
<div class="col-md-12 text-right">
    <a role="button" data-toggle="collapse" data-target="#descriptives8569089068023125674,#minihistogram8569089068023125674"
       aria-expanded="false" aria-controls="collapseExample">
        Toggle details
    </a>
</div>
<div class="row collapse col-md-12" id="descriptives8569089068023125674">
    <ul class="nav nav-tabs" role="tablist">
        <li role="presentation" class="active"><a href="#quantiles8569089068023125674"
                                                  aria-controls="quantiles8569089068023125674" role="tab"
                                                  data-toggle="tab">Statistics</a></li>
        <li role="presentation"><a href="#histogram8569089068023125674" aria-controls="histogram8569089068023125674"
                                   role="tab" data-toggle="tab">Histogram</a></li>
        <li role="presentation"><a href="#common8569089068023125674" aria-controls="common8569089068023125674"
                                   role="tab" data-toggle="tab">Common Values</a></li>
        <li role="presentation"><a href="#extreme8569089068023125674" aria-controls="extreme8569089068023125674"
                                   role="tab" data-toggle="tab">Extreme Values</a></li>

    </ul>

    <div class="tab-content">
        <div role="tabpanel" class="tab-pane active row" id="quantiles8569089068023125674">
            <div class="col-md-4 col-md-offset-1">
                <p class="h4">Quantile statistics</p>
                <table class="stats indent">
                    <tr>
                        <th>Minimum</th>
                        <td>0</td>
                    </tr>
                    <tr>
                        <th>5-th percentile</th>
                        <td>27342</td>
                    </tr>
                    <tr>
                        <th>Q1</th>
                        <td>44321</td>
                    </tr>
                    <tr>
                        <th>Median</th>
                        <td>61242</td>
                    </tr>
                    <tr>
                        <th>Q3</th>
                        <td>86462</td>
                    </tr>
                    <tr>
                        <th>95-th percentile</th>
                        <td>147080</td>
                    </tr>
                    <tr>
                        <th>Maximum</th>
                        <td>8713500</td>
                    </tr>
                    <tr>
                        <th>Range</th>
                        <td>8713500</td>
                    </tr>
                    <tr>
                        <th>Interquartile range</th>
                        <td>42141</td>
                    </tr>
                </table>
            </div>
            <div class="col-md-4 col-md-offset-2">
                <p class="h4">Descriptive statistics</p>
                <table class="stats indent">
                    <tr>
                        <th>Standard deviation</th>
                        <td>58878</td>
                    </tr>
                    <tr>
                        <th>Coef of variation</th>
                        <td>0.81828</td>
                    </tr>
                    <tr>
                        <th>Kurtosis</th>
                        <td>6603.2</td>
                    </tr>
                    <tr>
                        <th>Mean</th>
                        <td>71953</td>
                    </tr>
                    <tr>
                        <th>MAD</th>
                        <td>29995</td>
                    </tr>
                    <tr class="alert">
                        <th>Skewness</th>
                        <td>50.982</td>
                    </tr>
                    <tr>
                        <th>Sum</th>
                        <td>14053000000</td>
                    </tr>
                    <tr>
                        <th>Variance</th>
                        <td>3466600000</td>
                    </tr>
                    <tr>
                        <th>Memory size</th>
                        <td>2.0 MiB</td>
                    </tr>
                </table>
            </div>
        </div>
        <div role="tabpanel" class="tab-pane col-md-8 col-md-offset-2" id="histogram8569089068023125674">
            <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAlgAAAGQCAYAAAByNR6YAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAPYQAAD2EBqD%2BnaQAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAIABJREFUeJzt3X1cVHX%2B//%2BnMCADXjCpaPWxZBFqVRQCxat1V5RcL1BDjTYz21JvCYlYarlaGi6aH8nKXC3dzDK%2Bm2laWV7VrqnrFpBZWRsJJmqrCSoqDrByMb8/%2BjGfnbDlogMzA4/77Ta3bd7v9znndeaFe3vOnMPQwmaz2QQAAADDeDi7AAAAgKaGgAUAAGAwAhYAAIDBCFgAAAAGI2ABAAAYjIAFAABgMAIWAACAwQhYAAAABiNgAQAAGIyABQAAYDACFgAAgMEIWAAAAAYjYAEAABiMgAUAAGAwAhYAAIDBCFgAAAAGI2ABAAAYjIAFAABgMAIWAACAwQhYAAAABiNgAQAAGIyABQAAYDACFgAAgMEIWAAAAAYjYAEAABiMgAUAAGAwAhYAAIDBCFgAAAAGI2ABAAAYjIAFAABgMAIWAACAwQhYAAAABiNgAQAAGIyABQAAYDACFgAAgMEIWAAAAAYjYAEAABiMgAUAAGAwAhYAAIDBTM4uoLkoKCgyfJ8eHi103XV%2BunDBqspKm%2BH7R93QD9dCP1wL/XAtzakfHTq0dspx%2BQTLjXl4tFCLFi3k4dHC2aVA9MPV0A/XQj9cC/1oeAQsAAAAgzktYGVnZ%2Bv3v/%2B9%2BvTpowEDBmju3Lm6cOGCJOnzzz/XhAkTFB4erujoaG3evNlh223btikmJkZhYWGKi4vT4cOH7XMVFRVatmyZ%2Bvfvr/DwcE2fPl35%2Bfn2%2BfPnzyshIUGRkZGKiopSamqqysvL7fM1HRsAAKAmTglYpaWlmjJlisLDw/X3v/9d7777ri5evKg//OEPunTpkqZNm6axY8cqKytLqampWrp0qb744gtJUkZGhhYvXqynnnpKWVlZGj16tKZPn66SkhJJ0po1a3Tw4EG9%2BeabOnDggHx8fLRgwQL7sZOTk%2BXr66sDBw5oy5Yt%2Buijj7RhwwZJqvHYAAAAteGUgHX69GndeuutSkxMlLe3tywWi%2BLj45WVlaU9e/bI399fEydOlMlkUr9%2B/RQbG6v09HRJ0ubNmzVy5EhFRETIy8tL9913nywWi3bs2GGfnzp1qq6//nq1atVK8%2BfP1/79%2B3Xq1CmdOHFCmZmZmjNnjsxmszp37qyEhAT7vms6NgAAQG04JWD94he/0J///Gd5enrax3bv3q3u3bsrJydHISEhDuu7du2q7OxsSVJubu5PzhcVFen77793mG/fvr3atm2rb775Rjk5OfL391fHjh3t80FBQTp9%2BrQuX75c47EBAABqw%2Blf02Cz2fTss89q7969eu211/Tqq6/KbDY7rPHx8VFxcbEkyWq1/uS81WqVJPn6%2Blabr5r78bZVz6u2/2/Hrq38/HwVFBQ4jJlMvgoICKjTfmri6enh8L9wLvrhWuiHa6EfroV%2BNDynBqwrV65o3rx5%2Buqrr/Taa6/plltukdlsVlGR43dGlZaWys/PT9IPgai0tLTavMVisYejqvuxfry9zWarNlf13M/Pr8Zj19amTZu0atUqh7HExEQlJSXVaT%2B11aaNueZFaDT0w7XQD9dCP1wL/Wg4TgtYJ0%2Be1NSpU3XDDTdoy5Ytuu666yRJISEhOnjwoMPa3NxcBQcHS5KCg4OVk5NTbX7QoEFq27atOnbs6HAZsaCgQBcvXlRISIgqKyt18eJFnTt3Tu3bt5ckHTt2TJ06dVLr1q1rPHZtxcfHKzo62mHMZPJVYaG1Tvupiaenh9q0Mevy5RJVVFQaum/UHf1wLfTDtdAP19Kc%2BmGx1O1DEqM4JWBdunRJkydPVt%2B%2BfZWamioPj//7iDImJkbLly/Xhg0bNHHiRB06dEjbt2/X6tWrJUnjx49XYmKihg8froiICKWnp%2Bv8%2BfOKiYmRJMXFxWnNmjUKDQ2VxWLRkiVL1KdPH910002SpIiICC1ZskQpKSkqLCzU6tWrNX78%2BFodu7YCAgKqXQ4sKChSeXnD/BBXVFQ22L5Rd/TDtdAP10I/XAv9aDgtbDZbo39H/ssvv6ynnnpKZrNZLVo4fovs4cOHdeTIEaWmpuro0aO67rrrlJCQoLi4OPuat99%2BW2vWrNHZs2fVtWtXLViwQL169ZIklZWV6bnnntM777wjq9WqqKgoLV68WO3atZMknTt3TikpKcrIyJCHh4fGjh2r2bNn22%2B4r%2BnY9dUQfyrHZPKQxeKnwkIr/0BcAP1wLfTDtdAP19Kc%2BuGsP5XjlIDVHBGwmj764Vroh2uhH66lOfWDv0UIAADQRBCwAAAADOb078HCzxM5f5ezS6i1nckDnF0CAACNgk%2BwAAAADEbAAgAAMBgBCwAAwGAELAAAAIMRsAAAAAxGwAIAADAYAQsAAMBgBCwAAACDEbAAAAAMRsACAAAwGAELAADAYAQsAAAAgxGwAAAADEbAAgAAMBgBCwAAwGAELAAAAIMRsAAAAAxGwAIAADAYAQsAAMBgBCwAAACDEbAAAAAMRsACAAAwGAELAADAYAQsAAAAgxGwAAAADEbAAgAAMJhLBKwLFy4oJiZGGRkZkqQnnnhC4eHhDo9f/vKXeuCBByRJlZWVCg8PV1hYmMOa4uJiSdL58%2BeVkJCgyMhIRUVFKTU1VeXl5fbjff7555owYYLCw8MVHR2tzZs3O9Szbds2xcTEKCwsTHFxcTp8%2BHAjvRIAAKApcHrAOnTokOLj43Xy5En7WEpKig4fPmx/PP/882rTpo0ee%2BwxSVJubq7KysqUmZnpsM7X11eSlJycLF9fXx04cEBbtmzRRx99pA0bNkiSLl26pGnTpmns2LHKyspSamqqli5dqi%2B%2B%2BEKSlJGRocWLF%2Bupp55SVlaWRo8erenTp6ukpKRxXxgAAOC2nBqwtm3bptmzZ2vWrFk/uebChQuaPXu25s%2Bfr%2BDgYEnSkSNHdMstt8jb27va%2BhMnTigzM1Nz5syR2WxW586dlZCQoPT0dEnSnj175O/vr4kTJ8pkMqlfv36KjY21z2/evFkjR45URESEvLy8dN9998lisWjHjh0N8AoAAICmyKkBa%2BDAgXr//fc1YsSIn1yTlpamHj16aPTo0faxI0eO6N///rfGjRunvn37auLEifr0008lSTk5OfL391fHjh3t64OCgnT69GldvnxZOTk5CgkJcThG165dlZ2dLemHT8f%2B2zwAAEBNTM48eIcOHf7r/KlTp/TOO%2B9Uu0fKx8dHPXv21MyZM9W2bVulp6frgQce0DvvvCOr1Sqz2eywvup5cXHxNed9fHzs92/VNF8b%2Bfn5KigocBgzmXwVEBBQ633Uhqen06/w1onJ5F711lVVP9ytL00V/XAt9MO10I%2BG59SAVZM333zTfoP7f6q6F6vKAw88oK1bt2rfvn3q2LFjtfulqp77%2BfnJbDarqKjIYb60tFR%2Bfn6SfghjpaWl1eYtFkut6960aZNWrVrlMJaYmKikpKRa76Mpslj8nF1Co2jTxlzzIjQa%2BuFa6IdroR8Nx6UD1p49e3T//fdXG3/mmWc0bNgwdevWzT529epVtWzZUsHBwbp48aLOnTun9u3bS5KOHTumTp06qXXr1goJCdHBgwcd9pebm2u/vys4OFg5OTnV5gcNGlTruuPj4xUdHe0wZjL5qrDQWut91Ia7vfMw%2Bvxdjaenh9q0Mevy5RJVVFQ6u5xmj364FvrhWppTP5z15t5lA1ZhYaGOHTum3r17V5s7evSoPvnkEz377LNq27at1q5dqytXrigmJkb%2B/v6KiIjQkiVLlJKSosLCQq1evVrjx4%2BXJMXExGj58uXasGGDJk6cqEOHDmn79u1avXq1JGn8%2BPFKTEzU8OHDFRERofT0dJ0/f14xMTG1rj0gIKDa5cCCgiKVlzftH%2BKaNJfzr6iobDbn6g7oh2uhH66FfjQcl/0I5LvvvpMkh5vVqyxdulQ33XSTxowZo6ioKGVmZurll1%2BWv7%2B/JGnlypUqLy/XkCFDdOedd%2BpXv/qVEhISJEkWi0Xr16/Xrl27FBUVpQULFmjBggXq27evJKlfv35auHChFi1apD59%2Bui9997TunXr7PsGAACoSQubzWZzdhHNQUFBUc2L6shk8lBM2gHD99tQdiYPcHYJDcpk8pDF4qfCQivvCF0A/XAt9MO1NKd%2BdOjQ2inHddlPsAAAANwVAQsAAMBgBCwAAACDEbAAAAAMRsACAAAwGAELAADAYAQsAAAAgxGwAAAADEbAAgAAMBgBCwAAwGAELAAAAIMRsAAAAAxGwAIAADAYAQsAAMBgBCwAAACDEbAAAAAMRsACAAAwGAELAADAYAQsAAAAgxGwAAAADEbAAgAAMBgBCwAAwGAELAAAAIMRsAAAAAxGwAIAADAYAQsAAMBgBCwAAACDEbAAAAAMRsACAAAwmEsErAsXLigmJkYZGRn2sYULF6pHjx4KDw%2B3PzZt2mSfX7dunQYNGqSwsDBNmjRJ3377rX2uuLhY8%2BbNU1RUlCIiIjR37lxZrVb7/PHjxzV58mSFh4dr4MCBeuGFFxzq2bdvn2JjYxUWFqbhw4dr7969DXj2AACgqXF6wDp06JDi4%2BN18uRJh/EjR45o8eLFOnz4sP0RHx8vSdq2bZs2btyol156SRkZGerevbuSkpJks9kkSYsXL9aZM2e0e/du7dmzR2fOnFFaWpokqaysTA8%2B%2BKBCQ0OVkZGhtWvXKj09XTt37pQk5eXlacaMGZo5c6Y%2B%2BeQTzZgxQ8nJyTp79mwjvioAAMCdOTVgbdu2TbNnz9asWbMcxq9evaqjR4%2BqR48e19zujTfe0N13363g4GC1bNlSjzzyiE6fPq2MjAyVlJRo%2B/btSkpKkr%2B/v9q1a6fZs2dr69atKikpUVZWlvLz85WUlCRvb29169ZNkyZNUnp6ur2myMhIDR06VCaTSSNGjFDv3r0dPj0DAAD4b5wasAYOHKj3339fI0aMcBjPzs5WeXm5Vq5cqf79%2B2vYsGFau3atKisrJUm5ubkKCQmxr/fy8lKXLl2UnZ2tEydOqKyszGE%2BKChIpaWlysvLU05OjgIDA%2BXt7W2f79q1q7Kzs6%2B57x/PAwAA1MTkzIN36NDhmuNFRUXq06ePJk2apBUrVujrr79WYmKiPDw8NGXKFFmtVpnNZodtfHx8VFxcrCtXrkiSfH197XNVa61W6zW3NZvNKi4utq/5qX3XVn5%2BvgoKChzGTCZfBQQE1HofteHp6fQrvHViMrlXvXVV1Q9360tTRT9cC/1wLfSj4Tk1YP2UAQMGaMCAAfbnPXv21OTJk7Vjxw5NmTJFZrNZpaWlDtuUlpbKz8/PHqxKSkrk5%2Bdn/29JatWqlXx9fe3Pq/zn2v%2B279ratGmTVq1a5TCWmJiopKSkWu%2BjKbJYav8aurM2bcw1L0KjoR%2BuhX64FvrRcFwyYH3wwQc6d%2B6c7rrrLvvY1atX5ePjI0kKDg5WTk6OBg8eLOmHG9fz8vIUEhKiwMBAeXl5KTc3V7169ZIkHTt2zH4Z8fz588rLy1N5eblMph9OPzc3V8HBwZKkkJAQffXVVw715Obm/uT9YNcSHx%2Bv6OhohzGTyVeFhdaf2KJ%2B3O2dh9Hn72o8PT3Upo1Zly%2BXqKKi0tnlNHv0w7XQD9fSnPrhrDf3LhmwbDabli5dqptvvll9%2B/bVZ599pldffVXz5s2TJI0bN07PP/%2B8Bg0apMDAQD3zzDNq3769IiMj5eXlpeHDhystLU3PPfecJCktLU2jRo2Sj4%2BPoqKiZLFY9PTTTys5OVnHjx/Xxo0b7Tfajx49Wi%2B//LJ27Nih22%2B/XXv27FFmZqbmz59f6/oDAgKqXQ4sKChSeXnT/iGuSXM5/4qKymZzru6AfrgW%2BuFa6EfDccmAFRMTo3nz5mnRokU6e/as2rdvrxkzZmjMmDGSpPHjx6uoqEiJiYm6cOGCQkND9eKLL8rLy0vSD9%2BhtWzZMsXGxqqsrExDhgzR448/LkkymUxav369UlJSNGDAAPn6%2BmrSpEmKi4uT9MMN8X/605%2BUlpam%2BfPn68Ybb9Tzzz%2BvwMBA57wYAADA7bSwVX15FBpUQUGR4fs0mTwUk3bA8P02lJ3JA2pe5MZMJg9ZLH4qLLTyjtAF0A/XQj9cS3PqR4cOrZ1yXPe6iQcAAMANELAAAAAMRsACAAAwGAELAADAYAQsAAAAgxGwAAAADEbAAgAAMBgBCwAAwGAELAAAAIMRsAAAAAxGwAIAADAYAQsAAMBgBCwAAACDEbAAAAAMRsACAAAwGAELAADAYAQsAAAAgxGwAAAADEbAAgAAMBgBCwAAwGAELAAAAIMRsAAAAAxGwAIAADAYAQsAAMBgBCwAAACDEbAAAAAMRsACAAAwGAELAADAYAQsAAAAg7lEwLpw4YJiYmKUkZFhH9u9e7fGjBmj2267TdHR0Vq1apUqKyvt88OHD1evXr0UHh5ufxw7dkySVFxcrHnz5ikqKkoRERGaO3eurFarfdvjx49r8uTJCg8P18CBA/XCCy841LNv3z7FxsYqLCxMw4cP1969exv4FQAAAE2J0wPWoUOHFB8fr5MnT9rHvvzyS82dO1fJycn65JNPtG7dOm3dulUbNmyQJF25ckXHjx/Xjh07dPjwYfsjKChIkrR48WKdOXNGu3fv1p49e3TmzBmlpaVJksrKyvTggw8qNDRUGRkZWrt2rdLT07Vz505JUl5enmbMmKGZM2fqk08%2B0YwZM5ScnKyzZ8827gsDAADcllMD1rZt2zR79mzNmjXLYfxf//qX7rrrLg0ePFgeHh4KCgpSTEyMsrKyJP0QwPz9/XXjjTdW22dJSYm2b9%2BupKQk%2Bfv7q127dpo9e7a2bt2qkpISZWVlKT8/X0lJSfL29la3bt00adIkpaen22uKjIzU0KFDZTKZNGLECPXu3VubNm1q%2BBcEAAA0CU4NWAMHDtT777%2BvESNGOIwPGzZM8%2BbNsz8vLS3Vhx9%2BqO7du0uSjhw5IrPZrHvuuUdRUVGKi4uzX8Y7ceKEysrKFBISYt8%2BKChIpaWlysvLU05OjgIDA%2BXt7W2f79q1q7KzsyVJubm5Dtv%2BeB4AAKAmJmcevEOHDjWuuXLlimbOnCkfHx/dd999kqQWLVooNDRUDz/8sG644Qbt2rVLM2bM0Guvvaby8nJJkq%2Bvr30fZrNZkmS1WmW1Wu3P/3O%2BuLjYvubH8z4%2BPvb52sjPz1dBQYHDmMnkq4CAgFrvozY8PZ1%2BhbdOTCb3qreuqvrhbn1pquiHa6EfroV%2BNDynBqyafPvtt0pKSlK7du306quvqlWrVpKkKVOmOKwbPXq03n33Xe3evVuxsbGSfrhU6OfnZ/9vSWrVqpV8fX3tz6v851qz2azS0lKH%2BdLSUvt8bWzatEmrVq1yGEtMTFRSUlKt99EUWSy1fw3dWZs25poXodHQD9dCP1wL/Wg49QpYFRUV8vT0NLoWB/v27dPDDz%2BsO%2B%2B8U4888ohMpv8r9aWXXlK3bt3Ur18/%2B9jVq1fVsmVLBQYGysvLS7m5uerVq5ck6dixY/Ly8lKXLl10/vx55eXlqby83L7P3NxcBQcHS5JCQkL01VdfOdSSm5urHj161Lr2%2BPh4RUdHO4yZTL4qLLT%2BxBb1427vPIw%2Bf1fj6emhNm3Muny5RBUVlTVvgAZFP1wL/XAtzakfznpzX6%2BANWjQII0ZM0ZxcXHq2rWr0TXps88%2BU2JiohYtWqTx48dXmz9z5ow2b96sdevW6frrr9dbb72lw4cP68knn5TZbNbw4cOVlpam5557TpKUlpamUaNGycfHR1FRUbJYLHr66aeVnJys48ePa%2BPGjfYb7UePHq2XX35ZO3bs0O233649e/YoMzNT8%2BfPr3X9AQEB1S4HFhQUqby8af8Q16S5nH9FRWWzOVd3QD9cC/1wLfSj4dTrI5CHHnpIn376qUaNGqUJEybo9ddfV1FRkWFFvfDCCyovL1dqaqrD91xVXRqcO3euBg0apLvvvluRkZF6/fXXtXbtWt18882SpIULF6pLly6KjY3Vb3/7W/3P//yPnnjiCUmSyWTS%2BvXrdfToUQ0YMEDTpk3TpEmTFBcXJ%2BmHG%2BL/9Kc/6cUXX1Tv3r21evVqPf/88woMDDTs/AAAQNPWwmaz2eq7cV5enrZt26Z3331X586d09ChQzVu3Dj179/fyBqbhIIC4wJoFZPJQzFpBwzfb0PZmTzA2SU0KJPJQxaLnwoLrbwjdAH0w7XQD9fSnPrRoUNrpxz3Z93E06VLF82aNUu7du1SYmKi/vrXv%2BqBBx5QdHS0Xn75ZVVUVBhVJwAAgNv4Wb9F%2BPnnn%2Butt97Sjh07dPXqVcXExCguLk5nz57Vc889pyNHjmjFihVG1QoAAOAW6hWwVq9erbffflsnTpxQaGioZs2apVGjRtm/RkGSPD097fc9AQAANCf1ClivvfaaRo8erfHjx//kbxEGBQVp9uzZP6s4AAAAd1SvgLV//35duXJFFy9etI/t2LFD/fr1k8VikSR169ZN3bp1M6ZKAAAAN1Kvm9z/%2Bc9/atiwYQ5/AHn58uWKjY3V0aNHDSsOAADAHdUrYP3v//6vbr/9dvuXc0rSBx98oEGDBumpp54yrDgAAAB3VK%2BA9dVXX2natGny9va2j3l6emratGn67LPPDCsOAADAHdUrYLVq1UonT56sNv7999/Lx8fnZxcFAADgzuoVsIYNG6ZFixbpH//4h65cuSKr1aqPP/5YKSkpiomJMbpGAAAAt1Kv3yJ85JFHdOrUKd1///1q0aKFfTwmJkZz5841rDgAAAB3VK%2BAZTab9eKLL%2Br48eP65ptv5OXlpaCgIHXp0sXg8gAAANzPz/pTOYGBgQoMDDSqFgAAgCahXgHr%2BPHjSklJ0aFDh1RWVlZt/uuvv/7ZhQEAALiregWsRYsW6fTp05o9e7Zat25tdE0AAABurV4B6/Dhw3rllVcUHh5udD0AAABur15f02CxWOTn52d0LQAAAE1CvQLWpEmTtGLFChUVFRldDwAAgNur1yXCffv26bPPPlNUVJTatWvn8CdzJOmvf/2rIcUBAAC4o3oFrKioKEVFRRldCwAAQJNQr4D10EMPGV0HAABAk1Gve7AkKTs7W/PmzdNdd92ls2fPKj09XRkZGUbWBgAA4JbqFbC%2B/PJLTZgwQd99952%2B/PJLXb16VV9//bXuv/9%2B7d271%2BgaAQAA3Eq9AlZaWpruv/9%2Bbdy4UV5eXpKkP/7xj7r33nu1atUqQwsEAABwN/X%2BBGvs2LHVxn/3u9/p22%2B//dlFAQAAuLN6BSwvLy9duXKl2vjp06dlNpt/dlEAAADurF4Ba%2BjQoXr66adVWFhoHzt27JhSU1P1m9/8xqjaAAAA3FK9Atajjz6q0tJS9e/fXyUlJYqLi9OoUaNkMpk0d%2B5co2sEAABwK/X6HqxWrVrp9ddf10cffaR//vOfqqysVEhIiH71q1/Jw6Pe3/wAAADQJPysNNSvXz898MADmjp1qn7961/XK1xduHBBMTExDt%2Bh9fnnn2vChAkKDw9XdHS0Nm/e7LDNtm3bFBMTo7CwMMXFxenw4cP2uYqKCi1btkz9%2B/dXeHi4pk%2Bfrvz8fPv8%2BfPnlZCQoMjISEVFRSk1NVXl5eW1PjYAAEBN6vUJVnR0tFq0aPGT87X9W4SHDh3SY489ppMnT9rHLl26pGnTpikpKUnx8fHKyspSYmKibrnlFvXs2VMZGRlavHix1q1bp549eyo9PV3Tp0/X3r17ZTabtWbNGh08eFBvvvmmWrdurccff1wLFizQ2rVrJUnJycnq2LGjDhw4oHPnzmn69OnasGGDpkyZUuOxAQAAaqNen2DdcccdDo9Ro0YpNDRUhYWFmjx5cq32sW3bNs2ePVuzZs1yGN%2BzZ4/8/f01ceJEmUwm9evXT7GxsUpPT5ckbd68WSNHjlRERIS8vLx03333yWKxaMeOHfb5qVOn6vrrr1erVq00f/587d%2B/X6dOndKJEyeUmZmpOXPmyGw2q3PnzkpISLDvu6ZjAwAA1Ea9PsGaMWPGNcdfe%2B01HTp0SPfee2%2BN%2Bxg4cKBiY2NlMpkcQlZOTo5CQkIc1nbt2lVbtmyRJOXm5mrcuHHV5rOzs1VUVKTvv//eYfv27durbdu2%2BuabbyRJ/v7%2B6tixo30%2BKChIp0%2Bf1uXLl2s8NgAAQG3UK2D9lMGDB2vFihW1WtuhQ4drjlut1mrfpeXj46Pi4uIa561WqyTJ19e32nzV3I%2B3rXpetf1/O3Zt5efnq6CgwGHMZPJVQEBAnfZTE09P9/qFApPJveqtq6p%2BuFtfmir64Vroh2uhHw3P0ICVmZmpli1b/qx9mM1mFRUVOYyVlpbKz8/PPl9aWlpt3mKx2MNRSUnJNbe32WzV5qqe%2B/n51Xjs2tq0aVO1PxmUmJiopKSkOu2nqbFY6vY6uqs2bfiyXVdCP1wL/XAt9KPh1Ctg/fgSoM1m05UrV/TNN9/U6vLgfxMSEqKDBw86jOXm5io4OFiSFBwcrJycnGrzgwYNUtu2bdWxY0fl5ubaL/UVFBTo4sWLCgkJUWVlpS5evKhz586pffv2kn74gtROnTqpdevWNR67tuLj4xUdHe0wZjL5qrDQWqf91MTd3nkYff6uxtPTQ23amHX5cokqKiqdXU6zRz9cC/1wLc2pH856c1%2BvgHXDDTdU%2By1CLy8vTZ48WbGxsT%2BroJiYGC1fvlwbNmzQxIkTdejQIW3fvl2rV6%2BWJI0fP16JiYkaPny4IiIilJ6ervPnzysmJkaSFBcXpzVr1ig0NFQWi0VLlixRnz59dNNNN0mSIiIitGTJEqWkpKiwsFCrV6/W%2BPHja3Xs2goICKh2ObCgoEjl5U37h7gmzeX8Kyoqm825ugP64Vroh2uhHw2nXgHrqaeeMroOO4vFovXr1ys1NVUrV67UddddpwULFqhv376SfvjurYULF2rRokU6e/asunbtqnW%2BGp6aAAAd%2B0lEQVTr1snf31/SD5fiysvLNXHiRFmtVkVFRenZZ5%2B173/lypVKSUnRkCFD5OHhobFjxyohIaFWxwYAAKiNFjabzVbXjbKysmq9tnfv3nXdfZNUUFBU86I6Mpk8FJN2wPD9NpSdyQOcXUKDMpk8ZLH4qbDQyjtCF0A/XAv9cC3NqR8dOrR2ynHr9QnWfffdJ5vNZn9UqbpsWDXWokULff311waUCQAA4D7qFbCef/55LV26VI8%2B%2Bqj69u0rLy8vff7551q0aJHuvvtuDR482Og6AQAA3Ea9fg1t2bJlWrhwoYYOHapWrVqpZcuW6tOnj1JSUrR%2B/XrdeOON9gcAAEBzU6%2BAlZ%2Bfr%2Buvv77aeKtWrVRYWPiziwIAAHBn9QpYYWFhWrFiha5cuWIfu3jxopYvX65%2B/foZVhwAAIA7qtc9WAsWLNDkyZM1aNAgdenSRZJ0/PhxdejQQa%2B%2B%2BqqR9QEAALidegWsoKAg7dixQ9u3b9exY8ckSXfffbdGjhxZ7W/5AQAANDf1/luEbdq00YQJE/Tdd9%2Bpc%2BfOkn74NncAAIDmrl73YNlsNqWlpal3794aNWqUvv/%2Bez366KOaN2%2BeysrKjK4RAADArdQrYG3cuFFvv/22Fi5cKG9vb0nS0KFD9be//U3PPfecoQUCAAC4m3oFrE2bNumJJ55QXFyc/dvbR4wYodTUVL333nuGFggAAOBu6hWwvvvuO/3yl7%2BsNn7LLbfo3LlzP7soAAAAd1avgHXjjTfqiy%2B%2BqDa%2Bb98%2B%2Bw3vAAAAzVW9fovwgQce0JNPPqmzZ8/KZrPpo48%2B0uuvv66NGzdq3rx5RtcIAADgVuoVsMaNG6fy8nKtWbNGpaWleuKJJ9SuXTvNmjVLv/vd74yuEQAAwK3UK2C98847%2Bu1vf6v4%2BHhduHBBNptN7dq1M7o2AAAAt1Sve7D%2B%2BMc/2m9mv%2B666whXAAAA/6FeAatLly765ptvjK4FAACgSajXJcLg4GDNnj1bf/7zn9WlSxe1bNnSYX7p0qWGFAcAAOCO6hWwTp48qYiICElSQUGBoQUBAAC4u1oHrKVLl2rmzJny9fXVxo0bG7ImAAAAt1bre7BeffVVlZSUOIw98MADys/PN7woAAAAd1brgGWz2aqNffrpp/r3v/9taEEAAADurl6/RQgAAICfRsACAAAwWJ0CVosWLRqqDgAAgCajTl/T8Mc//tHhO6/Kysq0fPly%2Bfn5Oazje7AAAEBzVuuA1bt372rfeRUeHq7CwkIVFhYaXhgAAIC7qnXA4ruvAAAAasdlb3J/5513FB4e7vDo0aOHevToIUmaMmWKQkNDHeb3798vSaqoqNCyZcvUv39/hYeHa/r06Q7f13X%2B/HklJCQoMjJSUVFRSk1NVXl5uX3%2B888/14QJExQeHq7o6Ght3ry5cU8eAAC4NZcNWKNHj9bhw4ftj127dsnf31%2BpqamSpC%2B//FIvvfSSw5pBgwZJktasWaODBw/qzTff1IEDB%2BTj46MFCxbY952cnCxfX18dOHBAW7Zs0UcffaQNGzZIki5duqRp06Zp7NixysrKUmpqqpYuXaovvvii0V8DAADgnlw2YP0nm82mOXPm6De/%2BY3GjBmjU6dO6dKlS%2BrWrds112/evFlTp07V9ddfr1atWmn%2B/Pnav3%2B/Tp06pRMnTigzM1Nz5syR2WxW586dlZCQoPT0dEnSnj175O/vr4kTJ8pkMqlfv36KjY21zwMAANTELQLW22%2B/rdzcXD322GOSpCNHjsjPz0%2BzZs1S3759NWrUKG3ZskWSVFRUpO%2B//14hISH27du3b6%2B2bdvqm2%2B%2BUU5Ojvz9/dWxY0f7fFBQkE6fPq3Lly8rJyfHYVtJ6tq1q7KzsxvhTAEAQFNQp69pcIbKykqtWbNGDz74oFq1aiVJunr1qsLCwjRr1iwFBwcrIyNDM2bMkJ%2Bfn8LDwyVJvr6%2BDvvx8fGR1WqVJJnNZoe5qufFxcWyWq3V5n18fFRcXFzrmvPz86v9xqXJ5KuAgIBa76M2PD3dIh/bmUzuVW9dVfXD3frSVNEP10I/XAv9aHguH7AyMjKUn5%2Bv8ePH28fGjh2rsWPH2p8PHDhQY8eO1c6dO9W/f39JqvaHqUtLS%2BXn5yebzVZtruq5n5%2BfzGazioqKrrltbW3atEmrVq1yGEtMTFRSUlKt99EUWSy1fw3dWZs25poXodHQD9dCP1wL/Wg4Lh%2Bwdu/erZiYGIdPpLZs2SI/Pz8NHz7cPnb16lW1bNlSbdu2VceOHZWbm2u/1FdQUKCLFy8qJCRElZWVunjxos6dO6f27dtLko4dO6ZOnTqpdevWCgkJ0cGDBx1qyM3NVXBwcK1rjo%2BPV3R0tMOYyeSrwkJrnc//v3G3dx5Gn7%2Br8fT0UJs2Zl2%2BXKKKikpnl9Ps0Q/XQj9cS3Pqh7Pe3Lt8wDp06JDuvfdeh7ErV65oxYoVuvnmm3Xrrbdq//79evfdd/XSSy9JkuLi4rRmzRqFhobKYrFoyZIl6tOnj2666SZJUkREhJYsWaKUlBQVFhZq9erV9k/IYmJitHz5cm3YsEETJ07UoUOHtH37dq1evbrWNQcEBFS7HFhQUKTy8qb9Q1yT5nL%2BFRWVzeZc3QH9cC30w7XQj4bj8gHru%2B%2B%2BqxZWJk%2BerOLiYj300EM6f/68OnfurGXLlikyMlLSD5fjysvLNXHiRFmtVkVFRenZZ5%2B1b79y5UqlpKRoyJAh8vDw0NixY5WQkCBJslgsWr9%2BvVJTU7Vy5Updd911WrBggfr27dt4Jw0AANxaC5vNZnN2Ec1BQUFRzYvqyGTyUEzaAcP321B2Jg9wdgkNymTykMXip8JCK%2B8IXQD9cC30w7U0p3506NDaKcd1r5t4AAAA3AABCwAAwGAELAAAAIMRsAAAAAxGwAIAADAYAQsAAMBgBCwAAACDEbAAAAAMRsACAAAwGAELAADAYAQsAAAAgxGwAAAADEbAAgAAMBgBCwAAwGAELAAAAIMRsAAAAAxGwAIAADAYAQsAAMBgBCwAAACDEbAAAAAMRsACAAAwGAELAADAYAQsAAAAgxGwAAAADEbAAgAAMBgBCwAAwGAELAAAAIMRsAAAAAxGwAIAADCYywasHTt2qFu3bgoPD7c/5syZI0nat2%2BfYmNjFRYWpuHDh2vv3r0O265bt06DBg1SWFiYJk2apG%2B//dY%2BV1xcrHnz5ikqKkoRERGaO3eurFarff748eOaPHmywsPDNXDgQL3wwguNc8IAAKDJcNmAdeTIEY0ZM0aHDx%2B2P5YvX668vDzNmDFDM2fO1CeffKIZM2YoOTlZZ8%2BelSRt27ZNGzdu1EsvvaSMjAx1795dSUlJstlskqTFixfrzJkz2r17t/bs2aMzZ84oLS1NklRWVqYHH3xQoaGhysjI0Nq1a5Wenq6dO3c67XUAAADux6UDVo8ePaqNb9u2TZGRkRo6dKhMJpNGjBih3r17a9OmTZKkN954Q3fffbeCg4PVsmVLPfLIIzp9%2BrQyMjJUUlKi7du3KykpSf7%2B/mrXrp1mz56trVu3qqSkRFlZWcrPz1dSUpK8vb3VrVs3TZo0Senp6Y19%2BgAAwI25ZMCqrKzUV199pQ8//FCDBw/WoEGD9Pjjj%2BvSpUvKzc1VSEiIw/quXbsqOztbkqrNe3l5qUuXLsrOztaJEydUVlbmMB8UFKTS0lLl5eUpJydHgYGB8vb2vua%2BAQAAasPk7AKu5cKFC%2BrWrZuGDRumlStXqrCwUI8%2B%2BqjmzJmjq1evymw2O6z38fFRcXGxJMlqtf7k/JUrVyRJvr6%2B9rmqtVar9Zrbms1m%2B75rKz8/XwUFBQ5jJpOvAgIC6rSfmnh6umQ%2B/kkmk3vVW1dV/XC3vjRV9MO10A/XQj8anksGrPbt2ztcljObzZozZ47uvPNORUVFqbS01GF9aWmp/Pz87Gt/ar4qWJWUlNjXl5SUSJJatWolX19f%2B/Mq/7m2tjZt2qRVq1Y5jCUmJiopKalO%2B2lqLJa6vY7uqk0bc82L0Gjoh2uhH66FfjQclwxY2dnZevfdd/XII4%2BoRYsWkqSrV6/Kw8NDPXv21Ndff%2B2wPjc3136/VnBwsHJycjR48GBJP9y4npeXp5CQEAUGBsrLy0u5ubnq1auXJOnYsWP2y4jnz59XXl6eysvLZTKZ7PsODg6uU/3x8fGKjo52GDOZfFVYaP2JLerH3d55GH3%2BrsbT00Nt2ph1%2BXKJKioqnV1Os0c/XAv9cC3NqR/OenPvkgHL399f6enpatu2rX7/%2B98rPz9fy5cv1x133KGxY8fqlVde0Y4dO3T77bdrz549yszM1Pz58yVJ48aN0/PPP69BgwYpMDBQzzzzjNq3b6/IyEh5eXlp%2BPDhSktL03PPPSdJSktL06hRo%2BTj46OoqChZLBY9/fTTSk5O1vHjx7Vx40bNmjWrTvUHBARUuxxYUFCk8vKm/UNck%2BZy/hUVlc3mXN0B/XAt9MO10I%2BG08JW9f0FLiYzM1MrVqzQ0aNH1bJlS40cOVJz5sxRy5YtdeDAAaWlpenkyZO68cYbNWfOHP3617%2BWJNlsNr388stKT0/XhQsXFBoaqieffFKBgYGSpCtXrmjZsmX629/%2BprKyMg0ZMkSPP/64/fLhiRMnlJKSos8//1y%2Bvr665557NG3atJ99PgUFRT97Hz9mMnkoJu2A4fttKDuTBzi7hAZlMnnIYvFTYaGV/8NyAfTDtdAP19Kc%2BtGhQ2unHNdlA1ZTQ8AiYKFx0Q/XQj9cS3Pqh7MClnvdxAMAAOAGCFgAAAAGI2ABAAAYjIAFAABgMAIWAACAwQhYAAAABiNgAQAAGIyABQAAYDACFgAAgMEIWAAAAAYjYAEAABiMgAUAAGAwAhYAAIDBCFgAAAAGI2ABAAAYjIAFAABgMAIWAACAwQhYAAAABiNgAQAAGIyABQAAYDACFgAAgMEIWAAAAAYjYAEAABiMgAUAAGAwAhYAAIDBCFgAAAAGI2ABAAAYjIAFAABgMAIWAACAwVw2YGVnZ%2Bv3v/%2B9%2BvTpowEDBmju3Lm6cOGCJGnhwoXq0aOHwsPD7Y9NmzbZt123bp0GDRqksLAwTZo0Sd9%2B%2B619rri4WPPmzVNUVJQiIiI0d%2B5cWa1W%2B/zx48c1efJkhYeHa%2BDAgXrhhRca76QBAECT4JIBq7S0VFOmTFF4eLj%2B/ve/691339XFixf1hz/8QZJ05MgRLV68WIcPH7Y/4uPjJUnbtm3Txo0b9dJLLykjI0Pdu3dXUlKSbDabJGnx4sU6c%2BaMdu/erT179ujMmTNKS0uTJJWVlenBBx9UaGioMjIytHbtWqWnp2vnzp3OeSEAAIBbcsmAdfr0ad16661KTEyUt7e3LBaL4uPjlZWVpatXr%2Bro0aPq0aPHNbd94403dPfddys4OFgtW7bUI488otOnTysjI0MlJSXavn27kpKS5O/vr3bt2mn27NnaunWrSkpKlJWVpfz8fCUlJcnb21vdunXTpEmTlJ6e3sivAAAAcGcuGbB%2B8Ytf6M9//rM8PT3tY7t371b37t2VnZ2t8vJyrVy5Uv3799ewYcO0du1aVVZWSpJyc3MVEhJi387Ly0tdunRRdna2Tpw4obKyMof5oKAglZaWKi8vTzk5OQoMDJS3t7d9vmvXrsrOzm6EswYAAE2FydkF1MRms%2BnZZ5/V3r179dprr%2BncuXPq06ePJk2apBUrVujrr79WYmKiPDw8NGXKFFmtVpnNZod9%2BPj4qLi4WFeuXJEk%2Bfr62ueq1lqt1mtuazabVVxcXKea8/PzVVBQ4DBmMvkqICCgTvupiaenS%2Bbjn2QyuVe9dVXVD3frS1NFP1wL/XAt9KPhuXTAunLliubNm6evvvpKr732mm655RbdcsstGjBggH1Nz549NXnyZO3YsUNTpkyR2WxWaWmpw35KS0vl5%2BdnD1YlJSXy8/Oz/7cktWrVSr6%2BvvbnVf5zbW1t2rRJq1atchhLTExUUlJSnfbT1FgsdXsd3VWbNuaaF6HR0A/XQj9cC/1oOC4bsE6ePKmpU6fqhhtu0JYtW3TddddJkj744AOdO3dOd911l33t1atX5ePjI0kKDg5WTk6OBg8eLOmHG9fz8vIUEhKiwMBAeXl5KTc3V7169ZIkHTt2zH4Z8fz588rLy1N5eblMph9emtzcXAUHB9ep9vj4eEVHRzuMmUy%2BKiy0/sQW9eNu7zyMPn9X4%2BnpoTZtzLp8uUQVFZXOLqfZox%2BuhX64lubUD2e9uXfJgHXp0iVNnjxZffv2VWpqqjw8/i9I2Gw2LV26VDfffLP69u2rzz77TK%2B%2B%2BqrmzZsnSRo3bpyef/55DRo0SIGBgXrmmWfUvn17RUZGysvLS8OHD1daWpqee%2B45SVJaWppGjRolHx8fRUVFyWKx6Omnn1ZycrKOHz%2BujRs3atasWXWqPyAgoNrlwIKCIpWXN%2B0f4po0l/OvqKhsNufqDuiHa6EfroV%2BNByXDFhbt27V6dOntXPnTu3atcth7vDhw5o3b54WLVqks2fPqn379poxY4bGjBkjSRo/fryKioqUmJioCxcuKDQ0VC%2B%2B%2BKK8vLwk/fAdWsuWLVNsbKzKyso0ZMgQPf7445Ikk8mk9evXKyUlRQMGDJCvr68mTZqkuLi4xn0BAACAW2thq/qCKDSogoIiw/dpMnkoJu2A4fttKDuTB9S8yI2ZTB6yWPxUWGjlHaELoB%2BuhX64lubUjw4dWjvluO51Ew8AAIAbIGABAAAYjIAFAABgMAIWAACAwQhYAAAABiNgAQAAGIyABQAAYDACFgAAgMEIWAAAAAYjYAEAABiMgAUAAGAwAhYAAIDBCFgAAAAGI2ABAAAYjIAFAABgMAIWAACAwQhYAAAABiNgAQAAGIyABQAAYDACFgAAgMEIWAAAAAYjYAEAABiMgAUAAGAwAhYAAIDBCFgAAAAGI2ABAAAYjIAFAABgMAIWAACAwQhYAAAABiNgXcP58%2BeVkJCgyMhIRUVFKTU1VeXl5c4uCwAAuAkC1jUkJyfL19dXBw4c0JYtW/TRRx9pw4YNzi4LAAC4CQLWj5w4cUKZmZmaM2eOzGazOnfurISEBKWnpzu7NAAA4CYIWD%2BSk5Mjf39/dezY0T4WFBSk06dP6/Lly06sDAAAuAuTswtwNVarVWaz2WGs6nlxcbHatGlT4z7y8/NVUFDgMGYy%2BSogIMC4QiV5erpXPjaZ3Kveuqrqh7v1pamiH66FfrgW%2BtHwCFg/4uvrq5KSEoexqud%2Bfn612semTZu0atUqh7GHHnpIM2bMMKbI/19%2Bfr4md8pRfHy84eENdZefn69XXvkz/XAR9MO10A/XQj8aHtH1R4KDg3Xx4kWdO3fOPnbs2DF16tRJrVu3rtU%2B4uPjtXXrVodHfHy84bUWFBRo1apV1T4tg3PQD9dCP1wL/XAt9KPh8QnWj3Tp0kURERFasmSJUlJSVFhYqNWrV2v8%2BPG13kdAQADvCAAAaMb4BOsaVq5cqfLycg0ZMkR33nmnfvWrXykhIcHZZQEAADfBJ1jX0L59e61cudLZZQAAADfluWjRokXOLgL15%2Bfnpz59%2BtT6Bnw0LPrhWuiHa6EfroV%2BNKwWNpvN5uwiAAAAmhLuwQIAADAYAQsAAMBgBCwAAACDEbAAAAAMRsACAAAwGAELAADAYAQsAAAAgxGwAAAADEbAcnHnz59XQkKCIiMjFRUVpdTUVJWXl19z7b59%2BxQbG6uwsDANHz5ce/fubeRqm7669OMvf/mLhg0bpvDwcA0bNkzp6emNXG3TV5d%2BVDl69Kh69eqljIyMRqqy%2BahLPzIzMzVhwgSFh4fr17/%2BtV588cVGrrbpq0s/XnnlFUVHR%2Bu2225TbGysdu/e3cjVNkE2uLR77rnH9sgjj9iKi4ttJ0%2BetI0cOdK2bt26auuOHz9uCw0Ntb3//vu2srIy23vvvWfr2bOn7fvvv3dC1U1Xbfvx/vvv2yIjI22HDx%2B2VVZW2j799FNbZGSkbdeuXU6ouumqbT%2BqFBcX20aNGmULCQmxffzxx41YafNQ237k5ubaevXqZdu6dautsrLS9vXXX9v69Olj27lzpxOqbrpq248PP/zQ1q9fP9uxY8dsNpvNtmvXLtutt95qO3XqVGOX3KTwCZYLO3HihDIzMzVnzhyZzWZ17txZCQkJ1/wkZNu2bYqMjNTQoUNlMpk0YsQI9e7dW5s2bXJC5U1TXfpx9uxZTZ06VWFhYWrRooXCw8MVFRWlrKwsJ1TeNNWlH1WefPJJDR06tBGrbD7q0o//9//%2Bn4YMGaI77rhDLVq00K233qrXX39dERERTqi8aapLP7799lvZbDb7w9PTU15eXjKZTE6ovOkgYLmwnJwc%2Bfv7q2PHjvaxoKAgnT59WpcvX3ZYm5ubq5CQEIexrl27Kjs7u1FqbQ7q0o%2BJEydq2rRp9ufnz59XVlaWevTo0Wj1NnV16YckvfXWWzpx4oQeeuihxiyz2ahLP7744gv9z//8jx5%2B%2BGFFRUVp%2BPDhyszMVIcOHRq77CarLv0YOXKk2rdvrxEjRqh79%2B6aOXOmnnrqKXXq1Kmxy25SCFguzGq1ymw2O4xVPS8uLq5xrY%2BPT7V1qL%2B69OM/FRQUaOrUqerRo4dGjRrVoDU2J3Xpx7Fjx/TMM8/o6aeflqenZ6PV2JzUpR%2BXLl3Sq6%2B%2BqtGjR%2BvgwYNKSUnRsmXLtGvXrkart6mrSz/Kysp06623avPmzfrss8%2BUkpKi%2BfPn65tvvmm0epsiApYL8/X1VUlJicNY1XM/Pz%2BHcbPZrNLSUoex0tLSautQf3XpR5XPPvtM48ePV2BgoNasWcNH7gaqbT/%2B/e9/a9asWfrDH/6gG264oVFrbE7q8u/D29tbQ4YM0W9%2B8xuZTCb17t1bY8aM0c6dOxut3qauLv1YvHixgoOD1bNnT3l7e2vcuHEKCwvTtm3bGq3epoiA5cKCg4N18eJFnTt3zj527NgxderUSa1bt3ZYGxISopycHIex3NxcBQcHN0qtzUFd%2BiFJW7Zs0X333afJkyfr6aeflre3d2OW2%2BTVth9HjhxRXl6e5s%2Bfr8jISEVGRkqSHnzwQS1atKixy26y6vLvIygoSFevXnUYq6iokM1ma5Ram4O69OP06dPV%2BmEymeTl5dUotTZZzr3HHjX53e9%2BZ5s1a5atqKjI/lsgK1eurLYuNzfXFhoaanvvvffsv0UYGhpq%2B/bbb51QddNV237s2rXL1r17d9v%2B/fudUGXzUdt%2B/Bi/RdgwatuPf/zjH7Zu3brZ3nrrLVtlZaUtMzPTFhYWZvvggw%2BcUHXTVdt%2BPPPMM7aoqCjbl19%2BaauoqLDt3LnTFhoaavvnP//phKqbDgKWiysoKLDNmDHD1qdPH1vfvn1tTz31lK28vNxms9lsYWFhtrffftu%2Bdv/%2B/bbRo0fbwsLCbCNHjrR9%2BOGHziq7yaptP0aNGmW79dZbbWFhYQ6Pxx9/3JnlNzl1%2BffxnwhYDaMu/fjwww9tcXFxtvDwcNuQIUNsf/nLX5xVdpNV236UlZXZVq5caRs8eLDttttus91xxx28OTRAC5uNz2QBAACMxD1YAAAABiNgAQAAGIyABQAAYDACFgAAgMEIWAAAAAYjYAEAABiMgAUAAFzGhQsXFBMTo4yMjFqtHzlypMLDwx0et9xyi1588cUGrvS/4w%2BjAQAAl3Do0CE99thjOnnyZK23ee%2B99xyeP/vss/rwww91zz33GF1enfAJFgAAcLpt27Zp9uzZmjVrVrW5f/zjHxo/frwiIyM1cuRIvfPOO9fcx8cff6xXXnlFzz77bLU/at3YCFgAAMDpBg4cqPfff18jRoxwGM/Oztb06dM1bdo0ZWRkaPHixVqyZIkOHDjgsK6iokILFy7U9OnT1aVLl0as/NoIWAAAwOk6dOggk6n6nUuvv/66hgwZottvv12enp667bbbdOeddyo9Pd1h3fbt21VcXKx77723sUr%2Br7gHCwAAuKx//etf%2BvjjjxUZGWkfq6io0E033eSw7o033lB8fLx8fHwau8RrImABAACX1alTJ91xxx1KSUmxj%2BXn58tms9mfnzt3Tp9%2B%2BqmWLVvmjBKviUuEAADAZY0fP17vvvuu/v73v6uyslJ5eXm65557tH79evuaTz/9VAEBAercubMTK3XEJ1gAAMBl9erVSytWrNCKFSs0c%2BZMmc1mjRo1Sg8//LB9zalTp9SxY0cnVlnd/wcPtVtcs4D8ZQAAAABJRU5ErkJggg%3D%3D"/>
        </div>
        <div role="tabpanel" class="tab-pane col-md-12" id="common8569089068023125674">

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">60684.0</td>
        <td class="number">31</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">61188.0</td>
        <td class="number">30</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">59646.0</td>
        <td class="number">30</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">49630.0</td>
        <td class="number">30</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">61134.0</td>
        <td class="number">28</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">50255.0</td>
        <td class="number">28</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">59346.0</td>
        <td class="number">27</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">61044.0</td>
        <td class="number">27</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">61488.0</td>
        <td class="number">27</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">60072.0</td>
        <td class="number">27</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="other">
        <td class="fillremaining">Other values (60548)</td>
        <td class="number">195023</td>
        <td class="number">75.9%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="missing">
        <td class="fillremaining">(Missing)</td>
        <td class="number">61676</td>
        <td class="number">24.0%</td>
        <td>
            <div class="bar" style="width:32%">&nbsp;</div>
        </td>
</tr>
</table>
        </div>
        <div role="tabpanel" class="tab-pane col-md-12"  id="extreme8569089068023125674">
            <p class="h4">Minimum 5 values</p>

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">0.0</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:50%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">4033.0</td>
        <td class="number">2</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">4134.0</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:50%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">4699.0</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:50%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">4704.0</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:50%">&nbsp;</div>
        </td>
</tr>
</table>
            <p class="h4">Maximum 5 values</p>

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">1988000.0</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:50%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">2267570.0</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:50%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">5879400.0</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:50%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">7523240.0</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:50%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">8713547.0</td>
        <td class="number">2</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr>
</table>
        </div>
    </div>
</div>
</div><div class="row variablerow">
    <div class="col-md-3 namecol">
        <p class="h4 pp-anchor" id="pp_var_Bankruptcies">Bankruptcies<br/>
            <small>Numeric</small>
        </p>
    </div><div class="col-md-6">
    <div class="row">
        <div class="col-sm-6">
            <table class="stats ">
                <tr>
                    <th>Distinct count</th>
                    <td>9</td>
                </tr>
                <tr>
                    <th>Unique (%)</th>
                    <td>0.0%</td>
                </tr>
                <tr class="ignore">
                    <th>Missing (%)</th>
                    <td>0.2%</td>
                </tr>
                <tr class="ignore">
                    <th>Missing (n)</th>
                    <td>529</td>
                </tr>
                <tr class="ignore">
                    <th>Infinite (%)</th>
                    <td>0.0%</td>
                </tr>
                <tr class="ignore">
                    <th>Infinite (n)</th>
                    <td>0</td>
                </tr>
            </table>

        </div>
        <div class="col-sm-6">
            <table class="stats ">

                <tr>
                    <th>Mean</th>
                    <td>0.11032</td>
                </tr>
                <tr>
                    <th>Minimum</th>
                    <td>0</td>
                </tr>
                <tr>
                    <th>Maximum</th>
                    <td>7</td>
                </tr>
                <tr class="alert">
                    <th>Zeros (%)</th>
                    <td>89.4%</td>
                </tr>
            </table>
        </div>
    </div>
</div>
<div class="col-md-3 collapse in" id="minihistogram-102989683663415048">
    <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAABLCAYAAAA1fMjoAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAPYQAAD2EBqD%2BnaQAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAAQlJREFUeJzt1cEJAlEQBUEVQzIIc/JsTgaxOY13kQbB5YtU3QfepZnjzMwBeOu0egD8svPqAa8ut8fHN9v9usMS8EEgCQSCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIJxXD/iGy%2B3x8c12v%2B6whH/jg0AQCASBQBAIhOPMzOoR8Kt8EAgCgSAQCAKBIBAIAoEgEAgCgSAQCAKBIBAIAoEgEAgCgSAQCAKBIBAIAoEgEAgCgSAQCAKBIBAIAoEgEAhPBQMOkb154NMAAAAASUVORK5CYII%3D">

</div>
<div class="col-md-12 text-right">
    <a role="button" data-toggle="collapse" data-target="#descriptives-102989683663415048,#minihistogram-102989683663415048"
       aria-expanded="false" aria-controls="collapseExample">
        Toggle details
    </a>
</div>
<div class="row collapse col-md-12" id="descriptives-102989683663415048">
    <ul class="nav nav-tabs" role="tablist">
        <li role="presentation" class="active"><a href="#quantiles-102989683663415048"
                                                  aria-controls="quantiles-102989683663415048" role="tab"
                                                  data-toggle="tab">Statistics</a></li>
        <li role="presentation"><a href="#histogram-102989683663415048" aria-controls="histogram-102989683663415048"
                                   role="tab" data-toggle="tab">Histogram</a></li>
        <li role="presentation"><a href="#common-102989683663415048" aria-controls="common-102989683663415048"
                                   role="tab" data-toggle="tab">Common Values</a></li>
        <li role="presentation"><a href="#extreme-102989683663415048" aria-controls="extreme-102989683663415048"
                                   role="tab" data-toggle="tab">Extreme Values</a></li>

    </ul>

    <div class="tab-content">
        <div role="tabpanel" class="tab-pane active row" id="quantiles-102989683663415048">
            <div class="col-md-4 col-md-offset-1">
                <p class="h4">Quantile statistics</p>
                <table class="stats indent">
                    <tr>
                        <th>Minimum</th>
                        <td>0</td>
                    </tr>
                    <tr>
                        <th>5-th percentile</th>
                        <td>0</td>
                    </tr>
                    <tr>
                        <th>Q1</th>
                        <td>0</td>
                    </tr>
                    <tr>
                        <th>Median</th>
                        <td>0</td>
                    </tr>
                    <tr>
                        <th>Q3</th>
                        <td>0</td>
                    </tr>
                    <tr>
                        <th>95-th percentile</th>
                        <td>1</td>
                    </tr>
                    <tr>
                        <th>Maximum</th>
                        <td>7</td>
                    </tr>
                    <tr>
                        <th>Range</th>
                        <td>7</td>
                    </tr>
                    <tr>
                        <th>Interquartile range</th>
                        <td>0</td>
                    </tr>
                </table>
            </div>
            <div class="col-md-4 col-md-offset-2">
                <p class="h4">Descriptive statistics</p>
                <table class="stats indent">
                    <tr>
                        <th>Standard deviation</th>
                        <td>0.33623</td>
                    </tr>
                    <tr>
                        <th>Coef of variation</th>
                        <td>3.0479</td>
                    </tr>
                    <tr>
                        <th>Kurtosis</th>
                        <td>16.168</td>
                    </tr>
                    <tr>
                        <th>Mean</th>
                        <td>0.11032</td>
                    </tr>
                    <tr>
                        <th>MAD</th>
                        <td>0.19758</td>
                    </tr>
                    <tr class="">
                        <th>Skewness</th>
                        <td>3.4018</td>
                    </tr>
                    <tr>
                        <th>Sum</th>
                        <td>28291</td>
                    </tr>
                    <tr>
                        <th>Variance</th>
                        <td>0.11305</td>
                    </tr>
                    <tr>
                        <th>Memory size</th>
                        <td>2.0 MiB</td>
                    </tr>
                </table>
            </div>
        </div>
        <div role="tabpanel" class="tab-pane col-md-8 col-md-offset-2" id="histogram-102989683663415048">
            <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAlgAAAGQCAYAAAByNR6YAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAPYQAAD2EBqD%2BnaQAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAIABJREFUeJzt3XtU1XW%2B//EXsFE2oIIp2rSco6NQx3RGBhRvccYLOZqY4YUpF2N2OwVJeBQ9pqaj4WVEK3V0THMsZS0pRys9eGk6po4ZXjIzRxwwbx1KUEABYQTh90c/9jmEjbj9yHbzfT7WYq325/vdn/1%2BbVNf7P1141FdXV0tAAAAGOPp6gEAAAAaGwoWAACAYRQsAAAAwyhYAAAAhlGwAAAADKNgAQAAGEbBAgAAMIyCBQAAYBgFCwAAwDAKFgAAgGEULAAAAMMoWAAAAIZRsAAAAAyjYAEAABhGwQIAADCMggUAAGAYBQsAAMAwChYAAIBhFCwAAADDKFgAAACGUbAAAAAMo2ABAAAYRsECAAAwjIIFAABgGAULAADAMAoWAACAYRQsAAAAwyhYAAAAhlGwAAAADKNgAQAAGEbBAgAAMIyCBQAAYBgFCwAAwDAKFgAAgGEULAAAAMMoWAAAAIZRsAAAAAyjYAEAABhGwQIAADDM5uoBrCI/v9j4np6eHmrZ0k8FBaWqqqo2vv/ditzWyi1ZN7tVc0vWzU5u87lbt25mdL/64hUsN%2Bbp6SEPDw95enq4epQGRW5r5Zasm92quSXrZid348lNwQIAADCMggUAAGAYBQsAAMAwChYAAIBhFCwAAADDKFgAAACGUbAAAAAMo2ABAAAYRsECAAAwjIIFAABgGAULAADAMAoWAACAYRQsAAAAw2yuHgC3J3zadlePUG/bkvq4egQAABoEr2ABAAAYRsECAAAwjIIFAABgGAULAADAMAoWAACAYRQsAAAAwyhYAAAAhlGwAAAADKNgAQAAGEbBAgAAMIyCBQAAYBgFCwAAwDAKFgAAgGEULAAAAMMoWAAAAIZRsAAAAAyjYAEAABhGwQIAADCMggUAAGAYBQsAAMAwChYAAIBhFCwAAADDKFgAAACGUbAAAAAMo2ABAAAYRsECAAAwjIIFAABgGAULAADAMAoWAACAYRQsAAAAwyhYAAAAhlGwAAAADKNgAQAAGEbBAgAAMMxlBSsrK0vjxo1Tjx491KdPH02ePFkFBQWSpKNHj2rUqFEKDQ1V//799d5779W67%2BbNmxUVFaVu3bopJiZGR44ccRy7fv26FixYoN69eys0NFQvvPCC8vLyHMcvXbqk%2BPh4hYeHKyIiQikpKaqsrHQcv9ljAwAA3IxLClZ5ebmeeeYZhYaG6q9//au2bt2qoqIivfzyy7p8%2BbKee%2B45DR8%2BXAcPHlRKSormzZunL7/8UpKUmZmpOXPmaP78%2BTp48KCGDRumF154QWVlZZKkFStWaN%2B%2Bffrzn/%2BsvXv3ysfHR9OnT3c8dlJSknx9fbV3715t3LhR%2B/fv19q1ayXppo8NAABQHy4pWLm5uXrggQeUkJCgJk2aKDAwULGxsTp48KB27typgIAAjRkzRjabTb169VJ0dLTS0tIkSe%2B9954eeeQRhYWFydvbW08%2B%2BaQCAwOVkZHhOP7ss8/q3nvvlb%2B/v6ZNm6Y9e/bo/PnzOnv2rA4cOKDk5GTZ7Xa1a9dO8fHxjr1v9tgAAAD14ZKC9bOf/UyrV6%2BWl5eXY23Hjh168MEHlZ2drZCQkFrnd%2BrUSVlZWZKknJycHz1eXFys7777rtbxVq1aqUWLFjp58qSys7MVEBCgNm3aOI537NhRubm5unLlyk0fGwAAoD5srh6gurpar7/%2Bunbt2qX169frnXfekd1ur3WOj4%2BPrl69KkkqLS390eOlpaWSJF9f3zrHa4798L41t2vu/88eu77y8vKUn59fa81m81VQUNAt7XMzXl7u9W8UbDYz89bkdrf8t8uquSXrZrdqbsm62cndeHK7tGCVlJRo6tSpOn78uNavX6/7779fdrtdxcXFtc4rLy%2BXn5%2BfpO8LUXl5eZ3jgYGBjnJUcz3WD%2B9fXV1d51jNbT8/v5s%2Bdn2lp6dr2bJltdYSEhKUmJh4S/s0NoGBt/Y83kzz5vabn9QIWTW3ZN3sVs0tWTc7ud2fywrWuXPn9Oyzz%2BonP/mJNm7cqJYtW0qSQkJCtG/fvlrn5uTkKDg4WJIUHBys7OzsOscjIyPVokULtWnTptbbiPn5%2BSoqKlJISIiqqqpUVFSkixcvqlWrVpKkU6dOqW3btmrWrNlNH7u%2BYmNj1b9//1prNpuvCgtLb2mfm3G3pm8qv5eXp5o3t%2BvKlTJdv15lZE93YNXcknWzWzW3ZN3s5Daf2/Q39/XlkoJ1%2BfJljR07Vj179lRKSoo8Pf%2B3KERFRWnhwoVau3atxowZo8OHD2vLli1avny5JGnkyJFKSEjQ4MGDFRYWprS0NF26dElRUVGSpJiYGK1YsUJdu3ZVYGCg5s6dqx49euinP/2pJCksLExz587V7NmzVVhYqOXLl2vkyJH1euz6CgoKqvN2YH5%2BsSorrfOb5UZM579%2BvcqSz6lVc0vWzW7V3JJ1s5Pb/bmkYG3atEm5ubnatm2btm/fXuvYkSNHtGbNGqWkpGjJkiVq2bKlpk%2Bfrp49e0qSevXqpZkzZ2rWrFm6cOGCOnXqpFWrVikgIEDS92/FVVZWasyYMSotLVVERIRef/11x/5LlizR7NmzNWDAAHl6emr48OGKj4%2BXJAUGBv7TxwYAAKgPj%2Brq6mpXD2EF%2BfnFNz/pFtlsnopK3Wt83ztlW1IfI/vYbJ4KDPRTYWFpo/lOpz6smluybnar5pasm53c5nO3bt3M6H715V4X8QAAALgBChYAAIBhFCwAAADDKFgAAACGUbAAAAAMo2ABAAAYRsECAAAwjIIFAABgGAULAADAMAoWAACAYRQsAAAAwyhYAAAAhlGwAAAADKNgAQAAGEbBAgAAMIyCBQAAYBgFCwAAwDAKFgAAgGEULAAAAMMoWAAAAIZRsAAAAAyjYAEAABhGwQIAADCMggUAAGAYBQsAAMAwChYAAIBhFCwAAADDKFgAAACGUbAAAAAMo2ABAAAYRsECAAAwjIIFAABgGAULAADAMAoWAACAYRQsAAAAwyhYAAAAhlGwAAAADKNgAQAAGEbBAgAAMIyCBQAAYBgFCwAAwDAKFgAAgGEULAAAAMMoWAAAAIZRsAAAAAyjYAEAABhGwQIAADCMggUAAGAYBQsAAMAwChYAAIBhFCwAAADDKFgAAACGUbAAAAAMo2ABAAAYRsECAAAwjIIFAABg2F1RsAoKChQVFaXMzEzH2syZM9WlSxeFhoY6vtLT0x3HV61apcjISHXr1k1xcXH6%2BuuvHceuXr2qqVOnKiIiQmFhYZo8ebJKS0sdx0%2BfPq2xY8cqNDRUffv21R//%2BMda8%2BzevVvR0dHq1q2bBg8erF27dt3B9AAAoLFxecE6fPiwYmNjde7cuVrrx44d05w5c3TkyBHHV2xsrCRp8%2BbNWrdund566y1lZmbqwQcfVGJioqqrqyVJc%2BbM0bfffqsdO3Zo586d%2Bvbbb5WamipJqqio0PPPP6%2BuXbsqMzNTb775ptLS0rRt2zZJ0pkzZzR%2B/Hi99NJLOnTokMaPH6%2BkpCRduHChAZ8VAADgzlxasDZv3qxJkyZpwoQJtdavXbumv//97%2BrSpcsN7/fuu%2B/qiSeeUHBwsJo2baqJEycqNzdXmZmZKisr05YtW5SYmKiAgADdc889mjRpkjZt2qSysjIdPHhQeXl5SkxMVJMmTdS5c2fFxcUpLS3NMVN4eLgGDhwom82mIUOGqHv37rVePQMAAPhnXFqw%2Bvbtq48%2B%2BkhDhgyptZ6VlaXKykotWbJEvXv31qBBg/Tmm2%2BqqqpKkpSTk6OQkBDH%2Bd7e3mrfvr2ysrJ09uxZVVRU1DresWNHlZeX68yZM8rOzlaHDh3UpEkTx/FOnTopKyvrhnv/8DgAAMDN2Fz54K1bt77henFxsXr06KG4uDgtXrxYJ06cUEJCgjw9PfXMM8%2BotLRUdru91n18fHx09epVlZSUSJJ8fX0dx2rOLS0tveF97Xa7rl696jjnx/aur7y8POXn59das9l8FRQUVO896sPLy%2BXv8N4Sm83MvDW53S3/7bJqbsm62a2aW7JudnI3ntwuLVg/pk%2BfPurTp4/j9s9//nONHTtWGRkZeuaZZ2S321VeXl7rPuXl5fLz83MUq7KyMvn5%2BTn%2BW5L8/f3l6%2BvruF3j/577z/aur/T0dC1btqzWWkJCghITE%2Bu9R2MUGFj/57A%2Bmje33/ykRsiquSXrZrdqbsm62cnt/u7KgvWXv/xFFy9e1G9%2B8xvH2rVr1%2BTj4yNJCg4OVnZ2tvr16yfp%2BwvXz5w5o5CQEHXo0EHe3t7KycnRL37xC0nSqVOnHG8jXrp0SWfOnFFlZaVstu/j5%2BTkKDg4WJIUEhKi48eP15onJyfnR68Hu5HY2Fj179%2B/1prN5qvCwtIfuYdz3K3pm8rv5eWp5s3tunKlTNevVxnZ0x1YNbdk3exWzS1ZNzu5zec2/c19fd2VBau6ulrz5s3Tv/zLv6hnz5764osv9M4772jq1KmSpBEjRmjp0qWKjIxUhw4d9Nprr6lVq1YKDw%2BXt7e3Bg8erNTUVL3xxhuSpNTUVA0dOlQ%2BPj6KiIhQYGCgFi1apKSkJJ0%2BfVrr1q1zXGg/bNgw/elPf1JGRoYefvhh7dy5UwcOHNC0adPqPX9QUFCdtwPz84tVWWmd3yw3Yjr/9etVlnxOrZpbsm52q%2BaWrJud3O7vrixYUVFRmjp1qmbNmqULFy6oVatWGj9%2BvB599FFJ0siRI1VcXKyEhAQVFBSoa9euWrlypby9vSV9/xlaCxYsUHR0tCoqKjRgwADNmDFDkmSz2bRmzRrNnj1bffr0ka%2Bvr%2BLi4hQTEyPp%2Bwvi//CHPyg1NVXTpk3Tfffdp6VLl6pDhw6ueTIAAIDb8aiu%2BfAo3FH5%2BcXG97TZPBWVutf4vnfKtqQ%2BNz%2BpHmw2TwUG%2BqmwsLTRfKdTH1bNLVk3u1VzS9bNTm7zuVu3bmZ0v/py6iKe69evm54DAACg0XCqYEVGRur3v/%2B9cnJyTM8DAADg9pwqWC%2B%2B%2BKI%2B//xzDR06VKNGjdKGDRtUXGz%2BLTAAAAB35FTBevzxx7VhwwZt375dvXv31qpVq9S3b19NnDhRn376qekZAQAA3MptfZBS%2B/btNWHCBG3fvl0JCQn6%2BOOP9fTTT6t///7605/%2BxLVaAADAkm7rYxqOHj2q999/XxkZGbp27ZqioqIUExOjCxcu6I033tCxY8e0ePFiU7MCAAC4BacK1vLly/XBBx/o7Nmz6tq1qyZMmKChQ4fK39/fcY6Xl5deeeUVY4MCAAC4C6cK1vr16zVs2DCNHDlSnTp1uuE5HTt21KRJk25rOAAAAHfkVMHas2ePSkpKVFRU5FjLyMhQr169FBgYKEnq3LmzOnfubGZKAAAAN%2BLURe5/%2B9vfNGjQIKWnpzvWFi5cqOjoaP397383NhwAAIA7cqpg/f73v9fDDz/s%2BAHJkvSXv/xFkZGRmj9/vrHhAAAA3JFTBev48eN67rnn1KRJE8eal5eXnnvuOX3xxRfGhgMAAHBHThUsf39/nTt3rs76d999Jx8fn9seCgAAwJ05VbAGDRqkWbNm6dNPP1VJSYlKS0v12Wefafbs2YqKijI9IwAAgFtx6l8RTpw4UefPn9dTTz0lDw8Px3pUVJQmT55sbDgAAAB35FTBstvtWrlypU6fPq2TJ0/K29tbHTt2VPv27Q2PBwAA4H5u60fldOjQQR06dDA1CwAAQKPgVME6ffq0Zs%2BercOHD6uioqLO8RMnTtz2YAAAAO7KqYI1a9Ys5ebmatKkSWrWrJnpmQAAANyaUwXryJEjevvttxUaGmp6HgAAALfn1Mc0BAYGys/Pz/QsAAAAjYJTBSsuLk6LFy9WcXGx6XkAAADcnlNvEe7evVtffPGFIiIidM8999T6kTmS9PHHHxsZDgAAwB05VbAiIiIUERFhehYAAIBGwamC9eKLL5qeAwAAoNFw6hosScrKytLUqVP1m9/8RhcuXFBaWpoyMzNNzgYAAOCWnCpYX331lUaNGqVvvvlGX331la5du6YTJ07oqaee0q5du0zPCAAA4FacKlipqal66qmntG7dOnl7e0uSXn31Vf32t7/VsmXLjA4IAADgbpx%2BBWv48OF11h9//HF9/fXXtz0UAACAO3OqYHl7e6ukpKTOem5urux2%2B20PBQAA4M6cKlgDBw7UokWLVFhY6Fg7deqUUlJS9Ktf/crUbAAAAG7JqYI1ZcoUlZeXq3fv3iorK1NMTIyGDh0qm82myZMnm54RAADArTj1OVj%2B/v7asGGD9u/fr7/97W%2BqqqpSSEiIHnroIXl6Ov3JDwAAAI2CUwWrRq9evdSrVy9TswAAADQKThWs/v37y8PD40eP87MIAQCAlTlVsB577LFaBauiokJnz57Vnj17lJSUZGw4AAAAd%2BRUwRo/fvwN19evX6/Dhw/rt7/97W0NBQAA4M6MXpHer18/7d692%2BSWAAAAbsdowTpw4ICaNm1qcksAAAC349RbhD98C7C6ulolJSU6efIkbw8CAADLc6pg/eQnP6nzrwi9vb01duxYRUdHGxkMAADAXTlVsObPn296DgAAgEbDqYJ18ODBep/bvXt3Zx4CAADAbTlVsJ588klVV1c7vmrUvG1Ys%2Bbh4aETJ04YGBMAAMB9OFWwli5dqnnz5mnKlCnq2bOnvL29dfToUc2aNUtPPPGE%2BvXrZ3pOAAAAt%2BHUxzQsWLBAM2fO1MCBA%2BXv76%2BmTZuqR48emj17ttasWaP77rvP8QUAAGA1ThWsvLw83XvvvXXW/f39VVhYeNtDAQAAuDOnCla3bt20ePFilZSUONaKioq0cOFC9erVy9hwAAAA7sipa7CmT5%2BusWPHKjIyUu3bt5cknT59Wq1bt9Y777xjcj4AAAC341TB6tixozIyMrRlyxadOnVKkvTEE0/okUcekd1uNzogAACAu3GqYElS8%2BbNNWrUKH3zzTdq166dpO8/zR0AAMDqnLoGq7q6WqmpqerevbuGDh2q7777TlOmTNHUqVNVUVFhekYAAAC34lTBWrdunT744APNnDlTTZo0kSQNHDhQ//3f/6033njD6IAAAADuxqmClZ6erldeeUUxMTGOT28fMmSIUlJS9F//9V9GBwQAAHA3ThWsb775Rv/6r/9aZ/3%2B%2B%2B/XxYsXb3soAAAAd%2BZUwbrvvvv05Zdf1lnfvXu344J3AAAAq3LqXxE%2B/fTT%2Bt3vfqcLFy6ourpa%2B/fv14YNG7Ru3TpNnTrV9IwAAABuxalXsEaMGKH/%2BI//0Ntvv63y8nK98sorev/99zVhwgQ9/vjjt7RXQUGBoqKilJmZ6Vg7evSoRo0apdDQUPXv31/vvfderfts3rxZUVFR6tatm2JiYnTkyBHHsevXr2vBggXq3bu3QkND9cILLygvL89x/NKlS4qPj1d4eLgiIiKUkpKiysrKej82AADAzThVsD788EP9%2Bte/1ieffKJPP/1U%2B/bt0759%2BzRu3Lhb2ufw4cOKjY3VuXPnHGuXL1/Wc889p%2BHDh%2BvgwYNKSUnRvHnzHG9JZmZmas6cOZo/f74OHjyoYcOG6YUXXlBZWZkkacWKFdq3b5/%2B/Oc/a%2B/evfLx8dH06dMd%2ByclJcnX11d79%2B7Vxo0btX//fq1du7Zejw0AAFAfThWsV1991XExe8uWLXXPPffc8h6bN2/WpEmTNGHChFrrO3fuVEBAgMaMGSObzaZevXopOjpaaWlpkqT33ntPjzzyiMLCwuTt7a0nn3xSgYGBysjIcBx/9tlnde%2B998rf31/Tpk3Tnj17dP78eZ09e1YHDhxQcnKy7Ha72rVrp/j4eMfeN3tsAACA%2BnDqGqz27dvr5MmT6tixo9MP3LdvX0VHR8tms9UqWdnZ2QoJCal1bqdOnbRx40ZJUk5OjkaMGFHneFZWloqLi/Xdd9/Vun%2BrVq3UokULnTx5UpIUEBCgNm3aOI537NhRubm5unLlyk0fu77y8vKUn59fa81m81VQUNAt7XMzXl5O9WOXsdnMzFuT293y3y6r5pasm92quSXrZid348ntVMEKDg7WpEmTtHr1arVv315NmzatdXzevHk33aN169Y3XC8tLa3z8wx9fHx09erVmx4vLS2VJPn6%2BtY5XnPsh/etuV1z/3/22PWVnp6uZcuW1VpLSEhQYmLiLe3T2AQG%2Bhndr3lza/7cS6vmlqyb3aq5JetmJ7f7c6pgnTt3TmFhYZJU55Wa22W321VcXFxrrby8XH5%2Bfo7j5eXldY4HBgY6ylHN9Vg/vH91dXWdYzW3/fz8bvrY9RUbG6v%2B/fvXWrPZfFVYWHpL%2B9yMuzV9U/m9vDzVvLldV66U6fr1KiN7ugOr5pasm92quSXrZie3%2Bdymv7mvr3oXrHnz5umll16Sr6%2Bv1q1bd8cGCgkJ0b59%2B2qt5eTkKDg4WNL3r55lZ2fXOR4ZGakWLVqoTZs2ysnJcbzVl5%2Bfr6KiIoWEhKiqqkpFRUW6ePGiWrVqJUk6deqU2rZtq2bNmt30sesrKCioztuB%2BfnFqqy0zm%2BWGzGd//r1Kks%2Bp1bNLVk3u1VzS9bNTm73V%2B%2BXQN555506r/48/fTTtT4CwYSoqChdvHhRa9euVUVFhT777DNt2bLFcd3VyJEjtWXLFn322WeqqKjQ2rVrdenSJUVFRUmSYmJitGLFCp0/f14lJSWaO3euevTooZ/%2B9Kdq3769wsLCNHfuXJWUlOj8%2BfNavny5Ro4cWa/HBgAAqI96v4JVXV1dZ%2B3zzz/XP/7xD6MDBQYGas2aNUpJSdGSJUvUsmVLTZ8%2BXT179pQk9erVSzNnztSsWbN04cIFderUSatWrVJAQICk7691qqys1JgxY1RaWqqIiAi9/vrrjv2XLFmi2bNna8CAAfL09NTw4cMVHx9fr8cGAACoD4/qGzWnG3jggQe0b9%2B%2BWh/JEBoaqg8//JAfj1MP%2BfnFNz/pFtlsnopK3Wt83ztlW1IfI/vYbJ4KDPRTYWFpo3kpuT6smluybnar5pasm53c5nO3bt3M6H715V5XSQMAALiBWypYHh4ed2oOAACARuOWPqbh1VdfrfWZVxUVFVq4cGGdjzGoz%2BdgAQAANFb1Lljdu3ev85lXoaGhKiwsVGFhofHBAAAA3FW9C9ad/OwrAACAxoSL3AEAAAyjYAEAABhGwQIAADCMggUAAGAYBQsAAMAwChYAAIBhFCwAAADDKFgAAACGUbAAAAAMo2ABAAAYRsECAAAwjIIFAABgGAULAADAMAoWAACAYRQsAAAAwyhYAAAAhlGwAAAADKNgAQAAGEbBAgAAMIyCBQAAYBgFCwAAwDAKFgAAgGEULAAAAMMoWAAAAIZRsAAAAAyjYAEAABhGwQIAADCMggUAAGAYBQsAAMAwChYAAIBhFCwAAADDKFgAAACGUbAAAAAMo2ABAAAYRsECAAAwjIIFAABgGAULAADAMAoWAACAYRQsAAAAwyhYAAAAhlGwAAAADKNgAQAAGEbBAgAAMIyCBQAAYBgFCwAAwDAKFgAAgGEULAAAAMMoWAAAAIZRsAAAAAyjYAEAABhGwQIAADDsri1YGRkZ6ty5s0JDQx1fycnJkqTdu3crOjpa3bp10%2BDBg7Vr165a9121apUiIyPVrVs3xcXF6euvv3Ycu3r1qqZOnaqIiAiFhYVp8uTJKi0tdRw/ffq0xo4dq9DQUPXt21d//OMfGyYwAABoNO7agnXs2DE9%2BuijOnLkiONr4cKFOnPmjMaPH6%2BXXnpJhw4d0vjx45WUlKQLFy5IkjZv3qx169bprbfeUmZmph588EElJiaqurpakjRnzhx9%2B%2B232rFjh3bu3Klvv/1WqampkqSKigo9//zz6tq1qzIzM/Xmm28qLS1N27Ztc9nzAAAA3M9dXbC6dOlSZ33z5s0KDw/XwIEDZbPZNGTIEHXv3l3p6emSpHfffVdPPPGEgoOD1bRpU02cOFG5ubnKzMxUWVmZtmzZosTERAUEBOiee%2B7RpEmTtGnTJpWVlengwYPKy8tTYmKimjRpos6dOysuLk5paWkNHR8AALixu7JgVVVV6fjx4/rkk0/Ur18/RUZGasaMGbp8%2BbJycnIUEhJS6/xOnTopKytLkuoc9/b2Vvv27ZWVlaWzZ8%2BqoqKi1vGOHTuqvLxcZ86cUXZ2tjp06KAmTZrccG8AAID6sLl6gBspKChQ586dNWjQIC1ZskSFhYWaMmWKkpOTde3aNdnt9lrn%2B/j46OrVq5Kk0tLSHz1eUlIiSfL19XUcqzm3tLT0hve12%2B2OvesrLy9P%2Bfn5tdZsNl8FBQXd0j434%2BV1V/bjH2WzmZm3Jre75b9dVs0tWTe7VXNL1s1O7saT%2B64sWK1atar1tpzdbldycrJGjx6tiIgIlZeX1zq/vLxcfn5%2BjnN/7HhNsSorK3OcX1ZWJkny9/eXr6%2Bv43aN/3tufaWnp2vZsmW11hISEpSYmHhL%2BzQ2gYG39jzeTPPm9puf1AhZNbdk3exWzS1ZNzu53d9dWbCysrK0detWTZw4UR4eHpKka9euydPTUz//%2Bc914sSJWufn5OQ4rtcKDg5Wdna2%2BvXrJ%2Bn7C9fPnDmjkJAQdejQQd7e3srJydEvfvELSdKpU6ccbyNeunRJZ86cUWVlpWw2m2Pv4ODgW5o/NjZW/fv3r7Vms/mqsLD0R%2B7hHHdr%2Bqbye3l5qnlzu65cKdP161VG9nQHVs0tWTe7VXNL1s1ObvO5TX9zX193ZcEKCAhQWlqaWrRooXHjxikvL08LFy7UY489puHDh%2Bvtt99WRkaGHn74Ye3cuVMHDhzQtGnTJEkjRozQ0qVLFRkZqQ4dOui1115Tq1atFB4eLm9vbw0ePFipqal64403JEmpqakaOnSofHx8FBERocDAQC1atEhJSUk6ffq01q1bpwkTJtzS/EFBQXXeDszPL1ZpqBE0AAAK6klEQVRlpXV%2Bs9yI6fzXr1dZ8jm1am7JutmtmluybnZyu7%2B7smC1bdtWK1eu1OLFi7VixQo1bdpUjzzyiJKTk9W0aVP94Q9/UGpqqqZNm6b77rtPS5cuVYcOHSRJI0eOVHFxsRISElRQUKCuXbtq5cqV8vb2liTNnDlTCxYsUHR0tCoqKjRgwADNmDFDkmSz2bRmzRrNnj1bffr0ka%2Bvr%2BLi4hQTE%2BOy5wIAALgfj%2BqaD4jCHZWfX2x8T5vNU1Gpe43ve6dsS%2BpjZB%2BbzVOBgX4qLCxtNN/p1IdVc0vWzW7V3JJ1s5PbfO7WrZsZ3a%2B%2B3OsiHgAAADdAwQIAADCMggUAAGAYBQsAAMAwChYAAIBhFCwAAADDKFgAAACGUbAAAAAMo2ABAAAYRsECAAAwjIIFAABgGAULAADAMAoWAACAYRQsAAAAwyhYAAAAhlGwAAAADKNgAQAAGEbBAgAAMIyCBQAAYBgFCwAAwDAKFgAAgGEULAAAAMMoWAAAAIZRsAAAAAyjYAEAABhGwQIAADCMggUAAGCYzdUDwDoGv77P1SPckm1JfVw9AgDATfEKFgAAgGEULAAAAMMoWAAAAIZRsAAAAAyjYAEAABhGwQIAADCMggUAAGAYBQsAAMAwChYAAIBhFCwAAADDKFgAAACGUbAAAAAMo2ABAAAYRsECAAAwjIIFAABgGAULAADAMAoWAACAYRQsAAAAwyhYAAAAhlGwAAAADKNgAQAAGEbBAgAAMIyCBQAAYBgFCwAAwDAKFgAAgGEULAAAAMMoWAAAAIZRsAAAAAyjYN3ApUuXFB8fr/DwcEVERCglJUWVlZWuHgsAALgJCtYNJCUlydfXV3v37tXGjRu1f/9%2BrV271tVjAQAAN0HB%2BoGzZ8/qwIEDSk5Olt1uV7t27RQfH6%2B0tDRXjwYAANwEBesHsrOzFRAQoDZt2jjWOnbsqNzcXF25csWFkwEAAHdhc/UAd5vS0lLZ7fZaazW3r169qubNm990j7y8POXn59das9l8FRQUZG5QSV5e9OM7afDr%2B1w9wi35aNJDrh7hjqn5f91q/89bNbdk3ezkbjy5KVg/4Ovrq7KyslprNbf9/PzqtUd6erqWLVtWa%2B3FF1/U%2BPHjzQz5/%2BXl5Wls22zFxsYaL293s7y8PKWnp5PbQvLy8vT226stl92quSXrZid348ndeKqiIcHBwSoqKtLFixcda6dOnVLbtm3VrFmzeu0RGxurTZs21fqKjY01Pmt%2Bfr6WLVtW59Wyxo7c1sotWTe7VXNL1s1O7saTm1ewfqB9%2B/YKCwvT3LlzNXv2bBUWFmr58uUaOXJkvfcICgpqNA0cAADcOl7BuoElS5aosrJSAwYM0OjRo/XQQw8pPj7e1WMBAAA3wStYN9CqVSstWbLE1WMAAAA35TVr1qxZrh4CzvPz81OPHj3qfQF%2BY0Fua%2BWWrJvdqrkl62Ynd%2BPI7VFdXV3t6iEAAAAaE67BAgAAMIyCBQAAYBgFCwAAwDAKFgAAgGEULAAAAMMoWAAAAIZRsAAAAAyjYAEAABhGwXJTly5dUnx8vMLDwxUREaGUlBRVVla6eqwGU1BQoKioKGVmZrp6lAaRlZWlcePGqUePHurTp48mT56sgoICV4/VIPbv369Ro0bpl7/8pfr06aM5c%2BaovLzc1WM1iOvXrysuLk7/%2BZ//6epRGkxGRoY6d%2B6s0NBQx1dycrKrx7rjioqKNHnyZEVERKh79%2B6Kj49XXl6eq8e64z788MNav9ahoaHq0qWLunTp4urRbhsFy00lJSXJ19dXe/fu1caNG7V//36tXbvW1WM1iMOHDys2Nlbnzp1z9SgNory8XM8884xCQ0P117/%2BVVu3blVRUZFefvllV492xxUUFOjf//3f9fjjj%2BvQoUPavHmzDhw4oDfffNPVozWIZcuW6dChQ64eo0EdO3ZMjz76qI4cOeL4WrhwoavHuuPGjx%2Bvq1ev6qOPPtKuXbvk5eWlGTNmuHqsO27YsGG1fq23b9%2BugIAApaSkuHq020bBckNnz57VgQMHlJycLLvdrnbt2ik%2BPl5paWmuHu2O27x5syZNmqQJEya4epQGk5ubqwceeEAJCQlq0qSJAgMDFRsbq4MHD7p6tDuuZcuW%2BvTTTxUTEyMPDw8VFRXpH//4h1q2bOnq0e64/fv3a%2BfOnXr44YddPUqDOnbsWKN49eJWfPXVVzp69Kjmz5%2Bv5s2by9/fX3PmzNGkSZNcPVqDqq6uVnJysn71q1/p0UcfdfU4t42C5Yays7MVEBCgNm3aONY6duyo3NxcXblyxYWT3Xl9%2B/bVRx99pCFDhrh6lAbzs5/9TKtXr5aXl5djbceOHXrwwQddOFXD8ff3lyT927/9m6Kjo9W6dWvFxMS4eKo769KlS5o2bZoWLVoku93u6nEaTFVVlY4fP65PPvlE/fr1U2RkpGbMmKHLly%2B7erQ76ssvv1SnTp307rvvKioqSn379tWCBQvUunVrV4/WoD744APl5OQ0mrfEKVhuqLS0tM4fujW3r1696oqRGkzr1q1ls9lcPYbLVFdX67XXXtOuXbs0bdo0V4/ToHbu3Kk9e/bI09NTiYmJrh7njqmqqlJycrLGjRunBx54wNXjNKiCggJ17txZgwYNUkZGhjZs2KAzZ840%2BmuwLl%2B%2BrJMnT%2BrMmTPavHmz3n//fV24cEFTpkxx9WgNpqqqSitWrNDzzz/v%2BKbK3Vn3byo35uvrq7KyslprNbf9/PxcMRIaQElJiaZOnarjx49r/fr1uv/%2B%2B109UoPy8fGRj4%2BPkpOTNWrUKF2%2BfFktWrRw9VjGrVy5Uk2aNFFcXJyrR2lwrVq1qnWpg91uV3JyskaPHq2SkpJG8xfvDzVp0kSSNG3aNDVt2lT%2B/v5KSkrS6NGjVVpaaok/1zMzM5WXl6eRI0e6ehRjeAXLDQUHB6uoqEgXL150rJ06dUpt27ZVs2bNXDgZ7pRz585pxIgRKikp0caNGy1Trj7//HP9%2Bte/1rVr1xxr165dk7e3d6N96%2ByDDz7QgQMHFB4ervDwcG3dulVbt25VeHi4q0e747KyspSamqrq6mrH2rVr1%2BTp6ekoIY1Rp06dVFVVpYqKCsdaVVWVJNV6LhqzHTt2KCoqSr6%2Bvq4exRgKlhtq3769wsLCNHfuXJWUlOj8%2BfNavnx5o2r%2B%2BF%2BXL1/W2LFj9ctf/lJvvfWWJS7wrnH//fervLxcixYt0rVr1/Q///M/WrBggUaOHNlo/8Ldvn27Pv/8cx06dEiHDh3S0KFDNXToUEv8a8KAgAClpaVp9erVqqysVG5urhYuXKjHHnus0f56S1Lv3r3Vrl07vfzyyyotLVVBQYFee%2B01DRw4sNG%2BavdDhw8fVvfu3V09hlEULDe1ZMkSVVZWasCAARo9erQeeughxcfHu3os3AGbNm1Sbm6utm3bprCwsFqfF9PY%2Bfn5afXq1crOzlafPn0UFxen3r17W%2BIjKqyobdu2WrlypT7%2B%2BGP16NFDI0aMUNeuXfXKK6%2B4erQ7ytvbW%2BvWrZOXl5cGDRqkQYMGqW3btpo7d66rR2sw33zzjYKCglw9hlEe1VZ5/REAAKCB8AoWAACAYRQsAAAAwyhYAAAAhlGwAAAADKNgAQAAGEbBAgAAMIyCBQAAYBgFCwAAwDAKFgAAgGEULAAAAMMoWAAAAIZRsAAAAAyjYAEAABhGwQIAADCMggUAAGDY/wMgUk8UaRuREQAAAABJRU5ErkJggg%3D%3D"/>
        </div>
        <div role="tabpanel" class="tab-pane col-md-12" id="common-102989683663415048">

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">0.0</td>
        <td class="number">229661</td>
        <td class="number">89.4%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">1.0</td>
        <td class="number">25605</td>
        <td class="number">10.0%</td>
        <td>
            <div class="bar" style="width:12%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">2.0</td>
        <td class="number">957</td>
        <td class="number">0.4%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">3.0</td>
        <td class="number">180</td>
        <td class="number">0.1%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">4.0</td>
        <td class="number">33</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">5.0</td>
        <td class="number">15</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">6.0</td>
        <td class="number">3</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">7.0</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="missing">
        <td class="fillremaining">(Missing)</td>
        <td class="number">529</td>
        <td class="number">0.2%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr>
</table>
        </div>
        <div role="tabpanel" class="tab-pane col-md-12"  id="extreme-102989683663415048">
            <p class="h4">Minimum 5 values</p>

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">0.0</td>
        <td class="number">229661</td>
        <td class="number">89.4%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">1.0</td>
        <td class="number">25605</td>
        <td class="number">10.0%</td>
        <td>
            <div class="bar" style="width:12%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">2.0</td>
        <td class="number">957</td>
        <td class="number">0.4%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">3.0</td>
        <td class="number">180</td>
        <td class="number">0.1%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">4.0</td>
        <td class="number">33</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr>
</table>
            <p class="h4">Maximum 5 values</p>

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">3.0</td>
        <td class="number">180</td>
        <td class="number">0.1%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">4.0</td>
        <td class="number">33</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:19%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">5.0</td>
        <td class="number">15</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:9%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">6.0</td>
        <td class="number">3</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">7.0</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr>
</table>
        </div>
    </div>
</div>
</div><div class="row variablerow">
    <div class="col-md-3 namecol">
        <p class="h4 pp-anchor" id="pp_var_Credit Score">Credit Score<br/>
            <small>Numeric</small>
        </p>
    </div><div class="col-md-6">
    <div class="row">
        <div class="col-sm-6">
            <table class="stats ">
                <tr>
                    <th>Distinct count</th>
                    <td>335</td>
                </tr>
                <tr>
                    <th>Unique (%)</th>
                    <td>0.1%</td>
                </tr>
                <tr class="alert">
                    <th>Missing (%)</th>
                    <td>24.0%</td>
                </tr>
                <tr class="alert">
                    <th>Missing (n)</th>
                    <td>61676</td>
                </tr>
                <tr class="ignore">
                    <th>Infinite (%)</th>
                    <td>0.0%</td>
                </tr>
                <tr class="ignore">
                    <th>Infinite (n)</th>
                    <td>0</td>
                </tr>
            </table>

        </div>
        <div class="col-sm-6">
            <table class="stats ">

                <tr>
                    <th>Mean</th>
                    <td>1251.1</td>
                </tr>
                <tr>
                    <th>Minimum</th>
                    <td>585</td>
                </tr>
                <tr>
                    <th>Maximum</th>
                    <td>7510</td>
                </tr>
                <tr class="ignore">
                    <th>Zeros (%)</th>
                    <td>0.0%</td>
                </tr>
            </table>
        </div>
    </div>
</div>
<div class="col-md-3 collapse in" id="minihistogram7653690958453503572">
    <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAABLCAYAAAA1fMjoAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAPYQAAD2EBqD%2BnaQAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAARFJREFUeJzt1sEJwkAURVGVlJQi0lPW6cki0tO4F7loQCJyzn7gbS7zr2OMcQFeup09AH7ZdPaAZ/N6//jNvi1fWAJ%2BEEgCgSAQCAKBIBAIAoEgEAgCgSAQCAKBIBAIAoEgEAgCgSAQCAKBIBAIAoEgEAgCgSAQCAKBIBAIAoEgEAgCgSAQCAKBIBAIAoEgEAgCgSAQCAKBIBAIAoEgEAgCgSAQCAKBIBAIAoEwnT2A/zWv94/f7NvyhSXH%2BUEgCASCE4u3HDmX/sF1jDHOHgG/yokFQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQC4QHxtQ/6oOiS/wAAAABJRU5ErkJggg%3D%3D">

</div>
<div class="col-md-12 text-right">
    <a role="button" data-toggle="collapse" data-target="#descriptives7653690958453503572,#minihistogram7653690958453503572"
       aria-expanded="false" aria-controls="collapseExample">
        Toggle details
    </a>
</div>
<div class="row collapse col-md-12" id="descriptives7653690958453503572">
    <ul class="nav nav-tabs" role="tablist">
        <li role="presentation" class="active"><a href="#quantiles7653690958453503572"
                                                  aria-controls="quantiles7653690958453503572" role="tab"
                                                  data-toggle="tab">Statistics</a></li>
        <li role="presentation"><a href="#histogram7653690958453503572" aria-controls="histogram7653690958453503572"
                                   role="tab" data-toggle="tab">Histogram</a></li>
        <li role="presentation"><a href="#common7653690958453503572" aria-controls="common7653690958453503572"
                                   role="tab" data-toggle="tab">Common Values</a></li>
        <li role="presentation"><a href="#extreme7653690958453503572" aria-controls="extreme7653690958453503572"
                                   role="tab" data-toggle="tab">Extreme Values</a></li>

    </ul>

    <div class="tab-content">
        <div role="tabpanel" class="tab-pane active row" id="quantiles7653690958453503572">
            <div class="col-md-4 col-md-offset-1">
                <p class="h4">Quantile statistics</p>
                <table class="stats indent">
                    <tr>
                        <th>Minimum</th>
                        <td>585</td>
                    </tr>
                    <tr>
                        <th>5-th percentile</th>
                        <td>667</td>
                    </tr>
                    <tr>
                        <th>Q1</th>
                        <td>714</td>
                    </tr>
                    <tr>
                        <th>Median</th>
                        <td>733</td>
                    </tr>
                    <tr>
                        <th>Q3</th>
                        <td>744</td>
                    </tr>
                    <tr>
                        <th>95-th percentile</th>
                        <td>7110</td>
                    </tr>
                    <tr>
                        <th>Maximum</th>
                        <td>7510</td>
                    </tr>
                    <tr>
                        <th>Range</th>
                        <td>6925</td>
                    </tr>
                    <tr>
                        <th>Interquartile range</th>
                        <td>30</td>
                    </tr>
                </table>
            </div>
            <div class="col-md-4 col-md-offset-2">
                <p class="h4">Descriptive statistics</p>
                <table class="stats indent">
                    <tr>
                        <th>Standard deviation</th>
                        <td>1762</td>
                    </tr>
                    <tr>
                        <th>Coef of variation</th>
                        <td>1.4084</td>
                    </tr>
                    <tr>
                        <th>Kurtosis</th>
                        <td>7.2647</td>
                    </tr>
                    <tr>
                        <th>Mean</th>
                        <td>1251.1</td>
                    </tr>
                    <tr>
                        <th>MAD</th>
                        <td>970.2</td>
                    </tr>
                    <tr class="">
                        <th>Skewness</th>
                        <td>3.0383</td>
                    </tr>
                    <tr>
                        <th>Sum</th>
                        <td>244350000</td>
                    </tr>
                    <tr>
                        <th>Variance</th>
                        <td>3104700</td>
                    </tr>
                    <tr>
                        <th>Memory size</th>
                        <td>2.0 MiB</td>
                    </tr>
                </table>
            </div>
        </div>
        <div role="tabpanel" class="tab-pane col-md-8 col-md-offset-2" id="histogram7653690958453503572">
            <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAlgAAAGQCAYAAAByNR6YAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAPYQAAD2EBqD%2BnaQAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAIABJREFUeJzt3X9UlGX%2B//GXOCgDqJCI7XbalUWwNTFIlAxzUyPXEjWlaDOyVuuTkoSraK6arqbmSpY/NkvT3JRzokwrC9NtP6V9zNBcK2ujwERr/QECKj/l1/X9w8N8m7AV8VZg5vk4Zw7Odd33Ne/3MMWL%2B75naGWMMQIAAIBlPJq6AAAAAFdDwAIAALAYAQsAAMBiBCwAAACLEbAAAAAsRsACAACwGAELAADAYgQsAAAAixGwAAAALEbAAgAAsBgBCwAAwGIELAAAAIsRsAAAACxGwAIAALAYAQsAAMBiBCwAAACLEbAAAAAsRsACAACwGAELAADAYgQsAAAAixGwAAAALEbAAgAAsBgBCwAAwGIELAAAAIsRsAAAACxGwAIAALAYAQsAAMBiBCwAAACLEbAAAAAsRsACAACwGAELAADAYgQsAAAAixGwAAAALEbAAgAAsBgBCwAAwGIELAAAAIsRsAAAACxGwAIAALAYAQsAAMBitqYuwF3k5xc3dQmN5uHRSldd5aPCwlLV1pqmLueKond6p3f3Qe%2Bu2XunTu2a5HE5goUL8vBopVatWsnDo1VTl3LF0Tu9uxt6p3dYg4AFAABgMQIWAACAxQhYAAAAFiNgAQAAWIyABQAAYDECFgAAgMUIWAAAABYjYAEAAFiMgAUAAGAxAhYAAIDFCFgAAAAWI2ABAABYjIAFAABgMVtTF4BLM%2BS5XU1dQoNtTY5u6hIAALgiOIIFAABgMQIWAACAxZpFwCosLFRMTIwyMzMlSU8%2B%2BaQiIiKcbr/97W81duxYSVJtba0iIiIUHh7utE1ZWZkkqaCgQBMmTFBkZKSioqI0f/58VVdXOx7v888/1913362IiAgNHDhQr7/%2BulM9mzdvVkxMjMLDwzVy5Ejt37//Cj0TAADAFTR5wNq3b5/i4%2BN15MgRx9jcuXO1f/9%2Bx2358uVq3769nnjiCUlSTk6OqqqqtGfPHqftvL29JUnJycny9vbWRx99pI0bN2r37t1at26dJOn06dN65JFHNGLECO3du1fz58/XwoUL9cUXX0iSMjMzNW/ePD399NPau3evhg0bpvHjx6u8vPzKPjEAAKDFatKAtXnzZk2ZMkWTJk362W0KCws1ZcoUzZgxQyEhIZKkAwcOqFu3bmrTpk297Q8fPqw9e/YoJSVFdrtd1157rSZMmKC0tDRJ0vbt2%2BXn56fRo0fLZrOpb9%2B%2Bio2Ndcy//vrruvPOO9WrVy95enrqwQcflL%2B/vzIyMi7DMwAAAFxRk76LsF%2B/foqNjZXNZvvZkJWamqoePXpo2LBhjrEDBw7o7NmzGjVqlP7zn/8oODhYkydP1o033qjs7Gz5%2Bfmpc%2BfOju2Dg4N19OhRnTlzRtnZ2QoNDXV6jK5du2rjxo2Szh0dGzVqVL35rKysBveVl5en/Px8pzGbzVuBgYENXsMV2WxNfsD0orVu7eH01Z3QO727G3p3z94vlyYNWJ06dfqv899//73efvvtetdIeXl5qWfPnnr88cfVoUMHpaWlaezYsXr77bdVWloqu93utH3d/bKysvPOe3l5Oa7futB8Q6Snp2vFihVOY4mJiUpKSmrwGq7I39%2BnqUtotPbt7RfeyEXRu3uid/fkzr1brVl/DtYbb7zhuMD9x%2BquxaozduxYbdq0STt27FDnzp3rXS9Vd9/Hx0d2u13FxcVO8xUVFfLxOffD3263q6Kiot68v79/g%2BuOj4/XwIEDncZsNm8VFZU2eA1X1BL7b93aQ%2B3b23XmTLlqamqbupwrit7pnd7dhyv33lS/3DfrgLV9%2B3b98Y9/rDf%2B7LPPavDgwerevbtjrLKyUm3btlVISIhOnTqlkydPKiAgQJJ08OBBXX311WrXrp1CQ0O1a5fzh3Pm5OQ4ru8KCQlRdnZ2vfn%2B/fs3uO7AwMB6pwPz84tVXe1aL9qL1ZL7r6mpbdH1Xwp6p3d3Q%2B/u2bvVmu3J1qKiIh08eFC9e/euN/ftt99q/vz5ys/PV2VlpVasWKGSkhLFxMSoS5cu6tWrlxYsWKCSkhJ9//33ev755xUXFydJiomJ0cmTJ7Vu3TpVVVXpk08%2B0ZYtWxzXXcXFxWnLli365JNPVFVVpXXr1qmgoEAxMTFXtH8AANByNduA9cMPP0iS08XqdRYuXKhf/epXGj58uKKiorRnzx69/PLL8vPzkyQtW7ZM1dXVGjRokO655x7dcsstmjBhgiTJ399fa9eu1XvvvaeoqCjNnDlTM2fO1E033SRJ6tu3r2bPnq05c%2BaoT58%2Bevfdd7V69WrH2gAAABfSyhhjmroId5CfX3zhjRqBv0V4edlsHvL391FRUanbHTand3qnd/fhyr136tSuSR632R7BAgAAaKkIWAAAABYjYAEAAFiMgAUAAGAxAhYAAIDFCFgAAAAWI2ABAABYjIAFAABgMQIWAACAxQhYAAAAFiNgAQAAWIyABQAAYDECFgAAgMUIWAAAABYjYAEAAFiMgAUAAGAxAhYAAIDFCFgAAAAWI2ABAABYjIAFAABgMQIWAACAxQhYAAAAFiNgAQAAWIyABQAAYDECFgAAgMUIWAAAABYjYAEAAFiMgAUAAGAxAhYAAIDFCFgAAAAWI2ABAABYjIAFAABgsWYRsAoLCxUTE6PMzEzH2OzZs9WjRw9FREQ4bunp6Y751atXq3///goPD1dCQoK%2B%2B%2B47x1xZWZmmT5%2BuqKgo9erVS1OnTlVpaalj/tChQxozZowiIiLUr18/vfDCC0717NixQ7GxsQoPD9eQIUP0wQcfXMbuAQCAq2nygLVv3z7Fx8fryJEjTuMHDhzQvHnztH//fsctPj5ekrR582atX79ea9asUWZmpq6//nolJSXJGCNJmjdvno4dO6Zt27Zp%2B/btOnbsmFJTUyVJVVVVevTRRxUWFqbMzEytWrVKaWlp2rp1qyQpNzdXEydO1OOPP65PP/1UEydOVHJysk6cOHEFnxUAANCSNWnA2rx5s6ZMmaJJkyY5jVdWVurbb79Vjx49zrvfa6%2B9pvvuu08hISFq27atJk%2BerKNHjyozM1Pl5eXasmWLkpKS5Ofnp44dO2rKlCnatGmTysvLtXfvXuXl5SkpKUlt2rRR9%2B7dlZCQoLS0NEdNkZGRuu2222Sz2XTHHXeod%2B/eTkfPAAAA/psmDVj9%2BvXTP/7xD91xxx1O41lZWaqurtayZct08803a/DgwVq1apVqa2slSTk5OQoNDXVs7%2BnpqS5duigrK0uHDx9WVVWV03xwcLAqKiqUm5ur7OxsBQUFqU2bNo75rl27Kisr67xr/3QeAADgQmxN%2BeCdOnU673hxcbH69OmjhIQELVmyRF9//bUSExPl4eGhcePGqbS0VHa73WkfLy8vlZWVqaSkRJLk7e3tmKvbtrS09Lz72u12lZWVObb5ubUbKi8vT/n5%2BU5jNpu3AgMDG7yGK7LZmvyM9EVr3drD6as7oXd6dzf07p69Xy5NGrB%2BTnR0tKKjox33e/bsqTFjxigjI0Pjxo2T3W5XRUWF0z4VFRXy8fFxBKvy8nL5%2BPg4/i1Jvr6%2B8vb2dtyv8%2BNt/9vaDZWenq4VK1Y4jSUmJiopKanBa7gif/%2BGP4fNTfv29gtv5KLo3T3Ru3ty596t1iwD1vvvv6%2BTJ0/q3nvvdYxVVlbKy8tLkhQSEqLs7GwNGDBA0rkL13NzcxUaGqqgoCB5enoqJydHN9xwgyTp4MGDjtOIBQUFys3NVXV1tWy2c%2B3n5OQoJCREkhQaGqqvvvrKqZ6cnJyfvR7sfOLj4zVw4ECnMZvNW0VFpT%2Bzh3toif23bu2h9u3tOnOmXDU1tU1dzhVF7/RO7%2B7DlXtvql/um2XAMsZo4cKF%2BvWvf62bbrpJn332mV555RVNnz5dkjRq1CgtX75c/fv3V1BQkJ599lkFBAQoMjJSnp6eGjJkiFJTU7V06VJJUmpqqoYOHSovLy9FRUXJ399fzzzzjJKTk3Xo0CGtX7/ecaH9sGHD9PLLLysjI0O33367tm/frj179mjGjBkNrj8wMLDe6cD8/GJVV7vWi/ZiteT%2Ba2pqW3T9l4Le6d3d0Lt79m61ZhmwYmJiNH36dM2ZM0cnTpxQQECAJk6cqOHDh0uS4uLiVFxcrMTERBUWFiosLEwvvviiPD09JZ37DK1FixYpNjZWVVVVGjRokGbNmiVJstlsWrt2rebOnavo6Gh5e3srISFBI0eOlHTugvi//e1vSk1N1YwZM3TNNddo%2BfLlCgoKaponAwAAtDitTN2HR%2BGyys8vvizrDnlu12VZ93LYmhx94Y2aGZvNQ/7%2BPioqKnW73%2Brond7p3X24cu%2BdOrVrksfl7QIAAAAWI2ABAABYjIAFAABgMQIWAACAxQhYAAAAFiNgAQAAWIyABQAAYDECFgAAgMUIWAAAABYjYAEAAFiMgAUAAGAxAhYAAIDFCFgAAAAWI2ABAABYjIAFAABgMQIWAACAxQhYAAAAFiNgAQAAWIyABQAAYDECFgAAgMUIWAAAABYjYAEAAFiMgAUAAGAxAhYAAIDFCFgAAAAWI2ABAABYjIAFAABgMQIWAACAxQhYAAAAFiNgAQAAWIyABQAAYDECFgAAgMUIWAAAABZrFgGrsLBQMTExyszMdIxt27ZNw4cP14033qiBAwdqxYoVqq2tdcwPGTJEN9xwgyIiIhy3gwcPSpLKyso0ffp0RUVFqVevXpo6dapKS0sd%2Bx46dEhjxoxRRESE%2BvXrpxdeeMGpnh07dig2Nlbh4eEaMmSIPvjgg8v8DAAAAFfS5AFr3759io%2BP15EjRxxjX375paZOnark5GR9%2BumnWr16tTZt2qR169ZJkkpKSnTo0CFlZGRo//79jltwcLAkad68eTp27Ji2bdum7du369ixY0pNTZUkVVVV6dFHH1VYWJgyMzO1atUqpaWlaevWrZKk3NxcTZw4UY8//rg%2B/fRTTZw4UcnJyTpx4sSVfWIAAECL1aQBa/PmzZoyZYomTZrkNP6f//xH9957rwYMGCAPDw8FBwcrJiZGe/fulXQugPn5%2Bemaa66pt2Z5ebm2bNmipKQk%2Bfn5qWPHjpoyZYo2bdqk8vJy7d27V3l5eUpKSlKbNm3UvXt3JSQkKC0tzVFTZGSkbrvtNtlsNt1xxx3q3bu30tPTL/8TAgAAXIKtKR%2B8X79%2Bio2Nlc1mcwpZgwcP1uDBgx33Kyoq9OGHHyo2NlaSdODAAdntdt1///3Kzs7WNddco4kTJ2rAgAE6fPiwqqqqFBoa6tg/ODhYFRUVys3NVXZ2toKCgtSmTRvHfNeuXbVq1SpJUk5OjtO%2BdfNZWVkN7isvL0/5%2BflOYzabtwIDAxu8hiuy2Zr8gOlFa93aw%2BmrO6F3enc39O6evV8uTRqwOnXqdMFtSkpK9Pjjj8vLy0sPPvigJKlVq1YKCwvTn/70J/3yl7/Ue%2B%2B9p4kTJ2rDhg2qrq6WJHl7ezvWsNvtkqTS0lKVlpY67v94vqyszLHNT%2Be9vLwc8w2Rnp6uFStWOI0lJiYqKSmpwWu4In9/n6YuodHat7dfeCMXRe/uid7dkzv3brUmDVgX8t133ykpKUkdO3bUK6%2B8Il9fX0nSuHHjnLYbNmyY3nnnHW3bts1xlKu8vFw%2BPj6Of0uSr6%2BvvL29Hffr/Hhbu92uiooKp/mKigrHfEPEx8dr4MCBTmM2m7eKikp/Zg/30BL7b93aQ%2B3b23XmTLlqamovvIMLoXd6p3f34cq9N9Uv9802YO3YsUN/%2BtOfdM8992jy5Mmy2f5/qWvWrFH37t3Vt29fx1hlZaXatm2roKAgeXp6KicnRzfccIMk6eDBg/L09FSXLl1UUFCg3NxcVVdXO9bMyclRSEiIJCk0NFRfffWVUy05OTnq0aNHg2sPDAysdzowP79Y1dWu9aK9WC25/5qa2hZd/6Wgd3p3N/Tunr1brVmebP3ss8%2BUmJio6dOna9q0aU7hSpKOHTumv/zlL/r%2B%2B%2B9VXV2tjRs3av/%2B/brrrrtkt9s1ZMgQpaamqrCwUIWFhUpNTdXQoUPl5eWlqKgo%2Bfv765lnntHZs2eVlZWl9evXKy4uTtK5o2F79uxRRkaGqqurlZGRoT179mj48OFN8VQAAIAWqFkewXrhhRdUXV2t%2BfPna/78%2BY7xXr166aWXXtLUqVPl4eGh%2B%2B67T8XFxY6L1H/9619LkmbPnq1FixYpNjZWVVVVGjRokGbNmiVJstlsWrt2rebOnavo6Gh5e3srISFBI0eOlHTugvi//e1vSk1N1YwZM3TNNddo%2BfLlCgoKuvJPBAAAaJFaGWNMUxfhDvLziy/LukOe23VZ1r0ctiZHN3UJF81m85C/v4%2BKikrd7rA5vdM7vbsPV%2B69U6d2TfK4zfIUIQAAQEtGwAIAALAYAQsAAMBiBCwAAACLEbAAAAAsRsACAACwGAELAADAYgQsAAAAixGwAAAALEbAAgAAsBgBCwAAwGIELAAAAIsRsAAAACzWqIBVU1NjdR0AAAAuo1EBq3///vrrX/%2BqnJwcq%2BsBAABo8RoVsB577DH961//0tChQ3X33Xfr1VdfVXFxsdW1AQAAtEiNClh/%2BMMf9Oqrr%2Bq9997TzTffrNWrV6tfv36aPHmyPv74Y6trBAAAaFEu6SL3Ll26aNKkSXrvvfeUmJiof/7znxo7dqwGDhyol19%2BmWu1AACAW7Jdys6ff/653nzzTWVkZKiyslIxMTEaOXKkTpw4oaVLl%2BrAgQNasmSJVbUCAAC0CI0KWM8//7zeeustHT58WGFhYZo0aZKGDh0qX19fxzatW7fWk08%2BaVmhAAAALUWjAtaGDRs0bNgwxcXFqWvXrufdJjg4WFOmTLmk4gAAAFqiRgWsnTt3qqSkRKdOnXKMZWRkqG/fvvL395ckde/eXd27d7emSgAAgBakURe5//vf/9bgwYOVnp7uGFu8eLFiY2P17bffWlYcAABAS9SogPXXv/5Vt99%2BuyZNmuQYe//999W/f389/fTTlhUHAADQEjUqYH311Vd65JFH1KZNG8dY69at9cgjj%2Bizzz6zrDgAAICWqFEBy9fXV0eOHKk3fvz4cXl5eV1yUQAAAC1ZowLW4MGDNWfOHH388ccqKSlRaWmpPvnkE82dO1cxMTFW1wgAANCiNOpdhJMnT9b333%2BvP/7xj2rVqpVjPCYmRlOnTrWsOAAAgJaoUQHLbrfrxRdf1KFDh/TNN9/I09NTwcHB6tKli8XlAQAAtDyX9KdygoKCFBQUZFUtAAAALqFRAevQoUOaO3eu9u3bp6qqqnrzX3/99SUXBgAA0FI1KmDNmTNHR48e1ZQpU9SuXTurawIAAGjRGvUuwv379%2Buvf/2rHnjgAd111131bhejsLBQMTExyszMdIx9/vnnuvvuuxUREaGBAwfq9ddfd9pn8%2BbNiomJUXh4uEaOHKn9%2B/c75mpqarRo0SLdfPPNioiI0Pjx45WXl%2BeYLygo0IQJExQZGamoqCjNnz9f1dXVDX5sAACAC2lUwPL395ePj88lP/i%2BffsUHx/v9Jlap0%2Bf1iOPPKIRI0Zo7969mj9/vhYuXKgvvvhCkpSZmal58%2Bbp6aef1t69ezVs2DCNHz9e5eXlkqSVK1dq165deuONN/TRRx/Jy8tLM2fOdKyfnJwsb29vffTRR9q4caN2796tdevWNeixAQAAGqJRASshIUFLlixRcXFxox948%2BbNmjJlitOf25Gk7du3y8/PT6NHj5bNZlPfvn0VGxurtLQ0SdLrr7%2BuO%2B%2B8U7169ZKnp6cefPBB%2Bfv7KyMjwzH/8MMP6xe/%2BIV8fX01Y8YM7dy5U99//70OHz6sPXv2KCUlRXa7Xddee60mTJjgWPtCjw0AANAQjboGa8eOHfrss88UFRWljh07Ov3JHEn65z//ecE1%2BvXrp9jYWNlsNqeQlZ2drdDQUKdtu3btqo0bN0qScnJyNGrUqHrzWVlZKi4u1vHjx532DwgIUIcOHfTNN99Ikvz8/NS5c2fHfHBwsI4ePaozZ85c8LEBAAAaolEBKyoqSlFRUZf0wJ06dTrveGlpqex2u9OYl5eXysrKLjhfWloqSfL29q43Xzf3033r7tft/98eu6Hy8vKUn5/vNGazeSswMPCi1nE1NlujDpg2qdatPZy%2BuhN6p3d3Q%2B/u2fvl0qiA9dhjj1ldh4Pdbq936rGiosJxzZfdbldFRUW9eX9/f0c4qrse66f7G2PqzdXd9/HxueBjN1R6erpWrFjhNJaYmKikpKSLWsfV%2BPtf%2BnV7TaV9e/uFN3JR9O6e6N09uXPvVmv0B41mZWXp73//uw4dOqSlS5fq/fffV9euXS/5yFZoaKh27drlNJaTk6OQkBBJUkhIiLKzs%2BvN9%2B/fXx06dFDnzp2Vk5PjONWXn5%2BvU6dOKTQ0VLW1tTp16pROnjypgIAASdLBgwd19dVXq127dhd87IaKj4/XwIEDncZsNm8VFZVe1DqupiX237q1h9q3t%2BvMmXLV1NQ2dTlXFL3TO727D1fuval%2BuW9UwPryyy/1hz/8QeHh4fryyy9VWVmpr7/%2BWgsWLNCKFSs0YMCARhcUExOjxYsXa926dRo9erT27dunLVu26Pnnn5ckxcXFKTExUUOGDFGvXr2UlpamgoICxx%2BZHjlypFauXKmwsDD5%2B/trwYIF6tOnj371q19Jknr16qUFCxZo7ty5Kioq0vPPP6%2B4uLgGPXZDBQYG1jsdmJ9frOpq13rRXqyW3H9NTW2Lrv9S0Du9uxt6d8/erdaogJWamqo//vGPmjRpkiIiIiRJTz31lNq1a3fJAcvf319r167V/PnztWzZMl111VWaOXOmbrrpJklS3759NXv2bM2ZM0cnTpxQ165dtXr1avn5%2BUk6dyquurpao0ePVmlpqaKiovTcc8851l%2B2bJnmzp2rQYMGycPDQyNGjNCECRMa9NgAAAAN0coYYy52p8jISL3%2B%2BusKCgpSRESE3n77bV177bU6cuSIhg8f7vTBnzgnP7/xH2nx3wx5bteFN2omtiZHN3UJF81m85C/v4%2BKikrd7rc6eqd3encfrtx7p05N8xdnGvV2AU9PT5WUlNQbP3r0aL134QEAALibRgWs2267Tc8884yKioocYwcPHtT8%2BfN16623WlUbAABAi9SogDVt2jRVVFTo5ptvVnl5uUaOHKmhQ4fKZrNp6tSpVtcIAADQojTqIndfX1%2B9%2Buqr2r17t/7973%2BrtrZWoaGhuuWWW%2BThwYeUAQAA99boz8GSzr2jr2/fvlbVAgAA4BIaFbAGDhyoVq1a/ex8Q/4WIQAAgKtqVMC66667nAJWVVWVDh8%2BrJ07dyo5Odmy4gAAAFqiRgWsiRMnnnd8w4YN2rdvnx544IFLKgoAAKAls/SK9AEDBmjHjh1WLgkAANDiWBqw9uzZo7Zt21q5JAAAQIvTqFOEPz0FaIxRSUmJvvnmG04PAgAAt9eogPXLX/6y3rsIPT09NWbMGMXGxlpSGAAAQEvVqID19NNPW10HAACAy2hUwNq7d2%2BDt%2B3du3djHgIAAKDFalTAevDBB2WMcdzq1J02rBtr1aqVvv76awvKBAAAaDkaFbCWL1%2BuhQsXatq0abrpppvk6empzz//XHPmzNF9992nAQMGWF0nAABAi9Goj2lYtGiRZs%2Berdtuu02%2Bvr5q27at%2BvTpo7lz52rt2rW65pprHDcAAAB306iAlZeXp1/84hf1xn19fVVUVHTJRQEAALRkjQpY4eHhWrJkiUpKShxjp06d0uLFi9W3b1/LigMAAGiJGnUN1syZMzVmzBj1799fXbp0kSQdOnRInTp10iuvvGJlfQAAAC1OowJWcHCwMjIytGXLFh08eFCSdN999%2BnOO%2B%2BU3W63tEAAAICWplEBS5Lat2%2Bvu%2B%2B%2BWz/88IOuvfZaSec%2BzR0AAMDdNeoaLGOMUlNT1bt3bw0dOlTHjx/XtGnTNH36dFVVVVldIwAAQIvSqIC1fv16vfXWW5o9e7batGkjSbrtttv0v//7v1q6dKmlBQIAALQ0jQpY6enpevLJJzVy5EjHp7ffcccdmj9/vt59911LCwQAAGhpGhWwfvjhB/32t7%2BtN96tWzedPHnykosCAABoyRoVsK655hp98cUX9cZ37NjhuOAdAADAXTXqXYRjx47VX/7yF504cULGGO3evVuvvvqq1q9fr%2BnTp1tdIwAAQIvSqIA1atQoVVdXa%2BXKlaqoqNCTTz6pjh07atKkSfrDH/5gdY0AAAAtSqMC1ttvv63f//73io%2BPV2FhoYwx6tixo9W1AQAAtEiNugbrqaeeclzMftVVVxGuAAAAfqRRAatLly765ptvrK4FAADAJTTqFGFISIimTJmil156SV26dFHbtm2d5hcuXGhJcQAAAC1RowLWkSNH1KtXL0lSfn6%2BpQXVefvttzV79mynsbo/w/Pll19q3LhxyszMlM32/1tYunSp%2Bvfvr5qaGqWmpuqtt95SeXm5brrpJv3lL39RYGCgJKmgoECzZs3Snj171Lp1aw0bNkzTpk1zrPX555/rqaeeUk5Ojvz9/TV%2B/Hjdfffdl6VPAADgehocsBYuXKjHH39c3t7eWr9%2B/eWsSZI0bNgwDRs2zHH/xIkTGjVqlFJSUiSdC1lr1qxRnz596u27cuVK7dq1S2%2B88YbatWunWbNmaebMmVq1apUkKTk5WZ07d9ZHH32kkydPavz48Vq3bp3GjRun06dP65FHHlFSUpLi4%2BO1d%2B9eJSYmqlu3burZs%2Bdl7xsAALR8Db4G65VXXlF5ebnT2NixY5WXl2d5UT9ljFFKSopuvfVWDR8%2BXN9//71Onz6t7t27n3f7119/XQ8//LB%2B8YtfyNfXVzNmzNDOnTv1/fff6/Dhw9qzZ49SUlJkt9t17bXXasKECUpLS5Mkbd%2B%2BXX5%2Bfho9erRsNpsgiGWOAAAbIklEQVT69u2r2NhYxzwAAMCFNPgIljGm3ti//vUvnT171tKCzuett95STk6Onn/%2BeUnSgQMH5OPjo0mTJunAgQMKCAjQgw8%2BqLi4OBUXF%2Bv48eMKDQ117B8QEKAOHTo4Lsz38/NT586dHfPBwcE6evSozpw5o%2BzsbKd9Jalr167auHFjg%2BvNy8urd%2BrUZvN2nKJ0VzZbo95T0aRat/Zw%2BupO6J3e3Q29u2fvl0ujrsG6kmpra7Vy5Uo9%2Buij8vX1lSRVVlYqPDxckyZNUkhIiDIzMzVx4kT5%2BPgoIiJCkuTt7e20jpeXl0pLSyVJdrvdaa7ufllZmUpLS%2BvNe3l5qaysrME1p6ena8WKFU5jiYmJSkpKavAarsjf36epS2i09u3tF97IRdG7e6J39%2BTOvVut2QeszMxM5eXlKS4uzjE2YsQIjRgxwnG/X79%2BGjFihLZu3aqbb75ZkuqdzqyoqJCPj4%2BMMfXm6u77%2BPjIbreruLj4vPs2VHx8vAYOHOg0ZrN5q6iotMFruKKW2H/r1h5q396uM2fKVVNT29TlXFH0Tu/07j5cufem%2BuX%2BogJWq1atLlcdP2vbtm2KiYlxOiK1ceNG%2Bfj4aMiQIY6xyspKtW3bVh06dFDnzp2Vk5PjONWXn5%2BvU6dOKTQ0VLW1tTp16pROnjypgIAASdLBgwd19dVXq127dgoNDdWuXbucasjJyVFISEiDaw4MDKx3OjA/v1jV1a71or1YLbn/mpraFl3/paB3enc39O6evVvtogLWU0895fSZV1VVVVq8eHG9oztWfg7Wvn379MADDziNlZSUaMmSJfr1r3%2Bt6667Tjt37tQ777yjNWvWSJJGjhyplStXKiwsTP7%2B/lqwYIH69OmjX/3qV5KkXr16acGCBZo7d66Kior0/PPPO46QxcTEaPHixVq3bp1Gjx6tffv2acuWLY7rvwAAAC6kwQGrd%2B/e9S7cjoiIUFFRkYqKiiwvrM4PP/xQ72jQmDFjVFZWpscee0wFBQW69tprtWjRIkVGRko6d71TdXW1Ro8erdLSUkVFRem5555z7L9s2TLNnTtXgwYNkoeHh0aMGKEJEyZIkvz9/bV27VrNnz9fy5Yt01VXXaWZM2fqpptuumw9AgAA19LKnO/tgbBcfn7xhTdqhCHP7brwRs3E1uTopi7hotlsHvL391FRUanbHTand3qnd/fhyr136tSuSR6X92MCAABYjIAFAABgMQIWAACAxQhYAAAAFiNgAQAAWIyABQAAYDECFgAAgMUIWAAAABYjYAEAAFiMgAUAAGAxAhYAAIDFCFgAAAAWI2ABAABYjIAFAABgMQIWAACAxQhYAAAAFiNgAQAAWIyABQAAYDECFgAAgMUIWAAAABYjYAEAAFiMgAUAAGAxAhYAAIDFCFgAAAAWI2ABAABYjIAFAABgMQIWAACAxQhYAAAAFiNgAQAAWIyABQAAYDECFgAAgMUIWAAAABZrtgErIyND3bt3V0REhOOWkpIiSdqxY4diY2MVHh6uIUOG6IMPPnDad/Xq1erfv7/Cw8OVkJCg7777zjFXVlam6dOnKyoqSr169dLUqVNVWlrqmD906JDGjBmjiIgI9evXTy%2B88MKVaRgAALiMZhuwDhw4oOHDh2v//v2O2%2BLFi5Wbm6uJEyfq8ccf16effqqJEycqOTlZJ06ckCRt3rxZ69ev15o1a5SZmanrr79eSUlJMsZIkubNm6djx45p27Zt2r59u44dO6bU1FRJUlVVlR599FGFhYUpMzNTq1atUlpamrZu3dpkzwMAAGh5mnXA6tGjR73xzZs3KzIyUrfddptsNpvuuOMO9e7dW%2Bnp6ZKk1157Tffdd59CQkLUtm1bTZ48WUePHlVmZqbKy8u1ZcsWJSUlyc/PTx07dtSUKVO0adMmlZeXa%2B/evcrLy1NSUpLatGmj7t27KyEhQWlpaVe6fQAA0II1y4BVW1urr776Sh9%2B%2BKEGDBig/v37a9asWTp9%2BrRycnIUGhrqtH3Xrl2VlZUlSfXmPT091aVLF2VlZenw4cOqqqpymg8ODlZFRYVyc3OVnZ2toKAgtWnT5rxrAwAANIStqQs4n8LCQnXv3l2DBw/WsmXLVFRUpGnTpiklJUWVlZWy2%2B1O23t5eamsrEySVFpa%2BrPzJSUlkiRvb2/HXN22paWl593Xbrc71m6ovLw85efnO43ZbN4KDAy8qHVcjc3WLPP8f9W6tYfTV3dC7/TubujdPXu/XJplwAoICHA6LWe325WSkqJ77rlHUVFRqqiocNq%2BoqJCPj4%2Bjm1/br4uWJWXlzu2Ly8vlyT5%2BvrK29vbcb/Oj7dtqPT0dK1YscJpLDExUUlJSRe1jqvx97%2B457E5ad/efuGNXBS9uyd6d0/u3LvVmmXAysrK0jvvvKPJkyerVatWkqTKykp5eHioZ8%2Be%2Bvrrr522z8nJcVyvFRISouzsbA0YMEDSuQvXc3NzFRoaqqCgIHl6eionJ0c33HCDJOngwYOO04gFBQXKzc1VdXW1bDabY%2B2QkJCLqj8%2BPl4DBw50GrPZvFVUVPoze7iHlth/69Yeat/erjNnylVTU9vU5VxR9E7v9O4%2BXLn3pvrlvlkGLD8/P6WlpalDhw566KGHlJeXp8WLF%2Buuu%2B7SiBEj9Pe//10ZGRm6/fbbtX37du3Zs0czZsyQJI0aNUrLly9X//79FRQUpGeffVYBAQGKjIyUp6enhgwZotTUVC1dulSSlJqaqqFDh8rLy0tRUVHy9/fXM888o%2BTkZB06dEjr16/XpEmTLqr%2BwMDAeqcD8/OLVV3tWi/ai9WS%2B6%2BpqW3R9V8Keqd3d0Pv7tm71ZplwLr66qv14osvasmSJVq5cqXatm2rO%2B%2B8UykpKWrbtq3%2B9re/KTU1VTNmzNA111yj5cuXKygoSJIUFxen4uJiJSYmqrCwUGFhYXrxxRfl6ekpSZo9e7YWLVqk2NhYVVVVadCgQZo1a5YkyWazae3atZo7d66io6Pl7e2thIQEjRw5ssmeCwAA0PK0MnUfEIXLKj%2B/%2BLKsO%2BS5XZdl3ctha3J0U5dw0Ww2D/n7%2B6ioqNTtfqujd3qnd/fhyr136tSuSR6XtwsAAABYjIAFAABgMQIWAACAxQhYAAAAFiNgAQAAWIyABQAAYDECFgAAgMUIWAAAABYjYAEAAFiMgAUAAGAxAhYAAIDFCFgAAAAWI2ABAABYjIAFAABgMQIWAACAxQhYAAAAFiNgAQAAWIyABQAAYDECFgAAgMUIWAAAABYjYAEAAFiMgAUAAGAxAhYAAIDFCFgAAAAWI2ABAABYjIAFAABgMQIWAACAxQhYAAAAFiNgAQAAWIyABQAAYDECFgAAgMUIWAAAABYjYAEAAFis2QasrKwsPfTQQ%2BrTp4%2Bio6M1depUFRYWSpJmz56tHj16KCIiwnFLT0937Lt69Wr1799f4eHhSkhI0HfffeeYKysr0/Tp0xUVFaVevXpp6tSpKi0tdcwfOnRIY8aMUUREhPr166cXXnjhyjUNAABcQrMMWBUVFRo3bpwiIiL0f//3f3rnnXd06tQp/fnPf5YkHThwQPPmzdP%2B/fsdt/j4eEnS5s2btX79eq1Zs0aZmZm6/vrrlZSUJGOMJGnevHk6duyYtm3bpu3bt%2BvYsWNKTU2VJFVVVenRRx9VWFiYMjMztWrVKqWlpWnr1q1N80QAAIAWqVkGrKNHj%2Bq6665TYmKi2rRpI39/f8XHx2vv3r2qrKzUt99%2Bqx49epx339dee0333XefQkJC1LZtW02ePFlHjx5VZmamysvLtWXLFiUlJcnPz08dO3bUlClTtGnTJpWXl2vv3r3Ky8tTUlKS2rRpo%2B7duyshIUFpaWlX%2BBkAAAAtma2pCzif3/zmN3rppZecxrZt26brr79eWVlZqq6u1rJly7Rv3z61a9dOo0aN0rhx4%2BTh4aGcnBw9/PDDjv08PT3VpUsXZWVlyc/PT1VVVQoNDXXMBwcHq6KiQrm5ucrOzlZQUJDatGnjmO/atatWrVp1UfXn5eUpPz/facxm81ZgYOBFreNqbLZmmef/q9atPZy%2BuhN6p3d3Q%2B/u2fvl0iwD1o8ZY/Tcc8/pgw8%2B0IYNG3Ty5En16dNHCQkJWrJkib7%2B%2BmslJibKw8ND48aNU2lpqex2u9MaXl5eKisrU0lJiSTJ29vbMVe3bWlp6Xn3tdvtKisru6ia09PTtWLFCqexxMREJSUlXdQ6rsbf36epS2i09u3tF97IRdG7e6J39%2BTOvVutWQeskpISTZ8%2BXV999ZU2bNigbt26qVu3boqOjnZs07NnT40ZM0YZGRkaN26c7Ha7KioqnNapqKiQj4%2BPI1iVl5fLx8fH8W9J8vX1lbe3t%2BN%2BnR9v21Dx8fEaOHCg05jN5q2iotKf2cM9tMT%2BW7f2UPv2dp05U66amtqmLueKond6p3f34cq9N9Uv9802YB05ckQPP/ywfvnLX2rjxo266qqrJEnvv/%2B%2BTp48qXvvvdexbWVlpby8vCRJISEhys7O1oABAySdu3A9NzdXoaGhCgoKkqenp3JycnTDDTdIkg4ePOg4jVhQUKDc3FxVV1fLZjv31OTk5CgkJOSiag8MDKx3OjA/v1jV1a71or1YLbn/mpraFl3/paB3enc39O6evVutWZ5sPX36tMaMGaMbb7xRa9ascYQr6dwpw4ULF2r37t0yxmj//v165ZVXHO8iHDVqlDZs2KCsrCydPXtWzzzzjAICAhQZGSm73a4hQ4YoNTVVhYWFKiwsVGpqqoYOHSovLy9FRUXJ399fzzzzjM6ePausrCytX79ecXFxTfVUAACAFqhZHsHatGmTjh49qq1bt%2Bq9995zmtu/f7%2BmT5%2BuOXPm6MSJEwoICNDEiRM1fPhwSVJcXJyKi4uVmJiowsJChYWF6cUXX5Snp6ekc5%2BhtWjRIsXGxqqqqkqDBg3SrFmzJEk2m01r167V3LlzFR0dLW9vbyUkJGjkyJFX9gkAAAAtWitT9wFRuKzy84svy7pDntt1Wda9HLYmR194o2bGZvOQv7%2BPiopK3e6wOb3TO727D1fuvVOndk3yuM3yFCEAAEBLRsACAACwGAELAADAYgQsAAAAixGwAAAALEbAAgAAsBgBCwAAwGIELAAAAIsRsAAAACxGwAIAALAYAQsAAMBiBCwAAACLEbAAAAAsRsACAACwmK2pCwAAAJfHkOd2NXUJDbY1ObqpS7AUR7AAAAAsRsACAACwGAELAADAYgQsAAAAixGwAAAALEbAAgAAsBgBCwAAwGIELAAAAIsRsAAAACxGwAIAALAYAQsAAMBiBCwAAACLEbAAAAAsRsACAACwGAELAADAYgQsAAAAixGwAAAALEbAOo%2BCggJNmDBBkZGRioqK0vz581VdXd3UZQEAgBbC1tQFNEfJycnq3LmzPvroI508eVLjx4/XunXrNG7cuKYuDQDQhIY8t6upS0ALwRGsnzh8%2BLD27NmjlJQU2e12XXvttZowYYLS0tKaujQAANBCELB%2BIjs7W35%2BfurcubNjLDg4WEePHtWZM2easDIAANBScIrwJ0pLS2W3253G6u6XlZWpffv2F1wjLy9P%2Bfn5TmM2m7cCAwOtK7QFstlaXp5v3drD6as7oXd6dzfu3Htz0BJ/Rvw3BKyf8Pb2Vnl5udNY3X0fH58GrZGenq4VK1Y4jT322GOaOHGiNUX%2ByKfzf2/5mj%2BVl5en9PR0xcfHu11IzMvL09///hK907vboPf/3vuV%2BH9uU3Dn/89fLq4VFy0QEhKiU6dO6eTJk46xgwcP6uqrr1a7du0atEZ8fLw2bdrkdIuPj79cJV92%2Bfn5WrFiRb2jcu6A3und3dA7vcMaHMH6iS5duqhXr15asGCB5s6dq6KiIj3//POKi4tr8BqBgYH8BgAAgBvjCNZ5LFu2TNXV1Ro0aJDuuece3XLLLZowYUJTlwUAAFoIjmCdR0BAgJYtW9bUZQAAgBaq9Zw5c%2BY0dRFo/nx8fNSnT58GX%2BjvSuid3t0NvdM7Ll0rY4xp6iIAAABcCddgAQAAWIyABQAAYDECFgAAgMUIWAAAABYjYAEAAFiMgAUAAGAxAhYAAIDFCFgAAAAWI2C5qcLCQsXExCgzM9Mx9vnnn%2Bvuu%2B9WRESEBg4cqNdff91pn82bNysmJkbh4eEaOXKk9u/f75irqanRokWLdPPNNysiIkLjx49XXl7eFeunIbKysvTQQw%2BpT58%2Bio6O1tSpU1VYWCjJ9XvfvXu37r77bt14442Kjo7WvHnzVFFRIcn1e69TU1OjhIQEPfHEE46xHTt2KDY2VuHh4RoyZIg%2B%2BOADp31Wr16t/v37Kzw8XAkJCfruu%2B8cc2VlZZo%2BfbqioqLUq1cvTZ06VaWlpVesn4bIyMhQ9%2B7dFRER4bilpKRIcv3eT506palTpyoqKkq9e/fWhAkTHK9NV37Nv/32207f74iICPXo0UM9evSQ5Prf92bFwO18%2Bumn5rbbbjOhoaHmk08%2BMcYYc%2BrUKdOnTx%2BzYcMGU1VVZT7%2B%2BGMTERFhPv/8c2OMMZ988omJiIgwn376qamsrDQvv/yyiYqKMmVlZcYYY5YvX25iY2PN0aNHTXFxsUlOTjYPP/xwk/X4U%2BXl5SY6OtosXbrUnD171hQWFpqHH37Y/M///I/L915QUGDCwsLMG2%2B8YWpqasyJEyfM0KFDzdKlS12%2B9x977rnnzHXXXWemTZtmjDHm0KFDJiwszPzjH/8wVVVV5t133zU9e/Y0x48fN8YYs2nTJnPLLbeYb7/91lRUVJiFCxeaO%2B%2B809TW1hpjjHniiSfMmDFjTFFRkTl58qS5//77zZw5c5qsv/N5%2BumnzRNPPFFv3B16v//%2B%2B01iYqI5ffq0KS4uNo899ph55JFH3Oo1b4wxx48fN9HR0ebNN990i%2B97c0LAcjObNm0yt956q3n33XedAtZrr71mbr/9dqdtn3zySTN16lRjjDGTJ082M2fOdJr//e9/bzZu3GiMMaZ///7m7bffdszl5%2Bebbt26mSNHjlzOdhrs4MGDZuzYsaa6utox9v7775sbb7zR5Xs3xpji4mJjjDG1tbXmm2%2B%2BMTExMWb9%2BvVu0bsxxnz88cfmjjvuMElJSY6AtWTJEvPQQw85bTd27FizdOlSY4wx9957r1m5cqVjrrKy0kRERJjdu3ebsrIyc/3115t9%2B/Y55j/77DPTs2dPxw/i5mD06NFmw4YN9cZdvfcDBw6YsLAwx%2BveGGOKiorMt99%2B6zaveWPO/feekJBgZsyYYYxx/e97c8MpQjfTr18//eMf/9Add9zhNJ6dna3Q0FCnsa5duyorK0uSlJOT87PzxcXFOn78uNN8QECAOnTooG%2B%2B%2BeYydXJxfvOb3%2Bill15S69atHWPbtm3T9ddf7/K9S5Kvr68k6Xe/%2B51iY2PVqVMnjRw50i16Lygo0IwZM/TMM8/Ibrc7xv9bb%2Beb9/T0VJcuXZSVlaXDhw%2BrqqrKaT44OFgVFRXKzc29vA01UG1trb766it9%2BOGHGjBggPr3769Zs2bp9OnTLt/7F198oa5du%2Bq1115TTEyM%2BvXrp0WLFqlTp05u8Zqv89ZbbyknJ8dxWtzVv%2B/NDQHLzXTq1Ek2m63eeGlpqdMPH0ny8vJSWVnZBefrzsF7e3vXm2%2BO5%2BeNMXr22Wf1wQcfaMaMGW7V%2B/bt27Vz5055eHgoKSnJ5Xuvra1VSkqKHnroIV133XVOc5fSe0lJiSTn3uu2bS69FxYWqnv37ho8eLAyMjL06quvKjc3VykpKS7f%2B%2BnTp/XNN98oNzdXmzdv1ptvvqkTJ05o2rRpLv%2Bar1NbW6uVK1fq0UcfdfyC5erf9%2BaGgAVJ5/5DqbvouU5FRYV8fHwuOF/3H1l5efnP7t9clJSUKCkpSVu2bNGGDRvUrVs3t%2BldOvc/y86dOyslJUUfffSRy/f%2B4osvqk2bNkpISKg3dym91/2Q%2BXHvdf%2Bu%2B2HW1AICApSWlqa4uDjZ7Xb98pe/VEpKinbu3CljjEv33qZNG0nSjBkz5Ovrq4CAACUnJ2vHjh2X1HtLeM3XyczMVF5enuLi4hxjrv6ab24IWJAkhYaGKjs722ksJydHISEhkqSQkJCfne/QoYM6d%2B6snJwcx1x%2Bfr5OnTpV73B0Uzpy5IhGjRqlkpISbdy4Ud26dZPk%2Br3/61//0u9//3tVVlY6xiorK%2BXp6amuXbu6dO9vvfWW9uzZo8jISEVGRuqdd97RO%2B%2B8o8jIyIv%2BvldVVSk3N1ehoaEKCgqSp6enU%2B8HDx50nFJpDrKyspSamipjjGOssrJSHh4e6tmzp0v33rVrV9XW1qqqqsoxVltbK0n67W9/69Kv%2BTrbtm1TTEyM0xEnV3/NNztNewkYmtKPL3IvLCw0kZGR5uWXXzaVlZVm9%2B7djosbjTGOd9rs3r3b8c6a3r17m6KiImOMMc8%2B%2B6wZOnSoOXLkiOOdNffff3%2BT9fZTp06dMrfeeqt54oknTE1NjdOcq/deUlJifve735kFCxaYs2fPmh9%2B%2BMHExcWZ2bNnu3zvPzVt2jTHRe45OTkmLCzMvPvuu453VIWFhZnvvvvOGHPujR%2B33HKL%2Bfrrrx3vqIqJiTGVlZXGGGOmTJli7r//flNQUGAKCgrM/fff71i7OTh27JgJDw83q1atMlVVVeY///mPueeee8yf//xnl%2B%2B9srLSxMTEmIkTJ5qSkhJTUFBgHnjgAZOYmOg2r/mhQ4ea1157zWnM1b/vzQ0By439OGAZY8wXX3xh4uPjTUREhBk0aJB54403nLZ/8803zeDBg014eLiJi4szn332mWOusrLSLF682Nxyyy3mxhtvNOPHjzcnT568Yr1cyNq1a01oaKi54YYbTHh4uNPNGNfu3RhjsrOzzUMPPWQiIyPNgAEDzJIlS8zZs2eNMa7f%2B4/9OGAZY8zOnTvNsGHDTHh4uLnzzjvNhx9%2B6Jirra01a9asMQMHDjTh4eEmISHB8YPImHPvzJw5c6a5%2BeabTe/evc0TTzxhSktLr2g/F5KZmen43t50001m3rx5pqKiwhjj%2Br0fP37cJCcnm%2BjoaBMZGWmmTp1qTp8%2BbYxxj9d8eHi40/e0jqt/35uTVsb86PgxAAAALhnXYAEAAFiMgAUAAGAxAhYAAIDFCFgAAAAWI2ABAABYjIAFAABgMQIWAACAxQhYAAAAFiNgAQAAWIyABQAAYDECFgAAgMUIWAAAABYjYAEAAFiMgAUAAGAxAhYAAIDF/h/mEN44vuivBgAAAABJRU5ErkJggg%3D%3D"/>
        </div>
        <div role="tabpanel" class="tab-pane col-md-12" id="common7653690958453503572">

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">747.0</td>
        <td class="number">5669</td>
        <td class="number">2.2%</td>
        <td>
            <div class="bar" style="width:4%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">740.0</td>
        <td class="number">5537</td>
        <td class="number">2.2%</td>
        <td>
            <div class="bar" style="width:4%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">741.0</td>
        <td class="number">5499</td>
        <td class="number">2.1%</td>
        <td>
            <div class="bar" style="width:4%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">746.0</td>
        <td class="number">5486</td>
        <td class="number">2.1%</td>
        <td>
            <div class="bar" style="width:4%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">742.0</td>
        <td class="number">5219</td>
        <td class="number">2.0%</td>
        <td>
            <div class="bar" style="width:4%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">739.0</td>
        <td class="number">5105</td>
        <td class="number">2.0%</td>
        <td>
            <div class="bar" style="width:4%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">743.0</td>
        <td class="number">5082</td>
        <td class="number">2.0%</td>
        <td>
            <div class="bar" style="width:4%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">745.0</td>
        <td class="number">5061</td>
        <td class="number">2.0%</td>
        <td>
            <div class="bar" style="width:4%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">748.0</td>
        <td class="number">4773</td>
        <td class="number">1.9%</td>
        <td>
            <div class="bar" style="width:4%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">744.0</td>
        <td class="number">4739</td>
        <td class="number">1.8%</td>
        <td>
            <div class="bar" style="width:4%">&nbsp;</div>
        </td>
</tr><tr class="other">
        <td class="fillremaining">Other values (324)</td>
        <td class="number">143138</td>
        <td class="number">55.7%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="missing">
        <td class="fillremaining">(Missing)</td>
        <td class="number">61676</td>
        <td class="number">24.0%</td>
        <td>
            <div class="bar" style="width:43%">&nbsp;</div>
        </td>
</tr>
</table>
        </div>
        <div role="tabpanel" class="tab-pane col-md-12"  id="extreme7653690958453503572">
            <p class="h4">Minimum 5 values</p>

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">585.0</td>
        <td class="number">18</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:72%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">586.0</td>
        <td class="number">25</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">587.0</td>
        <td class="number">23</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:92%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">588.0</td>
        <td class="number">20</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:80%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">589.0</td>
        <td class="number">15</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:60%">&nbsp;</div>
        </td>
</tr>
</table>
            <p class="h4">Maximum 5 values</p>

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">7470.0</td>
        <td class="number">193</td>
        <td class="number">0.1%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">7480.0</td>
        <td class="number">153</td>
        <td class="number">0.1%</td>
        <td>
            <div class="bar" style="width:79%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">7490.0</td>
        <td class="number">72</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:37%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">7500.0</td>
        <td class="number">74</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:38%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">7510.0</td>
        <td class="number">38</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:20%">&nbsp;</div>
        </td>
</tr>
</table>
        </div>
    </div>
</div>
</div><div class="row variablerow">
    <div class="col-md-3 namecol">
        <p class="h4 pp-anchor" id="pp_var_Current Credit Balance">Current Credit Balance<br/>
            <small>Numeric</small>
        </p>
    </div><div class="col-md-6">
    <div class="row">
        <div class="col-sm-6">
            <table class="stats ">
                <tr>
                    <th>Distinct count</th>
                    <td>45704</td>
                </tr>
                <tr>
                    <th>Unique (%)</th>
                    <td>17.8%</td>
                </tr>
                <tr class="ignore">
                    <th>Missing (%)</th>
                    <td>0.0%</td>
                </tr>
                <tr class="ignore">
                    <th>Missing (n)</th>
                    <td>0</td>
                </tr>
                <tr class="ignore">
                    <th>Infinite (%)</th>
                    <td>0.0%</td>
                </tr>
                <tr class="ignore">
                    <th>Infinite (n)</th>
                    <td>0</td>
                </tr>
            </table>

        </div>
        <div class="col-sm-6">
            <table class="stats ">

                <tr>
                    <th>Mean</th>
                    <td>15407</td>
                </tr>
                <tr>
                    <th>Minimum</th>
                    <td>0</td>
                </tr>
                <tr>
                    <th>Maximum</th>
                    <td>1731412</td>
                </tr>
                <tr class="ignore">
                    <th>Zeros (%)</th>
                    <td>0.6%</td>
                </tr>
            </table>
        </div>
    </div>
</div>
<div class="col-md-3 collapse in" id="minihistogram8428251298770906812">
    <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAABLCAYAAAA1fMjoAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAPYQAAD2EBqD%2BnaQAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAAPtJREFUeJzt1bEJAlEQRVFXLGmLsCdje7IIexpzkQsbyN/gnHzgJZfZZmYuwE/X1QPgzG6rB3zbH6/DN%2B/n/Q9LwAeBJBAIAoEgEAgCgSAQCAKBIBAIAoEgEAgCgSAQCAKBIBAIAoEgEAgCgSAQCAKBIBAIAoEgEAgCgSAQCAKBIBAIAoEgEAgCgSAQCAKBIBAIAoEgEAgCgSAQCAKBIBAIAoEgEAgCgSAQCAKBIBAIAoEgEAjbzMzqEXBWPggEgUAQCASBQBAIBIFAEAgEgUAQCASBQBAIBIFAEAgEgUAQCASBQBAIBIFAEAgEgUAQCASBQBAIBIFAEAiED9obC49m6JdFAAAAAElFTkSuQmCC">

</div>
<div class="col-md-12 text-right">
    <a role="button" data-toggle="collapse" data-target="#descriptives8428251298770906812,#minihistogram8428251298770906812"
       aria-expanded="false" aria-controls="collapseExample">
        Toggle details
    </a>
</div>
<div class="row collapse col-md-12" id="descriptives8428251298770906812">
    <ul class="nav nav-tabs" role="tablist">
        <li role="presentation" class="active"><a href="#quantiles8428251298770906812"
                                                  aria-controls="quantiles8428251298770906812" role="tab"
                                                  data-toggle="tab">Statistics</a></li>
        <li role="presentation"><a href="#histogram8428251298770906812" aria-controls="histogram8428251298770906812"
                                   role="tab" data-toggle="tab">Histogram</a></li>
        <li role="presentation"><a href="#common8428251298770906812" aria-controls="common8428251298770906812"
                                   role="tab" data-toggle="tab">Common Values</a></li>
        <li role="presentation"><a href="#extreme8428251298770906812" aria-controls="extreme8428251298770906812"
                                   role="tab" data-toggle="tab">Extreme Values</a></li>

    </ul>

    <div class="tab-content">
        <div role="tabpanel" class="tab-pane active row" id="quantiles8428251298770906812">
            <div class="col-md-4 col-md-offset-1">
                <p class="h4">Quantile statistics</p>
                <table class="stats indent">
                    <tr>
                        <th>Minimum</th>
                        <td>0</td>
                    </tr>
                    <tr>
                        <th>5-th percentile</th>
                        <td>1590</td>
                    </tr>
                    <tr>
                        <th>Q1</th>
                        <td>5974</td>
                    </tr>
                    <tr>
                        <th>Median</th>
                        <td>11078</td>
                    </tr>
                    <tr>
                        <th>Q3</th>
                        <td>19319</td>
                    </tr>
                    <tr>
                        <th>95-th percentile</th>
                        <td>39670</td>
                    </tr>
                    <tr>
                        <th>Maximum</th>
                        <td>1731412</td>
                    </tr>
                    <tr>
                        <th>Range</th>
                        <td>1731412</td>
                    </tr>
                    <tr>
                        <th>Interquartile range</th>
                        <td>13345</td>
                    </tr>
                </table>
            </div>
            <div class="col-md-4 col-md-offset-2">
                <p class="h4">Descriptive statistics</p>
                <table class="stats indent">
                    <tr>
                        <th>Standard deviation</th>
                        <td>19665</td>
                    </tr>
                    <tr>
                        <th>Coef of variation</th>
                        <td>1.2764</td>
                    </tr>
                    <tr>
                        <th>Kurtosis</th>
                        <td>845.13</td>
                    </tr>
                    <tr>
                        <th>Mean</th>
                        <td>15407</td>
                    </tr>
                    <tr>
                        <th>MAD</th>
                        <td>10230</td>
                    </tr>
                    <tr class="">
                        <th>Skewness</th>
                        <td>16.004</td>
                    </tr>
                    <tr>
                        <th>Sum</th>
                        <td>3959238461</td>
                    </tr>
                    <tr>
                        <th>Variance</th>
                        <td>386710000</td>
                    </tr>
                    <tr>
                        <th>Memory size</th>
                        <td>2.0 MiB</td>
                    </tr>
                </table>
            </div>
        </div>
        <div role="tabpanel" class="tab-pane col-md-8 col-md-offset-2" id="histogram8428251298770906812">
            <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAlgAAAGQCAYAAAByNR6YAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAPYQAAD2EBqD%2BnaQAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAIABJREFUeJzt3XtU1WXe//%2BXuFE2mEqemlrNLSk44xHygIpy5wEdU8zxEJUxVlpTMpLenmK0dDQPjWR5KFPTnNR1Z5lOWZhOM2ZOKVpZOY4YqKjdqKBgchSQ6/dHP/a3LRqIF4Nbno%2B1WMt9XZ99fd7vj58NL/b%2B7E0tY4wRAAAArPGq7gIAAABuNgQsAAAAywhYAAAAlhGwAAAALCNgAQAAWEbAAgAAsIyABQAAYBkBCwAAwDICFgAAgGUELAAAAMsIWAAAAJYRsAAAACwjYAEAAFhGwAIAALCMgAUAAGAZAQsAAMAyAhYAAIBlBCwAAADLCFgAAACWEbAAAAAsI2ABAABYRsACAACwjIAFAABgGQELAADAMgIWAACAZQQsAAAAywhYAAAAlhGwAAAALCNgAQAAWEbAAgAAsIyABQAAYBkBCwAAwDICFgAAgGUELAAAAMsIWAAAAJYRsAAAACwjYAEAAFhGwAIAALCMgAUAAGCZo7oLqCkyMrKtr%2BnlVUu33uqnzMxclZQY6%2BvfyOid3um95qB3er%2Be3ps0ucViVRXHM1gezMurlmrVqiUvr1rVXcp/HL3Te01D7/Re03h67wQsAAAAywhYAAAAlhGwAAAALCNgAQAAWEbAAgAAsIyABQAAYBkBCwAAwDICFgAAgGUELAAAAMsIWAAAAJYRsAAAACwjYAEAAFhGwAIAALDMUd0F4Pp0mvZRdZdQYVvHh1V3CQAA/EfwDBYAAIBlBCwAAADLqi1gJSUl6dFHH1WXLl0UFhamKVOmKDMzU5I0Y8YMtW3bViEhIa6vDRs2uO67cuVKhYeHKzg4WNHR0Tp69KhrLi8vT3FxcQoNDVXHjh01ZcoU5ebmuuaPHTumUaNGKSQkRD169NBrr73mVtfOnTsVGRmp4OBgDRgwQDt27KjiIwEAAG421RKwCgoKNGbMGIWEhOif//ynPvjgA50/f15//OMfJUkHDhzQ7NmztX//ftdXVFSUJGnz5s1au3atVq1apcTERLVp00axsbEyxkiSZs%2BerVOnTmnbtm3avn27Tp06pfj4eElSUVGRnnzySbVr106JiYlasWKF1q9fr61bt0qSUlNTNW7cOD399NP64osvNG7cOI0fP15nzpyphqMEAAA8VbUErLS0NP3qV79STEyM6tSpI39/f0VFRWnfvn0qLCzUd999p7Zt217xvm%2B//bYeeughBQYGqm7dupo4caLS0tKUmJio/Px8bdmyRbGxsWrYsKEaNWqkSZMmadOmTcrPz9e%2BffuUnp6u2NhY1alTR61bt1Z0dLTWr18v6cfw1qlTJ/Xt21cOh0P33nuvOnfu7PbsGQAAQHmqJWDdddddev3111W7dm3X2LZt29SmTRslJSWpuLhYixcvVvfu3dW/f3%2BtWLFCJSUlkqSUlBQFBQW57uft7a3mzZsrKSlJx48fV1FRkdt8ixYtVFBQoNTUVCUnJysgIEB16tRxzbds2VJJSUlXXPvyeQAAgIqo9o9pMMbo5Zdf1o4dO7Ru3TqdPXtWXbp0UXR0tBYuXKhDhw4pJiZGXl5eGjNmjHJzc%2BV0Ot3W8PHxUV5ennJyciRJvr6%2BrrnSbXNzc694X6fTqby8PNc2V1v7WqSnpysjI8NtzOHwVdOmTa9pnfLUru1Z71FwOOzVW9q7px0DG%2Bid3msaeqd3T1StASsnJ0dxcXE6ePCg1q1bp1atWqlVq1YKC/t/n5fUvn17jRo1SgkJCRozZoycTqcKCgrc1ikoKJCfn58rWOXn58vPz8/1b0mqV6%2BefH19XbdL/XTbn1v7WmzYsEFLly51G4uJiVFsbOw1rXOz8fe/tuNYEfXrO8vf6CZF7zUTvddM9O55qi1gnThxQo8//rhuv/12bdy4Ubfeeqsk6eOPP9bZs2f1wAMPuLYtLCyUj4%2BPJCkwMFDJycnq1auXpB8vXE9NTVVQUJACAgLk7e2tlJQUdejQQZJ05MgR18uI586dU2pqqoqLi%2BVw/Nh6SkqKAgMDJUlBQUE6ePCgW50pKSlXvR7saqKiotS7d2%2B3MYfDV1lZuVe5R%2BV4Wqq32X/t2l6qX9%2BpCxfydelSibV1PQG90zu91xz0fv29V8Uv9xVRLQHrhx9%2B0KhRo9S1a1fNmTNHXl7/LygYYzRv3jz913/9l7p27aqvv/5ab775puLi4iRJw4YN05IlSxQeHq6AgAC99NJLaty4sTp16iRvb28NGDBA8fHxWrRokSQpPj5egwYNko%2BPj0JDQ%2BXv768XX3xR48eP17Fjx7R27VpNmDBBkjR48GC98cYbSkhIUL9%2B/bR9%2B3bt3btX06ZNu6b%2BmjZtWublwIyMbBUX16wHx%2BWqov9Ll0pq7HGld3qvaeid3j1JtQSsTZs2KS0tTVu3btVHH7n/qZf9%2B/crLi5OM2fO1JkzZ9S4cWONGzdO9913nyRp%2BPDhys7OVkxMjDIzM9WuXTstX75c3t7ekn78DK0XXnhBkZGRKioqUp8%2BffTss89KkhwOh1avXq1Zs2YpLCxMvr6%2Bio6O1tChQyX9eEH8K6%2B8ovj4eE2bNk133HGHlixZooCAgP/g0QEAAJ6ulin9AClUqYyMbOtrOhxeiojfZX3dqmLzbxE6HF7y9/dTVlauR/5mcz3ond7pveag9%2BvvvUmTWyxWVXGedREPAACAByBgAQAAWEbAAgAAsIyABQAAYBkBCwAAwDICFgAAgGUELAAAAMsIWAAAAJYRsAAAACwjYAEAAFhGwAIAALCMgAUAAGAZAQsAAMAyAhYAAIBlBCwAAADLCFgAAACWEbAAAAAsI2ABAABYRsACAACwjIAFAABgGQELAADAMgIWAACAZQQsAAAAywhYAAAAlhGwAAAALCNgAQAAWEbAAgAAsIyABQAAYBkBCwAAwDICFgAAgGUELAAAAMsIWAAAAJYRsAAAACwjYAEAAFhGwAIAALCMgAUAAGAZAQsAAMAyAhYAAIBlBCwAAADLCFgAAACWEbAAAAAsI2ABAABYRsACAACwjIAFAABgGQELAADAMgIWAACAZQQsAAAAywhYAAAAlhGwAAAALCNgAQAAWFZtASspKUmPPvqounTporCwME2ZMkWZmZmSpG%2B%2B%2BUYjRoxQSEiIevfurXfeecftvps3b1ZERISCg4M1dOhQ7d%2B/3zV36dIlvfDCC%2BrevbtCQkL01FNPKT093TV/7tw5jR07Vp06dVJoaKjmzJmj4uJi13x5%2BwYAAChPtQSsgoICjRkzRiEhIfrnP/%2BpDz74QOfPn9cf//hH/fDDD3riiSc0ZMgQ7du3T3PmzNG8efP07bffSpISExM1e/ZszZ8/X/v27dPgwYP11FNPKT8/X5K0bNkyffbZZ3r33Xe1a9cu%2Bfj4aPr06a59jx8/Xr6%2Bvtq1a5c2btyo3bt3a82aNZJU7r4BAAAqoloCVlpamn71q18pJiZGderUkb%2B/v6KiorRv3z5t375dDRs21MiRI%2BVwONStWzdFRkZq/fr1kqR33nlHAwcOVMeOHeXt7a1HHnlE/v7%2BSkhIcM0//vjj%2BsUvfqF69epp2rRp%2BvTTT3Xy5EkdP35ce/fu1eTJk%2BV0OnXnnXdq7NixrrXL2zcAAEBFOKpjp3fddZdef/11t7Ft27apTZs2Sk5OVlBQkNtcy5YttXHjRklSSkqKhg0bVmY%2BKSlJ2dnZOn36tNv9GzdurAYNGujw4cOSpIYNG6pZs2au%2BRYtWigtLU0XLlwod98VlZ6eroyMDLcxh8NXTZs2vaZ1ylO7tmddQudw2Ku3tHdPOwY20Du91zT0Tu%2BeqFoC1k8ZY/Tyyy9rx44dWrdund588005nU63bXx8fJSXlydJys3Nvep8bm6uJMnX17fMfOnc5fctvV16/5/bd0Vt2LBBS5cudRuLiYlRbGzsNa1zs/H397O%2BZv36zvI3uknRe81E7zUTvXueag1YOTk5iouL08GDB7Vu3Tq1atVKTqdT2dnZbtsVFBTIz%2B/HH85Op1MFBQVl5v39/V3hqPR6rMvvb4wpM1d628/Pr9x9V1RUVJR69%2B7tNuZw%2BCorK/ea1imPp6V6m/3Xru2l%2BvWdunAhX5culVhb1xPQO73Te81B79ffe1X8cl8R1RawTpw4occff1y33367Nm7cqFtvvVWSFBQUpM8%2B%2B8xt25SUFAUGBkqSAgMDlZycXGY%2BPDxcDRo0ULNmzZSSkuJ6qS8jI0Pnz59XUFCQSkpKdP78eZ09e1aNGzeWJB05ckS33XabbrnllnL3XVFNmzYt83JgRka2iotr1oPjclXR/6VLJTX2uNI7vdc09E7vnqRangL54YcfNGrUKN19991atWqVK1xJUkREhM6ePas1a9aoqKhIe/bs0ZYtW1zXXQ0fPlxbtmzRnj17VFRUpDVr1ujcuXOKiIiQJA0dOlTLli3TyZMnlZOTo7lz56pLly765S9/qebNm6tjx46aO3eucnJydPLkSb366qsaPnx4hfYNAABQEdXyDNamTZuUlpamrVu36qOPPnKb279/v1avXq05c%2BZo8eLFuvXWWzV9%2BnR17dpVktStWzfNmDFDM2fO1JkzZ9SyZUutXLlSDRs2lPTjtU7FxcUaOXKkcnNzFRoaqpdfftm1/uLFizVr1iz16dNHXl5eGjJkiMaOHStJ8vf3/9l9AwAAVEQtY4yp7iJqgoyM7PI3ukYOh5ci4ndZX7eqbB0fZm0th8NL/v5%2BysrK9cinjq8HvdM7vdcc9H79vTdpcovFqirOs66SBgAA8AAELAAAAMsIWAAAAJYRsAAAACwjYAEAAFhGwAIAALCMgAUAAGAZAQsAAMAyAhYAAIBlBCwAAADLCFgAAACWEbAAAAAsI2ABAABYRsACAACwjIAFAABgGQELAADAMgIWAACAZQQsAAAAywhYAAAAlhGwAAAALCNgAQAAWEbAAgAAsIyABQAAYBkBCwAAwDICFgAAgGUELAAAAMsIWAAAAJYRsAAAACwjYAEAAFhGwAIAALCMgAUAAGAZAQsAAMAyAhYAAIBlBCwAAADLCFgAAACWEbAAAAAsI2ABAABYRsACAACwrFIB69KlS7brAAAAuGlUKmCFh4frz3/%2Bs1JSUmzXAwAA4PEqFbD%2B8Ic/6KuvvtKgQYM0YsQIvfXWW8rOzrZdGwAAgEeqVMB68MEH9dZbb%2Bmjjz5S9%2B7dtXLlSvXo0UMTJ07U559/brtGAAAAj3JdF7k3b95cEyZM0EcffaSYmBj9/e9/1%2BjRo9W7d2%2B98cYbXKsFAABqJMf13Pmbb77RX//6VyUkJKiwsFAREREaOnSozpw5o0WLFunAgQNauHChrVoBAAA8QqUC1quvvqr33ntPx48fV7t27TRhwgQNGjRI9erVc21Tu3ZtPffcc9YKBQAA8BSVCljr1q3T4MGDNXz4cLVs2fKK27Ro0UKTJk26ruIAAAA8UaUC1qeffqqcnBydP3/eNZaQkKBu3brJ399fktS6dWu1bt3aTpUAAAAepFIXuf/73/9W//79tWHDBtfYggULFBkZqe%2B%2B%2B85acQAAAJ6oUgHrz3/%2Bs/r166cJEya4xj7%2B%2BGOFh4dr/vz51ooDAADwRJUKWAcPHtQTTzyhOnXquMZq166tJ554Ql9//fU1r5eZmamIiAglJia6xmbMmKG2bdsqJCTE9fXTZ8xWrlyp8PBwBQcHKzo6WkePHnXN5eXlKS4uTqGhoerYsaOmTJmi3Nxc1/yxY8c0atQohYSEqEePHnrttdfc6tm5c6ciIyMVHBysAQMGaMeOHdfcEwAAqLkqFbDq1aunEydOlBk/ffq0fHx8rmmtL7/8UlFRUWXWO3DggGbPnq39%2B/e7vqKioiRJmzdv1tq1a7Vq1SolJiaqTZs2io2NlTFGkjR79mydOnVK27Zt0/bt23Xq1CnFx8dLkoqKivTkk0%2BqXbt2SkxM1IoVK7R%2B/Xpt3bpVkpSamqpx48bp6aef1hdffKFx48Zp/PjxOnPmzDUfJwAAUDNVKmD1799fM2fO1Oeff66cnBzl5uZqz549mjVrliIiIiq8zubNmzVp0iS3lxolqbCwUN99953atm17xfu9/fbbeuihhxQYGKi6detq4sSJSktLU2JiovLz87VlyxbFxsaqYcOGatSokSZNmqRNmzYpPz9f%2B/btU3p6umJjY1WnTh21bt1a0dHRWr9%2BvaumTp06qW/fvnI4HLr33nvVuXNnt2fPAAAAfk6lAtbEiRN111136bHHHlPnzp3VqVMnPfroo2rZsqWmTJlS4XV69Oihv/3tb7r33nvdxpOSklRcXKzFixere/fu6t%2B/v1asWKGSkhJJUkpKioKCglzbe3t7q3nz5kpKStLx48dVVFTkNt%2BiRQsVFBQoNTVVycnJCggIcHt5s2XLlkpKSrri2pfPAwAAlKdSH9PgdDq1fPlyHTt2TIcPH5a3t7datGih5s2bX9M6TZo0ueJ4dna2unTpoujoaC1cuFCHDh1STEyMvLy8NGbMGOXm5srpdLrdx8fHR3l5ecrJyZEk%2Bfr6utUrSbm5uVe8r9PpVF5enmubq61dUenp6crIyHAbczh81bRp0wqvURG1a1/XXzr6j3M47NVb2runHQMb6J3eaxp6p3dPdF1/KicgIEABAQG2anEJCwtTWFiY63b79u01atQoJSQkaMyYMXI6nSooKHC7T0FBgfz8/FzBKj8/X35%2Bfq5/Sz9eO%2Bbr6%2Bu6Xeqn2/7c2hW1YcMGLV261G0sJiZGsbGxFV7jZuTvX/FjWFH16zvL3%2BgmRe81E73XTPTueSoVsI4dO6ZZs2bpyy%2B/VFFRUZn5Q4cOXVdRH3/8sc6ePasHHnjANVZYWOi6gD4wMFDJycnq1auXpB8vXE9NTVVQUJACAgLk7e2tlJQUdejQQZJ05MgR18uI586dU2pqqoqLi%2BVw/Nh%2BSkqKAgMDJUlBQUE6ePCgWz0pKSlXvR7sSqKiotS7d2%2B3MYfDV1lZuVe5R%2BV4Wqq32X/t2l6qX9%2BpCxfydelSibV1PQG90zu91xz0fv29V8Uv9xVRqYA1c%2BZMpaWladKkSbrlllts1yRjjObNm6f/%2Bq//UteuXfX111/rzTffVFxcnCRp2LBhWrJkicLDwxUQEKCXXnpJjRs3VqdOneTt7a0BAwYoPj5eixYtkiTFx8dr0KBB8vHxUWhoqPz9/fXiiy9q/PjxOnbsmNauXeu60H7w4MF64403lJCQoH79%2Bmn79u3au3evpk2bVuH6mzZtWublwIyMbBUX16wHx%2BWqov9Ll0pq7HGld3qvaeid3j1JpQLW/v379Ze//EUhISG265EkRUREKC4uTjNnztSZM2fUuHFjjRs3Tvfdd58kafjw4crOzlZMTIwyMzPVrl07LV%2B%2BXN7e3pJ%2B/AytF154QZGRkSoqKlKfPn307LPPSpIcDodWr16tWbNmKSwsTL6%2BvoqOjtbQoUMl/XhB/CuvvKL4%2BHhNmzZNd9xxh5YsWVIlL4UCAICbUy1T%2BuFR1%2BC///u/tXLlyjLvtsPVZWRkW1/T4fBSRPwu6%2BtWla3jw8rfqIIcDi/5%2B/spKyvXI3%2BzuR70Tu/0XnPQ%2B/X33qSJ/VfaKqJSF/GUvrsvO9t%2BaAAAAPB0lXqJcOfOnfr6668VGhqqRo0auX2mlCT9/e9/t1IcAACAJ6pUwAoNDVVoaKjtWgAAAG4KlQpYf/jDH2zXAQAAcNOo9AcpJSUlKS4uTg888IDOnDmj9evXKzEx0WZtAAAAHqlSAetf//qXRowYoe%2B//17/%2Bte/VFhYqEOHDumxxx7Tjh07bNcIAADgUSoVsOLj4/XYY49p7dq1rs%2Beev755/W73/2uzJ%2BIAQAAqGkq/QzWkCFDyow/%2BOCDOnr06HUXBQAA4MkqFbC8vb2Vk5NTZjwtLU1Op2f%2BUUYAAABbKhWw%2BvbtqxdffFFZWVmusSNHjmjOnDm65557bNUGAADgkSoVsKZOnaqCggJ1795d%2Bfn5Gjp0qAYNGiSHw6EpU6bYrhEAAMCjVOpzsOrVq6e33npLu3fv1r///W%2BVlJQoKChIPXv2lJdXpT/5AQAA4KZQqYBVqlu3burWrZutWgAAAG4KlQpYvXv3Vq1ata46z98iBAAANVmlAtZvf/tbt4BVVFSk48eP69NPP9X48eOtFQcAAOCJKhWwxo0bd8XxdevW6csvv9Tvfve76yoKAADAk1m9Ir1Xr17auXOnzSUBAAA8jtWAtXfvXtWtW9fmkgAAAB6nUi8RXv4SoDFGOTk5Onz4MC8PAgCAGq9SAev2228v8y5Cb29vjRo1SpGRkVYKAwAA8FSVCljz58%2B3XQcAAMBNo1IBa9%2B%2BfRXetnPnzpXZBQAAgMeqVMB65JFHZIxxfZUqfdmwdKxWrVo6dOiQhTIBAAA8R6UC1pIlSzRv3jxNnTpVXbt2lbe3t7755hvNnDlTDz30kHr16mW7TgAAAI9RqY9peOGFFzRjxgz17dtX9erVU926ddWlSxfNmjVLq1ev1h133OH6AgAAqGkqFbDS09P1i1/8osx4vXr1lJWVdd1FAQAAeLJKBazg4GAtXLhQOTk5rrHz589rwYIF6tatm7XiAAAAPFGlrsGaPn26Ro0apfDwcDVv3lySdOzYMTVp0kRvvvmmzfoAAAA8TqUCVosWLZSQkKAtW7boyJEjkqSHHnpIAwcOlNPptFogAACAp6lUwJKk%2BvXra8SIEfr%2B%2B%2B915513Svrx09wBAABqukpdg2WMUXx8vDp37qxBgwbp9OnTmjp1quLi4lRUVGS7RgAAAI9SqYC1du1avffee5oxY4bq1KkjSerbt6/%2B8Y9/aNGiRVYLBAAA8DSVClgbNmzQc889p6FDh7o%2Bvf3ee%2B/VnDlz9OGHH1otEAAAwNNUKmB9//33%2BvWvf11mvFWrVjp79ux1FwUAAODJKhWw7rjjDn377bdlxnfu3Om64B0AAKCmqtS7CEePHq0//elPOnPmjIwx2r17t9566y2tXbtWcXFxtmsEAADwKJUKWMOGDVNxcbGWLVumgoICPffcc2rUqJEmTJigBx980HaNAAAAHqVSAev999/Xb37zG0VFRSkzM1PGGDVq1Mh2bQAAAB6pUtdgPf/8866L2W%2B99VbCFQAAwE9UKmA1b95chw8ftl0LAADATaFSLxEGBgZq0qRJev3119W8eXPVrVvXbX7evHlWigMAAPBElQpYJ06cUMeOHSVJGRkZVgsCAADwdBUOWPPmzdPTTz8tX19frV27tiprAgAA8GgVvgbrzTffVH5%2BvtvY6NGjlZ6ebr0oAAAAT1bhgGWMKTP21Vdf6eLFi1YLAgAA8HSVehchAAAAro6ABQAAYNk1BaxatWpVVR0AAAA3jWv6mIbnn3/e7TOvioqKtGDBAvn5%2Bbltx%2BdgAQCAmqzCAatz585lPvMqJCREWVlZysrKsl4YAACAp6pwwKqqz77KzMxUVFSUnn/%2BeYWGhkqSvvnmGz3//PNKSUmRv7%2B/nnrqKY0YMcJ1n82bN%2BvVV19VRkaG7rrrLj377LMKCQmRJF26dEnx8fF67733lJ%2Bfr65du%2BpPf/qTmjZtKkk6d%2B6cnn32We3du1e1a9fW4MGDNXXqVDkcjgrtGwAAoDzVepH7l19%2BqaioKJ04ccI19sMPP%2BiJJ57QkCFDtG/fPs2ZM0fz5s3Tt99%2BK0lKTEzU7NmzNX/%2BfO3bt0%2BDBw/WU0895fqMrmXLlumzzz7Tu%2B%2B%2Bq127dsnHx0fTp093rT9%2B/Hj5%2Bvpq165d2rhxo3bv3q01a9ZUaN8AAAAVUW0Ba/PmzZo0aZImTJjgNr59%2B3Y1bNhQI0eOlMPhULdu3RQZGan169dLkt555x0NHDhQHTt2lLe3tx555BH5%2B/srISHBNf/444/rF7/4herVq6dp06bp008/1cmTJ3X8%2BHHt3btXkydPltPp1J133qmxY8e61i5v3wAAABVRqb9FaEOPHj0UGRkph8PhFrKSk5MVFBTktm3Lli21ceNGSVJKSoqGDRtWZj4pKUnZ2dk6ffq02/0bN26sBg0a6PDhw5Kkhg0bqlmzZq75Fi1aKC0tTRcuXCh33xWVnp5e5no1h8PX9TKlLbVre9anbDgc9uot7d3TjoEN9E7vNQ2907snqraA1aRJkyuO5%2Bbmyul0uo35%2BPgoLy%2Bv3Pnc3FxJkq%2Bvb5n50rnL71t6u/T%2BP7fvitqwYYOWLl3qNhYTE6PY2NhrWudm4%2B/vV/5G16h%2BfWf5G92k6L1moveaid49T7UFrKtxOp3Kzs52GysoKHB9FITT6VRBQUGZeX9/f1c4uvxvJpbe3xhTZq70tp%2BfX7n7rqioqCj17t3bbczh8FVWVu41rVMeT0v1NvuvXdtL9es7deFCvi5dKrG2riegd3qn95qD3q%2B/96r45b4ibriAFRQUpM8%2B%2B8xtLCUlRYGBgZKkwMBAJScnl5kPDw9XgwYN1KxZM6WkpLhe6svIyND58%2BcVFBSkkpISnT9/XmfPnlXjxo0lSUeOHNFtt92mW265pdx9V1TTpk3LvByYkZGt4uKa9eC4XFX0f%2BlSSY09rvRO7zUNvdO7J7nhngKJiIjQ2bNntWbNGhUVFWnPnj3asmWL67qr4cOHa8uWLdqzZ4%2BKioq0Zs0anTt3ThEREZKkoUOHatmyZTp58qRycnI0d%2B5cdenSRb/85S/VvHlzdezYUXPnzlVOTo5OnjypV199VcOHD6/QvgEAACrihnsGy9/fX6tXr9acOXO0ePFi3XrrrZo%2Bfbq6du0qSerWrZtmzJihmTNn6syZM2rZsqVWrlyphg0bSvrxWqfi4mKNHDlSubm5Cg0N1csvv%2Bxaf/HixZo1a5b69OkjLy8vDRkyRGPHjq3QvgEAACqiljHGVHcRNUFGRnb5G10jh8NLEfG7rK9bVbaOD7O2lsPhJX9/P2Vl5XrkU8fXg97pnd5rDnq//t6bNLnFYlUVd8PvdH5QAAAWkklEQVS9RAgAAODpCFgAAACWEbAAAAAsI2ABAABYRsACAACwjIAFAABgGQELAADAMgIWAACAZQQsAAAAywhYAAAAlhGwAAAALCNgAQAAWEbAAgAAsIyABQAAYBkBCwAAwDICFgAAgGUELAAAAMsIWAAAAJYRsAAAACwjYAEAAFhGwAIAALCMgAUAAGAZAQsAAMAyAhYAAIBlBCwAAADLCFgAAACWEbAAAAAsI2ABAABYRsACAACwjIAFAABgGQELAADAMgIWAACAZQQsAAAAywhYAAAAlhGwAAAALCNgAQAAWEbAAgAAsIyABQAAYBkBCwAAwDICFgAAgGUELAAAAMsIWAAAAJYRsAAAACwjYAEAAFhGwAIAALCMgAUAAGAZAQsAAMAyAhYAAIBlBCwAAADLbtiAlZCQoNatWyskJMT1NXnyZEnSzp07FRkZqeDgYA0YMEA7duxwu%2B/KlSsVHh6u4OBgRUdH6%2BjRo665vLw8xcXFKTQ0VB07dtSUKVOUm5vrmj927JhGjRqlkJAQ9ejRQ6%2B99tp/pmEAAHDTuGED1oEDB3Tfffdp//79rq8FCxYoNTVV48aN09NPP60vvvhC48aN0/jx43XmzBlJ0ubNm7V27VqtWrVKiYmJatOmjWJjY2WMkSTNnj1bp06d0rZt27R9%2B3adOnVK8fHxkqSioiI9%2BeSTateunRITE7VixQqtX79eW7durbbjAAAAPM8NHbDatm1bZnzz5s3q1KmT%2BvbtK4fDoXvvvVedO3fWhg0bJElvv/22HnroIQUGBqpu3bqaOHGi0tLSlJiYqPz8fG3ZskWxsbFq2LChGjVqpEmTJmnTpk3Kz8/Xvn37lJ6ertjYWNWpU0etW7dWdHS01q9f/59uHwAAeLAbMmCVlJTo4MGD%2BuSTT9SrVy%2BFh4fr2Wef1Q8//KCUlBQFBQW5bd%2ByZUslJSVJUpl5b29vNW/eXElJSTp%2B/LiKiorc5lu0aKGCggKlpqYqOTlZAQEBqlOnzhXXBgAAqAhHdRdwJZmZmWrdurX69%2B%2BvxYsXKysrS1OnTtXkyZNVWFgop9Pptr2Pj4/y8vIkSbm5uVedz8nJkST5%2Bvq65kq3zc3NveJ9nU6na%2B2KSk9PV0ZGhtuYw%2BGrpk2bXtM65ald%2B4bMx1flcNirt7R3TzsGNtA7vdc09E7vnuiGDFiNGzd2e1nO6XRq8uTJuv/%2B%2BxUaGqqCggK37QsKCuTn5%2Bfa9mrzpcEqPz/ftX1%2Bfr4kqV69evL19XXdLvXTbStqw4YNWrp0qdtYTEyMYmNjr2mdm42//7Udx4qoX99Z/kY3KXqvmei9ZqJ3z3NDBqykpCR98MEHmjhxomrVqiVJKiwslJeXl9q3b69Dhw65bZ%2BSkuK6XiswMFDJycnq1auXpB8vXE9NTVVQUJACAgLk7e2tlJQUdejQQZJ05MgR18uI586dU2pqqoqLi%2BVwOFxrBwYGXlP9UVFR6t27t9uYw%2BGrrKzcq9yjcjwt1dvsv3ZtL9Wv79SFC/m6dKnE2rqegN7pnd5rDnq//t6r4pf7irghA1bDhg21fv16NWjQQI8%2B%2BqjS09O1YMEC/fa3v9WQIUP0l7/8RQkJCerXr5%2B2b9%2BuvXv3atq0aZKkYcOGacmSJQoPD1dAQIBeeuklNW7cWJ06dZK3t7cGDBig%2BPh4LVq0SJIUHx%2BvQYMGycfHR6GhofL399eLL76o8ePH69ixY1q7dq0mTJhwTfU3bdq0zMuBGRnZKi6uWQ%2BOy1VF/5culdTY40rv9F7T0Du9e5IbMmDddtttWr58uRYuXKhly5apbt26GjhwoCZPnqy6devqlVdeUXx8vKZNm6Y77rhDS5YsUUBAgCRp%2BPDhys7OVkxMjDIzM9WuXTstX75c3t7ekqQZM2bohRdeUGRkpIqKitSnTx89%2B%2ByzkiSHw6HVq1dr1qxZCgsLk6%2Bvr6KjozV06NBqOxYAAMDz1DKlHxCFKpWRkW19TYfDSxHxu6yvW1W2jg%2BztpbD4SV/fz9lZeV65G8214Pe6Z3eaw56v/7emzS5xWJVFedZF/EAAAB4AAIWAACAZQQsAAAAywhYAAAAlhGwAAAALCNgAQAAWEbAAgAAsIyABQAAYBkBCwAAwDICFgAAgGUELAAAAMsIWAAAAJYRsAAAACwjYAEAAFhGwAIAALCMgAUAAGAZAQsAAMAyAhYAAIBlBCwAAADLCFgAAACWEbAAAAAsI2ABAABYRsACAACwjIAFAABgGQELAADAMgIWAACAZQQsAAAAywhYAAAAlhGwAAAALCNgAQAAWEbAAgAAsIyABQAAYBkBCwAAwDICFgAAgGUELAAAAMsIWAAAAJYRsAAAACwjYAEAAFhGwAIAALCMgAUAAGAZAQsAAMAyAhYAAIBlBCwAAADLCFgAAACWEbAAAAAsI2ABAABYRsACAACwjIAFAABgGQELAADAMgLWFZw7d05jx45Vp06dFBoaqjlz5qi4uLi6ywIAAB6CgHUF48ePl6%2Bvr3bt2qWNGzdq9%2B7dWrNmTXWXBQAAPAQB6zLHjx/X3r17NXnyZDmdTt15550aO3as1q9fX92lAQAAD0HAukxycrIaNmyoZs2aucZatGihtLQ0XbhwoRorAwAAnsJR3QXcaHJzc%2BV0Ot3GSm/n5eWpfv365a6Rnp6ujIwMtzGHw1dNmza1V6ik2rU9Kx87HPbqLe3d046BDfRO7zUNvdO7JyJgXcbX11f5%2BfluY6W3/fz8KrTGhg0btHTpUrexP/zhDxo3bpydIv9/6enpGnVbsqKioqyHtxtdenq6/vKX1%2Bmd3msMeqd3evcsnhkLq1BgYKDOnz%2Bvs2fPusaOHDmi2267TbfcckuF1oiKitKmTZvcvqKioqzXmpGRoaVLl5Z5tqwmoHd6r2nond5rGk/vnWewLtO8eXN17NhRc%2BfO1axZs5SVlaVXX31Vw4cPr/AaTZs29ci0DQAA7OAZrCtYvHixiouL1adPH91///3q2bOnxo4dW91lAQAAD8EzWFfQuHFjLV68uLrLAAAAHqr2zJkzZ1Z3Eag8Pz8/denSpcIX4N9M6J3eaxp6p/eaxpN7r2WMMdVdBAAAwM2Ea7AAAAAsI2ABAABYRsACAACwjIAFAABgGQELAADAMgIWAACAZQQsAAAAywhYAAAAlhGwPNS5c%2Bc0duxYderUSaGhoZozZ46Ki4uru6wrSkpK0qOPPqouXbooLCxMU6ZMUWZmpiRpxowZatu2rUJCQlxfGzZscN135cqVCg8PV3BwsKKjo3X06FHXXF5enuLi4hQaGqqOHTtqypQpys3Ndc0fO3ZMo0aNUkhIiHr06KHXXnvNra6dO3cqMjJSwcHBGjBggHbs2GG994SEBLVu3dqtv8mTJ1do/57c%2B/vvv%2B/Wc0hIiNq2bau2bdtKksaMGaN27dq5zX/66aeSpEuXLumFF15Q9%2B7dFRISoqeeekrp6emutcs797/55huNGDFCISEh6t27t9555x232jZv3qyIiAgFBwdr6NCh2r9/v7W%2BMzMzFRERocTERCv1eNKxuFLv27Zt03333ae7775bvXv31tKlS1VSUuKaHzBggDp06OB2Hhw5ckRS1Z/jP/f4stH7jfy9rSp7f%2B6558o89n/9619r9OjRkqSSkhKFhIQoODjYbZu8vDxJVXtOl/d4ss7AIz388MNm4sSJJi8vz5w4ccIMHDjQrFy5srrLKiM/P9%2BEhYWZRYsWmYsXL5rMzEzz%2BOOPm9///vfGGGN%2B%2B9vfmk2bNl3xvps2bTI9e/Y03333nSkoKDDz5s0zAwcONCUlJcYYY5555hkzatQok5WVZc6ePWsefvhhM3PmTGOMMYWFhaZfv35mwYIF5uLFi%2BbgwYOmR48eJiEhwRhjzLFjx0y7du3M3/72N1NUVGQ%2B/PBD0759e3P69Gmr/c%2BfP98888wzZcbL2//N0PtPnT592oSFhZm//vWvxhhjQkNDTWJi4hW3XbJkiYmMjDRpaWkmOzvbjB8/3jz%2B%2BOOu%2BZ8798%2BfP2%2B6dOli1q1bZ4qKisznn39uQkJCzDfffGOMMWbPnj0mJCTEfPHFF6awsNC88cYbJjQ01OTl5V13j1988YXp27evCQoKMnv27LFSj6cciyv1fuDAAdO%2BfXvzj3/8w1y6dMmkpKSYXr16mVWrVhljjMnOzjatWrUy33///RXXrMpzvLzH1/X2bsyN%2B73tP9H7T%2B3atct06dLFfPfdd8YYYw4fPmzatGljLl68eMXtq/KcLu/xZBsBywOlpqaaoKAgtx%2BIH374obnnnnuqsaorO3LkiBk9erQpLi52jX388cfm7rvvNhcvXjRt2rRxPfAu98ADD5hly5a5bhcWFpqQkBCze/duk5eXZ9q0aWO%2B/PJL1/zXX39t2rdvb/Ly8sxnn31mgoOD3R7Ey5cvNyNHjjTGGLNw4ULz6KOPuu1v9OjRZtGiRVb6LjVy5Eizbt26MuPl7f9m6L1USUmJiY6ONtOmTTPGGHPixAnzq1/9ymRnZ19x%2B/DwcPP%2B%2B%2B%2B7bmdkZJhWrVqZEydOlHvuv/3226Zfv35u6z333HNmypQpxhhjJk6caKZPn%2B42/5vf/MZs3LjxunrctGmTueeee8yHH37o9sPmeuvxhGNxtd4/%2BugjM3fuXLdt586da5588kljjDG7d%2B82oaGhV1yzqs/xn3t82ej9Rv7eVtW9/9S5c%2BdMaGioee%2B991xjGzduNEOHDr3imlV9Tv/c46kq8BKhB0pOTlbDhg3VrFkz11iLFi2UlpamCxcuVGNlZd111116/fXXVbt2bdfYtm3b1KZNGyUlJam4uFiLFy9W9%2B7d1b9/f61YscL1EkJKSoqCgoJc9/P29lbz5s2VlJSk48ePq6ioyG2%2BRYsWKigoUGpqqpKTkxUQEKA6deq45lu2bKmkpKQrrn35vA0lJSU6ePCgPvnkE/Xq1Uvh4eF69tln9cMPP5S7f0/v/afee%2B89paSk6JlnnpEkHThwQH5%2BfpowYYK6du2qQYMGaePGjZKk7OxsnT592q2%2Bxo0bq0GDBjp8%2BHC5535ycvI1HVdbvffo0UN/%2B9vfdO%2B997qNX089nnIsrtZ7//79FRcX57pdUFCgTz75RG3atJH043ngdDr18MMPKzQ0VEOHDnW9lFXV5/jPPb5s9H4jf2%2Br6t5/Kj4%2BXm3bttXgwYNdYwcOHNDFixc1bNgwde3aVSNHjtRXX30lqfyfbVX5eKoKjipZFVUqNzdXTqfTbaz0dl5enurXr18dZZXLGKOXX35ZO3bs0Lp163T27Fl16dJF0dHRWrhwoQ4dOqSYmBh5eXlpzJgxV%2BzTx8dHeXl5ysnJkST5%2Bvq65kq3zc3NveoxKn2d/%2BfWtiUzM1OtW7dW//79tXjxYmVlZWnq1KmaPHmyCgsLf3b/nt57qZKSEi1btkxPPvmk6tWrJ0kqLCxUcHCwJkyYoMDAQCUmJmrcuHHy8/NTSEhImd5K6yu9BuXnzv3yequq3ps0aXLF8eupp7TfG/1YXK33n8rJydHTTz8tHx8fPfLII5KkWrVqqV27dvqf//kf3X777froo480btw4rVu3znXNTVWd41Xde3Z29g37ve0/9f9%2B8uRJvf/%2B%2B2WukfLx8VH79u319NNPq0GDBlq/fr1Gjx6t999/v9yfbVX9eLKNgOWBfH19lZ%2Bf7zZWetvPz686SipXTk6O4uLidPDgQa1bt06tWrVSq1atFBYW5tqmffv2GjVqlBISEjRmzBg5nU4VFBS4rVNQUCA/Pz/XgyQ/P9/Vc%2BkxqFev3lWPUem2P7e2LY0bN9b69etdt51OpyZPnqz7779foaGhP7t/T%2B%2B9VGJiotLT0zV8%2BHDX2JAhQzRkyBDX7R49emjIkCHaunWrunfv7tbP5fUZY3723Hc6ncrOzr7ifaWr9%2B7v73%2BdnV7Z9dRT%2BoPC04/F0aNHFRsbq0aNGunNN990Be0xY8a4bTd48GB98MEH2rZtmyIjI139VMU5XtWPgbCwsBv2e9t/6vH/7rvvui5w/6nSZ7JLjR49Wps2bdLOnTvVrFmzKjuny3s8VQVeIvRAgYGBOn/%2BvM6ePesaO3LkiG677Tbdcsst1VjZlZ04cULDhg1TTk6ONm7cqFatWkmSPv74Y7311ltu2xYWFsrHx0fSj30mJye75oqKipSamqqgoCAFBATI29tbKSkprvkjR464nu4ODAxUamqq27tPUlJSFBgYKEkKCgpyW/vyeRuSkpIUHx8vY4xbf15eXmrfvv3P7t/Tey%2B1bds2RUREuP3WuHHjRm3dutVtu8LCQtWtW1cNGjRQs2bN3HrLyMjQ%2BfPnFRQUVO65X15vlx/Xy%2Bdtu556boZjsXPnTo0YMUI9e/bUqlWr1KBBA9fcqlWrtHv3brftS8%2BDqj7Hf%2B7xZcON/L2tqnsvtX37dt13331lxl966SX9%2B9//dhsr/X%2BvynO6vMdTlaiSK7tQ5R588EEzYcIEk52d7XqnxeLFi6u7rDLOnz9v7rnnHvPMM8%2BYS5cuuc1t377dtG/f3nz%2B%2BeempKTEfPXVVyY0NNT1TrO3337b9OzZ0xw6dMj1bpeIiAhTWFhojDFm0qRJ5uGHHzbnzp0z586dMw8//LCZOnWqMcaYoqIi07t3bzN//nxTUFBgDh06ZHr06GHeffddY4wxKSkppl27dubDDz90vdOmXbt25ujRo9Z6P3XqlAkODjYrVqwwRUVF5v/%2B7//M/fffb/74xz%2BWu39P773UoEGDzNtvv%2B029sYbb5hu3bqZgwcPmkuXLpkdO3aY9u3bm3379hljjHnppZfMoEGDzIkTJ1zv9Hn44Ydd9/%2B5cz8zM9N06tTJvPHGG6awsNDs3r3b7QLe0ncd7d692/Uuo86dO5usrCxrPf/0gt/rrcfTjsVPe9%2B/f79p06aNeeedd6647ezZs03//v3NiRMnTFFRkXnnnXdM%2B/btTWpqqjGmas/x8h5f19v7jfy9rap7N%2BbHcy8oKMj1f/lTTz75pHnooYdMenq6uXjxolmyZInp2rWr67yrynO6vMeTbQQsD5WRkWHGjRtnunTpYrp27Wrmz5/v9k69G8Xq1atNUFCQ6dChgwkODnb7MsaY//3f/zX9%2BvUzHTp0MH369HF7x11JSYlZtWqV6d27twkODjbR0dFuISA7O9tMnz7ddO/e3XTu3Nk888wzJjc31zWfmppqHnvsMdOxY0fTs2dPs3z5crfaPv30UzN48GATHBxsBg4caD755BPr/ScmJpqoqCgTEhJiunbtambPnm0KCgrK3f/N0LsxxgQHB5dZu6SkxLzyyiumV69epn379mbgwIFm69atrvnCwkKzYMEC07NnT3P33Xebp556ypw9e9Y1X965/%2B2337qOeZ8%2BfVw/eEr99a9/Nf379zfBwcFm%2BPDh5uuvv7ba8%2BU/bK6nHk87Fj/t/fe//71p1apVmcf96NGjjTE/vtNuzpw5pkePHqZDhw5m2LBhbsetKs/x8h5f19u7MTfu97b/RO/ffvutCQoKMvn5%2BWW2zcrKMs8884zp1q2ba/%2BHDh1yzVflOV3e48m2Wsb85PULAAAAXDeuwQIAALCMgAUAAGAZAQsAAMAyAhYAAIBlBCwAAADLCFgAAACWEbAAAAAsI2ABAABYRsACAACwjIAFAABgGQELAADAMgIWAACAZQQsAAAAywhYAAAAlhGwAAAALPv/ANTyLFbd/6JoAAAAAElFTkSuQmCC"/>
        </div>
        <div role="tabpanel" class="tab-pane col-md-12" id="common8428251298770906812">

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">0</td>
        <td class="number">1565</td>
        <td class="number">0.6%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">6746</td>
        <td class="number">32</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">3420</td>
        <td class="number">32</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">6259</td>
        <td class="number">30</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">6539</td>
        <td class="number">29</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">6980</td>
        <td class="number">29</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">3600</td>
        <td class="number">28</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">9550</td>
        <td class="number">28</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">7816</td>
        <td class="number">28</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">10228</td>
        <td class="number">28</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="other">
        <td class="fillremaining">Other values (45694)</td>
        <td class="number">255155</td>
        <td class="number">99.3%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr>
</table>
        </div>
        <div role="tabpanel" class="tab-pane col-md-12"  id="extreme8428251298770906812">
            <p class="h4">Minimum 5 values</p>

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">0</td>
        <td class="number">1565</td>
        <td class="number">0.6%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">1</td>
        <td class="number">24</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">2</td>
        <td class="number">12</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">3</td>
        <td class="number">20</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">4</td>
        <td class="number">19</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr>
</table>
            <p class="h4">Maximum 5 values</p>

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">690447</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:50%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">818209</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:50%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">854602</td>
        <td class="number">2</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">1730472</td>
        <td class="number">2</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">1731412</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:50%">&nbsp;</div>
        </td>
</tr>
</table>
        </div>
    </div>
</div>
</div><div class="row variablerow">
    <div class="col-md-3 namecol">
        <p class="h4 pp-anchor" id="pp_var_Current Loan Amount">Current Loan Amount<br/>
            <small>Numeric</small>
        </p>
    </div><div class="col-md-6">
    <div class="row">
        <div class="col-sm-6">
            <table class="stats ">
                <tr>
                    <th>Distinct count</th>
                    <td>27347</td>
                </tr>
                <tr>
                    <th>Unique (%)</th>
                    <td>10.6%</td>
                </tr>
                <tr class="ignore">
                    <th>Missing (%)</th>
                    <td>0.0%</td>
                </tr>
                <tr class="ignore">
                    <th>Missing (n)</th>
                    <td>0</td>
                </tr>
                <tr class="ignore">
                    <th>Infinite (%)</th>
                    <td>0.0%</td>
                </tr>
                <tr class="ignore">
                    <th>Infinite (n)</th>
                    <td>0</td>
                </tr>
            </table>

        </div>
        <div class="col-sm-6">
            <table class="stats ">

                <tr>
                    <th>Mean</th>
                    <td>13713000</td>
                </tr>
                <tr>
                    <th>Minimum</th>
                    <td>505</td>
                </tr>
                <tr>
                    <th>Maximum</th>
                    <td>99999999</td>
                </tr>
                <tr class="ignore">
                    <th>Zeros (%)</th>
                    <td>0.0%</td>
                </tr>
            </table>
        </div>
    </div>
</div>
<div class="col-md-3 collapse in" id="minihistogram-7712628620957852604">
    <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAABLCAYAAAA1fMjoAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAPYQAAD2EBqD%2BnaQAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAAzNJREFUeJzt3btLK2kYx/GfaxT9AwQrC4uITRANphMvKIvaCCE22gkKgqBImu2ErQM2doKCELAQRfCChYhIjCe2FoJ4QYsE7EQ0Os82u8K58JyzoIkcvp9yZl54pvjyTjHDVJiZCcAP/VHuAYDPLFTuAb4V/Wv7f6/58vefHzAJwA4CuAgEcBAI4CAQwEEggINAAAeBAA4CARwEAjgIBHAQCOAgEMBBIICDQAAHgQAOAgEcBAI4CARwEAjgIBDAQSCAg0AAB4EADgIBHAQCOAgEcBAI4CAQwEEggINAAAeBAA4CARwEAjgIBHAQCOAgEMBBIICDQADHp/sNNH4fv8MvvdlBAAeBAA4CARwEAjgIBHAQCOAgEMBRYWZW7iGAz4odBHAQCOAgEMBBIPgQ9/f36u3t1fHx8S9dHwSBUqmUOjo61NbWpkQioWw2%2B8FT/hyB4N3lcjkNDw/r%2Bvr6l9ek02nt7e1pdXVVJycn6u/v1/j4uJ6enj5w0p8jELyrtbU1zc7Oanp6%2BrtzR0dHisfjikajGhgY0MbGxtu5i4sLBUGgIAhkZqqoqFBNTU0pR/8xA95RPp%2B3YrFoZmbhcNgymYyZmZ2dnVkkErGdnR17eXmxXC5nsVjMDg4OzMzs/PzcOjs7LRwOW3Nzs7W0tFg2my3bffyHHQTvqq6uTqHQ958ZpdNp9fT0qK%2BvT5WVlWptbVUikdDKyookqVgsqr29XVtbWzo9PdXY2JimpqZUKBRKfQtf4YMplMTt7a0ymYyi0ejbsdfXVzU0NEiSksmkJiYm1NjYKEmanJzU%2Bvq6tre3NTo6WpaZJQJBidTX12toaEhzc3Nvx/L5vOzfFznu7u70/Pz81ZpQKKSqqqqSzvktHrFQEvF4XJubmzo8PFQQBLq8vNTIyIgWFxclSd3d3VpYWNDNzY2KxaKWlpZUKBTU1dVV1rl5FwsfpqmpScvLy4rFYpKk/f19zc/P6%2BrqSrW1tRocHNTMzIyqq6v18PCgVCql3d1dPT4%2BqqmpSclkUpFIpKz3QCCAg0cswEEggINAAAeBAA4CARwEAjgIBHAQCOAgEMBBIICDQAAHgQCOfwAFz8EadefR1AAAAABJRU5ErkJggg%3D%3D">

</div>
<div class="col-md-12 text-right">
    <a role="button" data-toggle="collapse" data-target="#descriptives-7712628620957852604,#minihistogram-7712628620957852604"
       aria-expanded="false" aria-controls="collapseExample">
        Toggle details
    </a>
</div>
<div class="row collapse col-md-12" id="descriptives-7712628620957852604">
    <ul class="nav nav-tabs" role="tablist">
        <li role="presentation" class="active"><a href="#quantiles-7712628620957852604"
                                                  aria-controls="quantiles-7712628620957852604" role="tab"
                                                  data-toggle="tab">Statistics</a></li>
        <li role="presentation"><a href="#histogram-7712628620957852604" aria-controls="histogram-7712628620957852604"
                                   role="tab" data-toggle="tab">Histogram</a></li>
        <li role="presentation"><a href="#common-7712628620957852604" aria-controls="common-7712628620957852604"
                                   role="tab" data-toggle="tab">Common Values</a></li>
        <li role="presentation"><a href="#extreme-7712628620957852604" aria-controls="extreme-7712628620957852604"
                                   role="tab" data-toggle="tab">Extreme Values</a></li>

    </ul>

    <div class="tab-content">
        <div role="tabpanel" class="tab-pane active row" id="quantiles-7712628620957852604">
            <div class="col-md-4 col-md-offset-1">
                <p class="h4">Quantile statistics</p>
                <table class="stats indent">
                    <tr>
                        <th>Minimum</th>
                        <td>505</td>
                    </tr>
                    <tr>
                        <th>5-th percentile</th>
                        <td>3558.2</td>
                    </tr>
                    <tr>
                        <th>Q1</th>
                        <td>8299</td>
                    </tr>
                    <tr>
                        <th>Median</th>
                        <td>14298</td>
                    </tr>
                    <tr>
                        <th>Q3</th>
                        <td>24367</td>
                    </tr>
                    <tr>
                        <th>95-th percentile</th>
                        <td>100000000</td>
                    </tr>
                    <tr>
                        <th>Maximum</th>
                        <td>99999999</td>
                    </tr>
                    <tr>
                        <th>Range</th>
                        <td>99999494</td>
                    </tr>
                    <tr>
                        <th>Interquartile range</th>
                        <td>16068</td>
                    </tr>
                </table>
            </div>
            <div class="col-md-4 col-md-offset-2">
                <p class="h4">Descriptive statistics</p>
                <table class="stats indent">
                    <tr>
                        <th>Standard deviation</th>
                        <td>34381000</td>
                    </tr>
                    <tr>
                        <th>Coef of variation</th>
                        <td>2.5071</td>
                    </tr>
                    <tr>
                        <th>Kurtosis</th>
                        <td>2.4574</td>
                    </tr>
                    <tr>
                        <th>Mean</th>
                        <td>13713000</td>
                    </tr>
                    <tr>
                        <th>MAD</th>
                        <td>23645000</td>
                    </tr>
                    <tr class="">
                        <th>Skewness</th>
                        <td>2.1113</td>
                    </tr>
                    <tr>
                        <th>Sum</th>
                        <td>3524100295981</td>
                    </tr>
                    <tr>
                        <th>Variance</th>
                        <td>1182100000000000</td>
                    </tr>
                    <tr>
                        <th>Memory size</th>
                        <td>2.0 MiB</td>
                    </tr>
                </table>
            </div>
        </div>
        <div role="tabpanel" class="tab-pane col-md-8 col-md-offset-2" id="histogram-7712628620957852604">
            <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAlgAAAGQCAYAAAByNR6YAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAPYQAAD2EBqD%2BnaQAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAIABJREFUeJzt3XtcVXW%2B//E3sEE2qEFeq1NHByGPZkGgZJqTF/J4wYwwuoxjp7JTkKTjpYdjFwczdcSazMnpbhpndHSistSsTqnTBcjsLgbeO5SgYCKX5LJ%2Bf/RjP2aHDZvdd7tZ9Ho%2BHjwe7u93re/67M9DHvvNWotFgGVZlgAAAGBMoL8LAAAAaG8IWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMIe/C/ilKCurNL5mYGCAzj47XOXlVWpstIyv/0tGb32H3voW/fUdeus7vuxtt26djK7nKc5g2VhgYIACAgIUGBjg71LaHXrrO/TWt%2Biv79Bb32mPvSVgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhDn8XgJ8nYd4Wf5fgsc3Th/i7BAAAzgjOYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABjmt4BVWFio//qv/9KgQYM0ZMgQzZkzR%2BXl5ZKkTz75RJMmTVJcXJxGjBih9evXu%2B2bm5urpKQkxcbGKiUlRbt27XLNNTQ0aMmSJbr88ssVFxenO%2B%2B8U6Wlpa75Y8eOKT09XQkJCUpMTNTChQtVX1/vmm/p2AAAAC3xS8Cqra3Vbbfdpri4OP3jH//Qq6%2B%2BquPHj%2Bv3v/%2B9vvvuO91%2B%2B%2B2aOHGiCgoKtHDhQi1atEiffvqpJCkvL08LFizQ4sWLVVBQoAkTJujOO%2B9UTU2NJGnlypV699139fe//107duxQaGio7r33Xtexp0%2BfrrCwMO3YsUMbNmzQ%2B%2B%2B/r1WrVklSi8cGAADwhF8CVklJifr27auMjAyFhIQoMjJSaWlpKigo0NatWxUREaGbbrpJDodDgwcPVnJysnJyciRJ69ev17hx4xQfH6/g4GDdfPPNioyM1KZNm1zzU6dO1TnnnKOOHTtq3rx52r59uw4fPqyDBw8qPz9fs2fPltPp1Pnnn6/09HTX2i0dGwAAwBMOfxz0V7/6lZ5%2B%2Bmm3sddff139%2B/dXUVGRYmJi3Ob69OmjDRs2SJKKi4t17bXXNpsvLCxUZWWlvv32W7f9u3btqrPOOkt79uyRJEVERKhHjx6u%2BaioKJWUlOjEiRMtHttTpaWlKisrcxtzOMLUvXv3Vq3TkqAge91C53DYp96m3tqtx3ZAb32L/voOvfWd9thbvwSsf2ZZlv70pz/p7bff1gsvvKDVq1fL6XS6bRMaGqrq6mpJUlVV1U/OV1VVSZLCwsKazTfN/XjfptdN%2B/%2BrY3tq3bp1WrFihdtYRkaGMjMzW7VOexMZGe7vElqtc2dnyxvBK/TWt%2Biv79Bb32lPvfVrwDp58qTmzp2rL774Qi%2B88IIuvPBCOZ1OVVZWum1XW1ur8PAfPpydTqdqa2ubzUdGRrrCUdP9WD/e37KsZnNNr8PDw1s8tqfS0tI0YsQItzGHI0wVFVWtWqcldkv6pt%2B/LwUFBapzZ6dOnKhRQ0Ojv8tpV%2Bitb9Ff36G3vuPL3vrrh3u/BaxDhw5p6tSpOvfcc7VhwwadffbZkqSYmBi9%2B%2B67btsWFxcrOjpakhQdHa2ioqJm88OGDdNZZ52lHj16qLi42HWpr6ysTMePH1dMTIwaGxt1/PhxHT16VF27dpUk7d27Vz179lSnTp1aPLanunfv3uxyYFlZperrf9nfkHZ8/w0Njbas2w7orW/RX9%2Bht77Tnnrrl1Mg3333naZMmaJLL71UzzzzjCtcSVJSUpKOHj2qVatWqa6uTh988IE2btzouu8qNTVVGzdu1AcffKC6ujqtWrVKx44dU1JSkiQpJSVFK1eu1OHDh3Xy5Ek99NBDGjRokC644AL16tVL8fHxeuihh3Ty5EkdPnxYjz/%2BuFJTUz06NgAAgCcCLMuyzvRBn3vuOS1evFhOp1MBAQFuc7t27dJnn32mhQsX6quvvtLZZ5%2Bt9PR0paSkuLZ5%2BeWXtXLlSh05ckR9%2BvTRvffeq0suuUSSVFdXp0cffVSvvPKKqqqqlJiYqAULFqhLly6SpKNHjyorK0t5eXkKDAzUxIkTNWvWLAUFBUlSi8f2VllZZcsbtZLDEaik7B3G1/WVzdOH%2BLsEjzkcgYqMDFdFRVW7%2BWmqraC3vkV/fYfe%2Bo4ve9utWyej63nKLwHrl4iARcDCD%2Bitb9Ff36G3vtMeA5a97pIGAACwAQIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGFtImCVl5crKSlJeXl5rrEHHnhAF110keLi4lxf69atc80/9dRTGjZsmGJjYzV58mTt27fPNVddXa25c%2BcqMTFR8fHxmjNnjqqqqlzz%2B/fv15QpUxQXF6ehQ4fqL3/5i1s927ZtU3JysmJjYzVmzBi9/fbbPnz3AACgvfF7wNq5c6fS0tJ06NAht/HPPvtMCxYs0K5du1xfaWlpkqTc3FytWbNGzzzzjPLy8tS/f39lZmbKsixJ0oIFC/TNN9/o9ddf19atW/XNN98oOztbklRXV6c77rhDAwYMUF5enp588knl5ORo8%2BbNkqQDBw5o2rRpuvvuu/Xhhx9q2rRpmj59uo4cOXIGuwIAAOzMrwErNzdXs2bN0owZM9zGT506pa%2B%2B%2BkoXXXTRaff729/%2BphtvvFHR0dHq0KGDZs6cqZKSEuXl5ammpkYbN25UZmamIiIi1KVLF82aNUsvvviiampqVFBQoNLSUmVmZiokJET9%2BvXT5MmTlZOT46opISFBo0aNksPh0NixYzVw4EC3s2cAAAD/il8D1tChQ/XGG29o7NixbuOFhYWqr6/X8uXLdfnll2v06NF68skn1djYKEkqLi5WTEyMa/vg4GD16tVLhYWFOnjwoOrq6tzmo6KiVFtbqwMHDqioqEi9e/dWSEiIa75Pnz4qLCw87do/ngcAAGiJw58H79at22nHKysrNWjQIE2ePFkPP/ywdu/erYyMDAUGBuq2225TVVWVnE6n2z6hoaGqrq7WyZMnJUlhYWGuuaZtq6qqTruv0%2BlUdXW1a5ufWttTpaWlKisrcxtzOMLUvXt3j9fwRFCQ36/wtorDYZ96m3prtx7bAb31LfrrO/TWd9pjb/0asH7KkCFDNGTIENfriy%2B%2BWFOmTNGmTZt02223yel0qra21m2f2tpahYeHu4JVTU2NwsPDXf%2BWpI4dOyosLMz1usk/b/uv1vbUunXrtGLFCrexjIwMZWZmerxGexQZ6XkP24rOnZ0tbwSv0Fvfor%2B%2BQ299pz31tk0GrDfffFNHjx7V9ddf7xo7deqUQkNDJUnR0dEqKirS8OHDJf1w4/qBAwcUExOj3r17Kzg4WMXFxbrkkkskSXv37nVdRjx27JgOHDig%2Bvp6ORw/vP3i4mJFR0dLkmJiYvTFF1%2B41VNcXPyT94OdTlpamkaMGOE25nCEqaKi6if28I7dkr7p9%2B9LQUGB6tzZqRMnatTQ0OjvctoVeutb9Nd36K3v%2BLK3/vrhvk0GLMuytGjRIv37v/%2B7LrvsMn388cdavXq15s6dK0m69tpr9dhjj2nYsGHq3bu3HnnkEXXt2lUJCQkKDg7WmDFjlJ2drUcffVSSlJ2drfHjxys0NFSJiYmKjIzUsmXLNH36dO3fv19r1qxx3Wg/YcIEPffcc9q0aZOuuuoqbd26Vfn5%2BZo3b57H9Xfv3r3Z5cCyskrV1/%2ByvyHt%2BP4bGhptWbcd0Fvfor%2B%2BQ299pz31tk0GrKSkJM2dO1fz58/XkSNH1LVrV02bNk1XX321JCk1NVWVlZXKyMhQeXm5BgwYoCeeeELBwcGSfniG1pIlS5ScnKy6ujqNHDlS9913nyTJ4XDo2WefVVZWloYMGaKwsDBNnjxZKSkpkn64If7Pf/6zsrOzNW/ePJ133nl67LHH1Lt3b/80AwAA2E6A1fTwKPhUWVml8TUdjkAlZe8wvq6vbJ4%2BpOWN2giHI1CRkeGqqKhqNz9NtRX01rfor%2B/QW9/xZW%2B7detkdD1P2esmHgAAABsgYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDvApYDQ0NpusAAABoN7wKWMOGDdMf//hHFRcXm64HAADA9rwKWHfddZc%2B%2BugjjR8/XpMmTdLatWtVWWn%2BSeUAAAB25FXAuuGGG7R27Vpt2bJFl19%2BuZ566ikNHTpUM2fO1HvvvWe6RgAAAFv5WTe59%2BrVSzNmzNCWLVuUkZGht956S7feeqtGjBih5557jnu1AADAL5Lj5%2Bz8ySef6KWXXtKmTZt06tQpJSUlKSUlRUeOHNGjjz6qzz77TA8//LCpWgEAAGzBq4D1%2BOOP6%2BWXX9bBgwc1YMAAzZgxQ%2BPHj1fHjh1d2wQFBen%2B%2B%2B83VigAAIBdeBWwXnjhBU2YMEGpqanq06fPabeJiorSrFmzflZxAAAAduRVwNq%2BfbtOnjyp48ePu8Y2bdqkwYMHKzIyUpLUr18/9evXz0yVAAAANuLVTe5ffvmlRo8erXXr1rnGli5dquTkZH311VfGigMAALAjrwLWH//4R1111VWaMWOGa%2BzNN9/UsGHDtHjxYmPFAQAA2JFXAeuLL77Q7bffrpCQENdYUFCQbr/9dn388cfGigMAALAjrwJWx44ddejQoWbj3377rUJDQ392UQAAAHbmVcAaPXq05s%2Bfr/fee08nT55UVVWVPvjgA2VlZSkpKcl0jQAAALbi1W8Rzpw5U4cPH9Ytt9yigIAA13hSUpLmzJljrDgAAAA78ipgOZ1OPfHEE9q/f7/27Nmj4OBgRUVFqVevXobLAwAAsJ%2Bf9adyevfurd69e5uqBQAAoF3wKmDt379fWVlZ2rlzp%2Brq6prN7969%2B2cXBgAAYFdeBaz58%2BerpKREs2bNUqdOnUzXBAAAYGteBaxdu3bp%2BeefV1xcnOl6AAAAbM%2BrxzRERkYqPDzcdC0AAADtglcBa/LkyXr44YdVWVlpuh4AAADb8%2BoS4bZt2/Txxx8rMTFRXbp0cfuTOZL01ltvGSkOAADAjrwKWImJiUpMTDRdCwAAQLvgVcC66667TNcBAADQbnh1D5YkFRYWau7cubr%2B%2But15MgR5eTkKC8vz2RtAAAAtuRVwPr88881adIkff311/r888916tQp7d69W7fccovefvtt0zUCAADYilcBKzs7W7fccovWrFmj4OBgSdKDDz6o3/72t1qxYoXRAgEAAOzG6zNYEydObDZ%2Bww03aN%2B%2BfT%2B7KAAAADvzKmAFBwfr5MmTzcZLSkrkdDp/dlEAAAB25lXAGjVqlJYtW6aKigrX2N69e7Vw4UJdeeWVpmoDAACwJa8C1j333KPa2lpdfvnlqqmpUUpKisaPHy%2BHw6E5c%2BaYrhEAAMBWvHoOVseOHbV27Vq9//77%2BvLLL9XY2KiYmBhdccUVCgz0%2BskPAAAA7YJXAavJ4MGDNXjwYFO1AAAAtAteBawRI0YoICDgJ%2Bf5W4QAAOCXzKuAdc0117gFrLq6Oh08eFDbt2/X9OnTjRUHAABgR14FrGnTpp12/IUXXtDOnTv129/%2B9mcVBQAAYGdG70gfPny4tm3bZnJJAAAA2zEasPLz89WhQweTSwIAANiOV5cIf3wJ0LIsnTx5Unv27OHyIAAA%2BMXzKmCde%2B65zX6LMDg4WFOmTFFycrKRwgAAAOzKq4C1ePFi03UAAAC0G14FrIKCAo%2B3HThwoDeHAAAAsC2vAtbNN98sy7JcX02aLhs2jQUEBGj37t0GygQAALAPrwLWY489pkWLFumee%2B7RZZddpuDgYH3yySeaP3%2B%2BbrzxRg0fPtx0nQAAALbh1WMalixZogceeECjRo1Sx44d1aFDBw0aNEhZWVl69tlndd5557m%2BAAAAfmm8ClilpaU655xzmo137NhRFRUVP7soAAAAO/MqYMXGxurhhx/WyZMnXWPHjx/X0qVLNXjwYGPFAQAA2JFX92Dde%2B%2B9mjJlioYNG6ZevXpJkvbv369u3bpp9erVJusDAACwHa8CVlRUlDZt2qSNGzdq7969kqQbb7xR48aNk9PpNFogAACA3XgVsCSpc%2BfOmjRpkr7%2B%2Bmudf/75kn54mjsAAMAvnVf3YFmWpezsbA0cOFDjx4/Xt99%2Bq3vuuUdz585VXV2d6RoBAABsxauAtWbNGr388st64IEHFBISIkkaNWqU/vd//1ePPvpoq9YqLy9XUlKS8vLyXGOffPKJJk2apLi4OI0YMULr16932yc3N1dJSUmKjY1VSkqKdu3a5ZpraGjQkiVLdPnllysuLk533nmnSktLXfPHjh1Tenq6EhISlJiYqIULF6q%2Bvt7jYwMAALTEq4C1bt063X///UpJSXE9vX3s2LFauHChXnvtNY/X2blzp9LS0nTo0CHX2Hfffafbb79dEydOVEFBgRYuXKhFixbp008/lSTl5eVpwYIFWrx4sQoKCjRhwgTdeeedqqmpkSStXLlS7777rv7%2B979rx44dCg0N1b333utaf/r06QoLC9OOHTu0YcMGvf/%2B%2B1q1apVHxwYAAPCEVwHr66%2B/1n/8x380G7/wwgt19OhRj9bIzc3VrFmzNGPGDLfxrVu3KiIiQjfddJMcDocGDx6s5ORk5eTkSJLWr1%2BvcePGKT4%2BXsHBwbr55psVGRmpTZs2ueanTp2qc845Rx07dtS8efO0fft2HT58WAcPHlR%2Bfr5mz54tp9Op888/X%2Bnp6a61Wzo2AACAJ7wKWOedd95pz%2Bps27bNdcN7S4YOHao33nhDY8eOdRsvKipSTEyM21ifPn1UWFgoSSouLv7J%2BcrKSn377bdu8127dtVZZ52lPXv2qKioSBEREerRo4drPioqSiUlJTpx4kSLxwYAAPCEV79FeOutt%2BoPf/iDjhw5Isuy9P7772vt2rVas2aN5s6d69Ea3bp1O%2B14VVVVs0c9hIaGqrq6usX5qqoqSVJYWFiz%2Baa5H%2B/b9Lpp/391bE%2BVlpaqrKzMbczhCFP37t1btU5LgoK8ysd%2B43DYp96m3tqtx3ZAb32L/voOvfWd9thbrwLWtddeq/r6eq1cuVK1tbW6//771aVLF82YMUM33HDDzyrI6XSqsrLSbay2tlbh4eGu%2Bdra2mbzkZGRrnDUdD/Wj/e3LKvZXNPr8PDwFo/tqXXr1mnFihVuYxkZGcrMzGzVOu1NZGTr%2BtgWdO7Mc918hd76Fv31HXrrO%2B2pt14FrFdeeUX/%2BZ//qbS0NJWXl8uyLHXp0sVIQTExMXr33XfdxoqLixUdHS1Jio6OVlFRUbP5YcOG6ayzzlKPHj3cLiOWlZXp%2BPHjiomJUWNjo44fP66jR4%2Bqa9eukqS9e/eqZ8%2Be6tSpU4vH9lRaWppGjBjhNuZwhKmioqpV67TEbknf9Pv3paCgQHXu7NSJEzVqaGj0dzntCr31LfrrO/TWd3zZW3/9cO9VwHrwwQfVv39/nXXWWTr77LONFpSUlKSlS5dq1apVuummm7Rz505t3LhRjz/%2BuCQpNTVVGRkZGjNmjOLj45WTk6Njx44pKSlJkpSSkqKVK1dqwIABioyM1EMPPaRBgwbpggsukCTFx8froYceUlZWlioqKvT4448rNTXVo2N7qnv37s0uB5aVVaq%2B/pf9DWnH99/Q0GjLuu2A3voW/fUdeus77am3XgWsXr16ac%2BePYqKijJdjyIjI/Xss89q4cKFWr58uc4%2B%2B2zde%2B%2B9uuyyyyRJgwcP1gMPPKD58%2BfryJEj6tOnj5566ilFRERI%2BuFSXH19vW666SZVVVUpMTFRf/rTn1zrL1%2B%2BXFlZWRo5cqQCAwM1ceJEpaene3RsAAAATwRYlmW1dqd58%2BYpNzdXffv2Va9evdShQwe3%2BUWLFhkrsL0oK6tseaNWcjgClZS9w/i6vrJ5%2BhB/l%2BAxhyNQkZHhqqioajc/TbUV9Na36K/v0Fvf8WVvu3XrZHQ9T3l1BuvQoUOKj4%2BXpGa/LQcAAPBL53HAWrRoke6%2B%2B26FhYVpzZo1vqwJAADA1jz%2BNbTVq1c3e8TBrbfe6vZ3/gAAANCKgHW6W7U%2B%2Bugjff/990YLAgAAsDt7PUgJAADABghYAAAAhrUqYAUEBPiqDgAAgHajVY9pePDBB92eeVVXV6elS5c2%2B1t9PAcLAAD8knkcsAYOHNjsmVdxcXGqqKhQRUWF8cIAAADsyuOAxbOvAAAAPMNN7gAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIa12YC1adMm9evXT3Fxca6v2bNnS5K2bdum5ORkxcbGasyYMXr77bfd9n3qqac0bNgwxcbGavLkydq3b59rrrq6WnPnzlViYqLi4%2BM1Z84cVVVVueb379%2BvKVOmKC4uTkOHDtVf/vKXM/OGAQBAu9FmA9Znn32mq6%2B%2BWrt27XJ9LV26VAcOHNC0adN0991368MPP9S0adM0ffp0HTlyRJKUm5urNWvW6JlnnlFeXp769%2B%2BvzMxMWZYlSVqwYIG%2B%2BeYbvf7669q6dau%2B%2BeYbZWdnS5Lq6up0xx13aMCAAcrLy9OTTz6pnJwcbd682W99AAAA9tOmA9ZFF13UbDw3N1cJCQkaNWqUHA6Hxo4dq4EDB2rdunWSpL/97W%2B68cYbFR0drQ4dOmjmzJkqKSlRXl6eampqtHHjRmVmZioiIkJdunTRrFmz9OKLL6qmpkYFBQUqLS1VZmamQkJC1K9fP02ePFk5OTln%2Bu0DAAAbc/i7gNNpbGzUF198IafTqaeffloNDQ369a9/rVmzZqm4uFgxMTFu2/fp00eFhYWSpOLiYk2dOtU1FxwcrF69eqmwsFARERGqq6tz2z8qKkq1tbU6cOCAioqK1Lt3b4WEhLit/eSTT7aq/tLSUpWVlbmNORxh6t69e6vWaUlQUJvNx6flcNin3qbe2q3HdkBvfYv%2B%2Bg699Z322Ns2GbDKy8vVr18/jR49WsuXL1dFRYXuuecezZ49W6dOnZLT6XTbPjQ0VNXV1ZKkqqqqn5w/efKkJCksLMw117RtVVXVafd1Op2utT21bt06rVixwm0sIyNDmZmZrVqnvYmMDPd3Ca3WubOz5Y3gFXrrW/TXd%2Bit77Sn3rbJgNW1a1e3y3JOp1OzZ8/Wddddp8TERNXW1rptX1tbq/DwcNe2PzXfFKxqampc29fU1EiSOnbsqLCwMNfrJv%2B8rafS0tI0YsQItzGHI0wVFVU/sYd37Jb0Tb9/XwoKClTnzk6dOFGjhoZGf5fTrtBb36K/vkNvfceXvfXXD/dtMmAVFhbq1Vdf1cyZMxUQECBJOnXqlAIDA3XxxRdr9%2B7dbtsXFxe77teKjo5WUVGRhg8fLumHG9cPHDigmJgY9e7dW8HBwSouLtYll1wiSdq7d6/rMuKxY8d04MAB1dfXy%2BFwuNaOjo5uVf3du3dvdjmwrKxS9fW/7G9IO77/hoZGW9ZtB/TWt%2Biv79Bb32lPvW2Tp0AiIiKUk5Ojp59%2BWvX19SopKdHSpUt1zTXXaOLEicrPz9emTZtUX1%2BvTZs2KT8/X1dffbUk6dprr9ULL7ygwsJCff/991q2bJm6du2qhIQEOZ1OjRkzRtnZ2SovL1d5ebmys7M1fvx4hYaGKjExUZGRkVq2bJm%2B//57FRYWas2aNUpNTfVzRwAAgJ20yTNYPXv21BNPPKGHH35YK1euVIcOHTRu3DjNnj1bHTp00J///GfZp3dbAAAMg0lEQVRlZ2dr3rx5Ou%2B88/TYY4%2Bpd%2B/ekqTU1FRVVlYqIyND5eXlGjBggJ544gkFBwdLkh544AEtWbJEycnJqqur08iRI3XfffdJkhwOh5599lllZWVpyJAhCgsL0%2BTJk5WSkuK3XgAAAPsJsJoeEAWfKiurNL6mwxGopOwdxtf1lc3Th/i7BI85HIGKjAxXRUVVuzld3VbQW9%2Biv75Db33Hl73t1q2T0fU81SYvEQIAANgZAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGObwdwEAAMA3xvzpXX%2BX4LEPF/6nv0swijNYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2CdxrFjx5Senq6EhAQlJiZq4cKFqq%2Bv93dZAADAJghYpzF9%2BnSFhYVpx44d2rBhg95//32tWrXK32UBAACbIGD9yMGDB5Wfn6/Zs2fL6XTq/PPPV3p6unJycvxdGgAAsAkC1o8UFRUpIiJCPXr0cI1FRUWppKREJ06c8GNlAADALhz%2BLqCtqaqqktPpdBtrel1dXa3OnTu3uEZpaanKysrcxhyOMHXv3t1coZKCguyVjx0O%2B9Tb1Fu79dgO6K1v0V/fobe%2B1556S8D6kbCwMNXU1LiNNb0ODw/3aI1169ZpxYoVbmN33XWXpk2bZqbI/6%2B0tFRTehYpLS3NeHj7pSstLdXzzz9Nb32A3voW/fUdO/b2w4X/6e8SPFJaWqrHHnvMVr1tSfuJioZER0fr%2BPHjOnr0qGts79696tmzpzp16uTRGmlpaXrxxRfdvtLS0ozXWlZWphUrVjQ7W4afj976Dr31LfrrO/TWd9pjbzmD9SO9evVSfHy8HnroIWVlZamiokKPP/64UlNTPV6je/fu7SaBAwCA1uMM1mksX75c9fX1GjlypK677jpdccUVSk9P93dZAADAJjiDdRpdu3bV8uXL/V0GAACwqaD58%2BfP93cR8F54eLgGDRrk8Q348By99R1661v013fore%2B0t94GWJZl%2BbsIAACA9oR7sAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbDauGPHjik9PV0JCQlKTEzUwoULVV9ff9ptt23bpuTkZMXGxmrMmDF6%2B%2B23z3C19tKa3v71r3/V6NGjFRcXp9GjRysnJ%2BcMV2svreltk6%2B%2B%2BkqXXHKJ8vLyzlCV9tWa/ubn52vSpEmKi4vTr3/9az3xxBNnuFp7aU1vn3/%2BeY0YMUKXXnqpkpOT9frrr5/hau2pvLxcSUlJ//J7vV18nllo037zm99YM2fOtKqrq61Dhw5Z48aNs5566qlm2%2B3fv98aMGCA9cYbb1h1dXXWa6%2B9Zl188cXWt99%2B64eq7cHT3r7xxhtWQkKCtWvXLquxsdH66KOPrISEBGvLli1%2BqNoePO1tk%2Brqamv8%2BPFWTEyM9cEHH5zBSu3J0/4WFxdbl1xyifXiiy9ajY2N1u7du61BgwZZmzdv9kPV9uBpb9955x1r8ODB1t69ey3LsqwtW7ZYffv2tQ4fPnymS7aVDz/80Bo1atS//F5vL59nnMFqww4ePKj8/HzNnj1bTqdT559/vtLT00979iQ3N1cJCQkaNWqUHA6Hxo4dq4EDB2rdunV%2BqLzta01vjxw5oqlTpyo2NlYBAQGKi4tTYmKiCgoK/FB529ea3jb5wx/%2BoFGjRp3BKu2rNf39n//5H40cOVLXXHONAgIC1LdvX61du1bx8fF%2BqLzta01v9%2B3bJ8uyXF9BQUEKDg6Ww%2BHwQ%2BX2kJubq1mzZmnGjBktbtcePs8IWG1YUVGRIiIi1KNHD9dYVFSUSkpKdOLECbdti4uLFRMT4zbWp08fFRYWnpFa7aY1vb3pppt0%2B%2B23u14fO3ZMBQUFuuiii85YvXbSmt5K0ksvvaSDBw/qrrvuOpNl2lZr%2Bvvpp5/q3/7t3/S73/1OiYmJGjNmjPLz89WtW7czXbYttKa348aNU9euXTV27Fj1799fd999txYvXqyePXue6bJtY%2BjQoXrjjTc0duzYf7lde/k8I2C1YVVVVXI6nW5jTa%2Brq6tb3DY0NLTZdvhBa3r7z8rKyjR16lRddNFFGj9%2BvE9rtKvW9Hbv3r165JFHtGzZMgUFBZ2xGu2sNf397rvvtHr1ak2YMEHvvvuusrKytGTJEm3ZsuWM1WsnreltXV2d%2Bvbtq/Xr1%2Bvjjz9WVlaW5s2bpz179pyxeu2mW7duHp3hay%2BfZwSsNiwsLEw1NTVuY02vw8PD3cadTqdqa2vdxmpra5tthx%2B0prdNPv74Y6Wmpqp3795auXIllwJ%2Bgqe9/f777zVjxgz9/ve/17nnnntGa7Sz1vzfDQkJ0ciRI3XllVfK4XBo4MCBuvrqq7V58%2BYzVq%2BdtKa3CxYsUHR0tC6%2B%2BGKFhITo2muvVWxsrHJzc89Yve1Ve/k8I2C1YdHR0Tp%2B/LiOHj3qGtu7d6969uypTp06uW0bExOjoqIit7Hi4mJFR0efkVrtpjW9laQNGzbo5ptv1pQpU7Rs2TKFhIScyXJtxdPefvbZZzpw4IDmzZunhIQEJSQkSJLuuOMOzZ8//0yXbRut%2Bb8bFRWlU6dOuY01NDTIsqwzUqvdtKa3JSUlzXrrcDgUHBx8Rmptz9rN55l/77FHS2644QZrxowZVmVlpes3WpYvX95su%2BLiYmvAgAHWa6%2B95vqtiwEDBlj79u3zQ9X24Glvt2zZYvXv39/avn27H6q0J097%2B2P8FqFnPO3ve%2B%2B9Z/Xr18966aWXrMbGRis/P9%2BKjY213nzzTT9UbQ%2Be9vaRRx6xEhMTrc8//9xqaGiwNm/ebA0YMMD68ssv/VC1/fyr7/X28nlGwGrjysrKrGnTplmDBg2yLrvsMmvx4sVWfX29ZVmWFRsba7388suubbdv325NmDDBio2NtcaNG2e98847/irbFjzt7fjx462%2BfftasbGxbl/33XefP8tv01rz//afEbA805r%2BvvPOO1ZKSooVFxdnjRw50vrrX//qr7JtwdPe1tXVWcuXL7eGDx9uXXrppdY111zDD2Gt8OPv9fb4eRZgWZwrBgAAMIl7sAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAANBmlJeXKykpSXl5eR5t39jYqEceeUTDhg1TfHy8rrvuOuXn5/u4ypYRsAAAQJuwc%2BdOpaWl6dChQx7vs3btWr355ptav369CgoKNHbsWP33f/%2B3vv/%2Bex9W2jICFgAA8Lvc3FzNmjVLM2bMaDb33nvvKTU1VQkJCRo3bpxeeeUV19y%2BffvU2NioxsZGWZalgIAAhYaGnsnST8vh7wIAAACGDh2q5ORkORwOt5BVWFioO%2B%2B8U0uXLtXIkSP1ySefKD09XZGRkbriiit0/fXX66233tKVV16poKAgdejQQU8%2B%2BaQ6dOjgx3fDGSwAANAGdOvWTQ5H8/M%2Ba9eu1ciRI3XVVVcpKChIl156qa677jrl5ORIkurq6jRo0CBt3rxZH330kW677TZlZmaqrKzsTL8FN5zBAgAAbdb//d//6YMPPlBCQoJrrKGhQRdccIEkac6cObrjjjv0q1/9SpKUkZGhl19%2BWVu2bNHkyZP9UrNEwAIAAG1Yz549dc011ygrK8s1VlpaKsuyJEklJSU6deqU2z4Oh0PBwcFntM4f4xIhAABos1JTU/Xqq6/qH//4hxobG3XgwAH95je/0bPPPitJGjFihFauXKnDhw%2Brrq5Ozz//vMrKyjR8%2BHC/1h1gNUVAAACANuDCCy/U6tWrlZiYKEl65513tHz5ch08eFBOp1Pjx4/X7373O4WEhKiqqkqPPPKItm7dqpqaGl144YWaM2eOLr74Yr%2B%2Bh/8HiIxT4/OG3YYAAAAASUVORK5CYII%3D"/>
        </div>
        <div role="tabpanel" class="tab-pane col-md-12" id="common-7712628620957852604">

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">99999999</td>
        <td class="number">35210</td>
        <td class="number">13.7%</td>
        <td>
            <div class="bar" style="width:16%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">9820</td>
        <td class="number">59</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">9793</td>
        <td class="number">58</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">10132</td>
        <td class="number">56</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">10025</td>
        <td class="number">54</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">9781</td>
        <td class="number">53</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">9941</td>
        <td class="number">53</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">10192</td>
        <td class="number">52</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">5920</td>
        <td class="number">51</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">10096</td>
        <td class="number">51</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="other">
        <td class="fillremaining">Other values (27337)</td>
        <td class="number">221287</td>
        <td class="number">86.1%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr>
</table>
        </div>
        <div role="tabpanel" class="tab-pane col-md-12"  id="extreme-7712628620957852604">
            <p class="h4">Minimum 5 values</p>

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">505</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">511</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">701</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">768</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">809</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr>
</table>
            <p class="h4">Maximum 5 values</p>

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">35875</td>
        <td class="number">6</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">37540</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">39304</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">41000</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">99999999</td>
        <td class="number">35210</td>
        <td class="number">13.7%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr>
</table>
        </div>
    </div>
</div>
</div><div class="row variablerow">
    <div class="col-md-3 namecol">
        <p class="h4 pp-anchor" id="pp_var_Customer ID">Customer ID<br/>
            <small>Categorical</small>
        </p>
    </div><div class="col-md-3">
    <table class="stats ">
        <tr class="alert">
            <th>Distinct count</th>
            <td>215700</td>
        </tr>
        <tr>
            <th>Unique (%)</th>
            <td>83.9%</td>
        </tr>
        <tr class="ignore">
            <th>Missing (%)</th>
            <td>0.0%</td>
        </tr>
        <tr class="ignore">
            <th>Missing (n)</th>
            <td>0</td>
        </tr>
    </table>
</div>
<div class="col-md-6 collapse in" id="minifreqtable6170738858310294870">
    <table class="mini freq">
        <tr class="">
    <th>2f29101f-560c-447a-bb1b-775f07c4445a</th>
    <td>
        <div class="bar" style="width:1%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 0.0%">
            &nbsp;
        </div>
        4
    </td>
</tr><tr class="">
    <th>a4b836f4-f0b9-430f-94a8-3848d5b43e6c</th>
    <td>
        <div class="bar" style="width:1%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 0.0%">
            &nbsp;
        </div>
        4
    </td>
</tr><tr class="">
    <th>7678662d-9873-40aa-a29a-44a938cd1ef5</th>
    <td>
        <div class="bar" style="width:1%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 0.0%">
            &nbsp;
        </div>
        4
    </td>
</tr><tr class="other">
    <th>Other values (215697)</th>
    <td>
        <div class="bar" style="width:100%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 100.0%">
            256972
        </div>

    </td>
</tr>
    </table>
</div>
<div class="col-md-12 text-right">
    <a role="button" data-toggle="collapse" data-target="#freqtable6170738858310294870, #minifreqtable6170738858310294870"
       aria-expanded="true" aria-controls="collapseExample">
        Toggle details
    </a>
</div>
<div class="col-md-12 extrapadding collapse" id="freqtable6170738858310294870">

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">2f29101f-560c-447a-bb1b-775f07c4445a</td>
        <td class="number">4</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">a4b836f4-f0b9-430f-94a8-3848d5b43e6c</td>
        <td class="number">4</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">7678662d-9873-40aa-a29a-44a938cd1ef5</td>
        <td class="number">4</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">6c307644-6302-49e1-9ddf-1057cf1047c3</td>
        <td class="number">4</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">950d54de-b2db-4748-ba6f-825f8155e9d7</td>
        <td class="number">4</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">69b339ac-6b56-4cbe-beec-0b10225af4cc</td>
        <td class="number">4</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">66fe7193-ef63-4402-a88c-3c35223f97b8</td>
        <td class="number">4</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">4319c138-7d16-4a81-af03-7368ffa4e341</td>
        <td class="number">4</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">3500a951-2746-4393-bbd8-725d4a4db930</td>
        <td class="number">4</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">4adba860-305b-4abb-86e5-dd6019cd6608</td>
        <td class="number">4</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="other">
        <td class="fillremaining">Other values (215690)</td>
        <td class="number">256944</td>
        <td class="number">100.0%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr>
</table>
</div>
</div><div class="row variablerow">
    <div class="col-md-3 namecol">
        <p class="h4 pp-anchor" id="pp_var_Home Ownership">Home Ownership<br/>
            <small>Categorical</small>
        </p>
    </div><div class="col-md-3">
    <table class="stats ">
        <tr class="">
            <th>Distinct count</th>
            <td>4</td>
        </tr>
        <tr>
            <th>Unique (%)</th>
            <td>0.0%</td>
        </tr>
        <tr class="ignore">
            <th>Missing (%)</th>
            <td>0.0%</td>
        </tr>
        <tr class="ignore">
            <th>Missing (n)</th>
            <td>0</td>
        </tr>
    </table>
</div>
<div class="col-md-6 collapse in" id="minifreqtable2522873527638604276">
    <table class="mini freq">
        <tr class="">
    <th>Home Mortgage</th>
    <td>
        <div class="bar" style="width:100%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 48.4%">
            124477
        </div>

    </td>
</tr><tr class="">
    <th>Rent</th>
    <td>
        <div class="bar" style="width:87%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 42.4%">
            109010
        </div>

    </td>
</tr><tr class="">
    <th>Own Home</th>
    <td>
        <div class="bar" style="width:19%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 8.9%">
            &nbsp;
        </div>
        22923
    </td>
</tr>
    </table>
</div>
<div class="col-md-12 text-right">
    <a role="button" data-toggle="collapse" data-target="#freqtable2522873527638604276, #minifreqtable2522873527638604276"
       aria-expanded="true" aria-controls="collapseExample">
        Toggle details
    </a>
</div>
<div class="col-md-12 extrapadding collapse" id="freqtable2522873527638604276">

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">Home Mortgage</td>
        <td class="number">124477</td>
        <td class="number">48.4%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">Rent</td>
        <td class="number">109010</td>
        <td class="number">42.4%</td>
        <td>
            <div class="bar" style="width:87%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">Own Home</td>
        <td class="number">22923</td>
        <td class="number">8.9%</td>
        <td>
            <div class="bar" style="width:19%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">HaveMortgage</td>
        <td class="number">574</td>
        <td class="number">0.2%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr>
</table>
</div>
</div><div class="row variablerow">
    <div class="col-md-3 namecol">
        <p class="h4 pp-anchor" id="pp_var_Loan ID">Loan ID<br/>
            <small>Categorical</small>
        </p>
    </div><div class="col-md-3">
    <table class="stats ">
        <tr class="alert">
            <th>Distinct count</th>
            <td>215700</td>
        </tr>
        <tr>
            <th>Unique (%)</th>
            <td>83.9%</td>
        </tr>
        <tr class="ignore">
            <th>Missing (%)</th>
            <td>0.0%</td>
        </tr>
        <tr class="ignore">
            <th>Missing (n)</th>
            <td>0</td>
        </tr>
    </table>
</div>
<div class="col-md-6 collapse in" id="minifreqtable244131924423349682">
    <table class="mini freq">
        <tr class="">
    <th>92f33016-7a19-4105-82ea-c69827dda19e</th>
    <td>
        <div class="bar" style="width:1%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 0.0%">
            &nbsp;
        </div>
        4
    </td>
</tr><tr class="">
    <th>8c341027-8760-4d22-8014-0969136fb6af</th>
    <td>
        <div class="bar" style="width:1%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 0.0%">
            &nbsp;
        </div>
        4
    </td>
</tr><tr class="">
    <th>91343210-b13d-405c-b1a9-20429278208d</th>
    <td>
        <div class="bar" style="width:1%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 0.0%">
            &nbsp;
        </div>
        4
    </td>
</tr><tr class="other">
    <th>Other values (215697)</th>
    <td>
        <div class="bar" style="width:100%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 100.0%">
            256972
        </div>

    </td>
</tr>
    </table>
</div>
<div class="col-md-12 text-right">
    <a role="button" data-toggle="collapse" data-target="#freqtable244131924423349682, #minifreqtable244131924423349682"
       aria-expanded="true" aria-controls="collapseExample">
        Toggle details
    </a>
</div>
<div class="col-md-12 extrapadding collapse" id="freqtable244131924423349682">

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">92f33016-7a19-4105-82ea-c69827dda19e</td>
        <td class="number">4</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">8c341027-8760-4d22-8014-0969136fb6af</td>
        <td class="number">4</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">91343210-b13d-405c-b1a9-20429278208d</td>
        <td class="number">4</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">70fa839d-8d3c-4e8e-b8ea-bc4dd9b4e548</td>
        <td class="number">4</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">ab1e2d16-536a-4367-b2e7-7a04e284b84c</td>
        <td class="number">4</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">e5762c25-dc8a-4cab-811f-c978f9b7ba79</td>
        <td class="number">4</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">70788128-fbcf-497a-bb99-fac132508073</td>
        <td class="number">4</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">f7bb8ada-36d1-49e0-a5cc-38d6bf19e210</td>
        <td class="number">4</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">64e39470-9848-45ed-9589-ae84eb78b929</td>
        <td class="number">4</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">3fe25a8c-3d4c-4136-9c5f-8f0200cadb5c</td>
        <td class="number">4</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="other">
        <td class="fillremaining">Other values (215690)</td>
        <td class="number">256944</td>
        <td class="number">100.0%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr>
</table>
</div>
</div><div class="row variablerow">
    <div class="col-md-3 namecol">
        <p class="h4 pp-anchor" id="pp_var_Loan Status">Loan Status<br/>
            <small>Categorical</small>
        </p>
    </div><div class="col-md-3">
    <table class="stats ">
        <tr class="">
            <th>Distinct count</th>
            <td>2</td>
        </tr>
        <tr>
            <th>Unique (%)</th>
            <td>0.0%</td>
        </tr>
        <tr class="ignore">
            <th>Missing (%)</th>
            <td>0.0%</td>
        </tr>
        <tr class="ignore">
            <th>Missing (n)</th>
            <td>0</td>
        </tr>
    </table>
</div>
<div class="col-md-6 collapse in" id="minifreqtable8930559222366969514">
    <table class="mini freq">
        <tr class="">
    <th>Fully Paid</th>
    <td>
        <div class="bar" style="width:100%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 68.6%">
            176191
        </div>

    </td>
</tr><tr class="">
    <th>Charged Off</th>
    <td>
        <div class="bar" style="width:46%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 31.4%">
            80793
        </div>

    </td>
</tr>
    </table>
</div>
<div class="col-md-12 text-right">
    <a role="button" data-toggle="collapse" data-target="#freqtable8930559222366969514, #minifreqtable8930559222366969514"
       aria-expanded="true" aria-controls="collapseExample">
        Toggle details
    </a>
</div>
<div class="col-md-12 extrapadding collapse" id="freqtable8930559222366969514">

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">Fully Paid</td>
        <td class="number">176191</td>
        <td class="number">68.6%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">Charged Off</td>
        <td class="number">80793</td>
        <td class="number">31.4%</td>
        <td>
            <div class="bar" style="width:46%">&nbsp;</div>
        </td>
</tr>
</table>
</div>
</div><div class="row variablerow">
    <div class="col-md-3 namecol">
        <p class="h4 pp-anchor" id="pp_var_Maximum Open Credit">Maximum Open Credit<br/>
            <small>Categorical</small>
        </p>
    </div><div class="col-md-3">
    <table class="stats ">
        <tr class="alert">
            <th>Distinct count</th>
            <td>87188</td>
        </tr>
        <tr>
            <th>Unique (%)</th>
            <td>33.9%</td>
        </tr>
        <tr class="ignore">
            <th>Missing (%)</th>
            <td>0.0%</td>
        </tr>
        <tr class="ignore">
            <th>Missing (n)</th>
            <td>0</td>
        </tr>
    </table>
</div>
<div class="col-md-6 collapse in" id="minifreqtable-1041094508832102846">
    <table class="mini freq">
        <tr class="">
    <th>0</th>
    <td>
        <div class="bar" style="width:1%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 0.6%">
            &nbsp;
        </div>
        1597
    </td>
</tr><tr class="">
    <th>0</th>
    <td>
        <div class="bar" style="width:1%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 0.1%">
            &nbsp;
        </div>
        234
    </td>
</tr><tr class="">
    <th>9082</th>
    <td>
        <div class="bar" style="width:1%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 0.0%">
            &nbsp;
        </div>
        19
    </td>
</tr><tr class="other">
    <th>Other values (87185)</th>
    <td>
        <div class="bar" style="width:100%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 99.3%">
            255134
        </div>

    </td>
</tr>
    </table>
</div>
<div class="col-md-12 text-right">
    <a role="button" data-toggle="collapse" data-target="#freqtable-1041094508832102846, #minifreqtable-1041094508832102846"
       aria-expanded="true" aria-controls="collapseExample">
        Toggle details
    </a>
</div>
<div class="col-md-12 extrapadding collapse" id="freqtable-1041094508832102846">

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">0</td>
        <td class="number">1597</td>
        <td class="number">0.6%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">0</td>
        <td class="number">234</td>
        <td class="number">0.1%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">9082</td>
        <td class="number">19</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">10180</td>
        <td class="number">19</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">11345</td>
        <td class="number">19</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">15662</td>
        <td class="number">19</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">14770</td>
        <td class="number">19</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">9749</td>
        <td class="number">18</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">12195</td>
        <td class="number">18</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">14939</td>
        <td class="number">18</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="other">
        <td class="fillremaining">Other values (87178)</td>
        <td class="number">255004</td>
        <td class="number">99.2%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr>
</table>
</div>
</div><div class="row variablerow">
    <div class="col-md-3 namecol">
        <p class="h4 pp-anchor" id="pp_var_Monthly Debt">Monthly Debt<br/>
            <small>Categorical</small>
        </p>
    </div><div class="col-md-3">
    <table class="stats ">
        <tr class="alert">
            <th>Distinct count</th>
            <td>129115</td>
        </tr>
        <tr>
            <th>Unique (%)</th>
            <td>50.2%</td>
        </tr>
        <tr class="ignore">
            <th>Missing (%)</th>
            <td>0.0%</td>
        </tr>
        <tr class="ignore">
            <th>Missing (n)</th>
            <td>0</td>
        </tr>
    </table>
</div>
<div class="col-md-6 collapse in" id="minifreqtable3229870892069146479">
    <table class="mini freq">
        <tr class="">
    <th>$0.00</th>
    <td>
        <div class="bar" style="width:1%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 0.1%">
            &nbsp;
        </div>
        254
    </td>
</tr><tr class="">
    <th>$636.87</th>
    <td>
        <div class="bar" style="width:1%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 0.0%">
            &nbsp;
        </div>
        12
    </td>
</tr><tr class="">
    <th>$775.08</th>
    <td>
        <div class="bar" style="width:1%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 0.0%">
            &nbsp;
        </div>
        12
    </td>
</tr><tr class="other">
    <th>Other values (129112)</th>
    <td>
        <div class="bar" style="width:100%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 99.9%">
            256706
        </div>

    </td>
</tr>
    </table>
</div>
<div class="col-md-12 text-right">
    <a role="button" data-toggle="collapse" data-target="#freqtable3229870892069146479, #minifreqtable3229870892069146479"
       aria-expanded="true" aria-controls="collapseExample">
        Toggle details
    </a>
</div>
<div class="col-md-12 extrapadding collapse" id="freqtable3229870892069146479">

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">$0.00</td>
        <td class="number">254</td>
        <td class="number">0.1%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">$636.87</td>
        <td class="number">12</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">$775.08</td>
        <td class="number">12</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">$679.66</td>
        <td class="number">12</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">$838.10</td>
        <td class="number">12</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">$847.85</td>
        <td class="number">12</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">$837.00</td>
        <td class="number">11</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">$789.58</td>
        <td class="number">11</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">$628.45</td>
        <td class="number">11</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">$713.84</td>
        <td class="number">11</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="other">
        <td class="fillremaining">Other values (129105)</td>
        <td class="number">256626</td>
        <td class="number">99.9%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr>
</table>
</div>
</div><div class="row variablerow">
    <div class="col-md-3 namecol">
        <p class="h4 pp-anchor" id="pp_var_Months since last delinquent">Months since last delinquent<br/>
            <small>Numeric</small>
        </p>
    </div><div class="col-md-6">
    <div class="row">
        <div class="col-sm-6">
            <table class="stats ">
                <tr>
                    <th>Distinct count</th>
                    <td>132</td>
                </tr>
                <tr>
                    <th>Unique (%)</th>
                    <td>0.1%</td>
                </tr>
                <tr class="alert">
                    <th>Missing (%)</th>
                    <td>54.6%</td>
                </tr>
                <tr class="alert">
                    <th>Missing (n)</th>
                    <td>140383</td>
                </tr>
                <tr class="ignore">
                    <th>Infinite (%)</th>
                    <td>0.0%</td>
                </tr>
                <tr class="ignore">
                    <th>Infinite (n)</th>
                    <td>0</td>
                </tr>
            </table>

        </div>
        <div class="col-sm-6">
            <table class="stats ">

                <tr>
                    <th>Mean</th>
                    <td>34.881</td>
                </tr>
                <tr>
                    <th>Minimum</th>
                    <td>0</td>
                </tr>
                <tr>
                    <th>Maximum</th>
                    <td>176</td>
                </tr>
                <tr class="ignore">
                    <th>Zeros (%)</th>
                    <td>0.2%</td>
                </tr>
            </table>
        </div>
    </div>
</div>
<div class="col-md-3 collapse in" id="minihistogram-4217212580898125458">
    <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAABLCAYAAAA1fMjoAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAPYQAAD2EBqD%2BnaQAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAARxJREFUeJzt3LENwkAQAEGMKIki6ImYniiCnp4G0AoQxjbM5JYuWV1wL09jjLEDHtovPQCs2WHpAT7heL6%2B/M3tcpphEn6NDQJhdRvknW0Ac7FBIAgEgkAgCASCQCAIBIJAIAgEgkAgrO6S/i3eb/EMGwSCQCAIBIJAIAgEgkAgCASCQCAIBMLfXtLf8er13eV9%2B2wQCAKBIBAIAoEgEAgCgSAQCAKBIBAIAoEgEAjeYs3In1O2zwaBIBAIAoEgEAgCgSAQCAKBIBAIAoEgEAgCgSAQCNMYYyw9BKyVDQJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBALhDqvUFf5c8RCAAAAAAElFTkSuQmCC">

</div>
<div class="col-md-12 text-right">
    <a role="button" data-toggle="collapse" data-target="#descriptives-4217212580898125458,#minihistogram-4217212580898125458"
       aria-expanded="false" aria-controls="collapseExample">
        Toggle details
    </a>
</div>
<div class="row collapse col-md-12" id="descriptives-4217212580898125458">
    <ul class="nav nav-tabs" role="tablist">
        <li role="presentation" class="active"><a href="#quantiles-4217212580898125458"
                                                  aria-controls="quantiles-4217212580898125458" role="tab"
                                                  data-toggle="tab">Statistics</a></li>
        <li role="presentation"><a href="#histogram-4217212580898125458" aria-controls="histogram-4217212580898125458"
                                   role="tab" data-toggle="tab">Histogram</a></li>
        <li role="presentation"><a href="#common-4217212580898125458" aria-controls="common-4217212580898125458"
                                   role="tab" data-toggle="tab">Common Values</a></li>
        <li role="presentation"><a href="#extreme-4217212580898125458" aria-controls="extreme-4217212580898125458"
                                   role="tab" data-toggle="tab">Extreme Values</a></li>

    </ul>

    <div class="tab-content">
        <div role="tabpanel" class="tab-pane active row" id="quantiles-4217212580898125458">
            <div class="col-md-4 col-md-offset-1">
                <p class="h4">Quantile statistics</p>
                <table class="stats indent">
                    <tr>
                        <th>Minimum</th>
                        <td>0</td>
                    </tr>
                    <tr>
                        <th>5-th percentile</th>
                        <td>5</td>
                    </tr>
                    <tr>
                        <th>Q1</th>
                        <td>16</td>
                    </tr>
                    <tr>
                        <th>Median</th>
                        <td>32</td>
                    </tr>
                    <tr>
                        <th>Q3</th>
                        <td>51</td>
                    </tr>
                    <tr>
                        <th>95-th percentile</th>
                        <td>75</td>
                    </tr>
                    <tr>
                        <th>Maximum</th>
                        <td>176</td>
                    </tr>
                    <tr>
                        <th>Range</th>
                        <td>176</td>
                    </tr>
                    <tr>
                        <th>Interquartile range</th>
                        <td>35</td>
                    </tr>
                </table>
            </div>
            <div class="col-md-4 col-md-offset-2">
                <p class="h4">Descriptive statistics</p>
                <table class="stats indent">
                    <tr>
                        <th>Standard deviation</th>
                        <td>21.854</td>
                    </tr>
                    <tr>
                        <th>Coef of variation</th>
                        <td>0.62653</td>
                    </tr>
                    <tr>
                        <th>Kurtosis</th>
                        <td>-0.76657</td>
                    </tr>
                    <tr>
                        <th>Mean</th>
                        <td>34.881</td>
                    </tr>
                    <tr>
                        <th>MAD</th>
                        <td>18.457</td>
                    </tr>
                    <tr class="">
                        <th>Skewness</th>
                        <td>0.42704</td>
                    </tr>
                    <tr>
                        <th>Sum</th>
                        <td>4067200</td>
                    </tr>
                    <tr>
                        <th>Variance</th>
                        <td>477.6</td>
                    </tr>
                    <tr>
                        <th>Memory size</th>
                        <td>2.0 MiB</td>
                    </tr>
                </table>
            </div>
        </div>
        <div role="tabpanel" class="tab-pane col-md-8 col-md-offset-2" id="histogram-4217212580898125458">
            <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAlgAAAGQCAYAAAByNR6YAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAPYQAAD2EBqD%2BnaQAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAIABJREFUeJzt3X9cVvX9//GneKFcoAiK2I%2BvG07BzZ%2BQCirGZ2LMj/kzxFEZs6a1BZP0o%2BhYPzQd/phUZi5XpnMqt2Wabtk0ra3UOUUrMysxMH%2BwoYICyk8BOd8/%2BnB9ukIT6y0XPx73243brev9Pud93q/rXOfqyTnHQwvLsiwBAADAGDdXTwAAAKCpIWABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMNsrp5Ac5GXV2R8TDe3Fmrf3kv5%2BSWqrraMj99QUTd1NwfUTd3NQX3U3bFj25sy7vVwBqsRc3NroRYtWsjNrYWrp1KvqJu6mwPqpu7moCnXTcACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMNsrp4Amo8RS/e6ego3ZPu0cFdPAQDQSHEGCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADD%2BFuEjVz/x99y9RQAAMDXcAYLAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwLAGG7D27dunCRMm6I477lB4eLjmz5%2Bv8vJySdLhw4c1YcIEhYSEKDIyUhs3bnRad8uWLYqKilJwcLCio6N16NAhR9%2BVK1e0ePFiDR48WCEhIXr00UeVm5vr6L9w4YLi4%2BPVv39/hYWFKSUlRVVVVfVTNAAAaBIaZMDKz8/XL37xC9133316//33tWXLFh04cEAvv/yyLl68qEceeUTjxo3TwYMHlZKSooULF%2Brjjz%2BWJKWnp2v%2B/PlatGiRDh48qDFjxujRRx9VWVmZJGnFihXau3evXn/9de3Zs0ceHh564oknHNueNm2aPD09tWfPHm3atEn79u3TmjVrXPE2AACARqpBBqz27dvrX//6l6Kjo9WiRQsVFhbq8uXLat%2B%2BvXbu3CkfHx9NnDhRNptNgwYN0ujRo5WWliZJ2rhxo0aOHKl%2B/frJ3d1dDz74oHx9fbVt2zZH/8MPP6xbb71Vbdq00eOPP67du3crOztbp06d0oEDB5SUlCS73a7OnTsrPj7eMTYAAEBdNNg/9tymTRtJ0n/913/p3Llz6t%2B/v6Kjo7V06VIFBQU5LdutWzdt2rRJkpSVlaXx48fX6s/IyFBRUZHOnj3rtL6fn5/atWunY8eOSZJ8fHzUqVMnR3/Xrl2Vk5OjS5cuydvbu05zz83NVV5enlObzeYpf3//OlZfNy1bNsh83GTYbA3r/a3Z381tv1M3dTcH1N306m6wAavGzp07dfHiRc2cOVOJiYnq1KmT7Ha70zIeHh4qLS2VJJWUlFyzv6SkRJLk6elZq7%2Bm7%2Bvr1rwuLS2tc8DasGGDli9f7tSWkJCgxMTEOq2PhsHX18vVU7gqb2/79Rdqgqi7eaHu5qUp1t3gA5aHh4c8PDyUlJSkCRMmKC4uTkVFRU7LlJeXy8vry/8Z2u12x83wX%2B339fV1hKWa%2B7G%2Bvr5lWbX6al7XjF8XsbGxioyMdGqz2TxVUFBS5zHqoikm/obE9P76rlq2dJO3t12XLpXpypVqV0%2Bn3lA3dTcH1H3z6nbVL8sNMmB9%2BOGH%2Bs1vfqM33nhDrVq1kiRVVFTI3d1d3bp10969e52Wz8rKUmBgoCQpMDBQmZmZtfojIiLUrl07derUSVlZWY7LhHl5eSosLFRQUJCqq6tVWFio8%2BfPy8/PT5J0/Phx3XLLLWrbtm2d5%2B/v71/rcmBeXpGqqprPQdMUNNT9deVKdYOd281E3c0LdTcvTbHuBnkKpHv37iovL9czzzyjiooK/ec//9HixYsVExOj4cOH6/z581qzZo0qKyu1f/9%2Bbd261XHfVUxMjLZu3ar9%2B/ersrJSa9as0YULFxQVFSVJio6O1ooVK5Sdna3i4mItWLBAoaGh%2Bt73vqeAgAD169dPCxYsUHFxsbKzs/Xiiy8qJibGlW8HAABoZBrkGSwvLy%2B98sorWrBggcLDw9W2bVuNHj1aCQkJatWqlVavXq2UlBQtW7ZM7du31xNPPKGBAwdKkgYNGqQ5c%2BZo7ty5OnfunLp166aVK1fKx8dH0pf3QlVVVWnixIkqKSlRWFiYli5d6tj2smXLNG/ePA0bNkxubm4aN26c4uPjXfI%2BAACAxqmFZVmWqyfRHOTlFV1/oRtks7kpKnWP8XHxpe3Twl09BSc2m5t8fb1UUFDS5E6lfxPqpu7mgLpvXt0dO9b9Fh%2BTGuQlQgAAgMaMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQ02YGVkZOihhx5SaGiowsPDNWvWLOXn50uS5syZo169eikkJMTxs2HDBse6K1euVEREhIKDgxUXF6cvvvjC0VdaWqrk5GSFhYWpX79%2BmjVrlkpKShz9J06c0KRJkxQSEqIhQ4boD3/4Q/0VDQAAmoQGGbDKy8s1ZcoUhYSE6J///KfefPNNFRYW6je/%2BY0k6ciRI5o/f74OHTrk%2BImNjZUkbdmyRevWrdOqVauUnp6unj17KjExUZZlSZLmz5%2BvM2fOaMeOHdq5c6fOnDmj1NRUSVJlZaV%2B%2Bctfqnfv3kpPT9fLL7%2BstLQ0bd%2B%2B3TVvBAAAaJQaZMDKycnRD3/4QyUkJKhVq1by9fVVbGysDh48qIqKCn3%2B%2Befq1avXVdd97bXXdP/99yswMFCtW7fWjBkzlJOTo/T0dJWVlWnr1q1KTEyUj4%2BPOnTooJkzZ2rz5s0qKyvTwYMHlZubq8TERLVq1Uo9evRQXFyc0tLS6vkdAAAAjVmDDFg/%2BMEP9Morr6hly5aOth07dqhnz57KyMhQVVWVli1bpsGDB2v48OF6%2BeWXVV1dLUnKyspSUFCQYz13d3cFBAQoIyNDp06dUmVlpVN/165dVV5erpMnTyozM1NdunRRq1atHP3dunVTRkZGPVQNAACaCpurJ3A9lmVp6dKlevfdd7V%2B/XqdP39eoaGhiouL07PPPqujR48qISFBbm5umjJlikpKSmS3253G8PDwUGlpqYqLiyVJnp6ejr6aZUtKSq66rt1uV2lp6Q3NOTc3V3l5eU5tNpun/P39b2ic62nZskHm4ybDZmtY72/N/m5u%2B526qbs5oO6mV3eDDljFxcVKTk7Wp59%2BqvXr16t79%2B7q3r27wsPDHcv06dNHkyZN0rZt2zRlyhTZ7XaVl5c7jVNeXi4vLy9HsCorK5OXl5fjvyWpTZs28vT0dLyu8dVl62rDhg1avny5U1tCQoISExNvaBy4lq/vje33%2BuLtbb/%2BQk0QdTcv1N28NMW6G2zAOn36tB5%2B%2BGHddttt2rRpk9q3by9Jeuedd3T%2B/Hnde%2B%2B9jmUrKirk4eEhSQoMDFRmZqaGDh0q6csb10%2BePKmgoCB16dJF7u7uysrKUt%2B%2BfSVJx48fd1xGvHDhgk6ePKmqqirZbF%2B%2BNVlZWQoMDLyhucfGxioyMtKpzWbzVEFByTXW%2BHaaYuJvSPo//parp3BD3p55p6uncFO0bOkmb2%2B7Ll0q05Ur1a6eTr2hbupuDuqjblf9stwgA9bFixc1adIkDRw4UCkpKXJz%2B78gYVmWFi5cqO9///saOHCgPvroI61du1bJycmSpPHjx%2BuFF15QRESEunTpoueee05%2Bfn7q37%2B/3N3dNWLECKWmpur555%2BXJKWmpmrUqFHy8PBQWFiYfH199cwzz2jatGk6ceKE1q1bp%2BnTp9/Q/P39/WtdDszLK1JVVfM5aFD/mvrn68qV6iZf49VQd/NC3U1HgwxYmzdvVk5OjrZv36633nI%2Bi3Do0CElJydr7ty5OnfunPz8/DR16lSNHTtWkhQTE6OioiIlJCQoPz9fvXv31ksvvSR3d3dJXz5Da/HixRo9erQqKys1bNgwPfnkk5Ikm82m1atXa968eQoPD5enp6fi4uIUHR1dv28AAABo1FpYNQ%2BIwk2Vl1dkfEybzU1RqXuMj4vGafu08Osv1AjZbG7y9fVSQUFJk/sN95tQN3U3B/VRd8eObW/KuNfDTTwAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhkPWFeuXDE9JAAAQKNiPGBFRETod7/7nbKyskwPDQAA0CgYD1i/%2BtWv9OGHH2rUqFGaMGGCXn31VRUVFZneDAAAQINlPGDdd999evXVV/XWW29p8ODBWrlypYYMGaIZM2boX//6l%2BnNAQAANDg37Sb3gIAATZ8%2BXW%2B99ZYSEhL097//XZMnT1ZkZKT%2B%2BMc/XvderYyMDD300EMKDQ1VeHi4Zs2apfz8fEnS4cOHNWHCBIWEhCgyMlIbN250WnfLli2KiopScHCwoqOjdejQIUfflStXtHjxYg0ePFghISF69NFHlZub6%2Bi/cOGC4uPj1b9/f4WFhSklJUVVVVUG3xkAANDU3bSAdfjwYT399NMaMmSIVqxYoaioKK1evVqJiYlau3atkpKSrrlueXm5pkyZopCQEP3zn//Um2%2B%2BqcLCQv3mN7/RxYsX9cgjj2jcuHE6ePCgUlJStHDhQn388ceSpPT0dM2fP1%2BLFi3SwYMHNWbMGD366KMqKyuTJK1YsUJ79%2B7V66%2B/rj179sjDw0NPPPGEY9vTpk2Tp6en9uzZo02bNmnfvn1as2bNzXqbAABAE2QzPeCLL76ov/71rzp16pR69%2B6t6dOna9SoUWrTpo1jmZYtW%2Bqpp5665hg5OTn64Q9/qISEBLVs2VKtWrVSbGysZs2apZ07d8rHx0cTJ06UJA0aNEijR49WWlqa%2BvTpo40bN2rkyJHq16%2BfJOnBBx/Uhg0btG3bNo0fP14bN27UzJkzdeutt0qSHn/8cQ0ZMkTZ2dmqrq7WgQMHtHv3btntdnXu3Fnx8fFasmSJpkyZYvqtAgAATZTxgLV%2B/XqNGTNGMTEx6tat21WX6dq1q2bOnHnNMX7wgx/olVdecWrbsWOHevbsqczMTAUFBTn1devWTZs2bZIkZWVlafz48bX6MzIyVFRUpLNnzzqt7%2Bfnp3bt2unYsWOSJB8fH3Xq1Mlprjk5Obp06ZK8vb3r8A5Iubm5ysvLc2qz2Tzl7%2B9fp/XrqmVLHmOG/2OzNc3PQ83nvLl93qmbupuDply38YC1e/duFRcXq7Cw0NG2bds2DRo0SL6%2BvpKkHj16qEePHnUaz7IsLV26VO%2B%2B%2B67Wr1%2BvtWvXym63Oy3j4eGh0tJSSVJJSck1%2B0tKSiRJnp6etfpr%2Br6%2Bbs3r0tLSOgesDRs2aPny5U5tCQkJSkxMrNP6wLfh6%2Bvl6incVN7e9usv1ARRd/NC3U2H8YD12Wef6eGHH1Z0dLRmz54tSVqyZIkqKyu1evXqWmefvklxcbGSk5P16aefav369erevbvsdnutxz6Ul5fLy%2BvL/7nY7XaVl5fX6vf19XWEpZr7sb6%2BvmVZtfpqXteMXxexsbGKjIx0arPZPFVQUFLnMeqiKSZ%2BfHumP18NRcuWbvL2tuvSpTJduVLt6unUG%2Bqm7uagPup21S%2BfxgPW7373O/3kJz/R9OnTHW3vvPOOnnzySS1atEirV6%2Bu0zinT5/Www8/rNtuu02bNm1S%2B/btJUlBQUHau3ev07JZWVkKDAyUJAUGBiozM7NWf0REhNq1a6dOnTopKyvLEfTy8vJUWFiooKAgVVdXq7CwUOfPn5efn58k6fjx47rlllvUtm3bOr8H/v7%2BtS4H5uUVqaqq%2BRw0qH9N/fN15Up1k6/xaqi7eaHupsP4KZBPP/1UjzzyiFq1auVoa9mypR555BF99NFHdRrj4sWLmjRpku644w6tWrXKEa4kKSoqSufPn9eaNWtUWVmp/fv3a%2BvWrY77rmJiYrR161bt379flZWVWrNmjS5cuKCoqChJUnR0tFasWKHs7GwVFxdrwYIFCg0N1fe%2B9z0FBASoX79%2BWrBggYqLi5Wdna0XX3xRMTExBt8hAADQ1Bk/g9WmTRudPn1anTt3dmo/e/asPDw86jTG5s2blZOTo%2B3bt%2Butt95y6jt06JBWr16tlJQULVu2TO3bt9cTTzyhgQMHSvryXxXOmTNHc%2BfO1blz59StWzetXLlSPj4%2Bkr68F6qqqkoTJ05USUmJwsLCtHTpUsf4y5Yt07x58zRs2DC5ublp3Lhxio%2BP/y5vCQAAaGZaWJZlmRzwt7/9rXbt2qWnn35affr0UYsWLXTkyBHNmzdPAwYM0NNPP21yc41GXp75Pxdks7kpKnWP8XHROG2fFu7qKdwUNpubfH29VFBQ0uQuIXwT6qbu5qA%2B6u7Yse63%2BJhk/AzWjBkzlJ2drZ///Odq0aKFoz0qKkqzZs0yvTkAAIAGx3jAstvteumll3TixAkdO3ZM7u7u6tq1qwICAkxvCgAAoEEyHrBqdOnSRV26dLlZwwMAADRYxgPWiRMnNG/ePH3wwQeqrKys1X/06FHTmwQAAGhQjAesuXPnKicnRzNnzryhZ0cBAAA0FcYD1qFDh/SnP/1JISEhpocGAABoFIw/aNTX1/eG/qwMAABAU2M8YMXFxenZZ5%2Bt9fcCAQAAmgvjlwh37dqljz76SGFhYerQoYPTn8yRpL///e%2BmNwkAANCgGA9YYWFhCgsLMz0sAABAo2E8YP3qV78yPSQAAECjYvweLEnKyMhQcnKy7r33Xp07d05paWlKT0%2B/GZsCAABocIwHrE8%2B%2BUQTJkzQv//9b33yySeqqKjQ0aNH9fOf/1zvvvuu6c0BAAA0OMYDVmpqqn7%2B859r3bp1cnd3lyT99re/1c9%2B9jMtX77c9OYAAAAaHOP3YH3yySeaM2dOrfb77rtPr776qunNAfhfI5budfUU6mz7tHBXTwEAbirjZ7Dc3d1VXFxcqz0nJ0d2u9305gAAABoc4wHrrrvu0jPPPKOCggJH2/Hjx5WSkqIf//jHpjcHAADQ4BgPWLNnz1Z5ebkGDx6ssrIyRUdHa9SoUbLZbJo1a5bpzQEAADQ4xu/BatOmjV599VXt27dPn332maqrqxUUFKQ777xTbm435akQAAAADYrxgFVj0KBBGjRo0M0aHgAAoMEyHrAiIyPVokWLa/bztwgBAEBTZzxg3XPPPU4Bq7KyUqdOndLu3bs1bdo005sDAABocIwHrKlTp161ff369frggw/0s5/9zPQmAQAAGpR6u%2Bt86NCh2rVrV31tDgAAwGXqLWAdOHBArVu3rq/NAQAAuIzxS4RfvwRoWZaKi4t17NgxLg8CAIBmwXjAuu2222r9K0J3d3dNmjRJo0ePNr05AACABsd4wFq0aJHpIQEAABoV4wHr4MGDdV52wIABpjcPAADgcsYD1oMPPijLshw/NWouG9a0tWjRQkePHjW9eQAAAJczHrBeeOEFLVy4ULNnz9bAgQPl7u6uw4cPa%2B7cubr//vs1dOhQ05sEAABoUIw/pmHx4sWaM2eO7rrrLrVp00atW7dWaGio5s2bp9WrV%2Bv22293/AAAADRFxgNWbm6ubr311lrtbdq0UUFBgenNAQAANDjGA1ZwcLCeffZZFRcXO9oKCwu1ZMkSDRo0yPTmAAAAGhzj92A98cQTmjRpkiIiIhQQECBJOnHihDp27Ki1a9ea3hwAAECDYzxgde3aVdu2bdPWrVt1/PhxSdL999%2BvkSNHym63m94cAABAg3NT/haht7e3JkyYoAceeEDJyckaO3bstw5X%2Bfn5ioqKUnp6uqNtzpw56tWrl0JCQhw/GzZscPSvXLlSERERCg4OVlxcnL744gtHX2lpqZKTkxUWFqZ%2B/fpp1qxZKikpcfSfOHFCkyZNUkhIiIYMGaI//OEP32reAACg%2BTIesCzLUmpqqgYMGKBRo0bp7Nmzmj17tpKTk1VZWXlDY33wwQeKjY3V6dOnndqPHDmi%2BfPn69ChQ46f2NhYSdKWLVu0bt06rVq1Sunp6erZs6cSExMdz9%2BaP3%2B%2Bzpw5ox07dmjnzp06c%2BaMUlNTJUmVlZX65S9/qd69eys9PV0vv/yy0tLStH37dgPvDAAAaC6MB6x169bpr3/9q%2BbMmaNWrVpJku666y794x//0PPPP1/ncbZs2aKZM2dq%2BvTpTu0VFRX6/PPP1atXr6uu99prr%2Bn%2B%2B%2B9XYGCgWrdurRkzZignJ0fp6ekqKyvT1q1blZiYKB8fH3Xo0EEzZ87U5s2bVVZWpoMHDyo3N1eJiYlq1aqVevToobi4OKWlpX37NwQAADQ7xgPWhg0b9NRTTyk6Otrx9Pa7775bKSkp%2Btvf/lbncYYMGaK3335bd999t1N7RkaGqqqqtGzZMg0ePFjDhw/Xyy%2B/rOrqaklSVlaWgoKCHMu7u7srICBAGRkZOnXqlCorK536u3btqvLycp08eVKZmZnq0qWLIxhKUrdu3ZSRkfGt3gsAANA8Gb/J/d///rd%2B9KMf1Wrv3r27zp8/X%2BdxOnbseNX2oqIihYaGKi4uTs8%2B%2B6yOHj2qhIQEubm5acqUKSopKal1v5eHh4dKS0sdj47w9PR09NUsW1JSctV17Xa7SktL6zxv6ctngeXl5Tm12Wye8vf3v6Fxrqdly5tyCx1w09lsdf/s1nzOm9vnnbqpuzloynUbD1i33367Pv74Y/2///f/nNp37dqlzp07f%2Bfxw8PDFR4e7njdp08fTZo0Sdu2bdOUKVNkt9tVXl7utE55ebm8vLwcwaqsrExeXl6O/5a%2BfBCqp6en43WNry5bVxs2bNDy5cud2hISEpSYmHhD4wBNla/vjR1TkuTt3Tz/FTJ1Ny/U3XQYD1iTJ0/W008/rXPnzsmyLO3bt0%2Bvvvqq1q1bp%2BTk5O88/jvvvKPz58/r3nvvdbRVVFTIw8NDkhQYGKjMzEzH3zysrKzUyZMnFRQUpC5dusjd3V1ZWVnq27evJOn48eOOy4gXLlzQyZMnVVVVJZvty7cmKytLgYGBNzTH2NhYRUZGOrXZbJ4qKCi5xhrfTlNM/GgebuRYaNnSTd7edl26VKYrV6pv4qwaFuqm7uagPur%2BNr/QmWA8YI0fP15VVVVasWKFysvL9dRTT6lDhw6aPn267rvvvu88vmVZWrhwob7//e9r4MCB%2Buijj7R27VpHeBs/frxeeOEFRUREqEuXLnruuefk5%2Ben/v37y93dXSNGjFBqaqrjhvvU1FSNGjVKHh4eCgsLk6%2Bvr5555hlNmzZNJ06c0Lp162rdaH89/v7%2BtS4H5uUVqaqq%2BRw0wDf5NsfClSvVzfIYou7mhbqbDuMB64033tB///d/KzY2Vvn5%2BbIsSx06dDA2flRUlJKTkzV37lydO3dOfn5%2Bmjp1qsaOHStJiomJUVFRkRISEpSfn6/evXvrpZdekru7u6Qvn6G1ePFijR49WpWVlRo2bJiefPJJSZLNZtPq1as1b948hYeHy9PTU3FxcYqOjjY2fwAA0PS1sGoeEGVIaGio/vznP6tr164mh2308vKKjI9ps7kpKnWP8XGBm237tPDrL/S/bDY3%2Bfp6qaCgpMn9hvtNqJu6m4P6qLtjx7Y3ZdzrMX4TT0BAgI4dO2Z6WAAAgEbD%2BCXCwMBAzZw5U6%2B88ooCAgLUunVrp/6FCxea3iQAAECDYjxgnT59Wv369ZOkWs%2BCAgAAaA6MBKyFCxfqsccek6enp9atW2diSAAAgEbLyD1Ya9eurfWAzsmTJys3N9fE8AAAAI2KkYB1tX%2BI%2BOGHH%2Bry5csmhgcAAGhUeBQ4AACAYQQsAAAAw4wFrBYtWpgaCgAAoFEz9piG3/72t07PvKqsrNSSJUvk5eX8RxZ5DhYAAGjqjASsAQMG1HrmVUhIiAoKClRQUGBiEwAAAI2GkYDFs68AAAD%2BDze5AwAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGNbgA1Z%2Bfr6ioqKUnp7uaDt8%2BLAmTJigkJAQRUZGauPGjU7rbNmyRVFRUQoODlZ0dLQOHTrk6Lty5YoWL16swYMHKyQkRI8aIRTKAAAW3klEQVQ%2B%2Bqhyc3Md/RcuXFB8fLz69%2B%2BvsLAwpaSkqKqq6uYXCgAAmowGHbA%2B%2BOADxcbG6vTp0462ixcv6pFHHtG4ceN08OBBpaSkaOHChfr4448lSenp6Zo/f74WLVqkgwcPasyYMXr00UdVVlYmSVqxYoX27t2r119/XXv27JGHh4eeeOIJx/jTpk2Tp6en9uzZo02bNmnfvn1as2ZNvdYNAAAatwYbsLZs2aKZM2dq%2BvTpTu07d%2B6Uj4%2BPJk6cKJvNpkGDBmn06NFKS0uTJG3cuFEjR45Uv3795O7urgcffFC%2Bvr7atm2bo//hhx/WrbfeqjZt2ujxxx/X7t27lZ2drVOnTunAgQNKSkqS3W5X586dFR8f7xgbAACgLmyunsC1DBkyRKNHj5bNZnMKWZmZmQoKCnJatlu3btq0aZMkKSsrS%2BPHj6/Vn5GRoaKiIp09e9ZpfT8/P7Vr107Hjh2TJPn4%2BKhTp06O/q5duyonJ0eXLl2St7d3neaem5urvLw8pzabzVP%2B/v51Wr%2BuWrZssPkY%2BEY2W90/uzWf8%2Bb2eadu6m4OmnLdDTZgdezY8artJSUlstvtTm0eHh4qLS29bn9JSYkkydPTs1Z/Td/X1615XVpaWueAtWHDBi1fvtypLSEhQYmJiXVaH2jqfH29bngdb2/79Rdqgqi7eaHupqPBBqxrsdvtKioqcmorLy%2BXl5eXo7%2B8vLxWv6%2BvryMs1dyP9fX1Lcuq1Vfzumb8uoiNjVVkZKRTm83mqYKCkjqPURdNMfGjebiRY6FlSzd5e9t16VKZrlypvomzaliom7qbg/qo%2B9v8QmdCowtYQUFB2rt3r1NbVlaWAgMDJUmBgYHKzMys1R8REaF27dqpU6dOysrKclwmzMvLU2FhoYKCglRdXa3CwkKdP39efn5%2BkqTjx4/rlltuUdu2bes8R39//1qXA/PyilRV1XwOGuCbfJtj4cqV6mZ5DFF380LdTUejOwUSFRWl8%2BfPa82aNaqsrNT%2B/fu1detWx31XMTEx2rp1q/bv36/KykqtWbNGFy5cUFRUlCQpOjpaK1asUHZ2toqLi7VgwQKFhobqe9/7ngICAtSvXz8tWLBAxcXFys7O1osvvqiYmBhXlgwAABqZRncGy9fXV6tXr1ZKSoqWLVum9u3b64knntDAgQMlSYMGDdKcOXM0d%2B5cnTt3Tt26ddPKlSvl4%2BMj6ct7oaqqqjRx4kSVlJQoLCxMS5cudYy/bNkyzZs3T8OGDZObm5vGjRun%2BPh4l9QKAAAapxaWZVmunkRzkJdXdP2FbpDN5qao1D3GxwVutu3Twuu8rM3mJl9fLxUUlDS5SwjfhLqpuzmoj7o7dqz7LT4mNbozWAAavxFL915/oQbkRgIhAEiN8B4sAACAho6ABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMCwRhuwtm3bph49eigkJMTxk5SUJEnatWuXRo8ereDgYI0YMULvvvuu07orV65URESEgoODFRcXpy%2B%2B%2BMLRV1paquTkZIWFhalfv36aNWuWSkpK6rU2AADQuDXagHXkyBGNHTtWhw4dcvwsWbJEJ0%2Be1NSpU/XYY4/p/fff19SpUzVt2jSdO3dOkrRlyxatW7dOq1atUnp6unr27KnExERZliVJmj9/vs6cOaMdO3Zo586dOnPmjFJTU11ZKgAAaGQadcDq1atXrfYtW7aof//%2Buuuuu2Sz2XT33XdrwIAB2rBhgyTptdde0/3336/AwEC1bt1aM2bMUE5OjtLT01VWVqatW7cqMTFRPj4%2B6tChg2bOnKnNmzerrKysvksEAACNVKMMWNXV1fr000/13nvvaejQoYqIiNCTTz6pixcvKisrS0FBQU7Ld%2BvWTRkZGZJUq9/d3V0BAQHKyMjQqVOnVFlZ6dTftWtXlZeX6%2BTJk/VSGwAAaPxsrp7At5Gfn68ePXpo%2BPDhWrZsmQoKCjR79mwlJSWpoqJCdrvdaXkPDw%2BVlpZKkkpKSq7ZX1xcLEny9PR09NUseyP3YeXm5iovL8%2BpzWbzlL%2B/f92LrIOWLRtlPgYaHZut/o%2B1muO7uR3n1E3dTUWjDFh%2Bfn5KS0tzvLbb7UpKStJPf/pThYWFqby83Gn58vJyeXl5OZa9Vn9NsCorK3MsX3NpsE2bNnWe34YNG7R8%2BXKntoSEBCUmJtZ5DAANh6%2Bvl8u27e1tv/5CTRB1Ny9Nse5GGbAyMjL05ptvasaMGWrRooUkqaKiQm5uburTp4%2BOHj3qtHxWVpbjfq3AwEBlZmZq6NChkqTKykqdPHlSQUFB6tKli9zd3ZWVlaW%2BfftKko4fP%2B64jFhXsbGxioyMdGqz2TxVUGD2XyM2xcQPNESmj926aNnSTd7edl26VKYrV6rrffuuQt3UbZqrfkFqlAHLx8dHaWlpateunR566CHl5uZqyZIluueeezRu3Dj96U9/0rZt2/STn/xEO3fu1IEDB/T4449LksaPH68XXnhBERER6tKli5577jn5%2Bfmpf//%2Bcnd314gRI5Samqrnn39ekpSamqpRo0bJw8OjzvPz9/evdTkwL69IVVXN56ABmhJXHrtXrlQ3y%2B8O6m5emmLdjTJg3XLLLXrppZf07LPPasWKFWrdurVGjhyppKQktW7dWr///e%2BVmpqqxx9/XLfffrteeOEFdenSRZIUExOjoqIiJSQkKD8/X71799ZLL70kd3d3SdKcOXO0ePFijR49WpWVlRo2bJiefPJJV5YLAAAamRZWzQOgcFPl5RUZH9Nmc1NU6h7j4wJwtn1aeL1v02Zzk6%2BvlwoKSprcb/bfhLqp27SOHdvelHGvh5t4AAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAesqLly4oPj4ePXv319hYWFKSUlRVVWVq6cFAAAaCQLWVUybNk2enp7as2ePNm3apH379mnNmjWunhYAAGgkCFhfc%2BrUKR04cEBJSUmy2%2B3q3Lmz4uPjlZaW5uqpAQCARoKA9TWZmZny8fFRp06dHG1du3ZVTk6OLl265MKZAQCAxsLm6gk0NCUlJbLb7U5tNa9LS0vl7e193TFyc3OVl5fn1Gazecrf39/cRCW1bEk%2BBurDiKV7XT2FG/L2zDtdPYVvreZ7rbl9v1F306ubgPU1np6eKisrc2qree3l5VWnMTZs2KDly5c7tf3qV7/S1KlTzUzyf%2BXm5mrSLZmKjY01Ht4astzcXG3YsIG6mwnqbn51/%2BlPr1B3M9GU6256kfE7CgwMVGFhoc6fP%2B9oO378uG655Ra1bdu2TmPExsZq8%2BbNTj%2BxsbHG55qXl6fly5fXOlvW1FE3dTcH1E3dzUFTrpszWF8TEBCgfv36acGCBZo3b54KCgr04osvKiYmps5j%2BPv7N7kkDgAA6o4zWFexbNkyVVVVadiwYfrpT3%2BqO%2B%2B8U/Hx8a6eFgAAaCQ4g3UVfn5%2BWrZsmaunAQAAGqmWc%2BfOnevqSeDb8/LyUmhoaJ1vwG8qqJu6mwPqpu7moKnW3cKyLMvVkwAAAGhKuAcLAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBq5G6cOGC4uPj1b9/f4WFhSklJUVVVVWunpZxGRkZeuihhxQaGqrw8HDNmjVL%2Bfn5kqQ5c%2BaoV69eCgkJcfxs2LDBxTM2Y9u2berRo4dTbUlJSZKkXbt2afTo0QoODtaIESP07rvvuni2ZrzxxhtO9YaEhKhXr17q1auXJGnKlCnq3bu3U//u3btdPOvvJj8/X1FRUUpPT3e0HT58WBMmTFBISIgiIyO1ceNGp3W2bNmiqKgoBQcHKzo6WocOHarvaX9nV6t7x44dGjt2rO644w5FRkZq%2BfLlqq6udvSPGDFCffv2ddr/x48fd8X0v7Wr1X2977GVK1cqIiJCwcHBiouL0xdffOGKqX8nX6/7qaeeqnWs/%2BhHP9LkyZMlSdXV1QoJCVFwcLDTMqWlpa4s48ZZaJQeeOABa8aMGVZpaal1%2BvRpa%2BTIkdbKlStdPS2jysrKrPDwcOv555%2B3Ll%2B%2BbOXn51sPP/yw9Ytf/MKyLMu65557rM2bN7t4ljfHokWLrF//%2Bte12k%2BcOGH17t3bevvtt63Kykrrb3/7m9WnTx/r7NmzLpjlzXX27FkrPDzc%2Bstf/mJZlmWFhYVZ6enpLp6VOe%2B//7511113WUFBQdb%2B/fsty7KswsJCKzQ01Fq/fr1VWVlp/etf/7JCQkKsw4cPW5ZlWfv377dCQkKs999/36qoqLD%2B%2BMc/WmFhYVZpaakrS7khV6v7yJEjVp8%2Bfax//OMf1pUrV6ysrCxr6NCh1qpVqyzLsqyioiKre/fu1r///W9XTv07uVrdlvXN32ObN2%2B27rzzTuvzzz%2B3ysvLrYULF1ojR460qqur62va39m16v6qPXv2WKGhodbnn39uWZZlHTt2zOrZs6d1%2BfLl%2BpyqcZzBaoROnTqlAwcOKCkpSXa7XZ07d1Z8fLzS0tJcPTWjcnJy9MMf/lAJCQlq1aqVfH19FRsbq4MHD6qiokKff/654%2BxGU3PkyJGr1rZlyxb1799fd911l2w2m%2B6%2B%2B24NGDCgyZy5q2FZlpKSkvTjH/9YY8eOVXZ2ti5evKgePXq4empGbNmyRTNnztT06dOd2nfu3CkfHx9NnDhRNptNgwYN0ujRox3H9saNGzVy5Ej169dP7u7uevDBB%2BXr66tt27a5oowbdq26//Of/%2Bjee%2B/V0KFD5ebmpq5duyoqKkoHDx6UJH3yySfy8fHR7bff7oppf2fXqvt632Ovvfaa7r//fgUGBqp169aaMWOGcnJynM6ANWTXqvur8vPzNXPmTD3%2B%2BOMKDAyU9OX3X/fu3dWqVav6mupNQcBqhDIzM%2BXj46NOnTo52rp27aqcnBxdunTJhTMz6wc/%2BIFeeeUVtWzZ0tG2Y8cO9ezZUxkZGaqqqtKyZcs0ePBgDR8%2BXC%2B//LLTJYXGqrq6Wp9%2B%2Bqnee%2B89DR06VBEREXryySd18eJFZWVlKSgoyGn5bt26KSMjw0WzvTn%2B%2Bte/KisrS7/%2B9a8lffmF6%2BXlpenTp2vgwIEaNWqUNm3a5OJZfntDhgzR22%2B/rbvvvtupPTMz8xv3b2Pf/9eqe/jw4UpOTna8Li8v13vvvaeePXtK%2BnL/2%2B12PfDAAwoLC1N0dHSjujR%2Brbqv9z329f3t7u6ugICARr%2B/vyo1NVW9evXSmDFjHG1HjhzR5cuXNX78eA0cOFATJ07Uhx9%2BWB9TNsrm6gngxpWUlMhutzu11bwuLS2Vt7e3K6Z1U1mWpaVLl%2Brdd9/V%2BvXrdf78eYWGhiouLk7PPvusjh49qoSEBLm5uWnKlCmunu53kp%2Bfrx49emj48OFatmyZCgoKNHv2bCUlJamioqLWvvfw8Gh89yZ8g%2Brqaq1YsUK//OUv1aZNG0lf/qYfHBys6dOnKzAwUOnp6Zo6daq8vLw0YsQIF8/4xnXs2PGq7Vc7tr%2B6f6/X39Bdq%2B6vKi4u1mOPPSYPDw89%2BOCDkqQWLVqod%2B/e%2Bp//%2BR/ddttteuuttzR16lStX79ewcHBN3nW39216i4qKvrG77Gmvr%2Bzs7P1xhtv1LrP0MPDQ3369NFjjz2mdu3aKS0tTZMnT9Ybb7yhzp0738wpG0XAaoQ8PT1VVlbm1Fbz2svLyxVTuqmKi4uVnJysTz/9VOvXr1f37t3VvXt3hYeHO5bp06ePJk2apG3btjX6gOXn5%2Bd0uddutyspKUk//elPFRYWpvLycqfly8vLm9R%2BT09PV25urmJiYhxt48aN07hx4xyvhwwZonHjxmn79u2NMmBdi91uV1FRkVPbV/ev3W6/6v739fWttzneTF988YUSExPVoUMHrV271hGwv35MjxkzRm%2B%2B%2BaZ27NjRKALWtYSHh3/j99i19ndTOd5ff/11xw3uX1Vz5rrG5MmTtXnzZu3atUsPPPBAfU7xO%2BESYSMUGBiowsJCnT9/3tF2/Phx3XLLLWrbtq0LZ2be6dOnNX78eBUXF2vTpk3q3r27JOmdd97Rq6%2B%2B6rRsRUWFPDw8XDFNozIyMpSamirLshxtFRUVcnNzU58%2BfZSZmem0fFZWluPehaZgx44dioqKkqenp6Nt06ZN2r59u9NyFRUVat26dX1P76YKCgr6xv0bGBjYZPf/rl27NGHCBN15551atWqV2rVr5%2BhbtWqV9u3b57R8U9j/1/se%2B/r%2Brqys1MmTJ2tdJm6sdu7cqbFjx9Zqf%2B655/TZZ585tTXG/U3AaoQCAgLUr18/LViwQMXFxcrOztaLL77o9Bt/U3Dx4kVNmjRJd9xxh1atWqX27ds7%2BizL0sKFC7Vv3z5ZlqVDhw5p7dq1io2NdeGMzfDx8VFaWppeeeUVVVVVKScnR0uWLNE999yjcePG6cCBA9q2bZuqqqq0bds2HThw4KpfUo3VBx98oAEDBji1FRcXa/78%2Bfrss89UXV2t9957T2%2B%2B%2BWaT2N9fFRUVpfPnz2vNmjWqrKzU/v37tXXrVo0fP16SFBMTo61bt2r//v2qrKzUmjVrdOHCBUVFRbl45t/NRx99pISEBCUnJ2v27Nmy2Zwvrpw5c0ZPP/20srOzVVVVpU2bNunQoUO65557XDRjM673PTZ%2B/HitX79eGRkZunz5sp555hn5%2Bfmpf//%2BLp75d1dQUKDjx4/XOtYl6fPPP1dKSory8vJUUVGh5cuXq7i4uPF9zl34LxjxHeTl5VlTp061QkNDrYEDB1qLFi2yqqqqXD0to1avXm0FBQVZffv2tYKDg51%2BLMuy/vznP1s/%2BclPrL59%2B1rDhg2z1q9f7%2BIZm5Oenm7FxsZaISEh1sCBA6358%2Bdb5eXllmVZ1u7du60xY8ZYwcHB1siRI6333nvPxbM1Kzg4uFZN1dXV1u9//3tr6NChVp8%2BfayRI0da27dvd9EMzfr6P1//%2BOOPHft%2B2LBh1uuvv%2B60/F/%2B8hdr%2BPDhVnBwsBUTE2N99NFH9T1lI75a9y9%2B8Qure/futY7zyZMnW5ZlWZcvX7ZSUlKsIUOGWH379rXGjx9/zX/y39B9fX9/0/dYdXW1tWrVKisyMtIKDg624uLirC%2B%2B%2BMIV0/7OrvY5DwoKssrKymotW1BQYP3617%2B2Bg0a5Kj76NGj9TldI1pY1leuQwAAAOA74xIhAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGDY/wd36rCDmm3McwAAAABJRU5ErkJggg%3D%3D"/>
        </div>
        <div role="tabpanel" class="tab-pane col-md-12" id="common-4217212580898125458">

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">12.0</td>
        <td class="number">2224</td>
        <td class="number">0.9%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">14.0</td>
        <td class="number">2196</td>
        <td class="number">0.9%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">15.0</td>
        <td class="number">2189</td>
        <td class="number">0.9%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">8.0</td>
        <td class="number">2164</td>
        <td class="number">0.8%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">9.0</td>
        <td class="number">2127</td>
        <td class="number">0.8%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">7.0</td>
        <td class="number">2116</td>
        <td class="number">0.8%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">10.0</td>
        <td class="number">2082</td>
        <td class="number">0.8%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">16.0</td>
        <td class="number">2074</td>
        <td class="number">0.8%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">13.0</td>
        <td class="number">2071</td>
        <td class="number">0.8%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">18.0</td>
        <td class="number">2052</td>
        <td class="number">0.8%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr><tr class="other">
        <td class="fillremaining">Other values (121)</td>
        <td class="number">95306</td>
        <td class="number">37.1%</td>
        <td>
            <div class="bar" style="width:68%">&nbsp;</div>
        </td>
</tr><tr class="missing">
        <td class="fillremaining">(Missing)</td>
        <td class="number">140383</td>
        <td class="number">54.6%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr>
</table>
        </div>
        <div role="tabpanel" class="tab-pane col-md-12"  id="extreme-4217212580898125458">
            <p class="h4">Minimum 5 values</p>

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">0.0</td>
        <td class="number">531</td>
        <td class="number">0.2%</td>
        <td>
            <div class="bar" style="width:40%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">1.0</td>
        <td class="number">734</td>
        <td class="number">0.3%</td>
        <td>
            <div class="bar" style="width:55%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">2.0</td>
        <td class="number">986</td>
        <td class="number">0.4%</td>
        <td>
            <div class="bar" style="width:74%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">3.0</td>
        <td class="number">1129</td>
        <td class="number">0.4%</td>
        <td>
            <div class="bar" style="width:84%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">4.0</td>
        <td class="number">1333</td>
        <td class="number">0.5%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr>
</table>
            <p class="h4">Maximum 5 values</p>

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">148.0</td>
        <td class="number">2</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:67%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">149.0</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:34%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">151.0</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:34%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">152.0</td>
        <td class="number">3</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">176.0</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:34%">&nbsp;</div>
        </td>
</tr>
</table>
        </div>
    </div>
</div>
</div><div class="row variablerow">
    <div class="col-md-3 namecol">
        <p class="h4 pp-anchor" id="pp_var_Number of Credit Problems">Number of Credit Problems<br/>
            <small>Numeric</small>
        </p>
    </div><div class="col-md-6">
    <div class="row">
        <div class="col-sm-6">
            <table class="stats ">
                <tr>
                    <th>Distinct count</th>
                    <td>12</td>
                </tr>
                <tr>
                    <th>Unique (%)</th>
                    <td>0.0%</td>
                </tr>
                <tr class="ignore">
                    <th>Missing (%)</th>
                    <td>0.0%</td>
                </tr>
                <tr class="ignore">
                    <th>Missing (n)</th>
                    <td>0</td>
                </tr>
                <tr class="ignore">
                    <th>Infinite (%)</th>
                    <td>0.0%</td>
                </tr>
                <tr class="ignore">
                    <th>Infinite (n)</th>
                    <td>0</td>
                </tr>
            </table>

        </div>
        <div class="col-sm-6">
            <table class="stats ">

                <tr>
                    <th>Mean</th>
                    <td>0.15663</td>
                </tr>
                <tr>
                    <th>Minimum</th>
                    <td>0</td>
                </tr>
                <tr>
                    <th>Maximum</th>
                    <td>11</td>
                </tr>
                <tr class="alert">
                    <th>Zeros (%)</th>
                    <td>86.8%</td>
                </tr>
            </table>
        </div>
    </div>
</div>
<div class="col-md-3 collapse in" id="minihistogram7415176150050136265">
    <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAABLCAYAAAA1fMjoAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAPYQAAD2EBqD%2BnaQAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAAQpJREFUeJzt1sEJAkEQRUEVQzIIc/JsTgaxObV3kQeCy4hU3Rv%2B5TFznJk5AG%2BdVg%2BAX3ZePeDV5fb4%2BGa7X3dYAl4QSAKBIBAIAoEgEAgCgSAQCAKBIBAIAoEgEAgCgSAQCAKBIBAIAoEgEAgCgSAQCAKBIBAIAoEgEAgCgSAQCAKBIBAIAoEgEAgCgSAQCAKBIBAIAoEgEAgCgSAQCAKBIBAIAoEgEAgCgSAQCAKBIBAI59UDvuFye3x8s92vOyzh3xxnZlaPgF/liwVBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBAJBIBAEAkEgEAQCQSAQBALhCV3BDpFBjPb7AAAAAElFTkSuQmCC">

</div>
<div class="col-md-12 text-right">
    <a role="button" data-toggle="collapse" data-target="#descriptives7415176150050136265,#minihistogram7415176150050136265"
       aria-expanded="false" aria-controls="collapseExample">
        Toggle details
    </a>
</div>
<div class="row collapse col-md-12" id="descriptives7415176150050136265">
    <ul class="nav nav-tabs" role="tablist">
        <li role="presentation" class="active"><a href="#quantiles7415176150050136265"
                                                  aria-controls="quantiles7415176150050136265" role="tab"
                                                  data-toggle="tab">Statistics</a></li>
        <li role="presentation"><a href="#histogram7415176150050136265" aria-controls="histogram7415176150050136265"
                                   role="tab" data-toggle="tab">Histogram</a></li>
        <li role="presentation"><a href="#common7415176150050136265" aria-controls="common7415176150050136265"
                                   role="tab" data-toggle="tab">Common Values</a></li>
        <li role="presentation"><a href="#extreme7415176150050136265" aria-controls="extreme7415176150050136265"
                                   role="tab" data-toggle="tab">Extreme Values</a></li>

    </ul>

    <div class="tab-content">
        <div role="tabpanel" class="tab-pane active row" id="quantiles7415176150050136265">
            <div class="col-md-4 col-md-offset-1">
                <p class="h4">Quantile statistics</p>
                <table class="stats indent">
                    <tr>
                        <th>Minimum</th>
                        <td>0</td>
                    </tr>
                    <tr>
                        <th>5-th percentile</th>
                        <td>0</td>
                    </tr>
                    <tr>
                        <th>Q1</th>
                        <td>0</td>
                    </tr>
                    <tr>
                        <th>Median</th>
                        <td>0</td>
                    </tr>
                    <tr>
                        <th>Q3</th>
                        <td>0</td>
                    </tr>
                    <tr>
                        <th>95-th percentile</th>
                        <td>1</td>
                    </tr>
                    <tr>
                        <th>Maximum</th>
                        <td>11</td>
                    </tr>
                    <tr>
                        <th>Range</th>
                        <td>11</td>
                    </tr>
                    <tr>
                        <th>Interquartile range</th>
                        <td>0</td>
                    </tr>
                </table>
            </div>
            <div class="col-md-4 col-md-offset-2">
                <p class="h4">Descriptive statistics</p>
                <table class="stats indent">
                    <tr>
                        <th>Standard deviation</th>
                        <td>0.46073</td>
                    </tr>
                    <tr>
                        <th>Coef of variation</th>
                        <td>2.9416</td>
                    </tr>
                    <tr>
                        <th>Kurtosis</th>
                        <td>40.584</td>
                    </tr>
                    <tr>
                        <th>Mean</th>
                        <td>0.15663</td>
                    </tr>
                    <tr>
                        <th>MAD</th>
                        <td>0.27204</td>
                    </tr>
                    <tr class="">
                        <th>Skewness</th>
                        <td>4.6975</td>
                    </tr>
                    <tr>
                        <th>Sum</th>
                        <td>40251</td>
                    </tr>
                    <tr>
                        <th>Variance</th>
                        <td>0.21227</td>
                    </tr>
                    <tr>
                        <th>Memory size</th>
                        <td>2.0 MiB</td>
                    </tr>
                </table>
            </div>
        </div>
        <div role="tabpanel" class="tab-pane col-md-8 col-md-offset-2" id="histogram7415176150050136265">
            <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAlgAAAGQCAYAAAByNR6YAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAPYQAAD2EBqD%2BnaQAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAIABJREFUeJzt3X9UVXW%2B//EXcEAOqIEiWi0bSKCuZcn1B5rmHX%2BQY4mZP6J0kf2wpiAJl7%2Buqemo%2BGNEKzXNLHNS1o1ydBq7mNaM16xrSGZmjhSYqC1MQFDhAMmv7x99OXdO2AjnfPJw9PlYi7U6n8/en/0%2B78WK19l7n61XfX19vQAAAGCMt7sLAAAAuNoQsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYRZ3F3CtKCoqM76mt7eX2rULVEmJTXV19cbXv5rRO%2BfRO9fQP%2BfRO9dcq/3r0KGNW47LGSwP5u3tJS8vL3l7e7m7FI9D75xH71xD/5xH71xD/64sAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADHNbwMrJydFjjz2m3r17q1%2B/fpo%2BfbpKSkokSXPnztXtt9%2Bu6Oho%2B09GRoZ93/Xr12vAgAHq3r27EhIS9N1339nnKioqNHPmTMXExKhHjx6aPn26bDabff748eOaMGGCoqOj1b9/f7366qsOde3Zs0dxcXHq3r27hg0bpt27d//KnQAAAFcbizsOWlVVpYkTJ%2BrBBx/UunXrZLPZNGPGDD3//PN69dVXdfjwYS1YsEAPPPBAo323bdumTZs26Y033tBNN92kF198UcnJydq%2Bfbu8vLy0YMECnT59Wjt37lRtba1SUlKUlpamuXPnqrq6Wk8//bRiY2O1fv165eXl6fe//71%2B85vfaNiwYcrPz9ekSZO0YsUK/fa3v9WuXbuUkpKiXbt2qWPHjm7o1OX1nPWBu0tosh0p/dxdAgAAV4RbzmAVFBTo1ltvVVJSkvz8/BQcHKz4%2BHhlZ2fr4sWL%2Bvbbb3X77bdfct933nlH48aNU2RkpFq1aqUpU6aooKBAWVlZqqys1Pbt25WcnKygoCC1b99eU6dO1datW1VZWans7GwVFhYqOTlZfn5%2B6tq1qxISEpSeni7pp/DWs2dPDRkyRBaLRffee6969erlcPYMAADgctwSsG6%2B%2BWa9/vrr8vHxsY/t3LlTt912m3JyclRTU6OVK1fqrrvu0tChQ/Xaa6%2Bprq5OkpSXl6eoqCj7fr6%2BvgoLC1NOTo5OnDih6upqh/kuXbqoqqpK%2Bfn5ys3NVXh4uPz8/OzzERERysnJueTaP58HAABoCrdcIvxn9fX1eumll7R7925t3rxZxcXF6t27txISErRixQodPXpUSUlJ8vb21sSJE2Wz2WS1Wh3W8Pf3V0VFhcrLyyVJAQEB9rmGbW022yX3tVqtqqiosG/zS2s3R2FhoYqKihzGLJYAhYaGNmudy/Hx8azvKFgsLafeht55Wg9bAnrnGvrnPHrnGvp3Zbk1YJWXl2vmzJk6cuSINm/erFtuuUW33HKL%2BvX7v3t17rjjDk2YMEGZmZmaOHGirFarqqqqHNapqqpSYGCgPVhVVlYqMDDQ/t%2BS1Lp1awUEBNhfN/jnbf/V2s2RkZGh1atXO4wlJSUpOTm5WetcbYKDm9fHK6FtW%2BvlN8Il0TvX0D/n0TvX0L8rw20B6%2BTJk3ryySd1ww03aMuWLWrXrp0k6aOPPlJxcbEeeugh%2B7YXL16Uv7%2B/JCkyMlK5ubkaOHCgJKm6ulr5%2BfmKiopSeHi4fH19lZeXpzvvvFOSdOzYMftlxLNnzyo/P181NTWyWH5663l5eYqMjJQkRUVF6ciRIw515uXl/eL9YL8kPj5egwYNchizWAJUWmr7hT2c42mfQky/f1f4%2BHirbVurLlyoVG1tnbvL8Sj0zjX0z3n0zjXXav/c9eHeLQHr/PnzmjBhgvr06aPU1FR5e/9fUKivr9fixYv1m9/8Rn369NGXX36pt956SzNnzpQkjR49WqtWrdKAAQMUHh6uF198USEhIerZs6d8fX01bNgwpaWl6eWXX5YkpaWlafjw4fL391dMTIyCg4O1fPlypaSk6Pjx49q0aZMmT54sSRoxYoTefPNNZWZm6p577tGuXbu0f/9%2BzZo1q1nvLzQ0tNHlwKKiMtXUXDu/0JfSEt9/bW1di6zLE9A719A/59E719C/K8MtAWvr1q0qKCjQjh079MEHjo8ZOHjwoGbOnKl58%2BbpzJkzCgkJ0aRJk3T//fdLksaMGaOysjIlJSWppKRE3bp107p16%2BTr6yvpp2doLV26VHFxcaqurtbgwYM1Z84cSZLFYtGGDRs0f/589evXTwEBAUpISNCoUaMk/XRD/CuvvKK0tDTNmjVLN954o1atWqXw8PAr2B0AAODpvOrr6%2BvdXcS1oKiozPiaFou3YtP2Gl/319KSnoNlsXgrODhQpaU2Psk1E71zDf1zHr1zzbXavw4d2rjluJ51Ew8AAIAHIGABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAY5raAlZOTo8cee0y9e/dWv379NH36dJWUlEiSDh06pLFjxyo6OlqDBg3Su%2B%2B%2B67Dvtm3bFBsbq%2B7du2vUqFE6ePCgfa62tlZLly7VXXfdpejoaD3zzDMqLCy0z589e1aJiYnq2bOnYmJilJqaqpqaGvv85Y4NAABwOW4JWFVVVZo4caKio6P1ySef6P3339e5c%2Bf0/PPP6/z583rqqac0cuRIZWdnKzU1VYsXL9ZXX30lScrKytKCBQu0ZMkSZWdna8SIEXrmmWdUWVkpSVq7dq0%2B/fRT/fnPf9bevXvl7%2B%2Bv2bNn24%2BdkpKigIAA7d27V1u2bNG%2Bffu0ceNGSbrssQEAAJrCLQGroKBAt956q5KSkuTn56fg4GDFx8crOztbu3btUlBQkMaPHy%2BLxaK%2BffsqLi5O6enpkqR3331X9913n3r06CFfX189%2BuijCg4OVmZmpn3%2BySef1PXXX6/WrVtr1qxZ%2Bvjjj3Xq1CmdOHFC%2B/fv17Rp02S1WtW5c2clJiba177csQEAAJrCLQHr5ptv1uuvvy4fHx/72M6dO3XbbbcpNzdXUVFRDttHREQoJydHkpSXl/eL82VlZfrhhx8c5kNCQnTdddfpm2%2B%2BUW5uroKCgtSxY0f7fJcuXVRQUKALFy5c9tgAAABNYXF3AfX19XrppZe0e/dubd68WW%2B99ZasVqvDNv7%2B/qqoqJAk2Wy2X5y32WySpICAgEbzDXM/37fhdcP%2B/%2BrYTVVYWKiioiKHMYslQKGhoc1a53J8fDzrOwoWS8upt6F3ntbDloDeuYb%2BOY/euYb%2BXVluDVjl5eWaOXOmjhw5os2bN%2BuWW26R1WpVWVmZw3ZVVVUKDAyU9FMgqqqqajQfHBxsD0cN92P9fP/6%2BvpGcw2vAwMDL3vspsrIyNDq1asdxpKSkpScnNysda42wcHN6%2BOV0Lat9fIb4ZLonWvon/PonWvo35XhtoB18uRJPfnkk7rhhhu0ZcsWtWvXTpIUFRWlTz/91GHbvLw8RUZGSpIiIyOVm5vbaH7AgAG67rrr1LFjR4fLiEVFRTp37pyioqJUV1enc%2BfOqbi4WCEhIZKkY8eOqVOnTmrTps1lj91U8fHxGjRokMOYxRKg0lJbs9a5HE/7FGL6/bvCx8dbbdtadeFCpWpr69xdjkehd66hf86jd665Vvvnrg/3bglY58%2Bf14QJE9SnTx%2BlpqbK2/v/gkJsbKyWLVumjRs3avz48Tpw4IC2b9%2BuNWvWSJLGjBmjpKQkDRs2TD169FB6errOnj2r2NhYSdKoUaO0du1adevWTcHBwVq0aJF69%2B6tm266SZLUo0cPLVq0SPPnz1dpaanWrFmjMWPGNOnYTRUaGtrocmBRUZlqaq6dX%2BhLaYnvv7a2rkXW5QnonWvon/PonWvo35XhVV9fX3%2BlD/rmm29qyZIlslqt8vLycpg7ePCgDh8%2BrNTUVH377bdq166dEhMTNWrUKPs27733ntauXaszZ84oIiJCs2fP1p133ilJqq6u1ssvv6y//vWvstlsiomJ0YIFC9S%2BfXtJUnFxsebPn6%2BsrCx5e3tr5MiRmjp1qv2G%2B8sd21lFRWWX36iZLBZvxabtNb7ur2VHSj93l2BnsXgrODhQpaU2/kfTTPTONfTPefTONddq/zp0aOOW47olYF2LCFgErKsFvXMN/XMevXPNtdo/dwUsz7qJBwAAwAMQsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADHMqYNXW1pquAwAA4KrhVMAaMGCA/vjHPyovL890PQAAAB7PqYD17LPP6osvvtDw4cM1duxYvf322yorKzNdGwAAgEdyKmA9/PDDevvtt/XBBx/orrvu0vr169W/f39NmTJF//u//2u6RgAAAI/i0k3uYWFhmjx5sj744AMlJSXpb3/7m5544gkNGjRIb775JvdqAQCAa5LFlZ0PHTqkv/zlL8rMzNTFixcVGxurUaNG6cyZM3r55Zd1%2BPBhrVixwlStAAAAHsGpgLVmzRq99957OnHihLp166bJkydr%2BPDhat26tX0bHx8fvfDCC8YKBQAA8BROBazNmzdrxIgRGjNmjCIiIi65TZcuXTR16lSXigMAAPBETgWsjz/%2BWOXl5Tp37px9LDMzU3379lVwcLAkqWvXruratauZKgEAADyIUze5/%2BMf/9DQoUOVkZFhH1u2bJni4uL07bffNnu9kpISxcbGKisryz42d%2B5c3X777YqOjrb//PPx1q9frwEDBqh79%2B5KSEjQd999Z5%2BrqKjQzJkzFRMTox49emj69Omy2Wz2%2BePHj2vChAmKjo5W//799eqrrzrUs2fPHsXFxal79%2B4aNmyYdu/e3ez3BAAArl1OBaw//vGPuueeezR58mT72EcffaQBAwZoyZIlzVrrwIEDio%2BP18mTJx3GDx8%2BrAULFujgwYP2n/j4eEnStm3btGnTJr3xxhvKysrSbbfdpuTkZNXX10uSFixYoNOnT2vnzp3atWuXTp8%2BrbS0NElSdXW1nn76aXXr1k1ZWVl67bXXlJ6erh07dkiS8vPzNWnSJD333HP6/PPPNWnSJKWkpOjMmTPOtAoAAFyDnApYR44c0VNPPSU/Pz/7mI%2BPj5566il9%2BeWXTV5n27Ztmjp1qkNQk6SLFy/q22%2B/1e23337J/d555x2NGzdOkZGRatWqlaZMmaKCggJlZWWpsrJS27dvV3JysoKCgtS%2BfXtNnTpVW7duVWVlpbKzs1VYWKjk5GT5%2Bfmpa9euSkhIUHp6ur2mnj17asiQIbJYLLr33nvVq1cvh7NnAAAA/4pT92C1bt1aJ0%2BeVOfOnR3Gf/jhB/n7%2Bzd5nf79%2BysuLk4Wi8UhZOXk5KimpkYrV67UgQMH1KZNG40ePVoTJ06Ut7e38vLy9OSTT9q39/X1VVhYmHJychQUFKTq6mpFRUXZ57t06aKqqirl5%2BcrNzdX4eHhDuEwIiJCr732miQpLy/PYd%2BG%2BZycnCa/r8LCQhUVFTmMWSwBCg0NbfIaTeHj41n/VrfF0nLqbeidp/WwJaB3rqF/zqN3rqF/V5ZTAWvo0KGaN2%2Be/vCHP%2BiOO%2B6Ql5eXDh8%2BrPnz5ys2NrbJ63To0OGS42VlZerdu7cSEhK0YsUKHT16VElJSfL29tbEiRNls9lktVod9vH391dFRYXKy8slSQEBAfa5hm1tNtsl97VaraqoqLBv80trN1VGRoZWr17tMJaUlKTk5OQmr3E1Cg4OdHcJjbRta738Rrgkeuca%2Buc8euca%2BndlOBWwpkyZolOnTunxxx%2BXl5eXfTw2NlbTp093uah%2B/fqpX79%2B9td33HGHJkyYoMzMTE2cOFFWq1VVVVUO%2B1RVVSkwMNAerCorKxUYGGj/b%2BmnM28BAQH21w3%2Bedt/tXZTxcfHa9CgQQ5jFkuASkttv7CHczztU4jp9%2B8KHx9vtW1r1YULlaqtrXN3OR6F3rmG/jmP3rnmWu2fuz7cOxWwrFar1q1bp%2BPHj%2Bubb76Rr6%2BvunTporCwMCNFffTRRyouLtZDDz1kH7t48aL98mNkZKRyc3M1cOBAST/duJ6fn6%2BoqCiFh4fL19dXeXl5uvPOOyVJx44ds19GPHv2rPLz81VTUyOL5ae3n5eXp8jISElSVFSUjhw54lBPXl7eL94PdimhoaGNLgcWFZWppuba%2BYW%2BlJb4/mtr61pkXZ6A3rmG/jmP3rmG/l0ZLp0CCQ8P1%2B9%2B9zsNHjzYWLiSpPr6ei1evFj79u1TfX29Dh48qLfeesv%2BLcLRo0dr8%2BbNysnJ0Y8//qjly5crJCREPXv2lNVq1bBhw5SWlqaSkhKVlJQoLS1Nw4cPl7%2B/v2JiYhQcHKzly5frxx9/VE5OjjZt2qQxY8ZIkkaMGKH9%2B/crMzNTNTU1yszM1P79%2B3X//fcbe38AAODq5tQZrOPHj2v%2B/Pk6cOCAqqurG80fPXrUpaJiY2M1c%2BZMzZs3T2fOnFFISIgmTZpkDzljxoxRWVmZkpKSVFJSom7dumndunXy9fWV9NMztJYuXaq4uDhVV1dr8ODBmjNnjiTJYrFow4YNmj9/vvr166eAgAAlJCRo1KhRkn66If6VV15RWlqaZs2apRtvvFGrVq1SeHi4S%2B8JAABcO7zqGx4e1QwTJkxQQUGBEhIS1KZNm0bzDzzwgJHiriZFRWXG17RYvBWbttf4ur%2BWHSn9Lr/RFWKxeCs4OFClpTZOlTcTvXMN/XMevXPNtdq/Dh0a55QrwakzWAcPHtSf/vQnRUdHm64HAADA4zl1D1ZwcHCzvlUHAABwLXEqYDU8n6qszPxlLwAAAE/n1CXCPXv26Msvv1RMTIzat2/v8FR0Sfrb3/5mpDgAAABP5FTAiomJUUxMjOlaAAAArgpOBaxnn33WdB0AAABXDacfNJqTk6OZM2fqoYce0pkzZ5Senq6srCyTtQEAAHgkpwLW119/rbFjx%2Br777/X119/rYsXL%2Bro0aN6/PHHtXv3btM1AgAAeBSnAlZaWpoef/xxbdq0yf709IULF%2BqRRx7R6tWrjRYIAADgaZw%2BgzVy5MhG4w8//LC%2B%2B%2B47l4sCAADwZE4FLF9fX5WXlzcaLygokNVqdbkoAAAAT%2BZUwBoyZIiWL1%2Bu0tJS%2B9ixY8eUmpqq3/72t6ZqAwAA8EhOBawZM2aoqqpKd911lyorKzVq1CgNHz5cFotF06dPN10jAACAR3HqOVitW7fW22%2B/rX379ukf//iH6urqFBUVpbvvvlve3k4/%2BQEAAOCq4FTAatC3b1/17dvXVC0AAABXBacC1qBBg%2BTl5fWL8/xbhAAA4FrmVMB64IEHHAJWdXW1Tpw4oY8//lgpKSnGigMAAPBETgWsSZMmXXJ88%2BbNOnDggB555BGXigIAAPBkRu9IHzhwoPbs2WNySQAAAI9jNGDt379frVq1MrkkAACAx3HqEuHPLwHW19ervLxc33zzDZcHAQDANc%2BpgHXDDTc0%2Bhahr6%2BvJkyYoLi4OCOFAQAAeCqnAtaSJUtM1wEAAHDVcCpgZWdnN3nbXr16OXMIAAAAj%2BVUwHr00UdVX19v/2nQcNmwYczLy0tHjx41UCYAAIDncCpgrVq1SosXL9aMGTPUp08f%2Bfr66tChQ5o3b57GjRungQMHmq4TAADAYzj1mIalS5dq7ty5GjJkiFq3bq1WrVqpd%2B/emj9/vjZs2KAbb7zR/gMAAHCtcSpgFRYW6vrrr2803rp1a5WWlrpcFAAAgCdzKmB1795dK1asUHl5uX3s3LlzWrZsmfr27WusOAAAAE/k1D1Ys2fP1oQJEzRgwACFhYVJko4fP64OHTrorbfeMlkfAACAx3EqYHXp0kWZmZnavn27jh07JkkaN26c7rvvPlmtVqMFAgAAeBqnApYktW3bVmPHjtX333%2Bvzp07S/rpae4AAADXOqfuwaqvr1daWpp69eql4cOH64cfftCMGTM0c%2BZMVVdXm64RAADAozgVsDZt2qT33ntPc%2BfOlZ%2BfnyRpyJAh%2Bvvf/66XX37ZaIEAAACexqmAlZGRoRdeeEGjRo2yP7393nvvVWpqqv77v//baIEAAACexqmA9f333%2Bvf/u3fGo3fcsstKi4udrkoAAAAT%2BZUwLrxxhv11VdfNRrfs2eP/YZ3AACAa5VT3yJ84okn9Ic//EFnzpxRfX299u3bp7ffflubNm3SzJkzTdcIAADgUZwKWKNHj1ZNTY3Wrl2rqqoqvfDCC2rfvr0mT56shx9%2B2HSNAAAAHsWpgPXXv/5Vv/vd7xQfH6%2BSkhLV19erffv2pmsDAADwSE7dg7Vw4UL7zezt2rUjXAEAAPwTpwJWWFiYvvnmG9O1AAAAXBWcukQYGRmpqVOn6vXXX1dYWJhatWrlML948WIjxQEAAHgipwLWyZMn1aNHD0lSUVGR0YIAAAA8XZMD1uLFi/Xcc88pICBAmzZt%2BjVrAgAA8GhNvgfrrbfeUmVlpcPYE088ocLCQuNFAQAAeLImB6z6%2BvpGY1988YV%2B/PFHowUBAAB4Oqe%2BRQgAAIBfRsACAAAwrFkBy8vL69eqAwAA4KrRrMc0LFy40OGZV9XV1Vq2bJkCAwMdtmvOc7BKSkoUHx%2BvhQsXKiYmRpJ06NAhLVy4UHl5eQoODtYzzzyjsWPH2vfZtm2b1qxZo6KiIt18882aM2eOoqOjJUm1tbVKS0vTe%2B%2B9p8rKSvXp00d/%2BMMfFBoaKkk6e/as5syZo/3798vHx0cjRozQjBkzZLFYmnRsAACAy2nyGaxevXqpqKhI33//vf0nOjpapaWlDmPff/99kw9%2B4MABxcfH6%2BTJk/ax8%2BfP66mnntLIkSOVnZ2t1NRULV68WF999ZUkKSsrSwsWLNCSJUuUnZ2tESNG6JlnnrF/w3Ht2rX69NNP9ec//1l79%2B6Vv7%2B/Zs%2BebV8/JSVFAQEB2rt3r7Zs2aJ9%2B/Zp48aNTTo2AABAUzT5DJbpZ19t27ZNK1eu1LRp0zR58mT7%2BK5duxQUFKTx48dLkvr27au4uDilp6frjjvu0Lvvvqv77rvP/qDTRx99VBkZGcrMzNTo0aP17rvvaurUqbr%2B%2BuslSbNmzVL//v116tQp1dXVaf/%2B/fr4449ltVrVuXNnJSYmatmyZZo4ceJljw0AANAUTj3J3YT%2B/fsrLi5OFovFIWDl5uYqKirKYduIiAht2bJFkpSXl6fRo0c3ms/JyVFZWZl%2B%2BOEHh/1DQkJ03XXX2f/txKCgIHXs2NE%2B36VLFxUUFOjChQuXPXZTFRYWNnrCvcUSYL9MaYqPj2d9R8FiaTn1NvTO03rYEtA719A/59E719C/K8ttAatDhw6XHLfZbLJarQ5j/v7%2BqqiouOy8zWaTJAUEBDSab5j7%2Bb4Nrxv2/1fHbqqMjAytXr3aYSwpKUnJycnNWudqExwcePmNrrC2ba2X3wiXRO9cQ/%2BcR%2B9cQ/%2BuDLcFrF9itVpVVlbmMFZVVWW/kd5qtaqqqqrRfHBwsD0c/fyJ8w3719fXN5preB0YGHjZYzdVfHy8Bg0a5DBmsQSotNTWrHUux9M%2BhZh%2B/67w8fFW27ZWXbhQqdraOneX41HonWvon/PonWuu1f6568N9iwtYUVFR%2BvTTTx3G8vLyFBkZKUmKjIxUbm5uo/kBAwbouuuuU8eOHZWXl2e/1FdUVKRz584pKipKdXV1OnfunIqLixUSEiJJOnbsmDp16qQ2bdpc9thNFRoa2uhyYFFRmWpqrp1f6Etpie%2B/trauRdblCeida%2Bif8%2Bida%2BjfldHiToHExsaquLhYGzduVHV1tT777DNt377dft/VmDFjtH37dn322Weqrq7Wxo0bdfbsWcXGxkqSRo0apbVr1%2BrUqVMqLy/XokWL1Lt3b910000KCwtTjx49tGjRIpWXl%2BvUqVNas2aNxowZ06RjAwAANEWLO4MVHBysDRs2KDU1VStXrlS7du00e/Zs9enTR9JP3%2BybO3eu5s2bpzNnzigiIkLr169XUFCQpJ/udaqpqdH48eNls9kUExOjl156yb7%2BypUrNX/%2BfA0ePFje3t4aOXKkEhMTm3QQhHH0AAAPl0lEQVRsAACApvCqv9S/4gzjiorKLr9RM1ks3opN22t83V/LjpR%2B7i7BzmLxVnBwoEpLbZwqbyZ65xr65zx655prtX8dOrRxy3Fb3CVCAAAAT0fAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMKzFBqzMzEx17dpV0dHR9p9p06ZJkvbs2aO4uDh1795dw4YN0%2B7dux32Xb9%2BvQYMGKDu3bsrISFB3333nX2uoqJCM2fOVExMjHr06KHp06fLZrPZ548fP64JEyYoOjpa/fv316uvvnpl3jAAALhqtNiAdfjwYd1///06ePCg/WfZsmXKz8/XpEmT9Nxzz%2Bnzzz/XpEmTlJKSojNnzkiStm3bpk2bNumNN95QVlaWbrvtNiUnJ6u%2Bvl6StGDBAp0%2BfVo7d%2B7Url27dPr0aaWlpUmSqqur9fTTT6tbt27KysrSa6%2B9pvT0dO3YscNtfQAAAJ6nRQes22%2B/vdH4tm3b1LNnTw0ZMkQWi0X33nuvevXqpYyMDEnSO%2B%2B8o3HjxikyMlKtWrXSlClTVFBQoKysLFVWVmr79u1KTk5WUFCQ2rdvr6lTp2rr1q2qrKxUdna2CgsLlZycLD8/P3Xt2lUJCQlKT0%2B/0m8fAAB4sBYZsOrq6nTkyBH9z//8jwYOHKgBAwZozpw5On/%2BvPLy8hQVFeWwfUREhHJyciSp0byvr6/CwsKUk5OjEydOqLq62mG%2BS5cuqqqqUn5%2BvnJzcxUeHi4/P79Lrg0AANAUFncXcCklJSXq2rWrhg4dqpUrV6q0tFQzZszQtGnTdPHiRVmtVoft/f39VVFRIUmy2Wy/OF9eXi5JCggIsM81bGuz2S65r9Vqta/dVIWFhSoqKnIYs1gCFBoa2qx1LsfHp0Xm419ksbSceht652k9bAnonWvon/PonWvo35XVIgNWSEiIw2U5q9WqadOm6cEHH1RMTIyqqqoctq%2BqqlJgYKB921%2BabwhWlZWV9u0rKyslSa1bt1ZAQID9dYN/3rapMjIytHr1aoexpKQkJScnN2udq01wcPP6eCW0bWu9/Ea4JHrnGvrnPHrnGvp3ZbTIgJWTk6P3339fU6ZMkZeXlyTp4sWL8vb21h133KGjR486bJ%2BXl2e/XysyMlK5ubkaOHCgpJ9uXM/Pz1dUVJTCw8Pl6%2BurvLw83XnnnZKkY8eO2S8jnj17Vvn5%2BaqpqZHFYrGvHRkZ2az64%2BPjNWjQIIcxiyVApaW2X9jDOZ72KcT0%2B3eFj4%2B32ra16sKFStXW1rm7HI9C71xD/5xH71xzrfbPXR/uW2TACgoKUnp6uq677jo99thjKiws1LJly/TAAw9o5MiR%2BtOf/qTMzEzdc8892rVrl/bv369Zs2ZJkkaPHq1Vq1ZpwIABCg8P14svvqiQkBD17NlTvr6%2BGjZsmNLS0vTyyy9LktLS0jR8%2BHD5%2B/srJiZGwcHBWr58uVJSUnT8%2BHFt2rRJkydPblb9oaGhjS4HFhWVqabm2vmFvpSW%2BP5ra%2BtaZF2egN65hv45j965hv5dGS0yYHXq1Enr1q3TihUrtHbtWrVq1Ur33Xefpk2bplatWumVV15RWlqaZs2apRtvvFGrVq1SeHi4JGnMmDEqKytTUlKSSkpK1K1bN61bt06%2Bvr6SpLlz52rp0qWKi4tTdXW1Bg8erDlz5kiSLBaLNmzYoPnz56tfv34KCAhQQkKCRo0a5bZeAAAAz%2BNV3/CAKPyqiorKjK9psXgrNm2v8XV/LTtS%2Brm7BDuLxVvBwYEqLbXxSa6Z6J1r6J/z6J1rrtX%2BdejQxi3H9aybeAAAADwAAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAtYlnD17VomJierZs6diYmKUmpqqmpoad5cFAAA8hMXdBbREKSkp6tixo/bu3avi4mI988wz2rhxoyZOnOju0jzasJc%2BdXcJzbIjpZ%2B7SwAAeCjOYP3MiRMntH//fk2bNk1Wq1WdO3dWYmKi0tPT3V0aAADwEASsn8nNzVVQUJA6duxoH%2BvSpYsKCgp04cIFN1YGAAA8BZcIf8Zms8lqtTqMNbyuqKhQ27ZtL7tGYWGhioqKHMYslgCFhoaaK1SSjw/5%2BNfkaZc0P5x69xU5TsPvHb9/zqF/zqN3rqF/VxYB62cCAgJUWVnpMNbwOjAwsElrZGRkaPXq1Q5jzz77rCZNmmSmyP%2BvsLBQEzrlKj4%2B3nh4u9oVFhYqIyOD3jmhsLBQf/rT6/TOSfTPefTONfTvyiLG/kxkZKTOnTun4uJi%2B9ixY8fUqVMntWnTpklrxMfHa%2BvWrQ4/8fHxxmstKirS6tWrG50tw%2BXRO%2BfRO9fQP%2BfRO9fQvyuLM1g/ExYWph49emjRokWaP3%2B%2BSktLtWbNGo0ZM6bJa4SGhvLpAACAaxhnsC5h5cqVqqmp0eDBg/Xggw/q7rvvVmJiorvLAgAAHoIzWJcQEhKilStXursMAADgoXzmzZs3z91FwHmBgYHq3bt3k2/Ax/%2Bhd86jd66hf86jd66hf1eOV319fb27iwAAALiacA8WAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACloc6e/asEhMT1bNnT8XExCg1NVU1NTXuLssj5OTk6LHHHlPv3r3Vr18/TZ8%2BXSUlJe4uy6PU1tYqISFB//mf/%2BnuUjzGuXPnNH36dMXExKhXr15KTExUYWGhu8vyGEeOHNH48ePVs2dP9e/fXwsXLtTFixfdXVaLVlJSotjYWGVlZdnHDh06pLFjxyo6OlqDBg3Su%2B%2B%2B68YKr24ELA%2BVkpKigIAA7d27V1u2bNG%2Bffu0ceNGd5fV4lVVVWnixImKjo7WJ598ovfff1/nzp3T888/7%2B7SPMrq1av1%2Beefu7sMjzJp0iRVVFToww8/1O7du%2BXj46M5c%2Ba4uyyPUFdXp9///vcaOnSo9u/fry1btuiTTz7R%2BvXr3V1ai3XgwAHFx8fr5MmT9rHz58/rqaee0siRI5Wdna3U1FQtXrxYX331lRsrvXoRsDzQiRMntH//fk2bNk1Wq1WdO3dWYmKi0tPT3V1ai1dQUKBbb71VSUlJ8vPzU3BwsOLj45Wdne3u0jzGvn37tGvXLt1zzz3uLsVjfP311zp06JCWLFmitm3bqnXr1lqwYIGmTp3q7tI8wvnz51VUVKS6ujo1/Otu3t7eslqtbq6sZdq2bZumTp2qyZMnO4zv2rVLQUFBGj9%2BvCwWi/r27au4uDj%2BdvxKCFgeKDc3V0FBQerYsaN9rEuXLiooKNCFCxfcWFnLd/PNN%2Bv111%2BXj4%2BPfWznzp267bbb3FiV5zh79qxmzZql5cuX88etGb766itFRETonXfeUWxsrPr376%2BlS5eqQ4cO7i7NIwQHB%2BvRRx/V0qVL1a1bN/3Hf/yHwsLC9Oijj7q7tBapf//%2B%2BvDDD3Xvvfc6jOfm5ioqKsphLCIiQjk5OVeyvGsGAcsD2Wy2Rn/cGl5XVFS4oySPVF9frxdffFG7d%2B/WrFmz3F1Oi1dXV6dp06bpscce06233urucjzK%2BfPn9c033yg/P1/btm3TX/7yF505c0YzZsxwd2keoa6uTv7%2B/pozZ46%2B/PJLvf/%2B%2Bzp27JhWrlzp7tJapA4dOshisTQav9TfDn9/f/5u/EoIWB4oICBAlZWVDmMNrwMDA91RkscpLy9XcnKytm/frs2bN%2BuWW25xd0kt3rp16%2BTn56eEhAR3l%2BJx/Pz8JEmzZs1S69atFRISopSUFO3Zs0c2m83N1bV8H374oXbu3Klx48bJz89PkZGRSkpK0n/913%2B5uzSPYrVaVVVV5TBWVVXF341fSeOIixYvMjJS586dU3FxsUJCQiRJx44dU6dOndSmTRs3V9fynTx5Uk8%2B%2BaRuuOEGbdmyRe3atXN3SR7hvffeU2FhoXr27ClJ9v9Rf/TRR9zwfhkRERGqq6tTdXW1WrVqJemnszKS7PcU4ZedPn260TcGLRaLfH193VSRZ4qKitKnn37qMJaXl6fIyEg3VXR14wyWBwoLC1OPHj20aNEilZeX69SpU1qzZo3GjBnj7tJavPPnz2vChAn693//d73xxhuEq2b44IMP9MUXX%2Bjzzz/X559/ruHDh2v48OGEqya466671LlzZz3//POy2WwqKSnRiy%2B%2BqCFDhqh169buLq/F69%2B/v4qKivTqq6%2BqtrZWp06d0tq1axUXF%2Bfu0jxKbGysiouLtXHjRlVXV%2Buzzz7T9u3bNXr0aHeXdlUiYHmolStXqqamRoMHD9aDDz6ou%2B%2B%2BW4mJie4uq8XbunWrCgoKtGPHDvXo0UPR0dH2H%2BDX4uvrq02bNsnHx0dDhw7V0KFD1alTJy1atMjdpXmEiIgIrVu3Tn//%2B98VExOjRx55RIMGDWr0LTn8a8HBwdqwYYM%2B%2BOADxcTEaPbs2Zo9e7b69Onj7tKuSl71nJ8GAAAwijNYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBh/w9wR/HzUf0OEQAAAABJRU5ErkJggg%3D%3D"/>
        </div>
        <div role="tabpanel" class="tab-pane col-md-12" id="common7415176150050136265">

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">0</td>
        <td class="number">223171</td>
        <td class="number">86.8%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">1</td>
        <td class="number">29547</td>
        <td class="number">11.5%</td>
        <td>
            <div class="bar" style="width:14%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">2</td>
        <td class="number">2987</td>
        <td class="number">1.2%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">3</td>
        <td class="number">791</td>
        <td class="number">0.3%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">4</td>
        <td class="number">275</td>
        <td class="number">0.1%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">5</td>
        <td class="number">125</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">6</td>
        <td class="number">42</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">7</td>
        <td class="number">16</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">8</td>
        <td class="number">12</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">9</td>
        <td class="number">10</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="other">
        <td class="fillremaining">Other values (2)</td>
        <td class="number">8</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr>
</table>
        </div>
        <div role="tabpanel" class="tab-pane col-md-12"  id="extreme7415176150050136265">
            <p class="h4">Minimum 5 values</p>

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">0</td>
        <td class="number">223171</td>
        <td class="number">86.8%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">1</td>
        <td class="number">29547</td>
        <td class="number">11.5%</td>
        <td>
            <div class="bar" style="width:14%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">2</td>
        <td class="number">2987</td>
        <td class="number">1.2%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">3</td>
        <td class="number">791</td>
        <td class="number">0.3%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">4</td>
        <td class="number">275</td>
        <td class="number">0.1%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr>
</table>
            <p class="h4">Maximum 5 values</p>

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">7</td>
        <td class="number">16</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">8</td>
        <td class="number">12</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:75%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">9</td>
        <td class="number">10</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:62%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">10</td>
        <td class="number">6</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:38%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">11</td>
        <td class="number">2</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:13%">&nbsp;</div>
        </td>
</tr>
</table>
        </div>
    </div>
</div>
</div><div class="row variablerow">
    <div class="col-md-3 namecol">
        <p class="h4 pp-anchor" id="pp_var_Number of Open Accounts">Number of Open Accounts<br/>
            <small>Numeric</small>
        </p>
    </div><div class="col-md-6">
    <div class="row">
        <div class="col-sm-6">
            <table class="stats ">
                <tr>
                    <th>Distinct count</th>
                    <td>59</td>
                </tr>
                <tr>
                    <th>Unique (%)</th>
                    <td>0.0%</td>
                </tr>
                <tr class="ignore">
                    <th>Missing (%)</th>
                    <td>0.0%</td>
                </tr>
                <tr class="ignore">
                    <th>Missing (n)</th>
                    <td>0</td>
                </tr>
                <tr class="ignore">
                    <th>Infinite (%)</th>
                    <td>0.0%</td>
                </tr>
                <tr class="ignore">
                    <th>Infinite (n)</th>
                    <td>0</td>
                </tr>
            </table>

        </div>
        <div class="col-sm-6">
            <table class="stats ">

                <tr>
                    <th>Mean</th>
                    <td>11.106</td>
                </tr>
                <tr>
                    <th>Minimum</th>
                    <td>0</td>
                </tr>
                <tr>
                    <th>Maximum</th>
                    <td>76</td>
                </tr>
                <tr class="ignore">
                    <th>Zeros (%)</th>
                    <td>0.0%</td>
                </tr>
            </table>
        </div>
    </div>
</div>
<div class="col-md-3 collapse in" id="minihistogram-6059613505534487769">
    <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAABLCAYAAAA1fMjoAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAPYQAAD2EBqD%2BnaQAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAARhJREFUeJzt3cEJwkAQQFEVS7IIe/JsTxZhT2sD8jHBmKjv3QNz%2BcxhYLMfY4wd8NRh7QFgy45rD/AOp8tt8jf363mBSfg1NggEgUAQCASBQBAIBIFAEAgEgUAQCASBQBAIBIFAEAgEgUAQCASBQBAIBIFAEAgEgUAQCASBQBAIBIFAEAgEgUAQCITNvc07551dWIoNAkEgEAQCQSAQBAJBIBAEAmFzd5BP8V9DXmGDQBAIBIFAEAgEgUAQCASBQBAIhL89FM4x9bjosPj9bBAI%2BzHGWHsI2CobBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBIJAIAgEgkAgCASCQCAIBMIDzuoS/K7Jg1IAAAAASUVORK5CYII%3D">

</div>
<div class="col-md-12 text-right">
    <a role="button" data-toggle="collapse" data-target="#descriptives-6059613505534487769,#minihistogram-6059613505534487769"
       aria-expanded="false" aria-controls="collapseExample">
        Toggle details
    </a>
</div>
<div class="row collapse col-md-12" id="descriptives-6059613505534487769">
    <ul class="nav nav-tabs" role="tablist">
        <li role="presentation" class="active"><a href="#quantiles-6059613505534487769"
                                                  aria-controls="quantiles-6059613505534487769" role="tab"
                                                  data-toggle="tab">Statistics</a></li>
        <li role="presentation"><a href="#histogram-6059613505534487769" aria-controls="histogram-6059613505534487769"
                                   role="tab" data-toggle="tab">Histogram</a></li>
        <li role="presentation"><a href="#common-6059613505534487769" aria-controls="common-6059613505534487769"
                                   role="tab" data-toggle="tab">Common Values</a></li>
        <li role="presentation"><a href="#extreme-6059613505534487769" aria-controls="extreme-6059613505534487769"
                                   role="tab" data-toggle="tab">Extreme Values</a></li>

    </ul>

    <div class="tab-content">
        <div role="tabpanel" class="tab-pane active row" id="quantiles-6059613505534487769">
            <div class="col-md-4 col-md-offset-1">
                <p class="h4">Quantile statistics</p>
                <table class="stats indent">
                    <tr>
                        <th>Minimum</th>
                        <td>0</td>
                    </tr>
                    <tr>
                        <th>5-th percentile</th>
                        <td>5</td>
                    </tr>
                    <tr>
                        <th>Q1</th>
                        <td>8</td>
                    </tr>
                    <tr>
                        <th>Median</th>
                        <td>10</td>
                    </tr>
                    <tr>
                        <th>Q3</th>
                        <td>14</td>
                    </tr>
                    <tr>
                        <th>95-th percentile</th>
                        <td>20</td>
                    </tr>
                    <tr>
                        <th>Maximum</th>
                        <td>76</td>
                    </tr>
                    <tr>
                        <th>Range</th>
                        <td>76</td>
                    </tr>
                    <tr>
                        <th>Interquartile range</th>
                        <td>6</td>
                    </tr>
                </table>
            </div>
            <div class="col-md-4 col-md-offset-2">
                <p class="h4">Descriptive statistics</p>
                <table class="stats indent">
                    <tr>
                        <th>Standard deviation</th>
                        <td>4.983</td>
                    </tr>
                    <tr>
                        <th>Coef of variation</th>
                        <td>0.44866</td>
                    </tr>
                    <tr>
                        <th>Kurtosis</th>
                        <td>2.9615</td>
                    </tr>
                    <tr>
                        <th>Mean</th>
                        <td>11.106</td>
                    </tr>
                    <tr>
                        <th>MAD</th>
                        <td>3.8126</td>
                    </tr>
                    <tr class="">
                        <th>Skewness</th>
                        <td>1.1784</td>
                    </tr>
                    <tr>
                        <th>Sum</th>
                        <td>2854133</td>
                    </tr>
                    <tr>
                        <th>Variance</th>
                        <td>24.83</td>
                    </tr>
                    <tr>
                        <th>Memory size</th>
                        <td>2.0 MiB</td>
                    </tr>
                </table>
            </div>
        </div>
        <div role="tabpanel" class="tab-pane col-md-8 col-md-offset-2" id="histogram-6059613505534487769">
            <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAlgAAAGQCAYAAAByNR6YAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAPYQAAD2EBqD%2BnaQAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAIABJREFUeJzt3Xt0VPW9//8XyQQzSYAMhoC66IKSRKtSiQmEW2kFIkUJ0hBMK03FtlhJJIYjlyJQKBguGhQRQUQpR8xZRtDUUiNgeyxQhCSghWobToLcbICEkECumMv%2B/cEv83UMSggbJjP7%2BVgrizWfz57Pfr9nj67X7L0z6WAYhiEAAACYxsfdBQAAAHgbAhYAAIDJCFgAAAAmI2ABAACYjIAFAABgMgIWAACAyQhYAAAAJiNgAQAAmIyABQAAYDICFgAAgMkIWAAAACYjYAEAAJiMgAUAAGAyAhYAAIDJCFgAAAAmI2ABAACYjIAFAABgMgIWAACAyQhYAAAAJiNgAQAAmIyABQAAYDICFgAAgMkIWAAAACYjYAEAAJiMgAUAAGAyAhYAAIDJCFgAAAAmI2ABAACYjIAFAABgMgIWAACAyQhYAAAAJiNgAQAAmIyABQAAYDICFgAAgMkIWAAAACYjYAEAAJiMgAUAAGAyAhYAAIDJCFgAAAAms7m7AKsoLa00fU0fnw7q2jVQZ89Wq6nJMH399sAKPUrW6JMevYcV%2BrRCj5I1%2BuzWrZNb9ssZLA/m49NBHTp0kI9PB3eXcs1YoUfJGn3So/ewQp9W6FGyTp/uQMACAAAwGQELAADAZAQsAAAAkxGwAAAATEbAAgAAMBkBCwAAwGQELAAAAJMRsAAAAExGwAIAADAZAQsAAMBkBCwAAACTEbAAAABMRsACAAAwmc3dBcA6Rq/Y7e4Srsj7aUPcXQIAwENxBgsAAMBkBCwAAACTEbAAAABMRsACAAAwGQELAADAZAQsAAAAkxGwAAAATEbAAgAAMBkBCwAAwGQELAAAAJMRsAAAAExGwAIAADAZAQsAAMBkBCwAAACTEbAAAABMRsACAAAwGQELAADAZAQsAAAAkxGwAAAATNYuAtbZs2cVGxur3NzcFnMlJSUaPHiw3nnnHZfxdevWadiwYerXr5%2BSkpL0%2BeefO%2Bdqamo0e/ZsxcTEKCoqSjNnzlR1dbVz/siRI3r44YcVGRmpoUOH6uWXX3ZZe8eOHYqLi1O/fv00evRoffjhhyZ3DAAAvJnbA9b%2B/fuVmJio48ePt5hramrS9OnTVV5e7jKenZ2tjRs36rXXXlNubq7uuOMOpaamyjAMSdKiRYt08uRJbdu2Tdu3b9fJkyeVkZEhSaqvr9djjz2mvn37Kjc3V6%2B88ooyMzP1/vvvS5KOHj2qqVOn6oknntC%2Bffs0depUpaWl6fTp09f4lQAAAN7CrQErOztb06dP17Rp0y45/9JLL6lHjx666aabXMbfeustPfTQQwoPD9cNN9ygJ598UsXFxcrNzVVtba22bNmi1NRUBQcH68Ybb9T06dP1zjvvqLa2Vvn5%2BSopKVFqaqo6duyo22%2B/XUlJScrMzHTWFB0drZEjR8pms%2Bm%2B%2B%2B5T//79lZWVdc1fDwAA4B1s7tz50KFDFRcXJ5vN1iJk7d27V%2B%2B9957efvttxcXFucwVFRVp8uTJzsd%2Bfn7q1auXCgoKFBwcrPr6ekVERDjn%2B/Tpo7q6Oh09elSFhYXq3bu3Onbs6JwPCwvTK6%2B84lz7q89tni8oKGh1XyUlJSotLXUZs9kCFBoa2uo1WsPX18flX5jLZrt%2Br6sVjiU9eg8r9GmFHiXr9OkObg1Y3bp1u%2BR4WVmZnnrqKa1cuVKBgYEt5qurq2W3213G/P39VVNTo6qqKklSQECAc6552%2Brq6ks%2B1263q6am5rJrt1ZWVpZWrVrlMpaSkqLU1NRWr3ElOne2X34jXDGHo%2BV771qzwrGkR%2B9hhT6t0KNknT6vJ7cGrEsxDEMzZ85UUlKS7rzzzktuY7fbVVdX5zJWV1enwMBAZ7Cqra11hrPa2lpJUlBQkAICApyPm311229bu7USExM1fPhwlzGbLUDl5dXf8Iy28fX1UefOdp0/X6vGxiZT14ZMP17fxgrHkh69hxX6tEKPkjX6dMeHZakdBqyTJ08qLy9PBw4c0EsvvSRJqqqq0u9//3tt27ZNa9euVXh4uAoLC3XPPfdIunjj%2BtGjRxUREaHevXvLz89PRUVFuuuuuyRJhw8fdl5GLCsr09GjR9XQ0CCb7WL7RUVFCg8PlyRFRETos88%2Bc6mpqKjoG8PepYSGhra4HFhaWqmGhmvz5m1sbLpma1uZO15TKxxLevQeVujTCj1K1unzemp3F11vvvlm/fOf/9S%2BffucPzfffLPmz5%2BvtWvXSpLGjx%2BvN954QwUFBbpw4YKWL1%2BukJAQRUdHy263a/To0crIyNDZs2d19uxZZWRkaMyYMfL391dMTIwcDoeWL1%2BuCxcuqKCgQBs3blRCQoIkaezYscrLy1NOTo4aGhqUk5OjvLw8PfDAA%2B58WQAAgAdpd2ewWiMhIUGVlZVKSUnR2bNn1bdvX61du1Z%2Bfn6SpPnz52vZsmWKi4tTfX29RowYoXnz5kmSbDab1q9fr4ULF2rIkCEKCAhQUlKS4uPjJV28If6ll15SRkaG5syZo1tuuUUvvviievfu7bZ%2BAQCAZ%2BlgNH95FK6p0tJK09e02XzkcASqvLzaI07tjl6x290lXJH304Zct3152rFsC3r0Hlbo0wo9Stbos1u3Tm7Zb7u7RAgAAODpCFgAAAAmI2ABAACYjIAFAABgMgIWAACAyQhYAAAAJiNgAQAAmIyABQAAYDICFgAAgMkIWAAAACYjYAEAAJiMgAUAAGAyAhYAAIDJCFgAAAAmI2ABAACYjIAFAABgMgIWAACAyQhYAAAAJiNgAQAAmIyABQAAYDICFgAAgMkIWAAAACYjYAEAAJiMgAUAAGAyAhYAAIDJCFgAAAAmI2ABAACYjIAFAABgMgIWAACAyQhYAAAAJnN7wDp79qxiY2OVm5vrHNu2bZseeOAB3X333Ro%2BfLhWrVqlpqYm53x2drZiY2PVr18/xcfH65NPPnHONTY2atmyZRo8eLAiIyM1ZcoUlZSUOOfLysqUnJys6OhoxcTEKD09XQ0NDc75AwcOaMKECYqMjNTw4cO1adOma/wKAAAAb%2BPWgLV//34lJibq%2BPHjzrFPP/1UM2fOVFpamvbt26d169bpnXfe0YYNGyRJubm5WrRokZYuXar8/HyNHTtWU6ZMUW1trSRpzZo12r17t95%2B%2B23t2rVL/v7%2Bmjt3rnP9tLQ0BQQEaNeuXdq8ebP27NnjXPvcuXN69NFHNW7cOOXn5ys9PV1LlizRwYMHr9trAgAAPJ/bAlZ2dramT5%2BuadOmuYz/5z//0U9/%2BlPdc8898vHxUZ8%2BfRQbG6v8/HxJ0qZNm3T//fcrKipKfn5%2BmjRpkhwOh3JycpzzkydP1k033aSgoCDNmTNHO3fu1IkTJ3Ts2DHl5eVpxowZstvt6tmzp5KTk5WZmSlJ2r59u4KDgzVx4kTZbDYNGjRIcXFxznkAAIDWsLlrx0OHDlVcXJxsNptLyBo1apRGjRrlfFxXV6e//e1viouLkyQVFRVp/PjxLmuFhYWpoKBAlZWVOnXqlCIiIpxzISEh6tKliw4dOiRJCg4OVvfu3Z3zffr0UXFxsc6fP6/CwkKX5zavvXnz5ivqraSkRKWlpS5jNluAQkNDr2idy/H19XH5F%2Bay2a7f62qFY0mP3sMKfVqhR8k6fbqD2wJWt27dLrtNVVWVnnjiCfn7%2B2vSpEmSpOrqatntdpft/P39VVNTo%2BrqaklSQEBAi/nmua8/t/lx8/O/ae0rkZWVpVWrVrmMpaSkKDU19YrWaa3One2X3whXzOEIvO77tMKxpEfvYYU%2BrdCjZJ0%2Brye3BazL%2Bfzzz5Wamqobb7xRr7/%2BuoKCgiRdDER1dXUu29bV1cnhcDjDUfP9WF%2BdDwwMlGEYLeaaHwcGBsput6uysvKSz70SiYmJGj58uMuYzRag8vLqK1rncnx9fdS5s13nz9eqsbHp8k/AFTH7eH0bKxxLevQeVujTCj1K1ujTHR%2BWpXYasHbs2KH/%2Bq//0oMPPqgnn3xSNtv/KzM8PFyFhYUu2xcVFWnYsGHq0qWLunfvrqKiIuelvtLSUlVUVCgiIkJNTU2qqKjQmTNnFBISIkk6fPiwevTooU6dOikiIkK7d%2B9usXZ4ePgV1R8aGtricmBpaaUaGq7Nm7exsemarW1l7nhNrXAs6dF7WKFPK/QoWafP66ndXXT9xz/%2BoZSUFM2ePVuzZs1yCVeSlJCQoC1btmjv3r2qr6/Xhg0bVFZWptjYWElSfHy81qxZoxMnTqiqqkqLFy/WgAED9J3vfEe9evVSVFSUFi9erKqqKp04cUKrV69WQkKCJCk2NlZnzpzRhg0bVF9fr71792rLli0t7vkCAAD4Nu3uDNbLL7%2BshoYGpaenKz093TkeFRWlV199VYMGDdL8%2BfO1YMECnT59WmFhYVq3bp2Cg4MlXbzXqaGhQRMnTlR1dbViYmK0YsUK5zorV67UwoULNWLECPn4%2BGjcuHFKTk6WJDkcDq1fv17p6elauXKlunbtqrlz52rgwIHX90UAAAAerYNhGIa7i7CC0tLKy290hWw2HzkcgSovr/aIU7ujV%2By%2B/EbtyPtpQ67bvjztWLYFPXoPK/RphR4la/TZrVsnt%2By33V0iBAAA8HQELAAAAJMRsAAAAExGwAIAADAZAQsAAMBkBCwAAACTEbAAAABMRsACAAAwGQELAADAZAQsAAAAkxGwAAAATEbAAgAAMBkBCwAAwGQELAAAAJMRsAAAAExGwAIAADAZAQsAAMBkBCwAAACTEbAAAABMRsACAAAwGQELAADAZAQsAAAAkxGwAAAATEbAAgAAMBkBCwAAwGQELAAAAJMRsAAAAExGwAIAADAZAQsAAMBkBCwAAACTuT1gnT17VrGxscrNzXWOHThwQBMmTFBkZKSGDx%2BuTZs2uTwnOztbsbGx6tevn%2BLj4/XJJ5845xobG7Vs2TINHjxYkZGRmjJlikpKSpzzZWVlSk5OVnR0tGJiYpSenq6GhoZW7xsAAOBy3Bqw9u/fr8TERB0/ftw5du7cOT366KMaN26c8vPzlZ6eriVLlujgwYOSpNzcXC1atEhLly5Vfn6%2Bxo4dqylTpqi2tlaStGbNGu3evVtvv/22du3aJX9/f82dO9e5flpamgICArRr1y5t3rxZe/bs0YYNG1q1bwAAgNZwW8DKzs7W9OnTNW3aNJfx7du3Kzg4WBMnTpTNZtOgQYMUFxenzMxMSdKmTZt0//33KyoqSn5%2Bfpo0aZIcDodycnKc85MnT9ZNN92koKAgzZkzRzt37tSJEyd07Ngx5eXlacaMGbLb7erZs6eSk5Oda19u3wAAAK1hc9eOhw4dqri4ONlsNpeQVVhYqIiICJdtw8LCtHnzZklSUVGRxo8f32K%2BoKBAlZWVOnXqlMvzQ0JC1KVLFx06dEiSFBwcrO7duzvn%2B/Tpo%2BLiYp0/f/6y%2B26tkpISlZaWuozZbAEKDQ29onUux9fXx%2BVfmMtmu36vqxWOJT16Dyv0aYUeJev06Q5uC1jdunW75Hh1dbXsdrvLmL%2B/v2pqai47X11dLUkKCAhoMd889/XnNj9ufv637bu1srKytGrVKpexlJQUpaamXtE6rdW5s/3yG%2BGKORyB132fVjiW9Og9rNCnFXqUrNPn9eS2gPVN7Ha7KisrXcbq6uoUGBjonK%2Brq2sx73A4nOGo%2BX6srz/fMIwWc82PAwMDL7vv1kpMTNTw4cNdxmy2AJWXV1/ROpfj6%2Bujzp3tOn%2B%2BVo2NTaauDZl%2BvL6NFY4lPXoPK/RphR4la/Tpjg/LUjsMWBEREdq9e7fLWFFRkcLDwyVJ4eHhKiwsbDE/bNgwdenSRd27d1dRUZHzUl9paakqKioUERGhpqYmVVRU6MyZMwoJCZEkHT58WD169FCnTp0uu%2B/WCg0NbXE5sLS0Ug0N1%2BbN29jYdM3WtjJ3vKZWOJb06D2s0KcVepSs0%2Bf11O4uusbGxurMmTPasGGD6uvrtXfvXm3ZssV531VCQoK2bNmivXv3qr6%2BXhs2bFBZWZliY2MlSfHx8VqzZo1OnDihqqoqLV68WAMGDNB3vvMd9erVS1FRUVq8eLGqqqp04sQJrV69WgkJCa3aNwAAQGu0uzNYDodD69evV3p6ulauXKmuXbtq7ty5GjhwoCRp0KBBmj9/vhYsWKDTp08rLCxM69atU3BwsKSL9zo1NDRo4sSJqq6uVkxMjFasWOFcf%2BXKlVq4cKFGjBghHx8fjRs3TsnJya3aNwAAQGt0MAzDcHcRVlBaWnn5ja6QzeYjhyNQ5eXVHnFqd/SK3ZffqB15P23IdduXpx3LtqBH72GFPq3Qo2SNPrt16%2BSW/ba7S4QAAACerk0Bq7Gx0ew6AAAAvEabAtawYcP0zDPPqKioyOx6AAAAPF6bAtbjjz%2Bujz/%2BWGPGjNGECRP05ptvtvj%2BKAAAAKtqU8D62c9%2BpjfffFNbt27V4MGDtW7dOg0dOlRPPvmkPvroI7NrBAAA8ChXdZN7r169NG3aNG3dulUpKSn661//ql/96lcaPny4/vCHP3CvFgAAsKSr%2Bh6sAwcO6I9//KNycnL05ZdfKjY2VvHx8Tp9%2BrReeOEF/fOf/9Rzzz1nVq0AAAAeoU0Ba/Xq1Xr33Xd17Ngx9e3bV9OmTdOYMWMUFBTk3MbX11e/%2B93vTCsUAADAU7QpYL3xxhsaO3asEhISFBYWdslt%2BvTpo%2BnTp19VcQAAAJ6oTQFr586dqqqqUkVFhXMsJydHgwYNksPhkCTdfvvtuv32282pEgAAwIO06Sb3f/3rXxo1apSysrKcY88%2B%2B6zi4uL0f//3f6YVBwAA4InaFLCeeeYZ3XvvvZo2bZpz7C9/%2BYuGDRumpUuXmlYcAACAJ2pTwPrss8/06KOPqmPHjs4xX19fPfroo/rHP/5hWnEAAACeqE0BKygoSMePH28xfurUKfn7%2B191UQAAAJ6sTQFr1KhRWrBggT766CNVVVWpurpae/fu1cKFCxUbG2t2jQAAAB6lTb9F%2BOSTT%2BrEiRP65S9/qQ4dOjjHY2NjNXPmTNOKAwAA8ERtClh2u11r167VkSNHdOjQIfn5%2BalPnz7q1auXyeUBAAB4nqv6Uzm9e/dW7969zaoFAADAK7QpYB05ckQLFy7U/v37VV9f32L%2B3//%2B91UXBgAA4KnaFLAWLFig4uJiTZ8%2BXZ06dTK7JgAAAI/WpoD1ySef6L//%2B78VGRlpdj0AAAAer01f0%2BBwOBQYGGh2LQAAAF6hTQErKSlJzz33nCorK82uBwAAwOO16RLhjh079I9//EMxMTG68cYbXf5kjiT99a9/NaU4AAAAT9SmgBUTE6OYmBizawEAAPAKbQpYjz/%2BuNl1AAAAeI023YMlSQUFBZo9e7Z%2B%2BtOf6vTp08rMzFRubq6ZtQEAAHikNgWsTz/9VBMmTNAXX3yhTz/9VF9%2B%2BaX%2B/e9/65e//KU%2B/PBDs2sEAADwKG0KWBkZGfrlL3%2BpjRs3ys/PT5L09NNP6xe/%2BIVWrVplaoEAAACeps1nsMaNG9di/Gc/%2B5k%2B//zzqy4KAADAk7UpYPn5%2BamqqqrFeHFxsex2%2B1UXJUmfffaZJk6cqOjoaA0dOlRPP/20vvzyS0kXvyYiLi5O/fr10%2BjRo1tclly3bp2GDRumfv36KSkpySX01dTUaPbs2YqJiVFUVJRmzpyp6upq5/yRI0f08MMPKzIyUkOHDtXLL79sSj8AAMA62hSwRo4cqeXLl6u8vNw5dvjwYaWnp%2BtHP/rRVRfV1NSk3/zmNxo1apTy8vK0efNm/f3vf9e6det09OhRTZ06VU888YT27dunqVOnKi0tTadPn5YkZWdna%2BPGjXrttdeUm5urO%2B64Q6mpqTIMQ5K0aNEinTx5Utu2bdP27dt18uRJZWRkSJLq6%2Bv12GOPqW/fvsrNzdUrr7yizMxMvf/%2B%2B1fdEwAAsI42BaxZs2aprq5OgwcPVm1treLj4zVmzBjZbDbNnDnzqos6d%2B6cSktL1dTU5AxGPj4%2Bstvtys7OVnR0tEaOHCmbzab77rtP/fv3V1ZWliTprbfe0kMPPaTw8HDdcMMNevLJJ1VcXKzc3FzV1tZqy5YtSk1NVXBwsG688UZNnz5d77zzjmpra5Wfn6%2BSkhKlpqaqY8eOuv3225WUlKTMzMyr7gkAAFhHm74HKygoSG%2B%2B%2Bab27Nmjf/3rX2pqalJERIR%2B8IMfyMenzd/84ORwODRp0iQtW7ZMzzzzjBobGzVixAhNmjRJU6dOVUREhMv2YWFhKigokCQVFRVp8uTJzjk/Pz/16tVLBQUFCg4OVn19vcvz%2B/Tpo7q6Oh09elSFhYXq3bu3yzfTh4WF6ZVXXrnqngAAgHW0KWA1GzRokAYNGmRWLU5NTU3y9/fXvHnzlJCQoGPHjunxxx/XypUrVV1d3eI%2BL39/f9XU1EjSt8433zcWEBDgnGvetrq6%2BpLPtdvtzrVbq6SkRKWlpS5jNluAQkNDr2idy/H19XH5F%2Bay2a7f62qFY0mP3sMKfVqhR8k6fbpDmwLW8OHD1aFDh2%2Bcv9q/RfjBBx9o27Zt2rp1qyQpPDxcKSkpSk9P19133626ujqX7evq6hQYGCjpYiD6pvnmYFVbW%2Bvcvra2VtLFs3IBAQHOx82%2Bum1rZWVltfi6ipSUFKWmpl7ROq3VubM5v1gAVw7HlR13M1jhWNKj97BCn1boUbJOn9dTmwLWT37yE5eAVV9fr2PHjmnnzp1KS0u76qJOnjzp/I3BZjabTX5%2BfoqIiNBnn33mMldUVKQ777xT0sUwVlhYqHvuucdZ29GjRxUREaHevXvLz89PRUVFuuuuuyRdvDm/%2BTJiWVmZjh49qoaGBtlsNufa4eHhV1R/YmKihg8f/rX6A1ReXv0Nz2gbX18fde5s1/nztWpsbDJ1bcj04/VtrHAs6dF7WKFPK/QoWaNPd3xYltoYsKZOnXrJ8TfeeEP79%2B/XL37xi6sqaujQoVq%2BfLlefvllTZ48WcXFxVqzZo3i4uI0duxY/eEPf1BOTo7uvfdebd%2B%2BXXl5eZozZ44kafz48XrxxRc1bNgw9e7dW88//7xCQkIUHR0tPz8/jR49WhkZGXrhhRckXfzS1DFjxsjf318xMTFyOBxavny50tLSdOTIEW3cuFHTpk27ovpDQ0NbXA4sLa1UQ8O1efM2NjZds7WtzB2vqRWOJT16Dyv0aYUeJev0eT1d1T1YX3fPPffoueeeu%2Bp1wsLCtHbtWq1YsUKvvvqqOnXqpLFjxyolJUUdO3bUSy%2B9pIyMDM2ZM0e33HKLXnzxRfXu3VuSlJCQoMrKSqWkpOjs2bPq27ev1q5d6/zG%2Bfnz52vZsmWKi4tTfX29RowYoXnz5km6eJZs/fr1WrhwoYYMGaKAgAAlJSUpPj7%2BqnsCAADW0cFo/h4EE2RnZ%2BuZZ57Rnj17zFrSa5SWVpq%2Bps3mI4cjUOXl1R7xyWP0it3uLuGKvJ825Lrty9OOZVvQo/ewQp9W6FGyRp/dunVyy37bdAbr65cADcNQVVWVDh06dNWXBwEAADxdmwLWzTff3OK3CP38/PTwww8rLi7OlMIAAAA8VZsC1tKlS82uAwAAwGu0KWDl5%2Be3etv%2B/fu3ZRcAAAAeq00Ba9KkSTIMw/nTrPmyYfNYhw4d9O9//9uEMgEAADxHmwLWiy%2B%2BqCVLlmjWrFkaOHCg/Pz8dODAAS1YsEAPPfSQ80s%2BAQAArKhNf3xo2bJlmj9/vkaOHKmgoCDdcMMNGjBggBYuXKj169frlltucf4AAABYTZsCVklJiW666aYW40FBQSovL7/qogAAADxZmwJWv3799Nxzz6mqqso5VlFRoWeffVaDBg0yrTgAAABP1KZ7sObOnauHH35Yw4YNU69evSRJR44cUbdu3fT666%2BbWR8AAIDHaVPA6tOnj3JycrRlyxYdPnxYkvTQQw/p/vvvl91uN7VAAAAAT9PmP/bcuXNnTZgwQV988YV69uwpSc4/qAwAAGBlbboHyzAMZWRkqH///hozZoxOnTqlWbNmafbs2aqvrze7RgAAAI/SpoC1ceNGvfvuu5o/f746duwoSRo5cqT%2B93//Vy%2B88IKpBQIAAHiaNgWsrKws/e53v1N8fLzz29vvu%2B8%2Bpaen67333jO1QAAAAE/TpoD1xRdf6Hvf%2B16L8VtvvVVnzpy56qIAAAA8WZsC1i233KKDBw%2B2GN%2BxY4fzhncAAACratNvEf7qV7/S73//e50%2BfVqGYWjPnj168803tXHjRs2ePdvsGgEAADxKmwLW%2BPHj1dDQoDVr1qiurk6/%2B93vdOONN2ratGn62c9%2BZnaNAAAAHqVNAetPf/qTfvzjHysxMVFnz56VYRi68cYbza4NAADAI7XpHqynn37aeTN7165dCVcAAABf0aaA1atXLx06dMjsWgAAALxCmy4RhoeHa/r06Xr11VfVq1cv3XDDDS7zS5YsMaU4AAAAT9SmgHX8%2BHFFRUVJkkpLS00tCAAAwNO1OmAtWbJETzzxhAICArRx48ZrWRMAAIBHa/U9WK%2B//rpqa2tdxn71q1%2BppKTE9KIAAAA8WasDlmEYLcY%2B/vhjXbhwwdSCAAAAPF2bfosQAAAA34yABQAAYLIrClgdOnS4VnUAAAB4jSv6moann37a5Tuv6uvr9eyzzyowMNBlOzO%2BB6uiokKLFy/Wjh071NTUpP79%2B2vBggUKDQ3VgQMH9PTTT6uoqEgOh0NTpkzRhAkTnM/Nzs7W6tWrVVpaqu9%2B97uaN2%2BeIiMjJUmNjY3KyMjQu%2B%2B%2Bq9raWg0cOFC///3vFRoaKkkqKyvTvHnzlJeXJ19fX40dO1azZs2Szdamb7S45qLnbHV3CQAA4GtafQarf//%2BKi0t1RdffOH8iYyMVHl5ucvYF198YUphU6dOVU1NjT744AN9%2BOGH8vX11bx583Tu3Dl7i9fbAAAaPUlEQVQ9%2BuijGjdunPLz85Wenq4lS5bo4MGDkqTc3FwtWrRIS5cuVX5%2BvsaOHaspU6Y4fwNyzZo12r17t95%2B%2B23t2rVL/v7%2Bmjt3rnO/aWlpCggI0K5du7R582bt2bNHGzZsMKUnAABgDa0%2BLXM9v/vq008/1YEDB/TRRx8pKChIkrRo0SKVlpZq%2B/btCg4O1sSJEyVJgwYNUlxcnDIzM/X9739fmzZt0v333%2B/8ItRJkyYpKytLOTk5Gj9%2BvDZt2qTp06frpptukiTNmTNHQ4cO1YkTJ9TU1KS8vDzt3LlTdrtdPXv2VHJysp599ln9%2Bte/vm79AwAAz9Yub3I/ePCgwsLC9NZbbyk2NlZDhw7VsmXL1K1bNxUWFioiIsJl%2B7CwMBUUFEiSioqKvnG%2BsrJSp06dcpkPCQlRly5ddOjQIRUWFio4OFjdu3d3zvfp00fFxcU6f/78NewYAAB4k3Z5Y9G5c%2Bd06NAh3XnnncrOzlZdXZ1mzpypWbNmKSQkRHa73WV7f39/1dTUSJKqq6u/cb66ulqSFBAQ0GK%2Bee7rz21%2BXFNTo86dO7eq/pKSkhZ/QshmC3De52UWX992mY%2B9hs12/V7f5mPpzceUHr2HFfq0Qo%2BSdfp0h3YZsDp27Cjp4uW7G264QUFBQUpLS9ODDz6o%2BPh41dXVuWxfV1fnvNHebrdfct7hcDjD0te/kb75%2BYZhtJhrfvz1G/m/TVZWllatWuUylpKSotTU1FavAfdzOFp/zM3SubP98ht5OHr0Hlbo0wo9Stbp83pqlwErLCxMTU1Nqq%2Bvd/7WYlNTkyTpe9/7nv7nf/7HZfuioiKFh4dLksLDw1VYWNhiftiwYerSpYu6d%2B/uchmxtLRUFRUVioiIUFNTkyoqKnTmzBmFhIRIkg4fPqwePXqoU6dOra4/MTFRw4cPdxmz2QJUXl59Ba/C5fGJ49oy%2B3h9G19fH3XubNf587VqbGy6bvu9nujRe1ihTyv0KFmjT3d8WJbaacAaPHiwevbsqaeeekpLlizRhQsX9Pzzz2vkyJEaM2aMVq5cqQ0bNmjixInav3%2B/tmzZotWrV0uSEhISlJKSotGjRysqKkqZmZkqKytTbGysJCk%2BPl5r1qxR37595XA4tHjxYg0YMEDf%2Bc53JElRUVFavHixFi5cqPLycq1evVoJCQlXVH9oaGiLy4GlpZVqaPDON6%2B3csfxamxs8vr3CT16Dyv0aYUeJev0eT21y1Mgfn5%2B2rhxo3x9fTVq1CiNGjVKPXr00OLFi%2BVwOLR%2B/Xpt3bpVMTExmjt3rubOnauBAwdKuvhbhfPnz9eCBQs0YMAAvffee1q3bp2Cg4MlXbxU98Mf/lATJ07UD3/4Q124cEErVqxw7nvlypVqaGjQiBEj9OCDD%2BoHP/iBkpOT3fI6AAAAz9TBuNRfcYbpSksrTV/TZvNRbMYu09fFRe%2BnDblu%2B7LZfORwBKq8vNprP0XSo/ewQp9W6FGyRp/durX%2BFh8ztcszWAAAAJ6MgAUAAGAyAhYAAIDJCFgAAAAmI2ABAACYjIAFAABgMgIWAACAyQhYAAAAJiNgAQAAmIyABQAAYDICFgAAgMkIWAAAACYjYAEAAJiMgAUAAGAyAhYAAIDJCFgAAAAmI2ABAACYjIAFAABgMgIWAACAyQhYAAAAJiNgAQAAmIyABQAAYDICFgAAgMkIWAAAACYjYAEAAJiMgAUAAGAyAhYAAIDJCFgAAAAmI2ABAACYjIAFAABgsnYfsBobG5WUlKTf/va3zrEdO3YoLi5O/fr10%2BjRo/Xhhx%2B6PGfdunUaNmyY%2BvXrp6SkJH3%2B%2BefOuZqaGs2ePVsxMTGKiorSzJkzVV1d7Zw/cuSIHn74YUVGRmro0KF6%2BeWXr32TAADAq7T7gLVq1Srt27fP%2Bfjo0aOaOnWqnnjiCe3bt09Tp05VWlqaTp8%2BLUnKzs7Wxo0b9dprryk3N1d33HGHUlNTZRiGJGnRokU6efKktm3bpu3bt%2BvkyZPKyMiQJNXX1%2Buxxx5T3759lZubq1deeUWZmZl6//33r3/jAADAY7XrgLVnzx5t375d9957r3MsOztb0dHRGjlypGw2m%2B677z71799fWVlZkqS33npLDz30kMLDw3XDDTfoySefVHFxsXJzc1VbW6stW7YoNTVVwcHBuvHGGzV9%2BnS98847qq2tVX5%2BvkpKSpSamqqOHTvq9ttvV1JSkjIzM931EgAAAA/UbgNWWVmZ5syZo%2BXLl8tutzvHi4qKFBER4bJtWFiYCgoKLjnv5%2BenXr16qaCgQMeOHVN9fb3LfJ8%2BfVRXV6ejR4%2BqsLBQvXv3VseOHS%2B5NgAAQGvY3F3ApTQ1NWnGjBl65JFHdNttt7nMVVdXuwQuSfL391dNTc1l56uqqiRJAQEBzrnmbaurqy/5XLvd7ly7tUpKSlRaWuoyZrMFKDQ09IrWuRxf33abj72CzXb9Xt/mY%2BnNx5QevYcV%2BrRCj5J1%2BnSHdhmw1q5dq44dOyopKanFnN1uV11dnctYXV2dAgMDLzvfHKxqa2ud29fW1kqSgoKCFBAQ4Hzc7KvbtlZWVpZWrVrlMpaSkqLU1NQrWgfu5XBc2XE3Q%2BfO9stv5OHo0XtYoU8r9ChZp8/rqV0GrHfffVclJSWKjo6WJGdg%2Bstf/qKJEyfqs88%2Bc9m%2BqKhId955pyQpPDxchYWFuueeeyRdvHH96NGjioiIUO/eveXn56eioiLdddddkqTDhw87LyOWlZXp6NGjamhokM1mc64dHh5%2BRfUnJiZq%2BPDhLmM2W4DKy6u/4RltwyeOa8vs4/VtfH191LmzXefP16qxsem67fd6okfvYYU%2BrdCjZI0%2B3fFhWWqnAWvr1q0uj5u/omHp0qU6fPiw/vCHPygnJ0f33nuvtm/frry8PM2ZM0eSNH78eL344osaNmyYevfureeff14hISGKjo6Wn5%2BfRo8erYyMDL3wwguSpIyMDI0ZM0b%2B/v6KiYmRw%2BHQ8uXLlZaWpiNHjmjjxo2aNm3aFdUfGhra4nJgaWmlGhq8883rrdxxvBobm7z%2BfUKP3sMKfVqhR8k6fV5P7TJgfZs%2BffropZdeUkZGhubMmaNbbrlFL774onr37i1JSkhIUGVlpVJSUnT27Fn17dtXa9eulZ%2BfnyRp/vz5WrZsmeLi4lRfX68RI0Zo3rx5kiSbzab169dr4cKFGjJkiAICApSUlKT4%2BHi39QsAADxPB6P5C6JwTZWWVpq%2Bps3mo9iMXaavi4veTxty3fZls/nI4QhUeXm1136KpEfvYYU%2BrdCjZI0%2Bu3Xr5Jb9chMPAACAyQhYAAAAJiNgAQAAmIyABQAAYDKP%2By1C4HoZvWK3u0u4ItfzpnwAwLfjDBYAAIDJCFgAAAAmI2ABAACYjIAFAABgMgIWAACAyQhYAAAAJiNgAQAAmIyABQAAYDICFgAAgMkIWAAAACYjYAEAAJiMgAUAAGAyAhYAAIDJCFgAAAAmI2ABAACYjIAFAABgMgIWAACAyQhYAAAAJiNgAQAAmIyABQAAYDICFgAAgMkIWAAAACYjYAEAAJiMgAUAAGAyAhYAAIDJ2m3AKigo0COPPKIBAwZoyJAhmjlzps6ePStJOnDggCZMmKDIyEgNHz5cmzZtcnludna2YmNj1a9fP8XHx%2BuTTz5xzjU2NmrZsmUaPHiwIiMjNWXKFJWUlDjny8rKlJycrOjoaMXExCg9PV0NDQ3Xp2kAAOAV2mXAqqur069//WtFRkbq73//u/785z%2BroqJCTz31lM6dO6dHH31U48aNU35%2BvtLT07VkyRIdPHhQkpSbm6tFixZp6dKlys/P19ixYzVlyhTV1tZKktasWaPdu3fr7bff1q5du%2BTv76%2B5c%2Bc6952WlqaAgADt2rVLmzdv1p49e7RhwwZ3vAwAAMBDtcuAVVxcrNtuu00pKSnq2LGjHA6HEhMTlZ%2Bfr%2B3btys4OFgTJ06UzWbToEGDFBcXp8zMTEnSpk2bdP/99ysqKkp%2Bfn6aNGmSHA6HcnJynPOTJ0/WTTfdpKCgIM2ZM0c7d%2B7UiRMndOzYMeXl5WnGjBmy2%2B3q2bOnkpOTnWsDAAC0RrsMWN/97nf16quvytfX1zm2bds23XHHHSosLFRERITL9mFhYSooKJAkFRUVfeN8ZWWlTp065TIfEhKiLl266NChQyosLFRwcLC6d%2B/unO/Tp4%2BKi4t1/vz5a9EqAADwQjZ3F3A5hmFoxYoV%2BvDDD/XGG2/o9ddfl91ud9nG399fNTU1kqTq6upvnK%2BurpYkBQQEtJhvnvv6c5sf19TUqHPnzq2quaSkRKWlpS5jNluAQkNDW/X81vL1bZf5GG5is7Xv90Pz%2B9Wb37dW6FGyRp9W6FGyTp/u0K4DVlVVlWbPnq3PPvtMb7zxhm699VbZ7XZVVla6bFdXV6fAwEBJFwNRXV1di3mHw%2BEMS833Y339%2BYZhtJhrfty8fmtkZWVp1apVLmMpKSlKTU1t9RrAlXI4Wv8edafOne2X38jDWaFHyRp9WqFHyTp9Xk/tNmAdP35ckydP1s0336zNmzera9eukqSIiAjt3r3bZduioiKFh4dLksLDw1VYWNhiftiwYerSpYu6d%2B/uchmxtLRUFRUVioiIUFNTkyoqKnTmzBmFhIRIkg4fPqwePXqoU6dOra49MTFRw4cPdxmz2QJUXl59ZS/CZfCJA19l9vvLbL6%2BPurc2a7z52vV2Njk7nKuCSv0KFmjTyv0KFmjT3d9%2BGyXAevcuXN6%2BOGHNXDgQKWnp8vH5/8FidjYWD377LPasGGDJk6cqP3792vLli1avXq1JCkhIUEpKSkaPXq0oqKilJmZqbKyMsXGxkqS4uPjtWbNGvXt21cOh0OLFy/WgAED9J3vfEeSFBUVpcWLF2vhwoUqLy/X6tWrlZCQcEX1h4aGtrgcWFpaqYYG73zzon3wlPdXY2OTx9TaVlboUbJGn1boUbJOn9dTuwxY77zzjoqLi/X%2B%2B%2B9r69atLnOffPKJ1q9fr/T0dK1cuVJdu3bV3LlzNXDgQEnSoEGDNH/%2BfC1YsECnT59WWFiY1q1bp%2BDgYEkXL9U1NDRo4sSJqq6uVkxMjFasWOFcf%2BXKlVq4cKFGjBghHx8fjRs3TsnJydeveQAA4PE6GIZhuLsIKygtrbz8RlfIZvNRbMYu09eFZ3o/bYi7S/hWNpuPHI5AlZdXe%2B0nZSv0KFmjTyv0KFmjz27dWn%2BLj5m4iQcAAMBkBCwAAACTEbAAAABMRsACAAAwGQELAADAZAQsAAAAkxGwAAAATEbAAgAAMBkBCwAAwGQELAAAAJMRsAAAAExGwAIAADAZAQsAAMBkBCwAAACTEbAAAABMRsACAAAwGQELAADAZAQsAAAAkxGwAAAATEbAAgAAMBkBCwAAwGQELAAAAJPZ3F0AAHOMXrHb3SW02vtpQ9xdAgBcU5zBAgAAMBkBCwAAwGQELAAAAJMRsAAAAExGwAIAADAZAQsAAMBkBCwAAACTEbAuoaysTMnJyYqOjlZMTIzS09PV0NDg7rIAAICHIGBdQlpamgICArRr1y5t3rxZe/bs0YYNG9xdFgAA8BAErK85duyY8vLyNGPGDNntdvXs2VPJycnKzMx0d2kAAMBD8KdyvqawsFDBwcHq3r27c6xPnz4qLi7W%2BfPn1blzZzdWB3gHT/qzPhJ/2gfAlSNgfU11dbXsdrvLWPPjmpqaVgWskpISlZaWuozZbAEKDQ01r1BJvr6cgASuB5utdf%2BtNf836e3/bVqhTyv0KFmnT3cgYH1NQECAamtrXcaaHwcGBrZqjaysLK1atcpl7PHHH9fUqVPNKfL/V1JSood7FCoxMdH08NZelJSUKCsry6t7lKzRp1V6/O//ftWre5Ss0acVepSs06c7EFm/Jjw8XBUVFTpz5oxz7PDhw%2BrRo4c6derUqjUSExP1zjvvuPwkJiaaXmtpaalWrVrV4myZN7FCj5I1%2BqRH72GFPq3Qo2SdPt2BM1hf06tXL0VFRWnx4sVauHChysvLtXr1aiUkJLR6jdDQUD4JAABgYZzBuoSVK1eqoaFBI0aM0IMPPqgf/OAHSk5OdndZAADAQ3AG6xJCQkK0cuVKd5cBAAA8lO%2BCBQsWuLsItF1gYKAGDBjQ6hvwPZEVepSs0Sc9eg8r9GmFHiXr9Hm9dTAMw3B3EQAAAN6Ee7AAAABMRsACAAAwGQELAADAZAQsAAAAkxGwAAAATEbAAgAAMBkBCwAAwGQELAAAAJMRsDxUWVmZkpOTFR0drZiYGKWnp6uhocHdZZni7Nmzio2NVW5urnPswIEDmjBhgiIjIzV8%2BHBt2rTJjRW2XUFBgR555BENGDBAQ4YM0cyZM3X27FlJ3tOjJO3Zs0cTJkzQ3XffrSFDhmjRokWqq6uT5F19SlJjY6OSkpL029/%2B1jm2Y8cOxcXFqV%2B/fho9erQ%2B/PBDN1Z4dXJycnT77bcrMjLS%2BTNjxgxJ3tNnRUWFZs6cqZiYGPXv31/JyckqKSmR5D3v1z/96U8uxzAyMlJ33nmn7rzzTknecyzbFQMe6ec//7nx5JNPGjU1Ncbx48eN%2B%2B%2B/31i3bp27y7pq%2B/btM0aOHGlEREQYe/fuNQzDMCoqKowBAwYYb7zxhlFfX2989NFHRmRkpHHgwAE3V3tlamtrjSFDhhgvvPCCceHCBePs2bPG5MmTjd/85jde06NhGEZZWZnRt29f4%2B233zYaGxuN06dPG2PGjDFeeOEFr%2Bqz2YoVK4zbbrvNmDVrlmEYhnHkyBGjb9%2B%2BxgcffGDU19cb7733nvH973/fOHXqlJsrbZulS5cav/3tb1uMe1OfP//5z42UlBTj3LlzRmVlpfH4448bjz76qFe%2BX5udOnXKGDJkiPHHP/7Rq45le8IZLA907Ngx5eXlacaMGbLb7erZs6eSk5OVmZnp7tKuSnZ2tqZPn65p06a5jG/fvl3BwcGaOHGibDabBg0apLi4OI/rt7i4WLfddptSUlLUsWNHORwOJSYmKj8/32t6lKSuXbvqo48%2BUnx8vDp06KCKigpduHBBXbt29ao%2BpYtn6rZv3657773XOZadna3o6GiNHDlSNptN9913n/r376%2BsrCw3Vtp2//znP51nOb7KW/r89NNPdeDAAS1dulSdO3dWUFCQFi1apOnTp3vd%2B7WZYRiaMWOGfvSjH%2BmBBx7wmmPZ3hCwPFBhYaGCg4PVvXt351ifPn1UXFys8%2BfPu7GyqzN06FB98MEHuu%2B%2B%2B1zGCwsLFRER4TIWFhamgoKC61neVfvud7%2BrV199Vb6%2Bvs6xbdu26Y477vCaHpsFBQVJkn74wx8qLi5O3bp1U3x8vFf1WVZWpjlz5mj58uWy2%2B3O8aKiIq/psampSZ999pn%2B9re/6Z577tGwYcM0b948nTt3zmv6PHjwoMLCwvTWW28pNjZWQ4cO1bJly9StWzever9%2B1bvvvquioiLnZW1vOZbtDQHLA1VXV7v8D12S83FNTY07SjJFt27dZLPZWoxfql9/f3%2BP7tUwDD3//PP68MMPNWfOHK/sUbp49nHnzp3y8fFRamqq1/TZ1NSkGTNm6JFHHtFtt93mMuctPUoX74e8/fbbNWrUKOXk5OjNN9/U0aNHNWPGDK/p89y5czp06JCOHj2q7Oxs/fGPf9Tp06c1a9Ysr%2Bnxq5qamrRmzRo99thjzg9C3thne0DA8kABAQGqra11GWt%2BHBgY6I6Srim73e68QbpZXV2dx/ZaVVWl1NRUbdmyRW%2B88YZuvfVWr%2Buxmb%2B/v7p3764ZM2Zo165dXtPn2rVr1bFjRyUlJbWY85YeJSkkJESZmZlKSEiQ3W7XzTffrBkzZmjnzp0yDMMr%2BuzYsaMkac6cOQoKClJISIjS0tK0Y8cOr%2Bnxq3Jzc1VSUqKEhATnmDe9Z9sTApYHCg8PV0VFhc6cOeMcO3z4sHr06KFOnTq5sbJrIyIiQoWFhS5jRUVFCg8Pd1NFbXf8%2BHGNHz9eVVVV2rx5s2699VZJ3tXjxx9/rB//%2BMf68ssvnWNffvml/Pz8FBYW5hV9vvvuu8rLy1N0dLSio6P15z//WX/%2B858VHR3tVceyoKBAGRkZMgzDOfbll1/Kx8dH3//%2B972iz7CwMDU1Nam%2Bvt451tTUJEn63ve%2B5xU9ftW2bdsUGxurgIAA55g3vWfbEwKWB%2BrVq5eioqK0ePFiVVVV6cSJE1q9erXLJxJvEhsbqzNnzmjDhg2qr6/X3r17tWXLFo0fP97dpV2Rc%2BfO6eGHH9bdd9%2Bt1157TV27dnXOeUuPknTrrbeqrq5Oy5cv15dffqn//Oc/WrZsmRISEjRq1Civ6HPr1q36%2BOOPtW/fPu3bt09jxozRmDFjtG/fPo0dO1Z5eXnKyclRQ0ODcnJylJeXpwceeMDdZV%2Bx4OBgZWZm6tVXX1VDQ4OKi4v17LPP6ic/%2BYnGjRvnFX0OHjxYPXv21FNPPaXq6mqdPXtWzz//vEaOHKkxY8Z4xfv1q/bv36/%2B/fu7jHnTe7ZdcevvMKLNSktLjalTpxoDBgwwBg4caCxdutRoaGhwd1mm%2BerXNBiGYRw8eNBITEw0IiMjjREjRhhvv/22G6trm/Xr1xsRERHGXXfdZfTr18/lxzC8o8dmhYWFxiOPPGJER0cb99xzj/Hcc88ZFy5cMAzDu/psNmvWLOfXNBiGYezcudMYO3as0a9fP%2BP%2B%2B%2B83/va3v7mxuquTm5vrPF4DBw40Fi1aZNTV1RmG4T19njp1ykhLSzOGDBliREdHGzNnzjTOnTtnGIb3vV/79et3yePkLceyPelgGF859wsAAICrxiVCAAAAkxGwAAAATEbAAgAAMBkBCwAAwGQELAAAAJMRsAAAAExGwAIAADAZAQsAAMBkBCwAAACTEbAAAABMRsACAAAwGQELAADAZAQsAAAAkxGwAAAATEbAAgAAMNn/Bwpt8C2Xsv/sAAAAAElFTkSuQmCC"/>
        </div>
        <div role="tabpanel" class="tab-pane col-md-12" id="common-6059613505534487769">

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">9</td>
        <td class="number">24412</td>
        <td class="number">9.5%</td>
        <td>
            <div class="bar" style="width:37%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">10</td>
        <td class="number">23306</td>
        <td class="number">9.1%</td>
        <td>
            <div class="bar" style="width:36%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">8</td>
        <td class="number">23140</td>
        <td class="number">9.0%</td>
        <td>
            <div class="bar" style="width:36%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">11</td>
        <td class="number">21577</td>
        <td class="number">8.4%</td>
        <td>
            <div class="bar" style="width:33%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">7</td>
        <td class="number">20851</td>
        <td class="number">8.1%</td>
        <td>
            <div class="bar" style="width:32%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">12</td>
        <td class="number">19056</td>
        <td class="number">7.4%</td>
        <td>
            <div class="bar" style="width:29%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">6</td>
        <td class="number">17454</td>
        <td class="number">6.8%</td>
        <td>
            <div class="bar" style="width:27%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">13</td>
        <td class="number">15987</td>
        <td class="number">6.2%</td>
        <td>
            <div class="bar" style="width:25%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">14</td>
        <td class="number">13649</td>
        <td class="number">5.3%</td>
        <td>
            <div class="bar" style="width:21%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">5</td>
        <td class="number">12232</td>
        <td class="number">4.8%</td>
        <td>
            <div class="bar" style="width:19%">&nbsp;</div>
        </td>
</tr><tr class="other">
        <td class="fillremaining">Other values (49)</td>
        <td class="number">65320</td>
        <td class="number">25.4%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr>
</table>
        </div>
        <div role="tabpanel" class="tab-pane col-md-12"  id="extreme-6059613505534487769">
            <p class="h4">Minimum 5 values</p>

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">0</td>
        <td class="number">5</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">1</td>
        <td class="number">37</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">2</td>
        <td class="number">1104</td>
        <td class="number">0.4%</td>
        <td>
            <div class="bar" style="width:16%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">3</td>
        <td class="number">3362</td>
        <td class="number">1.3%</td>
        <td>
            <div class="bar" style="width:47%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">4</td>
        <td class="number">7225</td>
        <td class="number">2.8%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr>
</table>
            <p class="h4">Maximum 5 values</p>

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">54</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:25%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">55</td>
        <td class="number">2</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:50%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">56</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:25%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">58</td>
        <td class="number">2</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:50%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">76</td>
        <td class="number">4</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr>
</table>
        </div>
    </div>
</div>
</div><div class="row variablerow">
    <div class="col-md-3 namecol">
        <p class="h4 pp-anchor" id="pp_var_Purpose">Purpose<br/>
            <small>Categorical</small>
        </p>
    </div><div class="col-md-3">
    <table class="stats ">
        <tr class="">
            <th>Distinct count</th>
            <td>10</td>
        </tr>
        <tr>
            <th>Unique (%)</th>
            <td>0.0%</td>
        </tr>
        <tr class="ignore">
            <th>Missing (%)</th>
            <td>0.0%</td>
        </tr>
        <tr class="ignore">
            <th>Missing (n)</th>
            <td>0</td>
        </tr>
    </table>
</div>
<div class="col-md-6 collapse in" id="minifreqtable6615373389756302133">
    <table class="mini freq">
        <tr class="">
    <th>Debt Consolidation</th>
    <td>
        <div class="bar" style="width:100%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 79.3%">
            203911
        </div>

    </td>
</tr><tr class="">
    <th>Home Improvements</th>
    <td>
        <div class="bar" style="width:8%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 5.8%">
            &nbsp;
        </div>
        14915
    </td>
</tr><tr class="">
    <th>other</th>
    <td>
        <div class="bar" style="width:7%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 5.6%">
            &nbsp;
        </div>
        14268
    </td>
</tr><tr class="other">
    <th>Other values (7)</th>
    <td>
        <div class="bar" style="width:12%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 9.3%">
            &nbsp;
        </div>
        23890
    </td>
</tr>
    </table>
</div>
<div class="col-md-12 text-right">
    <a role="button" data-toggle="collapse" data-target="#freqtable6615373389756302133, #minifreqtable6615373389756302133"
       aria-expanded="true" aria-controls="collapseExample">
        Toggle details
    </a>
</div>
<div class="col-md-12 extrapadding collapse" id="freqtable6615373389756302133">

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">Debt Consolidation</td>
        <td class="number">203911</td>
        <td class="number">79.3%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">Home Improvements</td>
        <td class="number">14915</td>
        <td class="number">5.8%</td>
        <td>
            <div class="bar" style="width:8%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">other</td>
        <td class="number">14268</td>
        <td class="number">5.6%</td>
        <td>
            <div class="bar" style="width:7%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">Other</td>
        <td class="number">9667</td>
        <td class="number">3.8%</td>
        <td>
            <div class="bar" style="width:5%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">Business Loan</td>
        <td class="number">4712</td>
        <td class="number">1.8%</td>
        <td>
            <div class="bar" style="width:3%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">Buy a Car</td>
        <td class="number">3276</td>
        <td class="number">1.3%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">Medical Bills</td>
        <td class="number">2868</td>
        <td class="number">1.1%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">Take a Trip</td>
        <td class="number">1570</td>
        <td class="number">0.6%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">Buy House</td>
        <td class="number">1530</td>
        <td class="number">0.6%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">Educational Expenses</td>
        <td class="number">267</td>
        <td class="number">0.1%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr>
</table>
</div>
</div><div class="row variablerow">
    <div class="col-md-3 namecol">
        <p class="h4 pp-anchor" id="pp_var_Tax Liens">Tax Liens<br/>
            <small>Numeric</small>
        </p>
    </div><div class="col-md-6">
    <div class="row">
        <div class="col-sm-6">
            <table class="stats ">
                <tr>
                    <th>Distinct count</th>
                    <td>13</td>
                </tr>
                <tr>
                    <th>Unique (%)</th>
                    <td>0.0%</td>
                </tr>
                <tr class="ignore">
                    <th>Missing (%)</th>
                    <td>0.0%</td>
                </tr>
                <tr class="ignore">
                    <th>Missing (n)</th>
                    <td>23</td>
                </tr>
                <tr class="ignore">
                    <th>Infinite (%)</th>
                    <td>0.0%</td>
                </tr>
                <tr class="ignore">
                    <th>Infinite (n)</th>
                    <td>0</td>
                </tr>
            </table>

        </div>
        <div class="col-sm-6">
            <table class="stats ">

                <tr>
                    <th>Mean</th>
                    <td>0.027203</td>
                </tr>
                <tr>
                    <th>Minimum</th>
                    <td>0</td>
                </tr>
                <tr>
                    <th>Maximum</th>
                    <td>11</td>
                </tr>
                <tr class="alert">
                    <th>Zeros (%)</th>
                    <td>98.2%</td>
                </tr>
            </table>
        </div>
    </div>
</div>
<div class="col-md-3 collapse in" id="minihistogram7646564361946184879">
    <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAABLCAYAAAA1fMjoAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAPYQAAD2EBqD%2BnaQAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAAPtJREFUeJzt1bEJAlEQRVFXLGmLsCdje7IIexpzkQsbyN/gnHzgJZfZZmYuwE/X1QPgzG6rB3zbH6/DN%2B/n/Q9LwAeBJBAIAoEgEAgCgSAQCAKBIBAIAoEgEAgCgSAQCAKBIBAIAoEgEAgCgSAQCAKBIBAIAoEgEAgCgSAQCAKBIBAIAoEgEAgCgSAQCAKBIBAIAoEgEAgCgSAQCAKBIBAIAoEgEAgCgSAQCAKBIBAIAoEgEAjbzMzqEXBWPggEgUAQCASBQBAIBIFAEAgEgUAQCASBQBAIBIFAEAgEgUAQCASBQBAIBIFAEAgEgUAQCASBQBAIBIFAEAiED9obC49m6JdFAAAAAElFTkSuQmCC">

</div>
<div class="col-md-12 text-right">
    <a role="button" data-toggle="collapse" data-target="#descriptives7646564361946184879,#minihistogram7646564361946184879"
       aria-expanded="false" aria-controls="collapseExample">
        Toggle details
    </a>
</div>
<div class="row collapse col-md-12" id="descriptives7646564361946184879">
    <ul class="nav nav-tabs" role="tablist">
        <li role="presentation" class="active"><a href="#quantiles7646564361946184879"
                                                  aria-controls="quantiles7646564361946184879" role="tab"
                                                  data-toggle="tab">Statistics</a></li>
        <li role="presentation"><a href="#histogram7646564361946184879" aria-controls="histogram7646564361946184879"
                                   role="tab" data-toggle="tab">Histogram</a></li>
        <li role="presentation"><a href="#common7646564361946184879" aria-controls="common7646564361946184879"
                                   role="tab" data-toggle="tab">Common Values</a></li>
        <li role="presentation"><a href="#extreme7646564361946184879" aria-controls="extreme7646564361946184879"
                                   role="tab" data-toggle="tab">Extreme Values</a></li>

    </ul>

    <div class="tab-content">
        <div role="tabpanel" class="tab-pane active row" id="quantiles7646564361946184879">
            <div class="col-md-4 col-md-offset-1">
                <p class="h4">Quantile statistics</p>
                <table class="stats indent">
                    <tr>
                        <th>Minimum</th>
                        <td>0</td>
                    </tr>
                    <tr>
                        <th>5-th percentile</th>
                        <td>0</td>
                    </tr>
                    <tr>
                        <th>Q1</th>
                        <td>0</td>
                    </tr>
                    <tr>
                        <th>Median</th>
                        <td>0</td>
                    </tr>
                    <tr>
                        <th>Q3</th>
                        <td>0</td>
                    </tr>
                    <tr>
                        <th>95-th percentile</th>
                        <td>0</td>
                    </tr>
                    <tr>
                        <th>Maximum</th>
                        <td>11</td>
                    </tr>
                    <tr>
                        <th>Range</th>
                        <td>11</td>
                    </tr>
                    <tr>
                        <th>Interquartile range</th>
                        <td>0</td>
                    </tr>
                </table>
            </div>
            <div class="col-md-4 col-md-offset-2">
                <p class="h4">Descriptive statistics</p>
                <table class="stats indent">
                    <tr>
                        <th>Standard deviation</th>
                        <td>0.24595</td>
                    </tr>
                    <tr>
                        <th>Coef of variation</th>
                        <td>9.0414</td>
                    </tr>
                    <tr>
                        <th>Kurtosis</th>
                        <td>328.62</td>
                    </tr>
                    <tr>
                        <th>Mean</th>
                        <td>0.027203</td>
                    </tr>
                    <tr>
                        <th>MAD</th>
                        <td>0.053423</td>
                    </tr>
                    <tr class="">
                        <th>Skewness</th>
                        <td>14.856</td>
                    </tr>
                    <tr>
                        <th>Sum</th>
                        <td>6990</td>
                    </tr>
                    <tr>
                        <th>Variance</th>
                        <td>0.060491</td>
                    </tr>
                    <tr>
                        <th>Memory size</th>
                        <td>2.0 MiB</td>
                    </tr>
                </table>
            </div>
        </div>
        <div role="tabpanel" class="tab-pane col-md-8 col-md-offset-2" id="histogram7646564361946184879">
            <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAlgAAAGQCAYAAAByNR6YAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAPYQAAD2EBqD%2BnaQAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAIABJREFUeJzt3XtU1XW%2B//GXsEE2oIEiWi1nJAE7miUHFG85J5U8mpTjJUoX2UU7BUm4RBtS06OhOWIXNc1L5qSsk%2BXoNHYwrRmXWePgJbNyxMBEa2GCAgobSG6/P/qxz%2BzUEfb%2B5Gbr87HWXsv9%2BXy/n%2B97vxdLXvv7/e5Nq4aGhgYBAADAGC93FwAAAHC9IWABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMs7i7gRlFcXG58TS%2BvVmrXLkAlJTbV1zcYX/96Ru%2BcR%2B9cQ/%2BcR%2B9cc6P2r0OHNm45LmewPJiXVyu1atVKXl6t3F2Kx6F3zqN3rqF/zqN3rqF/1xYBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMs7i7ALgmZuaH7i6hybanDnB3CQAAXBOcwQIAADDMbQErNzdXjz32mPr06aMBAwZoxowZKikpkSTNmTNHd9xxh6KiouyPTZs22fdds2aNBg0apF69eikxMVHffvutfa6yslLp6emKjY1VdHS0ZsyYIZvNZp8/ceKEJk6cqKioKA0cOFBvvPGGQ127d%2B9WfHy8evXqpeHDh2vXrl2/cCcAAMD1xi0Bq7q6WpMmTVJUVJQ%2B/fRTffDBByorK9Pzzz8vSfrqq680f/58HTp0yP5ISEiQJG3dulUbNmzQm2%2B%2BqZycHPXo0UMpKSlqaGiQJM2fP1%2BnT5/Wjh07tHPnTp0%2BfVqZmZmSpJqaGj311FPq2bOncnJytHr1amVlZWn79u2SpIKCAk2ZMkXPPvusDhw4oClTpig1NVVnzpxxQ5cAAICnckvAKiws1O23367k5GT5%2BvoqODhYCQkJ2r9/vy5evKhvvvlGd9xxx2X3fffddzV%2B/HhFRESodevWmjZtmgoLC5WTk6Oqqipt27ZNKSkpCgoKUvv27ZWWlqYtW7aoqqpK%2B/fvV1FRkVJSUuTr66vu3bsrMTFRWVlZkn4KbzExMRo6dKgsFotGjBih3r17O5w9AwAAuBq3BKzbbrtNa9eulbe3t31sx44d6tGjh3Jzc1VbW6ulS5eqf//%2BGjZsmFavXq36%2BnpJUn5%2BviIjI%2B37%2Bfj4qEuXLsrNzdXJkydVU1PjMN%2B1a1dVV1eroKBAeXl5CgsLk6%2Bvr30%2BPDxcubm5l1375/MAAABN4fZPETY0NOjVV1/Vrl27tHHjRp09e1Z9%2BvRRYmKiXn75ZR09elTJycny8vLSpEmTZLPZZLVaHdbw8/NTZWWlKioqJEn%2B/v72ucZtbTbbZfe1Wq2qrKy0b3OltZujqKhIxcXFDmMWi79CQ0Obtc7VeHt71mcULJaWU29j7zythy0BvXMN/XMevXMN/bu23BqwKioqlJ6eriNHjmjjxo3q1q2bunXrpgED/u/j/HfeeacmTpyo7OxsTZo0SVarVdXV1Q7rVFdXKyAgwB6sqqqqFBAQYP%2B3JAUGBsrf39/%2BvNE/b/uv1m6OTZs2afny5Q5jycnJSklJadY615vg4Ob18Vpo29Z69Y1wWfTONfTPefTONfTv2nBbwDp16pQmT56sW265RZs3b1a7du0kSR9//LHOnj2rhx56yL7txYsX5efnJ0mKiIhQXl6e7rnnHkk/3bheUFCgyMhIhYWFycfHR/n5%2BbrrrrskScePH7dfRjx37pwKCgpUW1sri%2BWnl56fn6%2BIiAhJUmRkpI4cOeJQZ35%2B/hXvB7uShIQEDR482GHMYvFXaantCns4x9PehZh%2B/a7w9vZS27ZWXbhQpbq6eneX41HonWvon/PonWtu1P656829WwLW%2BfPnNXHiRPXt21cZGRny8vq/oNDQ0KCFCxfq17/%2Btfr27asvvvhCb7/9ttLT0yVJY8aM0bJlyzRo0CCFhYXplVdeUUhIiGJiYuTj46Phw4crMzNTr732miQpMzNTI0eOlJ%2Bfn2JjYxUcHKwlS5YoNTVVJ06c0IYNGzR16lRJ0v3336%2B33npL2dnZuvfee7Vz507t27dPM2fObNbrCw0NveRyYHFxuWprb5wf6Mtpia%2B/rq6%2BRdblCeida%2Bif8%2Bida%2BjfteGWgLVlyxYVFhZq%2B/bt%2BvBDx28iP3TokNLT0zV37lydOXNGISEhmjJlih544AFJ0tixY1VeXq7k5GSVlJSoZ8%2BeWrVqlXx8fCT99B1aixYtUnx8vGpqajRkyBDNnj1bkmSxWLRu3TrNmzdPAwYMkL%2B/vxITEzV69GhJP90Q//rrryszM1MzZ87UrbfeqmXLliksLOwadgcAAHi6Vg2NXyCFX1RxcbnxNS0WL8Vl7jG%2B7i%2BlJf2pHIvFS8HBASottfFOrpnonWvon/PonWtu1P516NDGLcf1rJt4AAAAPAABCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDC3Bazc3Fw99thj6tOnjwYMGKAZM2aopKREknT48GGNGzdOUVFRGjx4sN577z2Hfbdu3aq4uDj16tVLo0eP1qFDh%2BxzdXV1WrRokfr376%2BoqCg9/fTTKioqss%2BfO3dOSUlJiomJUWxsrDIyMlRbW2ufv9qxAQAArsYtAau6ulqTJk1SVFSUPv30U33wwQcqKyvT888/r/Pnz%2BvJJ5/UqFGjtH//fmVkZGjhwoX68ssvJUk5OTmaP3%2B%2BXnrpJe3fv1/333%2B/nn76aVVVVUmSVq5cqc8%2B%2B0x//OMftWfPHvn5%2BWnWrFn2Y6empsrf31979uzR5s2btXfvXq1fv16SrnpsAACApnBLwCosLNTtt9%2Bu5ORk%2Bfr6Kjg4WAkJCdq/f7927typoKAgTZgwQRaLRf369VN8fLyysrIkSe%2B9957uu%2B8%2BRUdHy8fHR48%2B%2BqiCg4OVnZ1tn588ebJuvvlmBQYGaubMmfrkk0/03Xff6eTJk9q3b5%2BmT58uq9Wqzp07Kykpyb721Y4NAADQFG4JWLfddpvWrl0rb29v%2B9iOHTvUo0cP5eXlKTIy0mH78PBw5ebmSpLy8/OvOF9eXq4ffvjBYT4kJEQ33XSTjh07pry8PAUFBaljx472%2Ba5du6qwsFAXLly46rEBAACawuLuAhoaGvTqq69q165d2rhxo95%2B%2B21ZrVaHbfz8/FRZWSlJstlsV5y32WySJH9//0vmG%2Bd%2Bvm/j88b9/9Wxm6qoqEjFxcUOYxaLv0JDQ5u1ztV4e3vWZxQslpZTb2PvPK2HLQG9cw39cx69cw39u7bcGrAqKiqUnp6uI0eOaOPGjerWrZusVqvKy8sdtquurlZAQICknwJRdXX1JfPBwcH2cNR4P9bP929oaLhkrvF5QEDAVY/dVJs2bdLy5csdxpKTk5WSktKsda43wcHN6%2BO10Lat9eob4bLonWvon/PonWvo37XhtoB16tQpTZ48Wbfccos2b96sdu3aSZIiIyP12WefOWybn5%2BviIgISVJERITy8vIumR80aJBuuukmdezY0eEyYnFxscrKyhQZGan6%2BnqVlZXp7NmzCgkJkSQdP35cnTp1Ups2ba567KZKSEjQ4MGDHcYsFn%2BVltqatc7VeNq7ENOv3xXe3l5q29aqCxeqVFdX7%2B5yPAq9cw39cx69c82N2j93vbl3S8A6f/68Jk6cqL59%2ByojI0NeXv8XFOLi4rR48WKtX79eEyZM0MGDB7Vt2zatWLFCkjR27FglJydr%2BPDhio6OVlZWls6dO6e4uDhJ0ujRo7Vy5Ur17NlTwcHBWrBggfr06aNf/epXkqTo6GgtWLBA8%2BbNU2lpqVasWKGxY8c26dhNFRoaesnlwOLictXW3jg/0JfTEl9/XV19i6zLE9A719A/59E719C/a6NVQ0NDw7U%2B6FtvvaWXXnpJVqtVrVq1cpg7dOiQvvrqK2VkZOibb75Ru3btlJSUpNGjR9u3ef/997Vy5UqdOXNG4eHhmjVrlu666y5JUk1NjV577TX9%2Bc9/ls1mU2xsrObPn6/27dtLks6ePat58%2BYpJydHXl5eGjVqlNLS0uw33F/t2M4qLi6/%2BkbNZLF4KS5zj/F1fynbUwe4uwQ7i8VLwcEBKi218R9NM9E719A/59E719yo/evQoY1bjuuWgHUjImARsK4X9M419M959M41N2r/3BWwPOsmHgAAAA9AwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhjkVsOrq6kzXAQAAcN1wKmANGjRIv//975Wfn2%2B6HgAAAI/nVMB65pln9Pnnn2vkyJEaN26c3nnnHZWXl5uuDQAAwCM5FbAefvhhvfPOO/rwww/Vv39/rVmzRgMHDtS0adP0t7/9zXSNAAAAHsWlm9y7dOmiqVOn6sMPP1RycrL%2B8pe/6IknntDgwYP11ltvca8WAAC4IVlc2fnw4cP605/%2BpOzsbF28eFFxcXEaPXq0zpw5o9dee01fffWVXn75ZVO1AgAAeASnAtaKFSv0/vvv6%2BTJk%2BrZs6emTp2qkSNHKjAw0L6Nt7e3XnjhBWOFAgAAeAqnAtbGjRt1//33a%2BzYsQoPD7/sNl27dlVaWppLxQEAAHgipwLWJ598ooqKCpWVldnHsrOz1a9fPwUHB0uSunfvru7du5upEgAAwIM4dZP7P/7xDw0bNkybNm2yjy1evFjx8fH65ptvjBUHAADgiZwKWL///e917733aurUqfaxjz/%2BWIMGDdJLL71krDgAAABP5FTAOnLkiJ588kn5%2Bvrax7y9vfXkk0/qiy%2B%2BaPZ6JSUliouLU05Ojn1szpw5uuOOOxQVFWV//PMZszVr1mjQoEHq1auXEhMT9e2339rnKisrlZ6ertjYWEVHR2vGjBmy2Wz2%2BRMnTmjixImKiorSwIED9cYbbzjUs3v3bsXHx6tXr14aPny4du3a1ezXBAAAblxOBazAwECdOnXqkvEffvhBfn5%2BzVrr4MGDSkhIuGS9r776SvPnz9ehQ4fsj4SEBEnS1q1btWHDBr355pvKyclRjx49lJKSooaGBknS/Pnzdfr0ae3YsUM7d%2B7U6dOnlZmZKUmqqanRU089pZ49eyonJ0erV69WVlaWtm/fLkkqKCjQlClT9Oyzz%2BrAgQOaMmWKUlNTdebMmWb3CQAA3JicCljDhg3T3Llz9be//U0VFRWy2Wz6%2B9//rnnz5ikuLq7J62zdulVpaWkOlxol6eLFi/rmm290xx13XHa/d999V%2BPHj1dERIRat26tadOmqbCwUDk5OaqqqtK2bduUkpKioKAgtW/fXmlpadqyZYuqqqq0f/9%2BFRUVKSUlRb6%2BvurevbsSExOVlZVlrykmJkZDhw6VxWLRiBEj1Lt3b4ezZwAAAP%2BKU58inDZtmr777js9/vjjatWqlX08Li5OM2bMaPI6AwcOVHx8vCwWi0PIys3NVW1trZYuXaqDBw%2BqTZs2GjNmjCZNmiQvLy/l5%2Bdr8uTJ9u19fHzUpUsX5ebmKigoSDU1NYqMjLTPd%2B3aVdXV1SooKFBeXp7CwsIcLm%2BGh4dr9erVkqT8/HyHfRvnc3Nzm/y6ioqKVFxc7DBmsfgrNDS0yWs0hbe3S1/Ef81ZLC2n3sbeeVoPWwJ65xr65zx65xr6d205FbCsVqtWrVqlEydO6NixY/Lx8VHXrl3VpUuXZq3ToUOHy46Xl5erT58%2BSkxM1Msvv6yjR48qOTlZXl5emjRpkmw2m6xWq8M%2Bfn5%2BqqysVEVFhSTJ39/foV5Jstlsl93XarWqsrLSvs2V1m6qTZs2afny5Q5jycnJSklJafIa16Pg4AB3l3CJtm2tV98Il0XvXEP/nEfvXEP/rg2X/lROWFiYwsLCTNViN2DAAA0YMMD%2B/M4779TEiROVnZ2tSZMmyWq1qrq62mGf6upqBQQE2INVVVWVAgIC7P%2BWfrp3zN/f3/680T9v%2B6/WbqqEhAQNHjzYYcxi8Vdpqe0KezjH096FmH79rvD29lLbtlZduFClurp6d5fjUeida%2Bif8%2Bida27U/rnrzb1TAevEiROaN2%2BeDh48qJqamkvmjx496lJRH3/8sc6ePauHHnrIPnbx4kX7DfQRERHKy8vTPffcI%2BmnG9cLCgoUGRmpsLAw%2Bfj4KD8/X3fddZck6fjx4/bLiOfOnVNBQYFqa2tlsfz08vPz8xURESFJioyM1JEjRxzqyc/Pv%2BL9YJcTGhp6yeXA4uJy1dbeOD/Ql9MSX39dXX2LrMsT0DvX0D/n0TvX0L9rw6mANXfuXBUWFiotLU1t2rQxXZMaGhq0cOFC/frXv1bfvn31xRdf6O2331Z6erokacyYMVq2bJkGDRqksLAwvfLKKwoJCVFMTIx8fHw0fPhwZWZm6rXXXpMkZWZmauTIkfLz81NsbKyCg4O1ZMkSpaam6sSJE9qwYYP9HrD7779fb731lrKzs3Xvvfdq586d2rdvn2bOnGn8dQIAgOuTUwHr0KFD%2BsMf/qCoqCjT9Uj66Wb59PR0zZ07V2fOnFFISIimTJmiBx54QJI0duxYlZeXKzk5WSUlJerZs6dWrVolHx8fST99h9aiRYsUHx%2BvmpoaDRkyRLNnz5YkWSwWrVu3TvPmzdOAAQPk7%2B%2BvxMREjR49WtJPN8S//vrryszM1MyZM3Xrrbdq2bJlv8ilUAAAcH1q1dD45VHN8Jvf/EZr1qy55NN2uLLi4nLja1osXorL3GN83V/K9tQBV9/oGrFYvBQcHKDSUhunypuJ3rmG/jmP3rnmRu1fhw7mr7Q1hVN3STd%2Buq%2B83HxoAAAA8HROXSLcvXu3vvjiC8XGxqp9%2B/YO3yklSX/5y1%2BMFAcAAOCJnApYsbGxio2NNV0LAADAdcGpgPXMM8%2BYrgMAAOC64fQ3Vebm5io9PV0PPfSQzpw5o6ysLOXk5JisDQAAwCM5FbC%2B/vprjRs3Tt9//72%2B/vprXbx4UUePHtXjjz%2BuXbt2ma4RAADAozgVsDIzM/X4449rw4YN9u%2BeevHFF/XII49c8jf4AAAAbjROn8EaNWrUJeMPP/ywvv32W5eLAgAA8GROBSwfHx9VVFRcMl5YWCirlb/SDQAAbmxOBayhQ4dqyZIlKi0ttY8dP35cGRkZ%2Bo//%2BA9TtQEAAHgkpwLWc889p%2BrqavXv319VVVUaPXq0Ro4cKYvFohkzZpiuEQAAwKM49T1YgYGBeuedd7R371794x//UH19vSIjI3X33XfLy8vpb34AAAC4LjgVsBr169dP/fr1M1ULAADAdcGpgDV48GC1atXqivP8LUIAAHAjcypg/fa3v3UIWDU1NTp58qQ%2B%2BeQTpaamGisOAADAEzkVsKZMmXLZ8Y0bN%2BrgwYN65JFHXCoKAADAkxm9I/2ee%2B7R7t27TS4JAADgcYwGrH379ql169YmlwQAAPA4Tl0i/PklwIaGBlVUVOjYsWNcHgQAADc8pwLWLbfccsmnCH18fDRx4kTFx8cbKQwAAMBTORWwXnrpJdN1AAAAXDecClj79%2B9v8ra9e/d25hAAAAAey6mA9eijj6qhocH%2BaNR42bBxrFWrVjp69KiBMgEAADyHUwFr2bJlWrhwoZ577jn17dtXPj4%2BOnz4sObOnavx48frnnvuMV0nAACAx3DqaxoWLVqkOXPmaOjQoQoMDFTr1q3Vp08fzZs3T%2BvWrdOtt95qfwAAANxonApYRUVFuvnmmy8ZDwwMVGlpqctFAQAAeDKnAlavXr308ssvq6Kiwj5WVlamxYsXq1%2B/fsaKAwAA8ERO3YM1a9YsTZw4UYMGDVKXLl0kSSdOnFCHDh309ttvm6wPAADA4zgVsLp27ars7Gxt27ZNx48flySNHz9e9913n6xWq9ECAQAAPI1TAUuS2rZtq3Hjxun7779X586dJf30be4AAAA3OqfuwWpoaFBmZqZ69%2B6tkSNH6ocfftBzzz2n9PR01dTUmK4RAADAozgVsDZs2KD3339fc%2BbMka%2BvryRp6NCh%2Butf/6rXXnvNaIEAAACexqmAtWnTJr3wwgsaPXq0/dvbR4wYoYyMDP3v//6v0QIBAAA8jVMB6/vvv9e//du/XTLerVs3nT171uWiAAAAPJlTAevWW2/Vl19%2Becn47t277Te8AwAA3Kic%2BhThE088of/%2B7//WmTNn1NDQoL179%2Bqdd97Rhg0blJ6ebrpGAAAAj%2BJUwBozZoxqa2u1cuVKVVdX64UXXlD79u01depUPfzww6ZrBAAA8ChOBaw///nP%2Bs///E8lJCSopKREDQ0Nat%2B%2BvenaAAAAPJJT92C9%2BOKL9pvZ27VrR7gCAAD4J04FrC5duujYsWOmawEAALguOHWJMCIiQmlpaVq7dq26dOmi1q1bO8wvXLjQSHEAAACeyKmAderUKUVHR0uSiouLjRYEAADg6ZocsBYuXKhnn31W/v7%2B2rBhwy9ZEwAAgEdr8j1Yb7/9tqqqqhzGnnjiCRUVFRkvCgAAwJM1OWA1NDRcMvb555/rxx9/NFoQAACAp3PqU4QAAAC4MgIWAACAYc0KWK1atfql6gAAALhuNOtrGl588UWH77yqqanR4sWLFRAQ4LAd34MFAABuZE0%2Bg9W7d28VFxfr%2B%2B%2B/tz%2BioqJUWlrqMPb99983q4CSkhLFxcUpJyfHPnb48GGNGzdOUVFRGjx4sN577z2HfbZu3aq4uDj16tVLo0eP1qFDh%2BxzdXV1WrRokfr376%2BoqCg9/fTTDp90PHfunJKSkhQTE6PY2FhlZGSotra2yccGAAC4miafwfolvvvq4MGD%2Bt3vfqdTp07Zx86fP68nn3xSKSkpSkhI0P79%2B5WcnKxu3brpzjvvVE5OjubPn681a9bozjvvVFZWlp5%2B%2Bmnt2rVLVqtVK1eu1GeffaY//vGPatOmjWbPnq1Zs2Zp9erVkqTU1FR17NhRe/bs0dmzZ/X0009r/fr1mjRp0lWPDQAA0BRuu8l969atSktL09SpUx3Gd%2B7cqaCgIE2YMEEWi0X9%2BvVTfHy8srKyJEnvvfee7rvvPkVHR8vHx0ePPvqogoODlZ2dbZ%2BfPHmybr75ZgUGBmrmzJn65JNP9N133%2BnkyZPat2%2Bfpk%2BfLqvVqs6dOyspKcm%2B9tWODQAA0BRuC1gDBw7URx99pBEjRjiM5%2BXlKTIy0mEsPDxcubm5kqT8/PwrzpeXl%2BuHH35wmA8JCdFNN92kY8eOKS8vT0FBQerYsaN9vmvXriosLNSFCxeuemwAAICmcOpvEZrQoUOHy47bbDZZrVaHMT8/P1VWVl513mazSZL8/f0vmW%2Bc%2B/m%2Bjc8b9/9Xx26qoqKiS/5Go8Xir9DQ0GatczXe3p71LRsWS8upt7F3ntbDloDeuYb%2BOY/euYb%2BXVtuC1hXYrVaVV5e7jBWXV1t/6Si1WpVdXX1JfPBwcH2cPTzP%2BnTuH9DQ8Mlc43PAwICrnrsptq0aZOWL1/uMJacnKyUlJRmrXO9CQ5uXh%2BvhbZtrVffCJdF71xD/5xH71xD/66NFhewIiMj9dlnnzmM5efnKyIiQpIUERGhvLy8S%2BYHDRqkm266SR07dnS4jFhcXKyysjJFRkaqvr5eZWVlOnv2rEJCQiRJx48fV6dOndSmTZurHrupEhISNHjwYIcxi8VfpaW2Zq1zNZ72LsT063eFt7eX2ra16sKFKtXV1bu7HI9C71xD/5xH71xzo/bPXW/uW1zAiouL0%2BLFi7V%2B/XpNmDBBBw8e1LZt27RixQpJ0tixY5WcnKzhw4crOjpaWVlZOnfunOLi4iRJo0eP1sqVK9WzZ08FBwdrwYIF6tOnj371q19JkqKjo7VgwQLNmzdPpaWlWrFihcaOHdukYzdVaGjoJZcDi4vLVVt74/xAX05LfP11dfUtsi5PQO9cQ/%2BcR%2B9cQ/%2BujRYXsIKDg7Vu3TplZGRo6dKlateunWbNmqW%2BfftKkvr166c5c%2BZo7ty5OnPmjMLDw7VmzRoFBQVJ%2BulSXG1trSZMmCCbzabY2Fi9%2Buqr9vWXLl2qefPmaciQIfLy8tKoUaOUlJTUpGMDAAA0RauGhoYGdxdxIyguLr/6Rs1ksXgpLnOP8XV/Kdso0tN4AAAPaklEQVRTB7i7BDuLxUvBwQEqLbXxTq6Z6J1r6J/z6J1rbtT%2BdejQxi3H9aybeAAAADwAAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMCwFhuwsrOz1b17d0VFRdkf06dPlyTt3r1b8fHx6tWrl4YPH65du3Y57LtmzRoNGjRIvXr1UmJior799lv7XGVlpdLT0xUbG6vo6GjNmDFDNpvNPn/ixAlNnDhRUVFRGjhwoN54441r84IBAMB1o8UGrK%2B%2B%2BkoPPPCADh06ZH8sXrxYBQUFmjJlip599lkdOHBAU6ZMUWpqqs6cOSNJ2rp1qzZs2KA333xTOTk56tGjh1JSUtTQ0CBJmj9/vk6fPq0dO3Zo586dOn36tDIzMyVJNTU1euqpp9SzZ0/l5ORo9erVysrK0vbt293WBwAA4HladMC64447LhnfunWrYmJiNHToUFksFo0YMUK9e/fWpk2bJEnvvvuuxo8fr4iICLVu3VrTpk1TYWGhcnJyVFVVpW3btiklJUVBQUFq37690tLStGXLFlVVVWn//v0qKipSSkqKfH191b17dyUmJiorK%2Btav3wAAODBLO4u4HLq6%2Bt15MgRWa1WrV27VnV1dfrNb36jtLQ05efnKzIy0mH78PBw5ebmSpLy8/M1efJk%2B5yPj4%2B6dOmi3NxcBQUFqaamxmH/rl27qrq6WgUFBcrLy1NYWJh8fX0d1l69enWz6i8qKlJxcbHDmMXir9DQ0GatczXe3i02H1%2BWxdJy6m3snaf1sCWgd66hf86jd66hf9dWiwxYJSUl6t69u4YNG6alS5eqtLRUzz33nKZPn66LFy/KarU6bO/n56fKykpJks1mu%2BJ8RUWFJMnf398%2B17itzWa77L5Wq9W%2BdlNt2rRJy5cvdxhLTk5WSkpKs9a53gQHB7i7hEu0bWu9%2Bka4LHrnGvrnPHrnGvp3bbTIgBUSEuJwWc5qtWr69Ol68MEHFRsbq%2Brqaoftq6urFRAQYN/2SvONwaqqqsq%2BfVVVlSQpMDBQ/v7%2B9ueN/nnbpkpISNDgwYMdxiwWf5WW2q6wh3M87V2I6dfvCm9vL7Vta9WFC1Wqq6t3dzkehd65hv45j9655kbtn7ve3LfIgJWbm6sPPvhA06ZNU6tWrSRJFy9elJeXl%2B68804dPXrUYfv8/Hz7/VoRERHKy8vTPffcI%2BmnG9cLCgoUGRmpsLAw%2Bfj4KD8/X3fddZck6fjx4/bLiOfOnVNBQYFqa2tlsVjsa0dERDSr/tDQ0EsuBxYXl6u29sb5gb6clvj66%2BrqW2RdnoDeuYb%2BOY/euYb%2BXRst8hRIUFCQsrKytHbtWtXW1qqwsFCLFy/Wb3/7W40aNUr79u1Tdna2amtrlZ2drX379umBBx6QJI0ZM0YbN25Ubm6ufvzxRy1ZskQhISGKiYmR1WrV8OHDlZmZqZKSEpWUlCgzM1MjR46Un5%2BfYmNjFRwcrCVLlujHH39Ubm6uNmzYoLFjx7q5IwAAwJO0yDNYnTp10qpVq/Tyyy9r5cqVat26te677z5Nnz5drVu31uuvv67MzEzNnDlTt956q5YtW6awsDBJ0tixY1VeXq7k5GSVlJSoZ8%2BeWrVqlXx8fCRJc%2BbM0aJFixQfH6%2BamhoNGTJEs2fPliRZLBatW7dO8%2BbN04ABA%2BTv76/ExESNHj3abb0AAACep1VD4xdE4RdVXFxufE2LxUtxmXuMr/tL2Z46wN0l2FksXgoODlBpqY1T5c1E71xD/5xH71xzo/avQ4c2bjlui7xECAAA4MkIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWJdx7tw5JSUlKSYmRrGxscrIyFBtba27ywIAAB6CgHUZqamp8vf31549e7R582bt3btX69evd3dZAADAQxCwfubkyZPat2%2Bfpk%2BfLqvVqs6dOyspKUlZWVnuLg0AAHgIAtbP5OXlKSgoSB07drSPde3aVYWFhbpw4YIbKwMAAJ7C4u4CWhqbzSar1eow1vi8srJSbdu2veoaRUVFKi4udhizWPwVGhpqrlBJ3t6elY%2BHv/qZu0tolo/S7nZ3CS1S48%2Bdp/38tRT0z3n0zjX079oiYP2Mv7%2B/qqqqHMYanwcEBDRpjU2bNmn58uUOY88884ymTJlipsj/r6ioSBM75SkhIcF4eLveFRUVadOmTfTOCUVFRfrDH9bSOyfRP%2BfRO9fQv2uLGPszERERKisr09mzZ%2B1jx48fV6dOndSmTZsmrZGQkKAtW7Y4PBISEozXWlxcrOXLl19ytgxXR%2B%2BcR%2B9cQ/%2BcR%2B9cQ/%2BuLc5g/UyXLl0UHR2tBQsWaN68eSotLdWKFSs0duzYJq8RGhrKuwMAAG5gnMG6jKVLl6q2tlZDhgzRgw8%2BqLvvvltJSUnuLgsAAHgIzmBdRkhIiJYuXeruMgAAgIfynjt37lx3FwHnBQQEqE%2BfPk2%2BAR//h945j965hv45j965hv5dO60aGhoa3F0EAADA9YR7sAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbA81Llz55SUlKSYmBjFxsYqIyNDtbW17i7LI%2BTm5uqxxx5Tnz59NGDAAM2YMUMlJSXuLsuj1NXVKTExUb/73e/cXYrHKCsr04wZMxQbG6vevXsrKSlJRUVF7i7LYxw5ckQTJkxQTEyMBg4cqBdffFEXL150d1ktWklJieLi4pSTk2MfO3z4sMaNG6eoqCgNHjxY7733nhsrvL4RsDxUamqq/P39tWfPHm3evFl79%2B7V%2BvXr3V1Wi1ddXa1JkyYpKipKn376qT744AOVlZXp%2Beefd3dpHmX58uU6cOCAu8vwKFOmTFFlZaU%2B%2Bugj7dq1S97e3po9e7a7y/II9fX1%2Bq//%2Bi8NGzZM%2B/bt0%2BbNm/Xpp59qzZo17i6txTp48KASEhJ06tQp%2B9j58%2Bf15JNPatSoUdq/f78yMjK0cOFCffnll26s9PpFwPJAJ0%2Be1L59%2BzR9%2BnRZrVZ17txZSUlJysrKcndpLV5hYaFuv/12JScny9fXV8HBwUpISND%2B/fvdXZrH2Lt3r3bu3Kl7773X3aV4jK%2B//lqHDx/WSy%2B9pLZt2yowMFDz589XWlqau0vzCOfPn1dxcbHq6%2BvV%2BNfdvLy8ZLVa3VxZy7R161alpaVp6tSpDuM7d%2B5UUFCQJkyYIIvFon79%2Bik%2BPp7fHb8QApYHysvLU1BQkDp27Ggf69q1qwoLC3XhwgU3Vtby3XbbbVq7dq28vb3tYzt27FCPHj3cWJXnOHfunGbOnKklS5bwy60ZvvzyS4WHh%2Bvdd99VXFycBg4cqEWLFqlDhw7uLs0jBAcH69FHH9WiRYvUs2dP/eY3v1GXLl306KOPuru0FmngwIH66KOPNGLECIfxvLw8RUZGOoyFh4crNzf3WpZ3wyBgeSCbzXbJL7fG55WVle4oySM1NDTolVde0a5duzRz5kx3l9Pi1dfXa/r06Xrsscd0%2B%2B23u7scj3L%2B/HkdO3ZMBQUF2rp1q/70pz/pzJkzeu6559xdmkeor6%2BXn5%2BfZs%2BerS%2B%2B%2BEIffPCBjh8/rqVLl7q7tBapQ4cOslgsl4xf7neHn58fvzd%2BIQQsD%2BTv76%2BqqiqHscbnAQEB7ijJ41RUVCglJUXbtm3Txo0b1a1bN3eX1OKtWrVKvr6%2BSkxMdHcpHsfX11eSNHPmTAUGBiokJESpqanavXu3bDabm6tr%2BT766CPt2LFD48ePl6%2BvryIiIpScnKz/%2BZ//cXdpHsVqtaq6utphrLq6mt8bv5BLIy5avIiICJWVlens2bMKCQmRJB0/flydOnVSmzZt3Fxdy3fq1ClNnjxZt9xyizZv3qx27dq5uySP8P7776uoqEgxMTGSZP%2BP%2BuOPP%2BaG96sIDw9XfX29ampq1Lp1a0k/nZWRZL%2BnCFd2%2BvTpSz4xaLFY5OPj46aKPFNkZKQ%2B%2B%2Bwzh7H8/HxFRES4qaLrG2ewPFCXLl0UHR2tBQsWqKKiQt99951WrFihsWPHuru0Fu/8%2BfOaOHGi/v3f/11vvvkm4aoZPvzwQ33%2B%2Bec6cOCADhw4oJEjR2rkyJGEqybo37%2B/OnfurOeff142m00lJSV65ZVXNHToUAUGBrq7vBZv4MCBKi4u1htvvKG6ujp99913WrlypeLj491dmkeJi4vT2bNntX79etXU1Ojvf/%2B7tm3bpjFjxri7tOsSActDLV26VLW1tRoyZIgefPBB3X333UpKSnJ3WS3eli1bVFhYqO3btys6OlpRUVH2B/BL8fHx0YYNG%2BTt7a1hw4Zp2LBh6tSpkxYsWODu0jxCeHi4Vq1apb/%2B9a%2BKjY3VI488osGDB1/yKTn8a8HBwVq3bp0%2B/PBDxcbGatasWZo1a5b69u3r7tKuS60aOD8NAABgFGewAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADD/h8nmt0AzRubYgAAAABJRU5ErkJggg%3D%3D"/>
        </div>
        <div role="tabpanel" class="tab-pane col-md-12" id="common7646564361946184879">

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">0.0</td>
        <td class="number">252322</td>
        <td class="number">98.2%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">1.0</td>
        <td class="number">3276</td>
        <td class="number">1.3%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">2.0</td>
        <td class="number">872</td>
        <td class="number">0.3%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">3.0</td>
        <td class="number">247</td>
        <td class="number">0.1%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">4.0</td>
        <td class="number">124</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">5.0</td>
        <td class="number">61</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">6.0</td>
        <td class="number">30</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">9.0</td>
        <td class="number">10</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">8.0</td>
        <td class="number">8</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">7.0</td>
        <td class="number">6</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="other">
        <td class="fillremaining">Other values (2)</td>
        <td class="number">5</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="missing">
        <td class="fillremaining">(Missing)</td>
        <td class="number">23</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr>
</table>
        </div>
        <div role="tabpanel" class="tab-pane col-md-12"  id="extreme7646564361946184879">
            <p class="h4">Minimum 5 values</p>

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">0.0</td>
        <td class="number">252322</td>
        <td class="number">98.2%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">1.0</td>
        <td class="number">3276</td>
        <td class="number">1.3%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">2.0</td>
        <td class="number">872</td>
        <td class="number">0.3%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">3.0</td>
        <td class="number">247</td>
        <td class="number">0.1%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">4.0</td>
        <td class="number">124</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:1%">&nbsp;</div>
        </td>
</tr>
</table>
            <p class="h4">Maximum 5 values</p>

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">7.0</td>
        <td class="number">6</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:60%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">8.0</td>
        <td class="number">8</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:80%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">9.0</td>
        <td class="number">10</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">10.0</td>
        <td class="number">3</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:30%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">11.0</td>
        <td class="number">2</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:20%">&nbsp;</div>
        </td>
</tr>
</table>
        </div>
    </div>
</div>
</div><div class="row variablerow">
    <div class="col-md-3 namecol">
        <p class="h4 pp-anchor" id="pp_var_Term">Term<br/>
            <small>Categorical</small>
        </p>
    </div><div class="col-md-3">
    <table class="stats ">
        <tr class="">
            <th>Distinct count</th>
            <td>2</td>
        </tr>
        <tr>
            <th>Unique (%)</th>
            <td>0.0%</td>
        </tr>
        <tr class="ignore">
            <th>Missing (%)</th>
            <td>0.0%</td>
        </tr>
        <tr class="ignore">
            <th>Missing (n)</th>
            <td>0</td>
        </tr>
    </table>
</div>
<div class="col-md-6 collapse in" id="minifreqtable-2710614819152549963">
    <table class="mini freq">
        <tr class="">
    <th>Short Term</th>
    <td>
        <div class="bar" style="width:100%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 75.0%">
            192632
        </div>

    </td>
</tr><tr class="">
    <th>Long Term</th>
    <td>
        <div class="bar" style="width:34%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 25.0%">
            64352
        </div>

    </td>
</tr>
    </table>
</div>
<div class="col-md-12 text-right">
    <a role="button" data-toggle="collapse" data-target="#freqtable-2710614819152549963, #minifreqtable-2710614819152549963"
       aria-expanded="true" aria-controls="collapseExample">
        Toggle details
    </a>
</div>
<div class="col-md-12 extrapadding collapse" id="freqtable-2710614819152549963">

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">Short Term</td>
        <td class="number">192632</td>
        <td class="number">75.0%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">Long Term</td>
        <td class="number">64352</td>
        <td class="number">25.0%</td>
        <td>
            <div class="bar" style="width:34%">&nbsp;</div>
        </td>
</tr>
</table>
</div>
</div><div class="row variablerow">
    <div class="col-md-3 namecol">
        <p class="h4 pp-anchor" id="pp_var_Years in current job">Years in current job<br/>
            <small>Categorical</small>
        </p>
    </div><div class="col-md-3">
    <table class="stats ">
        <tr class="">
            <th>Distinct count</th>
            <td>12</td>
        </tr>
        <tr>
            <th>Unique (%)</th>
            <td>0.0%</td>
        </tr>
        <tr class="alert">
            <th>Missing (%)</th>
            <td>4.5%</td>
        </tr>
        <tr class="alert">
            <th>Missing (n)</th>
            <td>11476</td>
        </tr>
    </table>
</div>
<div class="col-md-6 collapse in" id="minifreqtable-2726032811493913434">
    <table class="mini freq">
        <tr class="">
    <th>10+ years</th>
    <td>
        <div class="bar" style="width:64%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 30.7%">
            78896
        </div>

    </td>
</tr><tr class="">
    <th>2 years</th>
    <td>
        <div class="bar" style="width:20%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 9.1%">
            &nbsp;
        </div>
        23462
    </td>
</tr><tr class="">
    <th>< 1 year</th>
    <td>
        <div class="bar" style="width:18%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 8.2%">
            &nbsp;
        </div>
        21012
    </td>
</tr><tr class="other">
    <th>Other values (8)</th>
    <td>
        <div class="bar" style="width:100%" data-toggle="tooltip" data-placement="right" data-html="true"
             data-delay=500 title="Percentage: 47.5%">
            122138
        </div>

    </td>
</tr>
    </table>
</div>
<div class="col-md-12 text-right">
    <a role="button" data-toggle="collapse" data-target="#freqtable-2726032811493913434, #minifreqtable-2726032811493913434"
       aria-expanded="true" aria-controls="collapseExample">
        Toggle details
    </a>
</div>
<div class="col-md-12 extrapadding collapse" id="freqtable-2726032811493913434">

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">10+ years</td>
        <td class="number">78896</td>
        <td class="number">30.7%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">2 years</td>
        <td class="number">23462</td>
        <td class="number">9.1%</td>
        <td>
            <div class="bar" style="width:30%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">< 1 year</td>
        <td class="number">21012</td>
        <td class="number">8.2%</td>
        <td>
            <div class="bar" style="width:27%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">3 years</td>
        <td class="number">20659</td>
        <td class="number">8.0%</td>
        <td>
            <div class="bar" style="width:26%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">5 years</td>
        <td class="number">17864</td>
        <td class="number">7.0%</td>
        <td>
            <div class="bar" style="width:23%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">1 year</td>
        <td class="number">16746</td>
        <td class="number">6.5%</td>
        <td>
            <div class="bar" style="width:22%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">4 years</td>
        <td class="number">16166</td>
        <td class="number">6.3%</td>
        <td>
            <div class="bar" style="width:21%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">6 years</td>
        <td class="number">14597</td>
        <td class="number">5.7%</td>
        <td>
            <div class="bar" style="width:19%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">7 years</td>
        <td class="number">13968</td>
        <td class="number">5.4%</td>
        <td>
            <div class="bar" style="width:18%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">8 years</td>
        <td class="number">12206</td>
        <td class="number">4.7%</td>
        <td>
            <div class="bar" style="width:16%">&nbsp;</div>
        </td>
</tr><tr class="missing">
        <td class="fillremaining">(Missing)</td>
        <td class="number">11476</td>
        <td class="number">4.5%</td>
        <td>
            <div class="bar" style="width:15%">&nbsp;</div>
        </td>
</tr>
</table>
</div>
</div><div class="row variablerow">
    <div class="col-md-3 namecol">
        <p class="h4 pp-anchor" id="pp_var_Years of Credit History">Years of Credit History<br/>
            <small>Numeric</small>
        </p>
    </div><div class="col-md-6">
    <div class="row">
        <div class="col-sm-6">
            <table class="stats ">
                <tr>
                    <th>Distinct count</th>
                    <td>541</td>
                </tr>
                <tr>
                    <th>Unique (%)</th>
                    <td>0.2%</td>
                </tr>
                <tr class="ignore">
                    <th>Missing (%)</th>
                    <td>0.0%</td>
                </tr>
                <tr class="ignore">
                    <th>Missing (n)</th>
                    <td>0</td>
                </tr>
                <tr class="ignore">
                    <th>Infinite (%)</th>
                    <td>0.0%</td>
                </tr>
                <tr class="ignore">
                    <th>Infinite (n)</th>
                    <td>0</td>
                </tr>
            </table>

        </div>
        <div class="col-sm-6">
            <table class="stats ">

                <tr>
                    <th>Mean</th>
                    <td>18.29</td>
                </tr>
                <tr>
                    <th>Minimum</th>
                    <td>3.4</td>
                </tr>
                <tr>
                    <th>Maximum</th>
                    <td>70.5</td>
                </tr>
                <tr class="ignore">
                    <th>Zeros (%)</th>
                    <td>0.0%</td>
                </tr>
            </table>
        </div>
    </div>
</div>
<div class="col-md-3 collapse in" id="minihistogram-5709218495563483937">
    <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAABLCAYAAAA1fMjoAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAPYQAAD2EBqD%2BnaQAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAAi1JREFUeJzt3aFOI1EYhuG/m01IcIgW7gCHWhKCQMIGTQKKK8CgV69FcQkYDAZTbgDM3gidYFGEWbcJyeZLS5aZofs8rqI5x7w5Z2Z6pqO2bdsC/upL3xOAIfva9wT%2BhW8/pgt/59fP7x8wE5aNFQQCgUAgEAgEAoFAIBAIBAKBQCAQCASCpXiS/h6evjMPKwgEAoFAIBAIBAKBQCAQCAQCgUAgEAgEAoFAIBAIBAKBQCAQCAQCgUAgEAgEAoFAIBAIBAKBQCAQCP7b1/68x6KvCvKaoM/PCgKBQCAY3BbrPW88hI9iBYFAIBAIBAKBQCAQCAZ3F2uZ%2BA%2BSz88KAoFAILDFGhjbsmERyBLwI8qPM2rbtu160NlsVtfX13V8fFyTyaTr4WFuvVyDNE1Tl5eX1TRNH8PD3FykQyAQCAQCQS%2BBjMfjOjs7q/F43MfwMLde7mLBZ2GLBYFAIBAIBAKBQCAQCAQCgUDQeSC3t7d1eHhY%2B/v7dXV11fXwsJBOz4M8Pj7WxcVF3dzc1MrKSp2cnNT29nZtbm52OQ2YW6cryP39fe3s7NTa2lqtrq7WwcFB3d3ddTkFWEingcxmszcHpCaTiTMhDFqngby%2BvtZoNPrzuW3bN59haDoNZGNj482K0TSNI7cMWqeB7O7u1sPDQz09PdXz83NNp9Pa29vrcgqwkE7vYq2vr9f5%2BXmdnp7Wy8tLHR0d1dbWVpdTgIU4DwKBJ%2BkQCAQCgUDwG4xdbGKNTraTAAAAAElFTkSuQmCC">

</div>
<div class="col-md-12 text-right">
    <a role="button" data-toggle="collapse" data-target="#descriptives-5709218495563483937,#minihistogram-5709218495563483937"
       aria-expanded="false" aria-controls="collapseExample">
        Toggle details
    </a>
</div>
<div class="row collapse col-md-12" id="descriptives-5709218495563483937">
    <ul class="nav nav-tabs" role="tablist">
        <li role="presentation" class="active"><a href="#quantiles-5709218495563483937"
                                                  aria-controls="quantiles-5709218495563483937" role="tab"
                                                  data-toggle="tab">Statistics</a></li>
        <li role="presentation"><a href="#histogram-5709218495563483937" aria-controls="histogram-5709218495563483937"
                                   role="tab" data-toggle="tab">Histogram</a></li>
        <li role="presentation"><a href="#common-5709218495563483937" aria-controls="common-5709218495563483937"
                                   role="tab" data-toggle="tab">Common Values</a></li>
        <li role="presentation"><a href="#extreme-5709218495563483937" aria-controls="extreme-5709218495563483937"
                                   role="tab" data-toggle="tab">Extreme Values</a></li>

    </ul>

    <div class="tab-content">
        <div role="tabpanel" class="tab-pane active row" id="quantiles-5709218495563483937">
            <div class="col-md-4 col-md-offset-1">
                <p class="h4">Quantile statistics</p>
                <table class="stats indent">
                    <tr>
                        <th>Minimum</th>
                        <td>3.4</td>
                    </tr>
                    <tr>
                        <th>5-th percentile</th>
                        <td>9</td>
                    </tr>
                    <tr>
                        <th>Q1</th>
                        <td>13.5</td>
                    </tr>
                    <tr>
                        <th>Median</th>
                        <td>17</td>
                    </tr>
                    <tr>
                        <th>Q3</th>
                        <td>21.7</td>
                    </tr>
                    <tr>
                        <th>95-th percentile</th>
                        <td>31.9</td>
                    </tr>
                    <tr>
                        <th>Maximum</th>
                        <td>70.5</td>
                    </tr>
                    <tr>
                        <th>Range</th>
                        <td>67.1</td>
                    </tr>
                    <tr>
                        <th>Interquartile range</th>
                        <td>8.2</td>
                    </tr>
                </table>
            </div>
            <div class="col-md-4 col-md-offset-2">
                <p class="h4">Descriptive statistics</p>
                <table class="stats indent">
                    <tr>
                        <th>Standard deviation</th>
                        <td>7.0757</td>
                    </tr>
                    <tr>
                        <th>Coef of variation</th>
                        <td>0.38686</td>
                    </tr>
                    <tr>
                        <th>Kurtosis</th>
                        <td>1.9016</td>
                    </tr>
                    <tr>
                        <th>Mean</th>
                        <td>18.29</td>
                    </tr>
                    <tr>
                        <th>MAD</th>
                        <td>5.3906</td>
                    </tr>
                    <tr class="">
                        <th>Skewness</th>
                        <td>1.1171</td>
                    </tr>
                    <tr>
                        <th>Sum</th>
                        <td>4700300</td>
                    </tr>
                    <tr>
                        <th>Variance</th>
                        <td>50.066</td>
                    </tr>
                    <tr>
                        <th>Memory size</th>
                        <td>2.0 MiB</td>
                    </tr>
                </table>
            </div>
        </div>
        <div role="tabpanel" class="tab-pane col-md-8 col-md-offset-2" id="histogram-5709218495563483937">
            <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAlgAAAGQCAYAAAByNR6YAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAPYQAAD2EBqD%2BnaQAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAIABJREFUeJzt3XtUVXX%2B//GXcFAOooKJWi1bmkBlWZIo3rLxQo4J5iDmt8xRK51EMVx5ybTR0fCSWOb41cpy/KZ%2Bv5GWNRapzYyjjhfQanRywi%2BYt76kIIjKTbns3x/9OKsTzYj0wcM55/lYy9U6n8/e%2B7z327Pzxd77bBpZlmUJAAAAxvi4ugAAAABPQ8ACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIbZXF2At7AsSwUFxaqqslxdikv4%2BDRSy5ZN6QE9oAf0gB6IHkg3rgchIc3qbdv/DmewbpBGjRrJx6eRq8twGR%2BfRvSAHtAD0QOJHkj0QPL8HhCwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwm6sLgPeInL3N1SVcl0%2BTeru6BACAm%2BIMFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABjm8oBVUFCg6OhopaenO8YOHz6sESNGKCIiQv3799emTZuc1tmyZYuio6PVpUsXxcXF6csvv3TMVVZWasmSJerVq5ciIiI0ceJE5ebmOubz8/OVkJCgyMhIRUVFKTk5WRUVFbV%2BbwAAgGtxacD6/PPPNXLkSJ0%2BfdoxdvHiRU2YMEHDhg3TwYMHlZycrEWLFunIkSOSpPT0dC1YsECLFy/WwYMHNXToUE2cOFGlpaWSpNWrV2vv3r16//33tWfPHvn7%2B2vOnDmO7SclJSkgIEB79uzR5s2btX//fq1bt65W7w0AAFAbLgtYW7Zs0bRp0zR16lSn8R07digoKEijRo2SzWZTz549FRsbq40bN0qSNm3apCFDhqhr167y8/PT2LFjFRwcrLS0NMf8%2BPHjdfPNNyswMFCzZ8/W7t27debMGZ06dUoZGRmaPn267Ha72rVrp4SEBMe2r/XeAAAAteGyB4326dNHsbGxstlsTiErKytL4eHhTsuGhoZq8%2BbNkqTs7GwNHz68xnxmZqYuX76ss2fPOq3fqlUrtWjRQseOHZMkBQUFqU2bNo75jh07KicnR5cuXbrme9dWbm6u8vLynMZCQkLk79/surbjSXx9XX41%2BrrZbGZrru6BO/bCFHpADyR6INEDyfN74LKAFRIS8pPjxcXFstvtTmP%2B/v4qKSm55nxxcbEkKSAgoMZ89dyP161%2BXb3%2Bv3vv2kpNTdXKlSudxiZPnqzExMTr2g5cKzi4ab1st3lz%2B7UX8nD0gB5I9ECiB5Ln9qDB/aocu92uy5cvO42VlZWpadOmjvmysrIa88HBwY5wVH0/1o/Xtyyrxlz166ZNm17zvWtr5MiR6t%2B/v9NYSEiILl0qVWVl1XVty1O4408oFy4UG92er6%2BPmje3e/3ngB7QA3pAD6Qb14P6%2BmH5WhpcwAoPD9fevXudxrKzsxUWFiZJCgsLU1ZWVo35vn37qkWLFmrTpo2ys7Mdl/ry8vJUWFio8PBwVVVVqbCwUOfPn1erVq0kScePH1fbtm3VrFmza753bbVu3VqtW7euMX7hQrEqKrzzQHJH9fV3VVlZ5fWfA3pADyR6INEDyXN70OBOK0RHR%2Bv8%2BfNat26dysvLdeDAAW3dutVx31V8fLy2bt2qAwcOqLy8XOvWrVN%2Bfr6io6MlSXFxcVq9erXOnDmjoqIiLVy4UN27d9dtt92m9u3bq2vXrlq4cKGKiop05swZrVq1SvHx8bV6bwAAgNpocGewgoODtXbtWiUnJ2vFihVq2bKl5syZox49ekiSevbsqblz52revHk6d%2B6cQkNDtWbNGgUFBUmSJk2apIqKCo0aNUrFxcWKiorS8uXLHdtfsWKF5s%2BfrwEDBsjHx0fDhg1TQkJCrd4bAACgNhpZlmW5ughv4c2XCG02H0Wn7HF1Gdfl06TeRrdns/koOLip138O6AE9oAf0QLpxPQgJcc03%2BBvcJUIAAAB3R8ACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDbK4uAGioBi/f6%2BoSrsunSb1dXQIA4P/jDBYAAIBhBCwAAADDGmzAOnr0qEaNGqXIyEj16dNHL730kq5evSpJ2rVrl2JjY9WlSxcNHjxYO3fudFp3zZo16tu3r7p06aLRo0frm2%2B%2BccyVlJRo1qxZioqKUteuXTVjxgwVFxc75k%2BcOKExY8YoIiJCffr00euvv35jdhgAAHiMBhmwqqqq9Jvf/EaDBg1SRkaGNm/erL/97W9as2aNTp48qcTERD377LM6dOiQEhMTlZSUpHPnzkmStmzZovXr1%2Bvtt99Wenq67r77bk2ZMkWWZUmSFixYoO%2B%2B%2B07bt2/Xjh079N133yklJUWSVF5ermeeeUadO3dWenq63nzzTW3cuFGffvqpy3oBAADcT4MMWBcvXlReXp6qqqocwcjHx0d2u11btmxRZGSkBg4cKJvNpocffljdunVTamqqJOm9997T448/rrCwMDVp0kTPPfeccnJylJ6ertLSUm3dulVTpkxRUFCQbrrpJk2bNk0ffPCBSktLdfDgQeXm5mrKlClq3LixOnXqpNGjR2vjxo2ubAcAAHAzDfJbhMHBwRo7dqyWLFmil19%2BWZWVlRowYIDGjh2rxMREhYeHOy0fGhqqzMxMSVJ2drbGjx/vmPPz81P79u2VmZmpoKAglZeXO63fsWNHlZWV6eTJk8rKylKHDh3UuHFjp22/%2Beab11V/bm6u8vLynMZCQkLk79/surbjSXx9G2SW9yg2W8PvcfXnwJs/D/SAHkj0QPL8HjTIgFVVVSV/f3%2B9%2BOKLio%2BP16lTpzR58mStWLFCxcXFstvtTsv7%2B/urpKREkv7tfFFRkSQpICDAMVe9bHFx8U%2Bua7fbHduurdTUVK1cudJpbPLkyUpMTLyu7QDXIzi4qatLqLXmze3XXsjD0QN6INEDyXN70CAD1meffabt27dr27ZtkqSwsDBNmjRJycnJuv/%2B%2B1VWVua0fFlZmZo2/f4fF7vd/i/nq4NVaWmpY/nS0lJJUmBgoAICAhyvq/1w2doaOXKk%2Bvfv7zQWEhKiS5dKVVlZdV3b8hSe%2BhNKQ3LhQvG1F3IxX18fNW9u9/pjgR7QA3pw43rgqh8%2BG2TA%2Bu677xzfGKxms9nk5%2Ben8PBwHT161GkuOztb99xzj6Tvw1hWVpb69esn6fsb10%2BePKnw8HB16NBBfn5%2Bys7O1n333SdJOn78uOMyYn5%2Bvk6ePKmKigrZbDbHtsPCwq6r/tatW6t169Y1xi9cKFZFhXceSKh/7vTZqqyscqt66wM9oAcSPZA8twcN8rRCnz59lJeXp9dff12VlZU6c%2BaMVq9erdjYWA0dOlQZGRlKS0tTRUWF0tLSlJGRoUceeUSSNHz4cG3YsEGZmZm6cuWKli1bplatWikyMlJ2u12DBw9WSkqKCgoKVFBQoJSUFMXExMjf319RUVEKDg7WsmXLdOXKFWVmZmr9%2BvWKj493cUcAAIA7aWRVf02vgdm3b5%2BWL1%2Bub775Rs2aNdPQoUM1adIkNW7cWHv27FFKSopOnz6tW2%2B9VdOnT9eDDz4oSbIsS3/4wx%2B0ceNGFRQUqHPnzvrd736nDh06SJKKioq0ZMkS/eUvf1F5ebkGDBigF1980XH58NSpU5o/f74OHz6sgIAAPfHEE5owYYKRffLmM1g2m4%2BiU/a4ugyP5g6/Ksdm81FwcFOvPxboAT2gBzeuByEhrvmCWYMNWJ7I2w8kAlb9ImC5B3pADyR6IHl%2BwGqQlwgBAADcGQELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMPqFLAqKytN1wEAAOAx6hSw%2Bvbtq5dfflnZ2dmm6wEAAHB7dQpYkydP1hdffKGYmBiNGDFC7777ri5fvmy6NgAAALdUp4D12GOP6d1339W2bdvUq1cvrVmzRn369NFzzz2nffv2ma4RAADArfysm9zbt2%2BvqVOnatu2bZo0aZL%2B/Oc/66mnnlL//v31hz/8gXu1AACAV7L9nJUPHz6sDz/8UGlpabp69aqio6MVFxenc%2BfO6bXXXtM//vEPvfLKK6ZqBQAAcAt1ClirVq3SRx99pFOnTqlz586aOnWqYmJiFBgY6FjG19dXv/3tb40VCgAA4C7qFLA2bNigoUOHKj4%2BXqGhoT%2B5TMeOHTVt2rSfVRwAAIA7qlPA2r17t4qKilRYWOgYS0tLU8%2BePRUcHCxJ6tSpkzp16mSmSgAAADdSp5vc//nPf2rQoEFKTU11jC1dulSxsbH63//9X2PFAQAAuKM6BayXX35ZDz30kKZOneoY%2B9Of/qS%2Bfftq8eLFxooDAABwR3UKWEePHtWECRPUuHFjx5ivr68mTJigv//978aKAwAAcEd1CliBgYE6ffp0jfGzZ8/K39//ZxcFAADgzuoUsAYNGqR58%2BZp3759KioqUnFxsQ4cOKD58%2BcrOjraSGGFhYWaMWOGoqKi1K1bNyUkJCg3N1fS98/fGjFihCIiItS/f39t2rTJad0tW7YoOjpaXbp0UVxcnL788kvHXGVlpZYsWaJevXopIiJCEydOdGxXkvLz85WQkKDIyEhFRUUpOTlZFRUVRvYJAAB4hzoFrOeee0633367nnzySXXr1k2RkZEaN26cQkNDNWPGDCOFJSYmqqSkRJ999pl27twpX19fvfjii7p48aImTJigYcOG6eDBg0pOTtaiRYt05MgRSVJ6eroWLFigxYsX6%2BDBgxo6dKgmTpyo0tJSSdLq1au1d%2B9evf/%2B%2B9qzZ4/8/f01Z84cx/smJSUpICBAe/bs0ebNm7V//36tW7fOyD4BAADvUKfHNNjtdr3xxhs6ceKEjh07Jj8/P3Xs2FHt27c3UtRXX32lw4cPa9%2B%2BfY6Hly5YsEB5eXnasWOHgoKCNGrUKElSz549FRsbq40bN%2Bree%2B/Vpk2bNGTIEHXt2lWSNHbsWKWmpiotLU3Dhw/Xpk2bNG3aNN18882SpNmzZ6tPnz46c%2BaMqqqqlJGRod27d8tut6tdu3ZKSEjQ0qVL9fTTTxvZNwAA4Pl%2B1q/K6dChgzp06GCqFocjR44oNDRU7733nv7nf/5HpaWleuCBBzRz5kxlZWUpPDzcafnQ0FBt3rxZkpSdna3hw4fXmM/MzNTly5d19uxZp/VbtWqlFi1a6NixY5KkoKAgtWnTxjHfsWNH5eTk6NKlS2revHmt6s/NzVVeXp7TWEhIiPz9m9W%2BCR7G1/dn/dpL1ILN1vB7XP058ObPAz2gBxI9kDy/B3UKWCdOnND8%2BfP1%2Beefq7y8vMb8119//bOKunjxoo4dO6Z77rlHW7ZsUVlZmWbMmKGZM2eqVatWstvtTsv7%2B/urpKREklRcXPwv54uLiyVJAQEBNear5368bvXrkpKSWges1NRUrVy50mls8uTJSkxMrNX6QF0EBzd1dQm11ry5/doLeTh6QA8keiB5bg/qFLDmzZunnJwcTZs2Tc2amT8rU/34h9mzZ6tJkyYKDAxUUlKSHn30UcXFxamsrMxp%2BbKyMjVt%2Bv0/Lna7/Sfng4ODHWGp%2Bn6sH69vWVaNuerX1duvjZEjR6p///5OYyEhIbp0qVSVlVW13o4n8dSfUBqSCxeKXV3CNfn6%2Bqh5c7vXHwv0gB7QgxvXA1f98FmngPXll1/qv/7rvxQREWG6HknfX9KrqqpSeXm5mjRpIkmqqvq%2B%2BXfddZf%2B%2B7//22n57OxshYWFSZLCwsKUlZVVY75v375q0aKF2rRpo%2BzsbMdlwry8PBUWFio8PFxVVVUqLCzU%2BfPn1apVK0nS8ePH1bZt2%2BsKkq1bt1br1q1rjF%2B4UKyKCu88kFD/3OmzVVlZ5Vb11gd6QA8keiB5bg/qdFohODj4us7oXK9evXqpXbt2euGFF1RcXKyCggK9%2BuqrGjhwoGJiYnT%2B/HmtW7dO5eXlOnDggLZu3eq47yo%2BPl5bt27VgQMHVF5ernXr1ik/P9/x%2BIi4uDitXr1aZ86cUVFRkRYuXKju3bvrtttuU/v27dW1a1ctXLhQRUVFOnPmjFatWqX4%2BPh621cAAOB56hSwRo8erVdeeUWXL182XY8kyc/PT%2BvXr5evr68GDRqkQYMGqW3btlq4cKGCg4O1du1abdu2TVFRUZozZ47mzJmjHj16SPr%2BW4Vz587VvHnz1L17d33yySdas2aNgoKCJEmTJk3Sgw8%2BqFGjRunBBx/UlStXtHz5csd7r1ixQhUVFRowYIAeffRRPfDAA0pISKiX/QQAAJ6pkWVZ1vWuNHr0aP39739XZWWlbrrpJqdfmSNJf/7zn40V6Em8%2BRKhzeaj6JQ9ri7Do32a1NvVJVyTzeaj4OCmXn8s0AN6QA9uXA9CQlzzDf463YMVFRWlqKgo07UAAAB4hDoFrMmTJ5uuAwAAwGPU%2BbvzmZmZmjVrlv7jP/5D586d08aNG5Wenm6yNgAAALdUp4D11VdfacSIEfr222/11Vdf6erVq/r666/15JNPaufOnaZrBAAAcCt1ClgpKSl68skntX79evn5%2BUmSXnrpJf3617%2Bu8QRzAAAAb1PnM1jDhg2rMf7YY4/pm2%2B%2B%2BdlFAQAAuLM6BSw/Pz8VFRXVGM/Jyanxu/wAAAC8TZ0C1sCBA7Vs2TJduHDBMXb8%2BHElJyfrF7/4hanaAAAA3FKdAtbMmTNVVlamXr16qbS0VHFxcYqJiZHNZtOMGTNM1wgAAOBW6vQcrMDAQL377rvav3%2B//vnPf6qqqkrh4eF64IEH5ONT5yc/AAAAeIQ6BaxqPXv2VM%2BePU3VAgAA4BHqFLD69%2B%2BvRo0a/ct5fhchAADwZnUKWL/61a%2BcAlZ5eblOnTql3bt3KykpyVhxAAAA7qhOASsxMfEnxzds2KDPP/9cv/71r39WUQAAAO7M6B3p/fr1065du0xuEgAAwO0YDVgZGRlq0qSJyU0CAAC4nTpdIvzxJUDLslRUVKRjx45xeRAAAHi9OgWsW265pca3CP38/DRmzBjFxsYaKQwAAMBd1SlgLV682HQdAAAAHqNOAevgwYO1XrZbt251eQsAAAC3VaeANXbsWFmW5fhTrfqyYfVYo0aN9PXXXxsoEwAAwH3UKWD9/ve/16JFizRz5kz16NFDfn5%2BOnz4sObNm6fHH39c/fr1M10nAACA26jTYxqWLFmiuXPnauDAgQoMDFSTJk3UvXt3zZ8/X2vXrtWtt97q%2BAMAAOBt6hSwcnNzdfPNN9cYDwwM1IULF352UQAAAO6sTgGrS5cueuWVV1RUVOQYKyws1NKlS9WzZ09jxQEAALijOt2DNWfOHI0ZM0Z9%2B/ZV%2B/btJUknTpxQSEiI3nnnHZP1AQAAuJ06BayOHTsqLS1NW7du1fHjxyVJjz/%2BuIYMGSK73W60QAAAAHdTp4AlSc2bN9eIESP07bffql27dpK%2Bf5o7AACAt6vTPViWZSklJUXdunVTTEyMzp49q5kzZ2rWrFkqLy83XSMAAIBbqVPAWr9%2BvT766CPNnTtXjRs3liQNHDhQf/nLX/Taa68ZLRAAAMDd1Clgpaam6re//a3i4uIcT29/%2BOGHlZycrE8%2B%2BcRogQAAAO6mTgHr22%2B/1V133VVj/I477tD58%2Bd/dlEAAADurE4B69Zbb9WRI0dqjO/atctxwzsAAIC3qtO3CJ966in97ne/07lz52RZlvbv3693331X69ev16xZs0zXCAAA4FbqFLCGDx%2BuiooKrV69WmVlZfrtb3%2Brm266SVOnTtVjjz1mukYAAAC3UqeA9cc//lG//OUvNXLkSBUUFMiyLN10002mawMAAHBLdboH66WXXnLczN6yZUvCFQAAwA/UKWC1b99ex44dM10LAACAR6jTJcKwsDBNmzZNb731ltq3b68mTZo4zS9atMhIcQAAAO6oTgHr9OnT6tq1qyQpLy/PaEEAAADurtYBa9GiRXr22WcVEBCg9evX12dNAAAAbq3W92C98847Ki0tdRp76qmnlJuba7woAAAAd1brgGVZVo2xL774QleuXDFaEAAAgLur07cIAQAA8K8RsAAAAAy7roDVqFGj%2BqoDAADAY1zXYxpeeuklp2delZeXa%2BnSpWratKnTcjwHCwAAeLNaB6xu3brVeOZVRESELly4oAsXLhgvDAAAwF3VOmDx7CsAAIDaafA3uVdWVmr06NF6/vnnHWO7du1SbGysunTposGDB2vnzp1O66xZs0Z9%2B/ZVly5dNHr0aH3zzTeOuZKSEs2aNUtRUVHq2rWrZsyYoeLiYsf8iRMnNGbMGEVERKhPnz56/fXX638nAQCAR2nwAWvlypU6dOiQ4/XJkyeVmJioZ599VocOHVJiYqKSkpJ07tw5SdKWLVu0fv16vf3220pPT9fdd9%2BtKVOmOJ7jtWDBAn333Xfavn27duzYoe%2B%2B%2B04pKSmSvr%2Bn7JlnnlHnzp2Vnp6uN998Uxs3btSnn35643ccAAC4rQYdsPbv368dO3booYcecoxt2bJFkZGRGjhwoGw2mx5%2B%2BGF169ZNqampkqT33ntPjz/%2BuMLCwtSkSRM999xzysnJUXp6ukpLS7V161ZNmTJFQUFBuummmzRt2jR98MEHKi0t1cGDB5Wbm6spU6aocePG6tSpk0aPHq2NGze6qgUAAMAN1emXPd8I%2Bfn5mj17tlatWqV169Y5xrOzsxUeHu60bGhoqDIzMx3z48ePd8z5%2Bfmpffv2yszMVFBQkMrLy53W79ixo8rKynTy5EllZWWpQ4cOaty4sdO233zzzeuqPTc3t8YXAkJCQuTv3%2By6tuNJfH0bdJb3CDZbw%2B9x9efAmz8P9IAeSPRA8vweNMiAVVVVpenTp2vcuHG68847neaKi4tlt9udxvz9/VVSUnLN%2BaKiIklSQECAY6562eLi4p9c1263O7ZdW6mpqVq5cqXT2OTJk5WYmHhd2wGuR3Bw02sv1EA0b26/9kIejh7QA4keSJ7bgwYZsN544w01btxYo0ePrjFnt9tVVlbmNFZWVuZ4Fte/m68OVqWlpY7lq3%2BBdWBgoAICAmr8QusfLltbI0eOVP/%2B/Z3GQkJCdOlSqSorq65rW57CU39CaUguXCi%2B9kIu5uvro%2BbN7V5/LNADekAPblwPXPXDZ4MMWB999JFyc3MVGRkpSY7A9Kc//UmjRo3S0aNHnZbPzs7WPffcI0kKCwtTVlaW%2BvXrJ%2Bn7G9dPnjyp8PBwdejQQX5%2BfsrOztZ9990nSTp%2B/LjjMmJ%2Bfr5OnjypiooK2Ww2x7bDwsKuq/7WrVurdevWNcYvXChWRYV3Hkiof%2B702aqsrHKreusDPaAHEj2QPLcHDfK0wrZt2/TFF1/o0KFDOnTokGJiYhQTE6NDhw5p6NChysjIUFpamioqKpSWlqaMjAw98sgjkqThw4drw4YNyszM1JUrV7Rs2TK1atVKkZGRstvtGjx4sFJSUlRQUKCCggKlpKQoJiZG/v7%2BioqKUnBwsJYtW6YrV64oMzNT69evV3x8vIs7AgAA3EmDPIP173Ts2FH/%2BZ//qZSUFM2ePVu33nqrfv/736tDhw6SpPj4eF2%2BfFmTJk1SQUGBOnfurDfeeEN%2Bfn6SpLlz52rJkiWKjY1VeXm5BgwYoBdffFGSZLPZtHbtWs2fP1%2B9e/dWQECARo8erbi4OJftLwAAcD%2BNrOoHRKHeefMlQpvNR9Epe1xdhkf7NKm3q0u4JpvNR8HBTb3%2BWKAH9IAe3LgehIS45hv8DfISIQAAgDsjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYJjN1QUAMGPw8r2uLqHWPpv2gKtLAIB6xRksAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAplI6/AAAQQElEQVQAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMJurC8DPM3j5XleXAAAAfoQzWAAAAIYRsAAAAAwjYAEAABhGwAIAADCswQaszMxMjRs3Tt27d1fv3r01Y8YMFRQUSJIOHz6sESNGKCIiQv3799emTZuc1t2yZYuio6PVpUsXxcXF6csvv3TMVVZWasmSJerVq5ciIiI0ceJE5ebmOubz8/OVkJCgyMhIRUVFKTk5WRUVFTdmpwEAgEdokAGrrKxMTz/9tCIiIvS3v/1NH3/8sQoLC/XCCy/o4sWLmjBhgoYNG6aDBw8qOTlZixYt0pEjRyRJ6enpWrBggRYvXqyDBw9q6NChmjhxokpLSyVJq1ev1t69e/X%2B%2B%2B9rz5498vf315w5cxzvnZSUpICAAO3Zs0ebN2/W/v37tW7dOle0AQAAuKkGGbBycnJ05513atKkSWrcuLGCg4M1cuRIHTx4UDt27FBQUJBGjRolm82mnj17KjY2Vhs3bpQkbdq0SUOGDFHXrl3l5%2BensWPHKjg4WGlpaY758ePH6%2Babb1ZgYKBmz56t3bt368yZMzp16pQyMjI0ffp02e12tWvXTgkJCY5tAwAA1EaDfA7W7bffrrfeestpbPv27br77ruVlZWl8PBwp7nQ0FBt3rxZkpSdna3hw4fXmM/MzNTly5d19uxZp/VbtWqlFi1a6NixY5KkoKAgtWnTxjHfsWNH5eTk6NKlS2revHmt6s/NzVVeXp7TWEhIiPz9m9VqfcDT%2Bfo2yJ/tbojqfacH9OCH//VGnt6DBhmwfsiyLC1fvlw7d%2B7Uhg0b9M4778hutzst4%2B/vr5KSEklScXHxv5wvLi6WJAUEBNSYr5778brVr0tKSmodsFJTU7Vy5UqnscmTJysxMbFW6wOernlz%2B7UX8nD0gB5I9EDy3B406IBVVFSkWbNm6ejRo9qwYYPuuOMO2e12Xb582Wm5srIyNW3aVNL3gaisrKzGfHBwsCMsVd%2BP9eP1LcuqMVf9unr7tTFy5Ej179/faSwkJESXLpWqsrKq1tsBPJU3Hwu%2Bvj5q3txOD%2BgBPbhBPQgOrv2/3yY12IB1%2BvRpjR8/Xrfccos2b96sli1bSpLCw8O1d6/zr4fJzs5WWFiYJCksLExZWVk15vv27asWLVqoTZs2ys7OdlwmzMvLU2FhocLDw1VVVaXCwkKdP39erVq1kiQdP35cbdu2VbNmtb%2B817p1a7Vu3brG%2BIULxaqo8M4DCfihysoqrz8W6AE9kOiB5Lk9aJAXPi9evKgxY8bo/vvv19tvv%2B0IV5IUHR2t8%2BfPa926dSovL9eBAwe0detWx31X8fHx2rp1qw4cOKDy8nKtW7dO%2Bfn5io6OliTFxcVp9erVOnPmjIqKirRw4UJ1795dt912m9q3b6%2BuXbtq4cKFKioq0pkzZ7Rq1SrFx8e7pA8AAMA9NcgzWB988IFycnL06aefatu2bU5zX375pdauXavk5GStWLFCLVu21Jw5c9SjRw9JUs%2BePTV37lzNmzdP586dU2hoqNasWaOgoCBJ0qRJk1RRUaFRo0apuLhYUVFRWr58uWP7K1as0Pz58zVgwAD5%2BPho2LBhSkhIuHE7DwAA3F4jy7IsVxfhLerjEuHg5XuvvRDQwHw27QGPvCRQGzabj4KDm3r1LQP0gB5IN64HISGu%2BQZ/g7xECAAA4M4IWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADLO5ugAA3ic6ZY%2BrS7gunyb1dnUJANwMZ7AAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADCNgAQAAGEbAAgAAMIyABQAAYBgBCwAAwDACFgAAgGEELAAAAMMIWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwm6sLAICGbvDyva4u4bp8mtTb1SUAXo8zWAAAAIYRsAAAAAwjYAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAtZPyM/PV0JCgiIjIxUVFaXk5GRVVFS4uiwAAOAmCFg/ISkpSQEBAdqzZ482b96s/fv3a926da4uCwAAuAkeNPojp06dUkZGhnbv3i273a527dopISFBS5cu1dNPP%2B3q8gDgmtzpwag8FBWeijNYP5KVlaWgoCC1adPGMdaxY0fl5OTo0qVLLqwMAAC4C85g/UhxcbHsdrvTWPXrkpISNW/e/JrbyM3NVV5entNYSEiI/P2bmSsUADyAO51tk6TPpj1gZDu%2Bvj5O//VGnt4DAtaPBAQEqLS01Gms%2BnXTpk1rtY3U1FStXLnSaaxbt2565ZVX1Lp1azOF/n%2BHkn9pdHv1JTc3V6mpqRo5cqTxHrgLekAPJHog0QPp%2Bx7813%2B9RQ88uAeeGRt/hrCwMBUWFur8%2BfOOsePHj6tt27Zq1qx2Z6BGjhypDz74wPFn6dKlOnjwYI2zWt4kLy9PK1eupAf0gB7QA3ogeiB5fg84g/Uj7du3V9euXbVw4ULNnz9fFy5c0KpVqxQfH1/rbbRu3doj0zgAAKgdzmD9hBUrVqiiokIDBgzQo48%2BqgceeEAJCQmuLgsAALgJzmD9hFatWmnFihWuLgMAALgp33nz5s1zdRHeoGnTpurevXutb5T3RPSAHkj0QKIHEj2Q6IHk2T1oZFmW5eoiAAAAPAn3YAEAABhGwAIAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2DVo/z8fCUkJCgyMlJRUVFKTk5WRUWFq8u6YQoKChQdHa309HTH2OHDhzVixAhFRESof//%2B2rRpkwsrrB%2BZmZkaN26cunfvrt69e2vGjBkqKCiQ5B37X23//v0aMWKE7r//fvXu3VsLFixQWVmZJO/qQ2VlpUaPHq3nn3/eMbZr1y7FxsaqS5cuGjx4sHbu3OnCCutXWlqaOnXqpIiICMef6dOnS/KePhQWFmrGjBmKiopSt27dlJCQoNzcXEnecSz88Y9/dPr7j4iI0D333KN77rlHkgd/DizUmyeeeMJ67rnnrJKSEuv06dPWkCFDrDVr1ri6rBvi0KFD1sCBA63w8HDrwIEDlmVZVmFhodW9e3drw4YNVnl5ubVv3z4rIiLCOnz4sIurNae0tNTq3bu39dprr1lXrlyxCgoKrPHjx1u/%2Bc1vvGL/q%2BXn51udO3e23n//fauystI6d%2B6cFRMTY7322mte1QfLsqzly5dbd955pzVz5kzLsizrxIkTVufOna3PPvvMKi8vtz755BPr3nvvtc6ePeviSuvH4sWLreeff77GuDf14YknnrAmTZpkXbx40bp8%2BbI1efJka8KECV53LFQ7e/as1bt3b%2BvDDz/06M8BZ7DqyalTp5SRkaHp06fLbrerXbt2SkhI0MaNG11dWr3bsmWLpk2bpqlTpzqN79ixQ0FBQRo1apRsNpt69uyp2NhYj%2BpJTk6O7rzzTk2aNEmNGzdWcHCwRo4cqYMHD3rF/ldr2bKl9u3bp7i4ODVq1EiFhYW6cuWKWrZs6VV92L9/v3bs2KGHHnrIMbZlyxZFRkZq4MCBstlsevjhh9WtWzelpqa6sNL6849//MNxpuKHvKUPX331lQ4fPqzFixerefPmCgwM1IIFCzRt2jSvOhaqWZal6dOn6xe/%2BIUeeeQRj/4cELDqSVZWloKCgtSmTRvHWMeOHZWTk6NLly65sLL616dPH3322Wd6%2BOGHncazsrIUHh7uNBYaGqrMzMwbWV69uv322/XWW2/J19fXMbZ9%2B3bdfffdXrH/PxQYGChJevDBBxUbG6uQkBDFxcV5TR/y8/M1e/ZsLVu2THa73TGenZ3tFfsvSVVVVTp69Kj%2B%2Bte/ql%2B/furbt69efPFFXbx40Wv6cOTIEYWGhuq9995TdHS0%2BvTpoyVLligkJMRrjoUf%2Buijj5Sdne24ZO7JnwMCVj0pLi52%2Bp%2BqJMfrkpISV5R0w4SEhMhms9UY/6me%2BPv7e2w/LMvSq6%2B%2Bqp07d2r27Nlet//VduzYod27d8vHx0dTpkzxij5UVVVp%2BvTpGjdunO68806nOW/Y/2oFBQXq1KmTBg0apLS0NL377rs6efKkpk%2Bf7jV9uHjxoo4dO6aTJ09qy5Yt%2BvDDD3Xu3DnNnDnTa3pQraqqSqtXr9Yzzzzj%2BAHMk3tAwKonAQEBKi0tdRqrft20aVNXlORydrvdcZNztbKyMo/sR1FRkaZMmaKtW7dqw4YNuuOOO7xq/3/I399fbdq00fTp07Vnzx6v6MMbb7yhxo0ba/To0TXmvGH/q7Vq1UobN25UfHy87Ha7brnlFk2fPl27d%2B%2BWZVle0YfGjRtLkmbPnq3AwEC1atVKSUlJ2rVrl9f0oFp6erpyc3MVHx/vGPPk44GAVU/CwsJUWFio8%2BfPO8aOHz%2Butm3bqlmzZi6szHXCw8OVlZXlNJadna2wsDAXVVQ/Tp8%2BreHDh6uoqEibN2/WHXfcIcl79l%2BSvvjiC/3yl7/U1atXHWNXr16Vn5%2BfQkNDPb4PH330kTIyMhQZGanIyEh9/PHH%2BvjjjxUZGelVn4PMzEylpKTIsizH2NWrV%2BXj46N7773XK/oQGhqqqqoqlZeXO8aqqqokSXfddZdX9KDa9u3bFR0drYCAAMeYJx8PBKx60r59e3Xt2lULFy5UUVGRzpw5o1WrVjkld28THR2t8%2BfPa926dSovL9eBAwe0detWDR8%2B3NWlGXPx4kWNGTNG999/v95%2B%2B221bNnSMecN%2B1/tjjvuUFlZmZYtW6arV6/q//7v/7RkyRLFx8dr0KBBHt%2BHbdu26YsvvtChQ4d06NAhxcTEKCYmRocOHdLQoUOVkZGhtLQ0VVRUKC0tTRkZGXrkkUdcXbZxQUFB2rhxo9566y1VVFQoJydHS5cu1a9%2B9SsNGzbMK/rQq1cvtWvXTi%2B88IKKi4tVUFCgV199VQMHDlRMTIzHHws/9Pnnn6tbt25OYx59PLj0O4weLi8vz0pMTLS6d%2B9u9ejRw1q8eLFVUVHh6rJuqB8%2BpsGyLOvIkSPWyJEjrYiICGvAgAHW%2B%2B%2B/78LqzFu7dq0VHh5u3XfffVaXLl2c/liW5%2B//D2VlZVnjxo2zIiMjrX79%2BlmvvPKKdeXKFcuyvKsPlmVZM2fOdDymwbIsa/fu3dbQoUOtLl26WEOGDLH%2B%2Bte/urC6%2BpWenu74u%2B7Ro4e1YMECq6yszLIs7%2BnD2bNnraSkJKt3795WZGSkNWPGDOvixYuWZXnXsdClS5ef/Dv21M9BI8v6wblbAAAA/GxcIgQAADCMgAUAAGAYAQsAAMAwAhYAAIBhBCwAAADDCFgAAACGEbAAAAAMI2ABAAAYRsACAAAwjIAFAABgGAELAADAMAIWAACAYQQsAAAAwwhYAAAAhhGwAAAADPt/WYqe5Kgh7/IAAAAASUVORK5CYII%3D"/>
        </div>
        <div role="tabpanel" class="tab-pane col-md-12" id="common-5709218495563483937">

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">16.0</td>
        <td class="number">3563</td>
        <td class="number">1.4%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">15.0</td>
        <td class="number">3379</td>
        <td class="number">1.3%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">17.0</td>
        <td class="number">3080</td>
        <td class="number">1.2%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">16.5</td>
        <td class="number">2963</td>
        <td class="number">1.2%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">14.0</td>
        <td class="number">2954</td>
        <td class="number">1.1%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">15.4</td>
        <td class="number">2878</td>
        <td class="number">1.1%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">14.5</td>
        <td class="number">2726</td>
        <td class="number">1.1%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">13.0</td>
        <td class="number">2663</td>
        <td class="number">1.0%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">18.0</td>
        <td class="number">2617</td>
        <td class="number">1.0%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">17.5</td>
        <td class="number">2616</td>
        <td class="number">1.0%</td>
        <td>
            <div class="bar" style="width:2%">&nbsp;</div>
        </td>
</tr><tr class="other">
        <td class="fillremaining">Other values (531)</td>
        <td class="number">227545</td>
        <td class="number">88.5%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr>
</table>
        </div>
        <div role="tabpanel" class="tab-pane col-md-12"  id="extreme-5709218495563483937">
            <p class="h4">Minimum 5 values</p>

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">3.4</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:7%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">3.7</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:7%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">3.8</td>
        <td class="number">4</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:27%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">3.9</td>
        <td class="number">5</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:34%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">4.0</td>
        <td class="number">15</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr>
</table>
            <p class="h4">Maximum 5 values</p>

<table class="freq table table-hover">
    <thead>
    <tr>
        <td class="fillremaining">Value</td>
        <td class="number">Count</td>
        <td class="number">Frequency (%)</td>
        <td style="min-width:200px">&nbsp;</td>
    </tr>
    </thead>
    <tr class="">
        <td class="fillremaining">64.6</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">65.0</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">65.8</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">66.0</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr><tr class="">
        <td class="fillremaining">70.5</td>
        <td class="number">1</td>
        <td class="number">0.0%</td>
        <td>
            <div class="bar" style="width:100%">&nbsp;</div>
        </td>
</tr>
</table>
        </div>
    </div>
</div>
</div>
    <div class="row headerrow highlight">
        <h1>Correlations</h1>
    </div>
    <div class="row variablerow">
    <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAt8AAAKTCAYAAADBkGTTAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAPYQAAD2EBqD%2BnaQAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAIABJREFUeJzs3Xt8zvX/x/HHtfMwmzDLOYetbxRjTGKYlZJjZEUkpSQjUXQgOStREfnKIUnmi8Q3xbeDQ4pVRnIoJjZz2MFpBztfvz/Wrp/Lhovrc23G83677bbtc3h93td7167r9Xld78/7YzKbzWZERERERMThnEq6ASIiIiIitwol3yIiIiIixUTJt4iIiIhIMVHyLSIiIiJSTJR8i4iIiIgUEyXfIiIiIiLFRMm3iIiIiEgxUfItIiIiIlJMlHyLiIiIiBQTl5JugIiIXLtjx47Rvn37y653dXWlXLly1K5dm7Zt2/LEE09Qrly5YmyhiIgUxaTby4uIlD4XJ9/%2B/v6FEuvs7GxOnz5NfHw8AFWrVmXx4sXUqlWr2NsqIiL/T8m3iEgpdHHyvWTJEoKDg4vcbseOHQwePJjU1FQCAwNZvnx5cTZTREQuoTHfIiI3seDgYF566SUAoqOj%2BeOPP0q4RSIitzYl3yIiN7n777/f8vPu3btLsCUiIqILLkVEbnJeXl6Wn9PS0qzW/fLLL3z66afs3LmTs2fPUr58eRo3bkzfvn259957i4x3/vx5li9fzubNmzl06BCpqal4enpSs2ZN2rVrR79%2B/fD29rbaJyAgAIBt27YxdepUvvvuO5ycnGjQoAELFy7ExcWF3bt3s3jxYvbt28eJEydwd3fnjjvuICwsjN69exd5wWhGRgbLly9n/fr1HDp0iOzsbKpUqULLli0ZMGAAtWvXttp%2Bx44d9OvXj0aNGvHZZ5/x6aefsmbNGo4ePYqrqysNGjSgb9%2B%2BhIWFXU9Xi4hclZJvEZGb3NGjRy0/%2B/n5WX6ePn068%2BfPB8Db2xt/f38SEhL47rvv%2BO6773jmmWd4%2BeWXrWIdOXKE/v37c%2BLECVxcXKhZsybVqlUjPj6evXv3snfvXr766itWrVpF2bJlC7UlIiKC6Oho/P39OX36NJUrV8bFxYWNGzcyfPhwcnJyqFChAvXq1SMtLY3ff/%2Bd3bt3s3btWpYvX26VgJ88eZKnnnqKw4cPA1C7dm3Kli1LTEwMkZGRrFmzhqlTp9KxY8dC7cjOzmbgwIH8/PPPVKhQgbp16/L333%2Bzfft2tm/fzrhx43j88cft63gRkaKYRUSk1ImLizP7%2B/ub/f39zdu3b7/itq%2B88orZ39/f3KBBA3NiYqLZbDabP//8c7O/v785KCjI/OWXX1q2zcvLM3/11Vfmxo0bm/39/c0rVqywivXEE0%2BY/f39zb169TKfOnXKar8vvvjCfOedd5r9/f3NS5cutdqvoK0NGzY0R0VFmc1mszk3N9d85swZc25urvm%2B%2B%2B4z%2B/v7m%2BfPn2/Oycmx7PfHH3%2BYW7RoYfb39zfPmzfPsjwnJ8fctWtXs7%2B/v7lDhw7m/fv3W9alpKSYX3/9dctj3rVrl2Xd9u3bLW1p3Lixee3atZZ158%2BfNz/55JNmf39/c/Pmzc3Z2dlX7FcRkeuhMd8iIjehjIwM9u3bx5tvvsmaNWsA6N%2B/P5UqVSIrK4tZs2YBMHnyZLp06WLZz2Qy0bFjR0vFe9asWeTk5ACQnJzMwYMHAZgwYQK%2Bvr5W%2B3Xr1o3mzZsD8OeffxbZroceeohmzZoB4OTkhI%2BPD6dPnyYxMRGAXr164ezsbNm%2BQYMGDB8%2BnLCwMHx8fCzLv/nmG/bv34%2B7uzvz58/nzjvvtKwrV64cEydOpHXr1mRnZzNz5swi2zJ06FA6d%2B5s%2Bd3Ly8vyuM%2BePcvff/99md4VEbl%2BGnYiIlLK9evX76rbPProowwbNgzIn/UkKSmJsmXLXvZGPV26dGHChAmcOnWKffv2cc8991CxYkW2b99ORkYGHh4ehfbJzc21DAvJyMgoMm7Tpk0LLatQoQLe3t6cO3eOkSNH8vzzz9OoUSOcnPLrQ7169aJXr15W%2B3z//fcAhIaGUqNGjSKP9dRTT7F161aioqJISUmxGvsO0K5du0L71K1b1/Lz%2BfPni4wrImIPJd8iIqXcpTfZMZlMuLu74%2BPjQ0BAAGFhYdSrV8%2ByvqB6nZ2dTZ8%2BfS4b19nZmby8PA4fPsw999xjWe7h4cGJEyfYvXs3sbGxxMXFERMTw/79%2B0lPTwcgLy%2BvyJiVK1cu8jgjR45kzJgxbN68mc2bN%2BPt7U1wcDD33Xcfbdu2tRqrDliq0g0aNLhs%2BwvW5ebmcvToURo2bGi1vkqVKoX2ufikIjc397KxRUSul5JvEZFS7o033rjsTXaKkpKSAkBWVhY7d%2B686vYXV4APHz7M22%2B/zebNm60S7HLlyhEUFERCQgIHDhy4bKyiKuaQX92uVasWixYt4qeffuLcuXNs3LiRjRs3YjKZaNu2LePGjbMk4ampqQCFqtkXu/iE5NJZXgBcXV0vuy%2BAWfegExEHUPItInKL8fT0BPIrw6tXr7Z5v%2BTkZJ544gmSk5OpWrUqvXr14q677qJOnTpUr14dk8nEiBEjrph8X0lwcDDBwcFkZGTw66%2B/8ssvv7B161b27t3LDz/8wIkTJ1izZg0mk8kyk0rBiURRLj5pKGrmFRGRkqDkW0TkFnPHHXcA%2BdMG5uTk4OJS%2BK3AbDazY8cO/Pz8qFq1Km5ubqxatYrk5GR8fHxYtWoVt912W6H9Tp06dc3tycrKIi4ujtTUVBo1aoSHhwetWrWiVatWDB8%2BnK%2B%2B%2BoqXXnqJAwcO8Oeff3LnnXdSp04d9u3bx969ey8bd8%2BePUD%2BMJyaNWtec7tERBxBs52IiNximjVrhpeXF2lpaZetfK9bt44nn3yShx56iJMnTwJw7NgxAKpWrVpk4n3o0CF27doFXNt46S1bttCxY0eeffZZsrKyCq1v2bKl5eeCuAUXS37//ffExcUVGXfJkiUANG7cmPLly9vcHhERR1LyLSJyiylTpgzPPvssAJMmTWLVqlVW47e//fZb3nzzTSB/asCCqnGdOnUAOHDgABs2bLBsbzab2bJlC8888wzZ2dkAXLhwweb2hISEUKFCBc6ePcuoUaM4e/asZV1aWhrTpk0D4Pbbb6d%2B/foAPPjggwQEBJCZmcnAgQOthrqkpqYyZswYfvzxR1xcXBg5cqTtnSMi4mAadiIicgsaOHAgcXFxrFixgtdee4133nmH6tWrc%2BrUKRISEgBo0qQJEydOtOzTs2dPli1bxtGjRxk6dCjVqlWjQoUKnDhxguTkZFxdXWnevDlRUVHXNPzEzc2N999/n6effpr169fz3XffUbNmTZycnIiLiyM9PR1PT0%2BmTp2Km5sbAC4uLsyZM4eBAwdy%2BPBhunbtanWHy4LpEN966y2CgoKM7TwRETso%2BRYRuQWZTCYmTJhAhw4dWL58Obt27bLctKZx48Z06tSJ8PBwS7IL%2BbOHrFy5kvnz5/PDDz9w7NgxkpKS8PPzo23btjz55JOUKVOGsLAwDhw4wPHjx6latapN7QkODuY///kPixYt4rfffuPIkSO4uLjg5%2BdHq1atGDBgQKFY1atXZ9WqVXz%2B%2Bed88803xMTEcPLkSW6//XZat25Nnz59qF27tpHdJiJiN5NZcymJiIiIiBQLjfkWERERESkmSr5FRERERIqJkm8RERERkWKi5FtEREREbgqnT5/m/vvvZ8eOHZfdZvPmzXTu3JnGjRvz0EMP8cMPP1itnz9/PiEhITRu3Ji%2Bffty%2BPBhQ9uo5FtERERESr3ffvuN8PBwYmNjL7vNkSNHiIiIYNiwYfz6669ERETw4osvWqZH/eKLL/j0009ZsGABO3bsoEGDBgwdOhQj5ydR8i0iIiIiJSohIYG9e/dafRXcc8AWX3zxBSNHjmT48OFX3S4oKIiwsDBcXFzo2LEjzZo1IzIyEoAVK1bQu3dv6tevj7u7OyNGjOD48eNXrKRfK83zLXIlJpOx8e64Aw4ehPr14e%2B/DQsbc8j4GUNdXKBmTYiNhZwc4%2BLWrZ5pXLACbm5QxG3J7eLigJdHJye46E6ShsYtBcwY/P8kmNBswUYrLc9To9%2BeSvrgkR98wOzZs62WDRkyhIiICJv2b9WqFZ07d8bFxeWKCfihQ4fw9/e3WlavXj3LXXIPHTrEwIEDLetcXV2pXbs2Bw4coEWLFrY%2BnCtS8i1SnHx8wNk5//sNzskp//X1hs/rTKb//7rRb1tQou%2BW16g09Celppmlpp1A6WlsKWlnKWlmiQsPDyc0NNRqWeXKlW3e39Zt09LS8PT0tFrm4eFBenq6TeuNoORbREREREqUr68vvr6%2BDj%2BOp6cnGRkZVssyMjIoW7asTeuNcKPXtERERETkRuLkZPxXMfH39%2BfgwYNWyw4dOkT9%2BvUBqF%2B/vtX67Oxsjhw5Umioij2UfIuIiIiI7Upx8t2lSxeioqJYv349OTk5rF%2B/nqioKLp27QpAjx49WLp0KQcOHCAzM5N3332XSpUqERQUZFgblHyLiIiIyE0rMDCQtWvXAlC3bl0%2B/PBD5s2bR7NmzZgzZw6zZs3ijjvuAKBnz57079%2BfF154gRYtWrBv3z7mzZuHq6urYe0xmY2cuFDkZmP0BXKBgbBzJzRpAtHRhoV1xGwnbm5QowbExRk7kYjhs52YTP8/24mRL2eOmO3E2Rlyc42P64iqkQOuEnPELBKl5WI2R7XTIbOd3OKdavTz1GF/%2B5K8ftvd3fiYmQ6YCesGpcq3iIiIiEgx0WwnIiIiImK7G34O2hubkm8RERERsZ2Sb7uo90REREREiokq3yIiIiJiO1W%2B7aLkW0RERERsp%2BTbLuo9EREREZFiosq3iIiIiNhOlW%2B7qPdERERERIqJKt8iIiIiYjtVvu2i3ithR44cKekm3JRyc3OJi4sr6WaIiIjcfJycjP%2B6hdy0j/bvv/9m1KhRhISEEBgYSFhYGNOnTyctLa2km2axb98%2BOnXqdNn1o0ePZvTo0cXYoqvbtGkTAQEBTJw4saSbckXDhw9nzZo1Jd0MERERESs3ZfK9c%2BdOunfvTrVq1VizZg3R0dHMnz%2Bf3bt3M2DAAHJzc0u6iQCkpKSQnZ1d0s24JkuXLuXxxx9n1apVnDt3rqSbc1lnzpwp6SaIiIjcnFT5tstN%2BWjHjh1Lt27dGDp0KLfddhsAd9xxBzNnzqRixYqW4QgBAQHs2LHDst/q1asJDQ0FYMeOHbRp04YRI0YQFBTEv//9b0aPHs3QoUN56KGHaNGiBbGxsSQlJTFy5Ejuu%2B8%2BWrVqxdixY0lNTbXECA0NZe7cubRu3ZrmzZsTERFBamoqcXFxDBw4EIDAwECio6Ov%2BXH%2B%2BeefDBw4kObNmxMSEsK4ceNISUkBwGw28%2B9//5vOnTsTFBREs2bNGDFiBBkZGUB%2BVX3s2LEMGjSIwMBA2rdvz5IlS654vKNHj7J9%2B3aGDBlCQEAAkZGRVuv79u3LBx98wOOPP07jxo3p0qULv//%2BOyNGjKBJkyaEhoayadMmy/a//vorffr0ISgoiNDQUN577z2ysrIAmDVrFn379rWKHxoayurVqy3Hevfdd%2BnTpw%2BBgYE89NBDrF%2B/HoDXX3%2BdX3/9lXnz5jFo0KBr7lcRERERR7npLriMjY3l4MGDjBs3rtC6SpUqMWfOHJtjnTx5kjp16jB16lQyMzOZOHEiW7duJTIyEj8/P8qVK8djjz1G7dq12bBhA9nZ2bz66quMHTuWGTNmABAfH8%2BpU6f43//%2Bx6lTp%2BjTpw/Lli3j2WefZf78%2BfTr1%2B%2B6Eu8zZ87Qr18/HnnkEWbNmkVKSgojR47klVdeYe7cuXz99dcsWbKEpUuXUrt2bWJiYujduzfr1q3j0UcfBfJPNubNm8fs2bNZuXIl48ePp0OHDlSpUqXIYy5dupQHHniASpUq0bdvX6ZOnUr//v1xc3OzbBMZGcknn3xCzZo1GTBgAL179%2Ba9995j6tSpzJgxgwkTJtC2bVsOHz7MU089xciRI1m0aBEnTpywnJi88cYbNvXBihUrWLRoEfXq1ePDDz9k7NixtG/fnkmTJhEbG2s52bFVQkICiYmJVssq33EHvj4%2BNse4qjvvtP5ukIv%2BBIZxdbX%2BbhiTyTHxjI4rIiJFu8Uq1Ua76ZLv06dPA/mJthF69uyJq6srrv9kII0bN8bf3x%2BA33//nb1797Jo0SLKli0LwKhRo3jwwQcZM2aMJcYLL7yAh4cHtWrVIjg4mL///tvudn333Xe4uroycuRInJ2d8fDwYMyYMTz88MMkJiYSEhJCkyZN8PPz4/Tp05w5cwYfHx9OnTpliREcHMx9990HQI8ePXjzzTeJjY0tMvlOT0/niy%2B%2BYMGCBQB06NCBt99%2Bm6%2B%2B%2Boru3btbtuvQoQP16tUDICgoiPPnzxMWFgZASEgIixYtAmDdunUEBATw5JNPAlCrVi1GjBjB0KFDee2112zqgw4dOnDXXXcB0L17dz766COSk5OpWrXqNfVlgcjISGbPnm21bMiwYUQMG3Zd8a5o2TJDw9UwNJo1Pz%2BjIzrgTAEccJbgIM7OJd0C2xl8QuOo06PSct7lmHY66MHfwp3qiEdeWrrTZkq%2B7XLTJd%2BVK1cGIDExkdq1axdan5SUdE2Jua%2Bv72V/P3bsGLm5ubRp08ZqGzc3N6uZNgraBODq6orZbLb5%2BJdTkGQ6X/RGXr16dSC/2l63bl1mzpzJDz/8wG233ca//vUvsrOzrY59absA8vLyijzemjVrSElJ4dlnn7UsS0tLY%2BHChVbJt89FVWJnZ2e8vb0tvzs5OVmOn5ycTI0a1ilj9erVycjIIDk52aY%2BuLj9Li4uV2y/LcLDwy3DjizH6NwZPvnkumMWcued%2BYl3795w4IBhYeO%2B3GlYrAKurvmJ98mTYOSlCTWqZBkXDPLf1Vxd8xtpwP%2BWhSOSZGdncMQ1J454IzSZjO1PwOyAtMYBzXQIR7XThCOC3tqdavTz1GF/%2B5stob%2BF3HTJd7Vq1fD392f9%2BvU0a9bMal1ycjLt2rVjypQpdOrUCScnJ6sLHou6SM90ybP74t/9/Pzw8PBgx44dliQ4KyuLuLg4atWqxW%2B//WbkQ7NSrVo1jh8/Tm5uruXYsbGxQH5SOn36dI4fP873339PuXLlAOjcufN1H2/ZsmUMGzaMRx55xLLszJkz9OjRgx9//JFWrVoBhfvrSu3fuHGj1bLY2Fjc3Nzw9vYu9LfJy8vj7Nmz191%2BW/j6%2BhY62cKATymKdOAAXMdwo8vJMjifvVh2tsHxHfWmbjaXjoRBRKS0U%2BXbLjdl740ZM4ZVq1Yxe/Zszpw5g9lsZv/%2B/QwaNIgGDRrQoUMHAOrWrcuGDRvIyckhNjaWlStXXtNx7rnnHmrVqsXUqVNJS0sjIyODyZMn079/f5tmVHF3dwewXCRZlAsXLnDy5Emrr9TUVEu1ffr06WRkZJCYmMikSZNo0aIF1apVIzU1FXd3d5ydncnMzGThwoX89ddf1zW7ys8//8yRI0cIDw/Hz8/P8vWvf/2LkJAQFi5ceM0xH374YWJiYvjkk0/IysoiNjaWGTNm0LlzZ9zc3Khbty5//vknBw8eJCcnh48//pj09HSb47u5uV2xX0VERERKwk2ZfDdv3pylS5eyb98%2BHn74YZo0acLQoUNp0aIFH3/8sWWIxZtvvsnevXtp3rw5L774Ij179rym47i4uDBv3jySkpJ44IEHaNWqFbGxsSxatMiSWF%2BJv78/TZs2pXXr1mzevLnIbb755hvatGlj9fXRRx/h5eXFokWL%2BOuvv2jTpg2dOnWiWrVqvP/%2B%2BwC8%2BOKLZGRk0LJlS0JDQ9m1axddu3blr7/%2BuqbHCPDZZ58REhJCxYoVC6177LHH2LZtGweucQhF9erV%2Bfjjj9mwYQMtW7akd%2B/e3HfffYwdOxaAsLAwOnfuTP/%2B/WndujVnzpyhadOmNsfv1q0bq1atonfv3tfULhEREbkKTTVoF5PZiAHIIjcrowfVBQbCzp3QpImhw05iDhn/b%2BzmBjVqQFycscNO6lbPNC4Y5P%2BN3NzyG2nky5mLA0blacy3ofHglh%2BerDHfGvNdMu64w/iYjhrmeQO6tU41RERERERK0E13waWIiIiIONAtNkzEaOo9EREREZFiosq3iIiIiNhOlW%2B7KPkWEREREdsp%2BbaLek9EREREpJio8i0iIiIitlPl2y7qPRERERGRYqLKt4iIiIjYTpVvuyj5FhERERHbKfm2i3pPRERERKSYqPItIiIiIrZT5dsu6j0RERERkWKiyreIiIiI2E6Vb7so%2BRa5gphDZkPjublBDSDuy51kZRkXt249k3HBCgQGws6d1OjaBKKjDQt7Id3YPjWZwAPIyHPDbGBoN%2BNCWTgDuTgbHzjP%2BJDOzpCbZ%2BzzyplcQ%2BPlB3XGlGdwXIckFiZMGPvcBzBj/P%2B%2ByUFxjeaodhr/d3LM356S/Bsp%2BbaLek9EREREpJio8i0iIiIitlPl2y7qPRERERGRYqLKt4iIiIjYTpVvuyj5FhERERHbKfm2i3pPRERERKSYqPItIiIiIrZT5dsuSr5FREREpFRLTk5mzJgxREVF4ezsTJcuXRg1ahQuLtap7jPPPMNvv/1mtSw9PZ3w8HDGjx9PUlIS9913H2XKlLGsr1ChAt9//71hbVXyLSIiIiK2uwEr3y%2B%2B%2BCJVqlRh69atJCUl8fzzz7N48WKeeeYZq%2B0%2B/vhjq99XrlzJ7NmzGTJkCAB79uyhWrVqhibbl1LyLSIiIiK2c0DynZCQQGJiotWyypUr4%2Bvre9V9jx49SlRUFFu2bMHT05MaNWowePBg3nnnnULJ98UOHz7MhAkTWLBggeU4e/bsoWHDhvY9mKtQ8i0iIiIiJSoyMpLZs2dbLRsyZAgRERFX3ffgwYP4%2BPhQpUoVy7K6dety/Phxzp8/T/ny5Yvc76233qJbt24EBQVZlu3Zs4dz587RqVMnkpKSuPvuuxk1ahT16tW7zkdWmJJvEREREbGdAyrf4eHhhIaGWi2rXLmyTfumpaXh6elptazg9/T09CKT719//ZXdu3czffp0q%2BXly5enXr16DBw4EDc3N95//32eeuop1q9fj5eX17U8pMtS8i0iIiIiJcrX19emISZFKVOmDBcuXLBaVvB72bJli9wnMjKShx56qFCC/%2B6771r9/uqrr7Jq1Sp%2B/fVX2rVrd13tu9SNN2JeRERERG5cTk7Gf9mhfv36nD17lqSkJMuymJgY/Pz8iqxW5%2BTk8N1339GlSxer5ampqUybNo34%2BHjLstzcXHJycvDw8LCrjRdT8i0iIiIitrvBku/atWvTtGlTJk%2BeTGpqKnFxccyZM4eePXsWuf2ff/5JZmYmTZo0sVperlw5fvrpJ6ZNm0ZKSgppaWlMmDCB6tWrW40Lt5eSbxEREREp1T744ANycnJo3749vXr1onXr1gwePBiAwMBA1q5da9k2Li4Ob29v3N3dC8WZM2cOeXl5hIWF0bp1axITE5k/fz6urq6GtdVkNpvNhkWTW8qRI0eoXbt2STfDoWJijI3n5gY1akBcHGRlGRe3bj2TccEKBAbCzp3QpAlERxsW9kK6sS85JhN4eEBGBhj5aubmZlysAs7OkJtrfFxHcERbnXHAg3dEQx0xh7HJZOwT9B9mjP/fd1BTDeeodpowOKjDGuqA131bdehgfMwNG4yPeYNS5buU%2Bvvvvxk1ahQhISEEBgYSFhbG9OnTSUtLM/Q4AQEB7NixA4CHH37Ycub42WefMWbMmMvul5WVxbvvvktYWBiBgYG0aNGCiIgIYozOZkVERKR43WDDTkqbW%2BvR3iR27txJ9%2B7dqVatGmvWrCE6Opr58%2Beze/duBgwYQK6DSmtfffWV5eKE06dPX3HbCRMmEB0dzeLFi4mOjmbjxo34%2BfnRp08fzp8/75D2iYiIiNzolHyXQmPHjqVbt24MHTqU2267DYA77riDmTNnUrFiReLi4oD8qvXEiRMJDg5m0KBBAPz000/07NmToKAgq0o2QHZ2NlOmTCE4OJgWLVoUugVraGgoq1ev5osvvmDevHn8%2Buuvl70A4bfffqN169ZUr14dyJ8385VXXqFdu3aWO1ilp6czfvx47r33XoKCghg4cKDlCuMzZ84wZswYWrVqRXBwMM899xxHjhwB4NixYwQEBDB16lSaNWvGW2%2B9BeSfHHTu3JmmTZvyyCOP8OOPPxrR3SIiInIxVb7tonm%2BS5nY2FgOHjzIuHHjCq2rVKkSc%2BbMKbT9pk2byM7O5sCBAzz//PO88847tG/fnt27dzN48GAqVKhA69atmTNnDps2bWLlypVUrFixyGMAdO/enWPHjhEVFcWnn35a5DYPP/wws2fP5u%2B//6ZFixY0atSIO%2B64gylTpli2GT9%2BPDExMaxevZqKFSvy5ptv8tJLLxEZGcnQoUNxcnLiiy%2B%2BwMvLi/fff5/%2B/fvz3//%2B17J/Wloa27ZtIyMjg82bN/Pmm28yd%2B5cmjRpwpYtW4iIiGDFihXUr1/fpr4t6ta2mZmVqVz5%2BuYdLUrB9RoGXreRLzDQ4IDAnXdafzeI0cMUC%2BKV5PBHERERWyn5LmUKhntUqlTJpu07deqEp6cnnp6ezJgxg/bt2/PAAw8A0KRJE3r16sVnn31G69at%2BfLLLxk0aBA1atQA4I033rCqjF%2BLF154gX/961%2BsWbOGadOmcfr0aXx9fXn66afp378/WVlZfPXVV8ydO5fbb78dyJ/I/ujRo8TFxREVFcVXX31lmfx%2B5MiRrFu3js2bN9OoUSMAunXrhpubG25ubixdupTHH3%2BcZs2aAdCuXTtCQ0NZvnz5FcemX6yoW9u%2B8MIQhg69%2Bq1tr5Wfn8EBd%2B40OOBFli0zNJxxM6VaK%2BKi9RuSs3NJt8B2xrfVQQ%2B%2BtHSqA84QHXXOWVpOZh3TTgcELS0daqtbrFJtNCXfpUxBMpqYmFjkTCNJSUlWifnFd4uKj49n%2B/btVkNFcnNzqVmzJpBf%2BS1IhCF/qIi3t/ctJawRAAAgAElEQVR1tzU0NNRyq9jY2Fg2btzI9OnTKVu2LG3btiUrK4uqVataHe/uu%2B8m%2Bp%2BZNQpOAgCcnZ25/fbbiY%2BPtyTflz62qKgoPv/8c6vH1qJFC5vbW9StbTMzK/PPKB5DuLrmJ94nT0J2tnFxa3RtcvWNrtWdd%2BYn3r17w4EDhoXN%2BMnYEwWTKT/xzsw0dkIBwz%2BdQLOdaLYTzXZiJM12UoIJvZJvuyj5LmWqVauGv78/69evt1R5CyQnJ9OuXTumTJlCp06dADBd9M/p5%2BdH9%2B7dGT9%2BvGVZQkICBbNN%2Bvn5WcaLQ/6Y7JSUlGtuY0xMDN26dWPVqlX4%2B/sDULNmTZ555hl2797N/v376dGjB25ubpw4cYI6depY2j9//nwGDBgA5CfsBUNGcnNzOX78uNVtYC99bN26dePZZ5%2B1LDt%2B/Pg13ZGqqFvbxsQYOyVggexsg%2BMaOBVgIQcOGBrfUW/qZnPpSBhEROTWplOXUmjMmDGsWrWK2bNnc%2BbMGcxmM/v372fQoEE0aNCADpeZf7Nnz57897//5ccffyQvL48jR47wxBNPsHDhQgAeffRRPv74Y2JiYsjMzGTq1KmXnTnF3d2d1NRUipomvk6dOjRo0ICxY8fy%2B%2B%2B/k5mZyYULF9i8eTM7duzg/vvvx8nJiW7dujFr1ixOnTpFZmYm7733Hrt27cLX15c2bdowceJEEhMTycjIYPr06eTm5tKuXbsi29OrVy%2BWLFnC77//DsCePXt45JFHrMaIi4iIiAF0waVdVPkuhZo3b87SpUv56KOPePjhh7lw4QKVKlXiwQcf5LnnnrvsXZgaNWrEjBkzmDFjBsOGDcPT05NOnTrx0ksvATBw4EAuXLjAE088QU5ODr169cLHx6fIWO3atePzzz%2BnadOmbNq0ifLly1vWmUwm5s%2Bfz5w5c3j55Zc5deoUTk5O/Otf/%2BKdd97h3nvvBWD06NHMnDmTRx99lIyMDJo3b877778PwNtvv8306dPp3r076enpNG7cmE8%2B%2BQQfHx9SU1MLtefBBx8kPT2d1157jePHj%2BPj40P//v3p27evXX0tIiIiYiTd4VLkCnSHS93h0kga860x30bTmG8HxNWY76vr0cP4mKtWGR/zBqXKt4iIiIjY7hYbJmI09Z6IiIiISDFR5VtEREREbKfKt13UeyIiIiIixUSVbxERERGxnSrfdlHyLSIiIiK2U/JtF/WeiIiIiEgxUeVbRERERGynyrdd1HsiIiIiIsVElW8RERERsZ0q33ZR8i0iIiIitlPybRf1noiIiIhIMVHlW0RERERsp8q3XdR7IiIiIiLFRJVvEREREbGdKt92UfItcgV1q2caG9BkAtyoUSULzGbDwl5INy5WAZMJPICMn3Ya2VQ8y5iMCwYQGAg7d%2BLRsglERxsX96%2B/jIsF4O4ONWviHB8LmcY%2Br8751jc0npMTeHlBejrk5RkX1zvpiHHBANzcoEYNOH4csrIMC5tbu65hsQo4O0NunsHPfcD56/8aG7B8eQgJwbR1C5w/b1jY1LadDIsF%2Bc/RMmXgwgVjn6MA5ZwzjAtmMoGHR/7/vJEvpACensbGuxZKvu2i3hMRERERKSaqfIuIiIiI7VT5tot6T0RERESkmKjyLSIiIiK2U%2BXbLkq%2BRURERMR2Sr7tot4TERERESkmqnyLiIiIiO1U%2BbaLek9EREREpJio8i0iIiIitlPl2y5KvkVERETEdkq%2B7aLeExEREREpJqp8i4iIiIjtVPm2i3pPRERERKSYqPItIiIiIrZT5dsuSr5FRERExHZKvu2i3hMRERERKSaqfIuIiIiI7VT5tot67wbw2WefERAQwOLFi0u6KRahoaGsXr26yHWzZs2ib9%2B%2BxdwiERERuSE4ORn/Zafk5GQGDx5MUFAQwcHBTJo0iZycnCK3feaZZ7j77rsJDAy0fG3ZsgWA3Nxcpk2bRsuWLQkMDOT5558nISHB7vZdTMn3DeCzzz7j8ccfZ8mSJZd9ooiIiIhI0V588UXKlCnD1q1bWblyJT///PNli5p//PEHCxYsIDo62vIVEhICwNy5c9m2bRurVq1i69ateHh48MYbbxjaVg07KWE///wzycnJjB49mk2bNrFhwwYefvhhIL/6HB4eztdff83Ro0epVasWo0ePpkWLFhw7doz27dszceJE5s6dy7lz57jnnnuYMmUKfn5%2BrF69mtmzZ/P9999bjtW3b1%2BaN29OREQEqampTJ06laioKBISEvDy8qJPnz4MGjTomtp/tXYArFu3jnnz5hEfH4%2Bfnx8RERF07NgRgP/85z8sXryYEydOUK1aNQYOHEiXLl0s7W3WrBk///wz%2B/fvp2bNmkycOJFPPvmEH374AR8fH8aOHUvbtm0B2Lt3L1OnTuXAgQNUqFCB3r178%2BSTT2IymWx6LAkJCSQmJlotq%2Bztja%2Bv7zX1yRUVtMXGNl1rWEfENDx2YKCx8e680/q7UdzdjY3n6mr93UBGfwJcEM/wT5bd3IyN58A%2BLTXKlzc2Xrly1t8NYvRz6eLXJ8Ofp0a%2B6DnshbSEOWDYSZHvwZUr2/QefPToUaKiotiyZQuenp7UqFGDwYMH88477/DMM89YbRsXF8e5c%2Be46667ioz1n//8h5EjR3L77bcD8Prrr9OqVSvi4uKoUaPGdT46a0q%2BS9inn35Kr1698PDwoHfv3ixcuNCSfAOsWrWK%2BfPn4%2Bvry1tvvcW4ceP45ptvLOs3bdrEmjVryMrK4qmnnmLOnDmMHz/%2BqsedPn06x44dY%2BXKlXh5ebFx40aGDh3KQw89RK1ata75cVyuHTt27OC1115j9uzZtG7dmh9//JHBgwfj7%2B/P77//ztSpU5k9ezbNmzcnKiqKIUOG4Onpyf333w9AZGQkn3zyCTVr1mTAgAH07t2b9957j6lTpzJjxgwmTJhA27ZtOXXqFE8%2B%2BSTDhw9n4cKFHD16lMGDB%2BPh4cFjjz1m02OIjIxk9uzZVsuGvPACEUOHXnN/XJXByYKHodGsGZ2DsnOnwQH/sWyZY%2BIa7Z8XdCN5GR4xX9myBgf0MuaNq5B/TvSN4mxotIviOiLwP9U6wzVpYmi4MoZG%2B3%2Beno6I6oBXVMNfSG8%2BRb4HDxlCRETEVfc9ePAgPj4%2BVKlSxbKsbt26HD9%2BnPPnz1P%2BopPUPXv2ULZsWYYPH86ePXuoVKkS/fv3p2fPnqSkpHDy5En8/f0t21eqVAlvb2/%2B/PNPJd83g/j4eLZu3crYsWMB6NWrFx9%2B%2BCFRUVE0b94cgJ49e1qS4c6dO7NmzRqrGAMHDrQ8qUJDQ4mOjrbp2BERETg7O1OuXDlOnjyJ%2Bz8vDAkJCdeVfF%2BuHWvWrOGBBx6gTZs2AISEhLBs2TKqVKnCqlWrCA8P59577wXg3nvvJTw8nOXLl1uS7w4dOlCvXj0AgoKCOH/%2BPGFhYZZYixYtAmDt2rXUrVuXPn36AFCvXj2efvppli5danPyHR4eTmhoqNWyyt7ekJV1zf1xWSZTfuKdnQ1ms2FhM/IMriiS31R3d8jMNLSpeLQ09k2dO%2B/MT7x794YDB4yLe8n/mt1cXfMT7xMn8v/%2BBkqpUNPQeE5O%2BYl3Whrk5RkX1%2BtsnHHBIL9P/fzg5ElD%2BzS3qvEnCc7OkJtreFict20xNmC5cvmJ986dkJpqWNj0IGNPEkym/MT7wgVjX58AyjhlGBfMUS%2BkAB6OLLtchQMq30W%2BB1eubNO%2BaWlpeF5yJlbwe3p6ulXynZWVRePGjRk%2BfDj169dnx44dREREULZsWQL/%2BWS2TBnr00UPDw/S0tKu%2BTFdjpLvErRs2TJycnLo2rWrZVlOTg4LFy60JN%2BVKlWyrHNxccF8yT/v1dZfTnJyMpMmTWLfvn1Ur16dhg0bApB3ne%2B0l2tHQkJCoY927rnnHgCSkpIKnUVWr17daqiMj4%2BP5WdnZ2e8vb0tvzs5OVmOEx8fz969ewkKCrKsz8vLw/kaSk2%2Bvr6FP95yxAsm5Mc0MK4jmnhxbEPj23iCeM0OHDA2dmamcbEulp1teGwjE%2BRL4xoa28gT2YtlZzsu9o3u/HnHxE1NNTS20c/RgtzPbHbA899047/mlzgHJN9FvgfbqEyZMly4cMFqWcHvZS/5CK9bt25069bN8nurVq3o1q0bX3/9NS1btrTat0BGRkahOPZQ8l1CMjMzWblyJZMmTbL8sQH%2B%2Busvnn32WWJiYuyK7%2BTkRNYlb0Znzpyx/Dxs2DBCQ0NZsGABLi4unDlzhhUrVth1zKLcfvvtHD9%2B3GrZwoULady4MdWrVyc2NtZqXVxcnNWZrq3jtf38/AgODmbBggWWZWfOnDH0TFVERERuPPXr1%2Bfs2bMkJSVZioExMTH4%2Bfnh5WU9MG/lypWULVuWhx56yLIsKysLd3d3vL29qVKlCocOHbIMPUlMTOTs2bNWQ1HspdlOSsi6deswmUx07twZPz8/y1dISAj%2B/v52TztYt25dkpKS2L59O2azmS%2B//NIqoU9JScHDwwNnZ2dOnz7NxIkTAcg2%2BOPw7t2787///Y8ff/yRvLw8tm7dyqxZs/Dy8qJnz55ERkby888/k5uby/bt24mMjKRHjx7XfJzOnTuza9cu1q5dS05ODgkJCQwaNIipU6ca%2BnhERERueTfYVIO1a9emadOmTJ48mdTUVOLi4pgzZw49e/YstG1qaioTJkxg37595OXlsWnTJv773/8SHh4OwCOPPMLcuXOJi4sjNTWVyZMn07x5c2rWNG54nyrfJWTZsmV07twZ1yIuvAsPD2fatGk2V32Lcvfdd/P8888zevRo0tLSCAsLo0OHDpb1U6ZMYfLkySxcuBBvb286duzIXXfdxV9//UWrVq2u%2B7iXatq0KdOmTWPatGnEx8dTrVo1ZsyYQf369alfvz6pqalMnDiR48ePU6VKFV555RWrj4NsVa1aNT7%2B%2BGOmT5/OxIkTcXZ2pm3btrz%2B%2BuuGPRYRERG5MX3wwQeMHz%2Be9u3b4%2BTkRLdu3Rg8eDAAgYGBvPXWW3Tp0oUnn3yS9PR0hgwZQnJyMjVq1GDatGmWYasvvPACOTk59OnTh7S0NIKDg3nvvfcMbavJbOsgYZFbkdHjfk2m/OnWsrIMHf93Ic/4K%2BlNpvzreTIyjB2q6FnG4Cm3AgPzLw5r0sTYMd9//WVcLMi/6KpmTYiNNfx5dc63vqHxnJzAywtSUowdT%2BudZN9wukLc3KBGDYiLM3TMd27tuobFKuCwCy6//q%2BxAcuXz59BZcsWQ8d8p7btZFgsyH%2BOlikD6enGj/ku53zh6hvZylEvpOCoqV5sM2WK8TFffdX4mDcoVb5FRERExHa6vbxd1HsiIiIiIsVElW8RERERsZ0q33ZR74mIiIiIFBNVvkVERETEdqp820XJt4iIiIjYTsm3XdR7IiIiIiLFRJVvEREREbGdKt92Ue%2BJiIiIiBQTVb5FRERExHaqfNtFybeIiIiI2E7Jt13UeyIiIiIixUSVbxERERGxnSrfdlHviYiIiIgUE1W%2BRa7ExUH/Is7OhoZzMzSaNVdXgwP%2B9Zex8dzd87%2BvWQOZmcbF9fc3LhZAYCDs3AndukF0tKGhnVPMhsYrKGo5O4PJ5IDARsdzcjI0tnPqOcNiAflt8/LCOT0F8vKMjX377cbG8/TM/16pEpQta1jYcrkG96nZCfCiTK4D%2BtS9jLHxwPDX/BKnyrddlHyLiIiIiO2UfNtFvSciIiIiUkxU%2BRYRERER26nybRf1noiIiIhIMVHlW0RERERsp8q3XZR8i4iIiIjtlHzbRb0nIiIiIlJMVPkWEREREdup8m0X9Z6IiIiISDFR5VtEREREbKfKt12UfIuIiIiI7ZR820W9JyIiIiJSTFT5FhERERHbqfJtF/WeiIiIiEgxUeVbRERERGynyrddlHyLiIiIiO2UfNtFvSeXlZOTQ1xcXLEd79y5c5w%2BfbrYjiciIiJS3Epl8j1u3Djuu%2B8%2BkpOTrZbn5OTQq1cvnnvuOcxmcwm1zjYLFy6kWbNmNGvWjIMHDxa5zebNm3n66adp0aIFQUFBdO/enRUrVhjajp9%2B%2Bom77roLgLi4OAIDAzl16hQAw4YNY926dUXul5OTQ0BAAL/%2B%2BmuhdTNnzqR///4A7Nixg6CgoKu2Iy8vjwceeIDDhw9f5yMRERGRYuHkZPzXLaRUPtpXX32VSpUq8eqrr1otnzVrFklJSUybNg2TyVRCrbPN0qVLiYiI4JdffqF%2B/fqF1n/88ce8/PLLdO/enU2bNrFjxw5GjRrFBx98wIwZMxzSpho1ahAdHU2VKlUADKlCBwcHF5mgXyovL4%2BzZ8/afTwRERFxMCXfdimVj9bd3Z2ZM2fyyy%2B/8OmnnwIQFRXF4sWLee%2B99/Dx8QEgNTWVcePGERISwr333suIESOsquXffvst4eHh3HvvvTRq1Ii%2BffsSGxsLwH/%2B8x8effRR%2BvfvT1BQEOvXr2f79u088sgjBAUF8cADDzB16lRyc3OLbGNcXBxDhw6lRYsW3Hfffbz88sskJSUB%2BQnp8ePHeeeddxgwYEChfU%2BePMmMGTOYOHEinTp1wsPDA2dnZ1q0aMGkSZNITEwkJyeHn376idDQUIYPH05QUBALFiwgLy%2BPxYsX06FDB4KCgnjiiSfYu3evJfapU6d47rnnaNKkCWFhYfz888%2BWdUePHiUgIICTJ08yevRodu3axZw5c3jhhReu%2B291cWUd4L333iMkJITmzZvTs2dPfvjhBwAefPBBAJ5%2B%2BmkWLVoEwMaNG%2BnevTtNmjShQ4cOLFmyxPKJxsiRIxk2bBgPPvggLVq0YM6cOTz88MNWx/73v/9Nv379rrvtIiIiIkYrtRdc1qlTh7Fjx/LWW28RFBTE6NGjeeWVV7jnnnss24waNYqsrCzWrFmDm5sbkydPZujQoXz22WfEx8fz4osv8uGHH9KmTRtOnz7N4MGDmTt3LlOmTAHg999/55133uHf//43eXl53H///YwcOZKuXbsSFxfH448/TlBQEGFhYVZty8rK4qmnniIwMJD//e9/mM1mxo4dy/PPP8/y5cvZsWMHISEhjBgxgq5duxZ6bJs2bcLNzY3Q0NBC69q0aUObNm0sv8fHx9OrVy/efvttMjMz%2BfTTT1myZAlz586lTp06fPHFFzz11FN888033HbbbQwbNgxfX1%2B2bNnCuXPnGDRoUJH9O3XqVI4ePUrr1q0ZPHjwZf8OAwcOxNnZ2WpZZmYmTZs2LbTttm3bWL16NatWraJSpUosW7aM119/nS1btvDNN9/QoEEDFixYQFBQENu2beOll17i3XffpX379uzfv5/BgwdjMpno27cvAFu3bmXFihX4%2BvqSnp7OrFmz%2BOOPP2jYsCEAa9as4dlnn71s2y%2BVkJBAYmKi1bLKFSviW7myzTHEBu7uxsZzdbX%2BbpTAQGPj3Xmn9XcDGV00Kvjg0GQyOLabm4HBcNzf3ugOLYjniOqep6ex8Tw8rL8bpTT1qVyd%2Bt0upTb5BujevTs///wzjz32GGFhYfTp08ey7tSpU3z77bf873//47bbbgPgtddeo3nz5hw4cIA6deqwfv16atasSWpqKidPnuS2226zjHcG8PDwoHPnzpYhLJ6ennz99dd4e3vTrFkztmzZglMRT8CoqChOnjzJuHHjKFu2LADjx4%2BnefPm7Nu3j7vvvvuKj%2Bv06dNUqFABFxfb/jw9e/bE1dUVV1dXli1bxvPPP09AQAAAvXr1YsWKFaxbt4527doRHR3Nt99%2BS7ly5ShXrhxDhgxh%2BPDhNh2nKPPnzy80pnvmzJns3r270Lbu7u6cOXOGyMhIQkNDeeyxx%2Bjduzcmk4mcnByrbVevXk2HDh3o0KEDAHfffTcDBw4kMjLSknw3adKEevXqAVC%2BfHlatmzJl19%2BScOGDfn99985deqUZX9bREZGMnv2bKtlQ154gYihQ22OYbNLTljsDmdotEtiGx28Zk2DA/7j9tuNjbdzp7HxCixbZnjIMoZHzGd0XkeZagYH/Ievr2PiGu2f9wNDXfTJoqHq1HFMXKM5ok8dwegTRCnVSnXyDTBkyBC%2B/PJLhg0bZrU8Pj4egEceecRquYuLC8eOHSMgIIC1a9cSGRmJs7Mz/v7%2BnD9/Ho%2BLzvYrV65sNXZ8yZIlzJo1izfffJPk5GRat27NuHHjLGOkCyQlJXHbbbdZEm/ITw69vb2Jj4%2B/avJduXJlTp8%2BTU5OTqEEPDc3l3PnzllOKJydnalUqZLV4548eTLTpk2zLMvJyeH48eOWE4vbL0pSajoqESpCUFAQ77//PkuXLuXjjz/G09OTfv36FVl9T0pKonHjxlbLqlevbvm7Avhe8obbo0cPJk6cyKhRo1i9ejUdO3bE8xqyh/Dw8EKfNlSuWBEuM7Toujk7Gx4z10HptwOainN8rLEBXV3zE%2B8TJyA727i43boZFwvyK97LlkHv3nDggKGh03809kTBZMpPvC9cACOvXS9zJv7qG10LV9f8xDshwdi/ffnyxsWC/Cph2bKQlgZ5ecbGNnpGKg%2BP/MT78GHIyDAubo0axsUCx/ap0VV/V1djn58Xxy0pqnzbpdQn3wWV50sr0H5%2BfkD%2BuOGCRNVsNhMTE0PNmjVZt24dy5cv5/PPP6fGPy8Kb775JkePHrXEuDjxzsjIICYmhvHjx%2BPs7Mzhw4d5/fXXmTZtWqELIKtXr87p06dJS0uzJOBnz57l3LlzVLZhCENISAg5OTn88MMP3H///VbrvvvuO4YPH873339f5L5VqlTh5ZdftoyhBoiNjaVChQqWCxqPHTtG7dq1gfzx5cUlPj4eX19fFi5cSFZWFtu2bSMiIoKGDRty7733Wm1brVq1QtMcxsbGWvXfpRfVhoWF8dZbb/HTTz/xzTff8NFHH11T%2B3x9fQsl9IZnngKZmY6Jm51tbOzoaONiXezAAcNjG517FLycms0Gx87KMjDYRbKzjY1tdIdeHNfo2BcuGBuvQEaGsbFLU5/K1Sn5tstN23tVq1alVatWTJo0ibNnz5Kdnc2HH37Io48%2BSkpKCikpKTg5OeHu7k5eXh6bN29m3bp1ZF/h7HT48OF88skn5ObmUrlyZVxcXKhQoUKh7Ro1akTt2rUZN24cqampnD9/nnHjxlGnTp1C1dyiVKlShRdeeIE33niD9evXk5WVRXZ2Nt9//z1jx47lqaeeKlRtLxAeHs6cOXP4%2B%2B%2B/gfzpCjt27MjOnTupUaMGLVq0YMqUKZw/f56EhIRCwywu5u7uTkpKylXba6vdu3czcOBA/vzzT9zc3KhYsSKAZYiNs7MzqampQH4Ve%2BPGjWzYsIHc3Fz%2B%2BOMPFixYQI8ePS4b383NjU6dOjFz5kwqVKhgU1%2BLiIiIFKdSX/m%2BknfffZfp06fTpUsX0tLS8Pf3Z8GCBVSsWJGePXsSHR1Nx44dcXZ2pm7duvTr14/IyMgiE3APDw/mzJnD22%2B/zYcffoiLiwtt2rQpcry0q6sr8%2BbNY9q0adx///3k5OTQsmVLFi5cWOjixMsZPHgw1atXZ8mSJYwbN47c3Fxq1arFiBEjePTRRy%2B739NPPw3Ac889R2JiIn5%2Bfrz11luWizTfe%2B89xo0bR9u2bfHy8qJbt27s37%2B/yFjdunVj/Pjx7N27lyVLltjU7ivp2LEjR44cYdCgQZw5c4bKlSszZswYywWS4eHhDBs2jAEDBjBs2DBmzpzJnDlzGD16NBUqVKBv374888wzVzzGI488wtKlS3n55Zftbq%2BIiIgUQZVvu5jMN/rdaESuwenTp2nTpg3ff/%2B9TUN8rsoRw05u9THfh4u%2BqdR1c3fPv4gzNtbYYSf%2B/sbFgvzZU3buhCZNDB92kppi7Mu4kxOUKQPp6cZ%2Bol8u8W/jgkH%2B7CnVqkF8vLHDTv4ZqmgYJyfw8oKUFOOHSBw6ZGw8T8/8izj37TN22Mk/F8cbxpF9WsbgS5hvxjHfGzYYH/MaJkgo7W7qyrfcOjIzM4mNjWXRokWEhoYak3iLiIhIYap820XJt9wULly4QHh4ONWqVWPevHkl3RwREZGb1w2YfCcnJzNmzBiioqJwdnamS5cujBo1qshpmz///HMWL15MQkICvr6%2B9OvXzzJddV5eHk2bNsVsNltN7LBt2zbKGPSpiJJvuSn4%2BPiw01HzMouIiMgN7cUXX6RKlSps3bqVpKQknn/%2BeRYvXlzoWrFvv/2WGTNmMH/%2BfBo1asSuXbt49tlnqVSpEh06dODQoUNkZ2ezc%2BdO3Iy%2BMdg/lHyLiIiIiO0cUPku8i7TlSsXngK4CEePHiUqKootW7bg6elJjRo1GDx4MO%2B8806h5PvUqVMMHDjQMiNaYGAgwcHB/PLLL3To0IE9e/YQEBDgsMQblHyLiIiISAkr8i7TQ4YQERFx1X0PHjyIj4%2BP1TTMdevW5fjx45w/f57yF9046%2BK7oUP%2BcJVffvmFV199FYA9e/aQmZlJjx49iI%2BPp27duowYMYImTZrY8/CsKPkWEREREds5oPJd5F2mbZw8IS0trdAdrQt%2BT09Pt0q%2BL5aYmMhzzz1Hw4YN6dSpE5A/tfQ999zDsGHD8Pb25rPPPuPpp59m7dq1lpsy2kvJt4iIiIjYzgHJd5F3mbZRmTJluHDJ1JgFvxfcafxSu3btYtiwYQQFBTFlyhTLhZmjR4%2B22u7pp59m9erVbN68mSeeeOK62nepG%2B9yVRERERERG9WvX5%2BzZ8%2BSlJRkWRYTE4Ofnx9eXl6Ftl%2B5ciX9%2B/fnySef5N1337Ua3z1z5kz27dtntX1WVhbu7u6GtVfJt4iIiIjYzsnJ%2BC871K5dm6ZNmzJ58mRSU1OJi4tjzpw59OzZs9C2GzZsYNy4ccyaNYsBAwYUWv/XX38xadIkEhMTycrKYvbs2aSmpnL//ffb1caLKfkWERERkVLtgwQzQygAACAASURBVA8%2BICcnh/bt29OrVy9at27N4MGDgfwZTdauXQvA7Nmzyc3NZejQoQQGBlq%2Bxo4dC8CUKVOoWbMmXbt2JTg4mKioKBYtWoSPj49hbdWYbxERERGx3Q14k51KlSrxwQcfFLkuOjra8vO6deuuGMfHx4cpU6YY2rZLKfkWEREREdvdgMl3aaLeExEREREpJqp8i4iIiIjtVPm2i3pPRERERKSYqPItciWOOrs3Om6eseEc6ZxvfUPjOTmBF5BSoSZ5BvaDc4rZuGDkt7MMkP7jTkPbCVDOy2RswMBA2LmTMq2awEUXKtnrQrqxfWoygQeQUbEaZgNDe54/ZVwwgH9u3kFWFuTkGBo6s2FTQ%2BOZTOAGZNW7y9A%2BdU%2BIMy4YgKsreHlBWhpkZxsb%2BzJ3Q7SLy02WbqnybZeb7NkgIiIiIg6l5Nsu6j0RERERkWKiyreIiIiI2E6Vb7uo90REREREiokq3yIiIiJiO1W%2B7aLkW0RERERsp%2BTbLuo9EREREZFiosq3iIiIiNhOlW%2B7qPdERERERIqJKt8iIiIiYjtVvu2i5FtEREREbKfk2y7qPRERERGRYqLKt4iIiIjYTpVvu6j3RERERESKiSrfIiIiImI7Vb7touRbRERERGyn5NsuN2zvZWZmcvLkyZJuRqly5MiRkm7CDUX9ISIiIjeaa0q%2BAwICCAgI4PDhw4XWLVq0iICAAGbN%2Bj/27jwuivp/4PhruVEsFEQIrzLxzK9coqYoqKkh3kWZmpmlZWAeiZpX4YF9SfNIwfCo6NDUDlOzsjT75pVSJn7JOzmUuzhk2QXm9weyPzdQF3cW8%2Bv7%2BXjsA5iZfc9nZmd33/vmPbMrVRnYiBEj%2BOmnnwA4dOgQrVq1UiXujYSEhPDFF19YfD3XWrlyJaNGjTI7zgcffMCcOXNMXn7btm0EBwebtOy1Y/ziiy8ICQm5pTHWppMnTzJgwIDbPQwhhBDif4%2BVlfq3u0iNt7Z%2B/fp8%2BumnVaZv27YNJycnVQYFkJeXp1osU%2B3YsYOBAwfW%2BnrVkJubWyvrGThwIDt27KiVdZmjoKAAvV5/u4chhBBCCGGkxj3foaGhfP7550yePBmrq59Ujh8/jk6no23btoblysvLiY%2BPZ/PmzeTl5XH//fczadIkunfvDkBwcDBhYWHs2rWLP/74g2bNmjFjxgw6d%2B7M2LFjSU9PZ968eZw4cYK%2BffsCsG7dOj7%2B%2BGOysrIIDAxk0aJFODk5kZGRwauvvsrx48dxcHCgQ4cOzJ07Fzc3tyrjP3LkCIsXL%2BbixYvUr1%2Bfnj17EhkZiY2NDcHBwbz00ksMHTqUUaNG0bFjR44dO8bJkydxd3cnPDycRx99FICUlBQWLlzIkSNHsLOzo2/fvsyaNQs7OzsuXrzIokWLSExMpE6dOgwcOJCJEydiZ2d3w32rKArvvPMO27dv59KlS2g0GgIDA1m4cCEODg6cPn2a%2BfPnc%2BrUKZycnOjUqRNz5szhm2%2B%2BIS4ujrKyMvz8/Pj555%2BrxD579izz58/nxIkTNG7cmICAAKP5SUlJREdHk5ycTP369RkxYgRPP/00Go3GaLlt27axatUqvvvuOw4dOsTMmTN57LHH%2BPDDDykpKSEgIIDFixfj5OSEoijExcWRkJBAcXExAwcO5Pfff2f48OGGfdypUyfCw8MBSE1NpVevXuzZs4fGjRuTnZ1NdHQ0Bw4cQKPREBwczPTp03FycrrhuvPy8njuuecA8Pb2Zv369Xh7e99w3wNkZmaSlZVlNK2hq2u1x5G4dWoXOCrjWSquWiqfShqNBYo8JhzfNdK6tfFPlfzt5US1eGrHxUbl06GsrY1/quiO2ae2turGq3yM1H6shGnuskq16pQa8PLyUn788Uelc%2BfOyv79%2Bw3T58yZo6xdu1YZOXKksmLFCkVRFGXFihVKYGCgcuLECUWv1ys7duxQ2rdvr/z666%2BKoihKUFCQ0qdPH%2BXChQvKlStXlMjISKVv376GmEFBQcrWrVsVRVGUgwcPKl5eXsprr72maLVa5fLly0r37t2V2NhYRVEUZfr06cqrr76q6HQ6paCgQHnmmWeUqKioarehZ8%2BeyrZt2xRFUZSUlBSlW7duyldffVVlnSNHjlQ6deqkJCUlKSUlJcrSpUsVX19fRavVKnq9XunTp48ye/ZspbCwUMnOzlYGDRqkxMTEKEVFRUpQUJASExOjaLVaJT09XRk%2BfLgSExNT7XhWrFihjBw5UlEURdmxY4fy8MMPK%2BfPn1cURVHOnDmjdOrUSdm8ebOiKIry1FNPKStXrlTKy8uVnJwcZcCAAcr69eurxPk7nU6n9OrVy7D/Tp06pfTo0UMJCgpSFEVRLl%2B%2BrPj6%2BioJCQmKTqdTTp8%2BrfTp00f56KOPqsTeunWr4X6Vj8u8efOU4uJi5cKFC8rDDz%2BsxMXFKYqiKJs3b1Y6d%2B6snDhxQtFqtUp0dLTSqlUro31cebxUPh5eXl5KSkqKUlZWpjz22GPKK6%2B8ohQUFCi5ubnK%2BPHjlcmTJ5u07sr5NbFixQrFy8vL6LZi%2BfIaxRBCCCH%2B56Wnq3%2B7i9T4I6ONjQ2hoaF8%2BumndOvWDa1Wy%2B7du/nyyy/54YcfDMtt3bqV559/nnbt2gHw6KOPsnv3brZs2UKHDh0AGD58OM2aNQMqKuqfffbZDdcdHh6Ovb09jRo1wt/fn4sXLwJgb2/PkSNH2LFjB126dCE%2BPt5Qlf87e3t7du3ahbOzM/7%2B/uzbt%2B%2B6y/bt29dQzR8yZAixsbHk5OSQmppKWloas2bNwtHRkbp167Jq1SrKy8vZu3cvOp2OKVOmoNFo8PDwYNKkSURERDB16tQbbl9gYCA%2BPj64u7uTm5tLXl4ezs7OZGRkGMa%2Bf/9%2BWrRoQZcuXfj888%2BvO/ZrJSYmcunSJaZPn469vT0tW7bkmWee4d133wUq%2BrhbtGjBU089BcCDDz7Is88%2BS0JCAk888cRN40%2BcOBEHBweaNWtGQEAA58%2BfB%2BDzzz/n8ccfNxwDU6dOveljXOnEiRMkJSWxYcMG6tatC0BkZCT9%2BvUz6m2/3rpvRVhYWJU%2B%2BIaurqAotxyzWhqN6jHLytUuU1WwtoayMnVjXrmibjwrK6hbF4qKoLxcvbhqFyk1GnB0hOJi9Q%2BpOt181A3YujV8%2BCGMGAHJyaqF1f50TLVYULFP7e2hpETdfepQlKNeMKg4mJyd4c8/VX9C6eq5qBpPo6koUuv16u5Tu1yVL6BgYwOurpCdDaWl6sZu1EjdeBZ4zTfEFXekW/p/zdChQwkLC6OwsJBvv/0WHx8fGjZsaLRMdnY2TZo0MZrWuHFjkq95IXd1df3/gdjYoNzk4Kxfv77hd1tbW8quvojNnj2buLg41q1bx4wZM2jdujWzZ8/Gz8%2BvSox3332XlStX8tprr5GVlUX37t2ZP38%2B7u7uVZa9dptsrv5rq7y8nKysLOrXr4%2Bjo6PRtgHs3r2b3Nxc/P39DfMURUGv15OTk4OLy/VfKBVFYdmyZXz//fc0aNCANm3aoNfrDfvlrbfeYuXKlSxbtowpU6bg4%2BPD/Pnzadmy5Q33W0ZGBvXr18fBwcEwrWnTpobf09LSSEpKMtpf5eXlWJuYfVy7n2xtbQ3jzcnJwcPDwzDPxsamyjFxPampqZSVldGjRw%2Bj6XZ2dqSkpNx03bfCzc2taouJJV4w73JqJsh/j6tmbLXf1yo/JyuKBfZBYqLKAa9KTlY1tqWeToqicmy1k7lKZWWqx75j9qmlzsEpLbVcbHF90nZilltKvlu3bs0DDzzArl272L59O08//XSVZTw9PY2SJKjok7ZE/%2BzJkycJCwsjPDyc3Nxc3n77bV566SUOHjxotFxJSQlnzpxh/vz52NjYcP78eWbPns2iRYtYsWKFyetzd3cnLy%2BP4uJiQwL%2B888/c%2BLECdzd3WnatClfffWVYfnCwkJycnJo0KDBDePGxMSQnp7Od999Zzh5NTQ0FKhIhk%2BePEl4eDizZs3i0qVLLF68mBkzZrB169YbxvXw8CA3N5eioiJDFfnayzi6u7sTEBDAunXrDNPy8vIoKioyeZ9Up0mTJkbHgKIohio%2BgJWVldFJkdeeZOvu7o6DgwOHDh0yfAjQ6XSkpKTQrFkzjh49atbYhBBCCHGLJPk2yy3vvaFDh7Jx40bOnz9fpToJ8Nhjj7F27VqSkpIoKytj165dfPfddwwZMsSk%2BHZ2dhQUFJi0bGxsLFFRURQWFnLPPffg6OhoVCWvpNFomDJlCuvXr6e0tJSGDRtiY2NT7bI30qFDB5o3b86SJUsoLi4mOzubxYsXk5ubS1BQEEVFRcTHx6PT6cjPzycyMpLJkydXOXnx7woLC7G3t8fa2pqSkhLWr1/PqVOn0Ov1WFlZsWDBAt566y1KSkpo0KAB9vb2hrHb29tTWFhYbeXX29ub%2B%2B%2B/nwULFlBcXMwff/zB%2BvXrDfNDQ0P55Zdf%2BOKLLygtLSUzM5MJEyYQHR1do/3yd0899RSbN2/m2LFj6PV61q5da5T0t2jRgv3795Ofn09BQQHvvPOO0T5u1qwZ0dHRFBUVodVqWbRoEWPGjDH8x%2BNG7O3tAUw%2BhoQQQgghasMtJ98DBgzgjz/%2BYODAgYaWjGs988wzPPXUU0yePBk/Pz/i4uJYunQpnTp1Min%2B8OHDWbZsGdOmTbvpsq%2B//jrl5eX06tULf39/fv31V5YvX15lOTs7O9asWcOePXsICAggODiYhg0bmrSOa9na2hIbG0tGRgY9e/Zk0KBB%2BPv7ExERgZOTExs3buTQoUMEBgbSu3dvrKysWLNmzU3jvvzyy2i1Wrp27UpwcDC//PILgwYN4tSpU0BF28nZs2fp1q0bXbt2paCggKioKACCgoL4888/8fX1JT8/3yiutbU1a9euJTMzk65duzJu3Dh69eplmO/p6Ul8fDybNm2ia9euDBo0iAceeMDs5LtHjx68%2BuqrzJw5k27dupGWlmb0n4/x48fj4uJCr169GDRokFG/tY2NDXFxcWRnZ/PII4/QrVs3Ll68yIYNGwyJ9Y14eXnh6%2BtL9%2B7d2bdvn1nbIYQQQohryHW%2BzaJRzGmSFaKGrr2c4x3BUifJ3MUnXBYWqhvPygrq1YOCgn/2CZdWVlCnTsUJp2r3fDvVU/nx9/aGY8fAx0fVnu/iK%2Boe9xoNODiAVqvuU8oxP%2BPmC9WEjQ24uEBOjuo93yXO6p4cqNGAnR3odOruU/vMlJsvVBO2tuDuDpcvq9/zffUcLtX8L55wmaPySclQ8Ry5S8gFMoUQQgghhOnuskq12iT5FkIIIYQQppPk2yySfIta9d13393uIQghhBBC3DaSfAshhBBCCNNJ5dsssveEEEIIIYSoJVL5FkIIIYQQppPKt1kk%2BRZCCCGEEKaT5NsssveEEEIIIYSoJVL5FkIIIYQQppPKt1lk7wkhhBBCCFFLpPIthBBCCCFMJ5Vvs8jeE0IIIYQQprOyUv9mppycHF588UX8/PwICAhg4cKFlJaWVrvsvn37CA0NpWPHjvTv35/vv//eaP4777xDYGAgHTt2ZNSoUZw7d87s8V1Lkm8hhBBCCHFHe/nll6lTpw779%2B9ny5YtHDhwgI0bN1ZZ7sKFC4SHhzNp0iR%2B/vlnwsPDefnll8nIyADg008/5f3332fdunUcOnSIdu3aERERgaIoqo1Vkm8hhBBCCGE6C1S%2BMzMzSUpKMrplZmaaNJw//viDw4cP88orr%2BDo6EiTJk148cUX%2BeCDD6os%2B%2Bmnn%2BLn50fv3r2xsbHh0Ucfxd/fn02bNgGwefNmRowYQcuWLbG3t2fq1Kmkp6dz6NAh1Xaf9HwLcQMKGtVjaiwQ15oyVeNdG1nt2PdmX1A1HnZ2UK8J9f5MAZ1Ovbhq9zTa2UEdT%2Brkpak7TqD4inoVGQCNBhwA7U/HULHYg2MdlZ9P3t5w7BgOXX0gMVG1sGWl6u5PAGugzNlF9bj2hw%2BoG7BuXejQAbvk41BUpFpYvV8X1WJVsgX0Lu4WiKv%2B4y9ubtOmTaxatcpo2ksvvUR4ePhN73v69GmcnZ1p1KiRYVqLFi1IT08nPz%2Bfe%2B65xzD9zJkzeHl5Gd3/wQcfJDk52TD/ueeeM8yztbWlefPmJCcn07lz51vatr%2BT5FsIIYQQQpjMEoWpsLAwgoODjaY1bNjQpPsWFRXh6OhoNK3y7ytXrhgl39Ut6%2BDgwJUrV0yarwZJvoUQQgghhMnKy9WP6ebmhpub2y3dt06dOhQXFxtNq/y7bt26RtMdHR3RarVG07RarWG5m81Xg/R8CyGEEEKIO1bLli35888/yc7ONkw7e/Ys7u7u1KtXz2hZLy8vTp8%2BbTTtzJkztGzZ0hDr2vl6vZ4LFy5UaVUxhyTfQgghhBDCZOXl6t/M0bx5c3x9fVm0aBGFhYWkpKSwevVqhg8fXmXZgQMHcvjwYXbu3ElpaSk7d%2B7k8OHDDBo0CIBhw4aRkJBAcnIyJSUlvPnmm7i6uuLn52feIK8hybcQQgghhLijrVixgtLSUnr16sXjjz9O9%2B7defHFFwHw9vbmiy%2B%2BACpOxHz77beJi4vD39%2Bf1atXs3LlSu6//34Ahg8fzpgxY5g4cSKdO3fm5MmTxMXFYWtrq9pYNYqaFy4U4n%2BMJZ4dGo36cTXlFrraibU1lKkc%2B8IFdePZ2UGTJpByB1ztxNMT0ixwtRP3%2B1WNp9GAgwNoteoeq5a62gk%2Bd8DVTizwVAKwttDVTjh%2BB1ztxBb0etXDYmuj9gu0BV70K%2BPeJiUl6se0t1c/5j%2BVnHAphBBCCCFMZokTLu8m0nYihBBCCCFELZHKtxBCCCGEMJlUvs0jlW8hhBBCCCFqiVS%2BhRBCCCGEyaTybR5JvoUQQgghhMkk%2BTaPtJ0IIYQQQghRS6TyLYQQQgghTCaVb/NI5VsIIYQQQohaIpVvIYQQQghhMql8m0eSb3FHKygoQK/X06BBg9s9FCGEEOKuIMm3eSzadtKqVSuef/55FEUxmr5t2zaCg4Mtss7g4GC2bdtmkdim2LlzJ126dMHX15fvv/%2B%2B2mUOHDjAuHHj8Pf3x9vbm5CQEFatWoVWq63l0VY1fPhwHnroIbKysm73UEzSp08fTp8%2BfbuHIYQQQghhEov3fO/bt4/4%2BHhLr%2BYf45NPPiEkJISjR48SFBRUZf5HH33Eiy%2B%2ByMMPP8zu3bs5evQoS5Ys4cCBA4SFhVFUVHQbRl3h119/5fLlywQGBpKQkHDbxlETeXl5t3sIQgghxF2lvFz9293E4m0no0aNYvny5fj6%2BuLj41NlfmpqKr169WLPnj00btwYgJUrV3L48GHef/99tm3bxpYtW/jXv/7F1q1bsbKyYuLEidjb27NmzRry8/MJCQnh9ddfN8RMSkoiISGB1NRUHnroIebMmUPz5s0BuHjxIosWLSIxMZE6deowcOBAJk6ciJ2dHdu2bSMhIQFnZ2eOHz/OvHnzCA0NNRpvXl4eS5cu5fvvv0ev19OxY0dmzpxJ8%2BbNGT58OElJSRw5coS9e/fy7bffGt03KyuLxYsXExUVxaBBgwzT27dvT3x8PKGhoaxevZpXXnmFlStX8t///hdra2v2799PgwYNGD9%2BPGFhYQAUFhaydOlS9uzZg06no3Pnzrz66qu4uroa9umCBQtYs2YNf/31Fx06dGDx4sW4u7tf97FKSEigX79%2BBAUFMWXKFCZMmICjo6Nh/n/%2B8x%2BWLVvG2bNnqV%2B/PmPHjmXkyJEAbN%2B%2Bnbi4ONLS0nB3dyc8PJxHH30UqPhAsnHjRi5duoSnpyfPPfccAwcONBwfnTp1Ijw8vNrjoVWrVsyePZuEhAQyMzNp1aoVr732Gq1ataJv374APPfcc4SHh/Pkk08yZ84cfvrpJ2xsbGjdujWzZs2iRYsW193ma2VmZlap%2BLu6NsTNzc2k%2BwsT2dmpG8/W1vinWqxUrk1YapyARmOZeGrHxdtb3XitWxv/vBvVratuvMrX/Gte%2B4UQKlMsyMvLSzl48KDy%2BuuvKz169FDy8vIURVGUrVu3KkFBQYqiKEpKSori5eWlpKSkGO63YsUKZeTIkYZlvby8lA0bNihlZWXKBx98oLRp00aZMmWKcuXKFeX48eNKmzZtlMOHDyuKoihBQUFKYGCgkpycrGi1WmXu3LnKI488ouj1eqWoqEgJCgpSYmJiFK1Wq6SnpyvDhw9XYmJijNa1bds2paSkRCkuLq6yTSNHjlRGjx6tZGZmKsXFxUp0dLTSo0cPpaCgwDB/xYoV1e6PrVu3Ku3bt1dKSkqqnf/WW28pwcHBhn3g5eWlrF%2B/XtHpdMr%2B/fuVdu3aKT/99JOiKIoSHh6ujB07VsnOzlYKCwuV2bNnK2FhYUp5eblhn7744ovKX3/9pWRlZSkDBgxQ5syZc93HKjs7W3nooYeUM2fOKOXl5Ur//v2V999/3zD/3LlzSvv27ZVPPvlE0ev1ym%2B//aZ4e3srP/zwg3Lw4EGlffv2yt69e5WysjJl3759Srt27ZTTp08rW7duVXx8fJSffvpJKS0tVX766SfFx8dH%2Bfrrr6vdX38/Hry8vJSwsDAlMzNTyc/PV8aMGaOMHTvWsHzlMaYoirJ8%2BXJl3LhxSnFxsVJSUqJERkYqEyZMuO42/13lPr/2tnx59Y%2BlEEIIcbdKT1f/djeplRMuIyMjSUxMZMaMGaxZs6bG969Tpw5PP/00Go2Gbt26UVZWxrPPPoujoyMPPfQQbm5upKWl4e/vD8DYsWNp1aoVADNmzMDPz4/jx49z%2BfJldDodU6ZMQaPR4OHhwaRJk4iIiGDq1KkA2NraMmjQIKyqqXqlpKRw%2BPBhduzYQcOGDQGYNm0a27dvZ9%2B%2BfYSEhNxwOzIzM7n33nuxu07lz83NjczMTMPfrVq14plnngGgW7du9O3bl88//xwvLy92797Nrl27cHFxAWDWrFn4%2BfmRlJSEs7MzUFERvueee4CKXvjExMTrjm3Tpk106tTJUCUeNWoU69atY8SIEVhZWbFjxw7atWvH8OHDgYpq/Ycffoibmxv//ve/eeSRR%2BjRowcAgYGBfPjhhzRq1IitW7cSFhZGly5dAOjSpQthYWF8/PHH9OnT54b7q9KoUaMM%2B7t///7ExcVVu5yDgwPJycl89tlnPPzwwyxatKjax/F6wsLCqpyL4OrakL%2BdsmA2jQb1Y5aXqRuwkrU1lKkcOz1d3Xi2tuDuDpcvg16vXlxLVL7d3CAzU91xAloXT1XjaTRgbw8lJeoeqw5dq/730yytW8OHH8KIEZCcrFrYsiPHVItVyRJPJQDrpOPqBnR0hJYt4fRpKC5WLay%2BTQfVYlWytVX9qVQR1%2BYOeNGvjHub3G1tImqrleTbzs6Ot956iyFDhrB%2B/Xrq169fo/s7OzujuXqQVSZTlUll5bTya46EyvYVAEdHR5ydncnIyCAtLY3c3FxDkg6gKAp6vZ6cnBwAGjZseN2ELTs7G4AmTZoYpllbW%2BPh4UFaWtpNt6Nhw4bk5ORQUlKCvb19lfmpqamGJBMwtMpU8vDw4L///a9hXY8//rjRfGtra1JTUw3Jt6urq2GejY1NlRNfK5WWlvLxxx%2BTn59PQEAAAOXl5eTn5/PNN9/Qt29fMjMzue%2B%2B%2B4zu1/rqv3ozMzNp27at0bwOHSpeaLOzs432F1Q8Pt999121Y6mOqdvx3HPPYWdnx5YtW3j99ddp0qQJU6dO5ZFHHjFpPW5ublVaTCzxennX0%2BksE1evVze22sl3JbXHieWOU0VROfYNCgBmSU62XOx/OkudJ1RcbLnYQtzlau1Sg02bNiUqKorp06czdOhQw3Rra2sA9Nd8fP37SXSaGn66u7Z6XFhYSF5eHp6enpSWltK0aVO%2B%2Buoro/k5OTmGS9XdaF2enhXVpYsXL9KyZUsAysrKSE9PN0qarycoKAhbW1u2bdvGk08%2BaTSvqKiInTt30q9fP8O0jIwMo2VSU1Px8PCgUaNGAOzatctovWfOnKFJkyY1vlLJN998g06nY8eOHYbHA2D58uVs2LCBvn374uHhwb59%2B4zut3XrVlxcXPDw8CD9b9XM9evX07FjRxo3bszFixeN5qWkpBjGbWVldcPHviZ%2B//13goODGTNmDAUFBXz44YdMnjyZgwcPUq9evVuOK4QQQoj/J5Vv89TqN1w%2B%2BuijDBs2jE2bNhmmubi4cO%2B997Jjxw4URSEpKckoOb4V69ev59y5cxQXF7Nw4ULatGlD%2B/btCQoKoqioiPj4eHQ6Hfn5%2BURGRjJ58mSTEnw3Nzd69OjBggULyMrKQqvVEhMTQ1lZWbVXNvm7Bg0aMHfuXN544w02btxIbm4uer2e48ePM27cOOrWrcvEiRMNy//yyy98/vnnlJWVsW/fPvbs2cOwYcNo1KgRPXv2ZOHCheTl5aHX61mzZg3Dhw8nPz%2B/xvsrISGB0NBQPD09cXd3N9xGjRpFYmIix44dIyQkhJMnT/LZZ59RVlbGiRMniI6OxsbGhiFDhvDNN9/w448/Ul5ezv79%2B1m5ciX16tVj%2BPDhbNq0iQMHDlBWVsbBgwfZtGkTw4YNA6BFixbs37%2Bf/Px8CgoKeOedd2o0djs7OwoKCoCKEzunT59OTk4OTk5OODk5UadOneu2%2BQghhBCi5uRqJ%2Bap9S/ZmTVrFr/%2B%2BqshSbSzsyMqKooVK1awbt062rdvz%2BOPP87Ro0dveR29e/dmwoQJ5OXl4e/vz%2BrVq7GyssLJyYmNGzcSHR1NfHw85eXlBAQE1KgP/Y033iAmJoYhQ4Zw5coVOnbsyLvvvmto9biZ4cOH07RpU9avX09sbCwlJSV4eHjQr18/xo0bR506dQzLtmnThj179rBgwQJcXV3597//jffVqwW88cYbvPnmmwwePJjCwkJatmxJfHw8DRs2JDU11eTtSU5O5uefCrKL1QAAIABJREFUf2b27NlV5rVt25b27duzfv16Vq1axdq1a3nzzTeJiorCxcWFGTNm0K1bNwCWLFnCkiVLSEtLw9PTk6VLl9KyZUtatmxJYWEhCxYsID09nUaNGjF9%2BnQGDx4MwPjx43n11Vfp1asX9erVIyIigt27d5s8/rCwMKZOncqYMWOYMmUKr7/%2BOiEhIZSUlPDAAw%2BwevXqalt8hBBCCCFuB41yvQZacVtde7lFcftY6hyZu/qEywsX1I1nZwdNmkBKyj%2B759vODjw9IS1N9Z7vYvf7VY2n0YCDA2i16h6rjnVUPkHM2xuOHQMfH1V7vstK1X/iW%2ByEy8MH1A1Yty506ADHj6va863366JarEpywuXtO%2BHy/Hn1Y96v7svYP1qttp0IIYQQQghxN6v1thMhhBBCCHHnutt6tNUmyfc/VOU3PgohhBBC/JNI8m0eaTsRQgghhBCilkjlWwghhBBCmEwq3%2BaRyrcQQgghhBC1RCrfQgghhBDCZFL5No8k30IIIYQQwmSSfJtH2k6EEEIIIYSoJVL5FkIIIYQQJpPKt3mk8i2EEEIIIUQtkcq3EEIIIYQwmVS%2BzSPJtxBCCCGEMJkk3%2BaRthMhhBBCCCFqiVS%2BhfhfYGXBz9Eqxy5r3kLVeADWQNl9TdSNWfiXqvEM%2B/Gee1QvGznmZ6gaDxsbcHDBoSgHSktVC1tWqqgWq5I1UHbkmLoxbTSqxsPbG44dw9rfBxITVQ2dmqLuPrW1hUZARqMO6PXqxW3cu4d6wQBatoT4eGxfGAenT6sbu1079WI1aQIzZ0J0NKSkqBcXYPVqdePVgFS%2BzSOVbyGEEEIIIWqJVL6FEEIIIYTJpPJtHkm%2BhRBCCCGEyST5No%2B0nQghhBBCCFFLpPIthBBCCCFMJpVv80jlWwghhBBCiFoilW8hhBBCCGEyqXybR5JvIYQQQghhsjst%2Bb5y5QpRUVF89913lJaW0qtXL%2BbNm0fdunWrXX737t2sXr2alJQUnJ2dGTp0KC%2B%2B%2BCJWV7%2BvoX///qSnpxv%2BBtiyZQstWpj2PRaSfAshhBBCiP9ZUVFRXLp0id27d1NWVsbLL79MTEwM8%2BbNq7LsiRMnmD59Om%2B99RY9evTg/PnzPPfcc9SpU4exY8dSWFjI%2BfPn2bNnD56enrc0Hun5FkIIIYQQJisvV/%2BWmZlJUlKS0S0zM9PssRYXF7N9%2B3YiIiJwdnbGxcWFadOmsW3bNoqLi6ssn5aWxhNPPEFQUBBWVla0aNGCPn36cOTIEaAiOXd2dr7lxBuk8i2EEEIIIW6zTZs2sWrVKqNpL730EuHh4Te9r1arJSMjo9p5xcXF6PV6vLy8DNNatGiBVqvlwoULtGnTxmj5vn370rdvX6PYe/fuJTQ0FIDffvsNR0dHRo4cyenTp/H09CQ8PJygoCCTt1WSbyGEEEIIYTJL9HyHhYURHBxsNK1hw4Ym3ffXX39l9OjR1c6bNGkSAHXq1DFMc3R0BKCoqOiGcQsLC5k0aRIODg6MGTMGAI1Gw0MPPcSUKVO47777%2BOqrrwgPDychIYGOHTuaNF5JvoUQQgghhMkskXy7ubnh5uZ2S/cNCAjg999/r3beyZMnWb58OcXFxYYTLCvbTZycnK4b89y5c0RERODi4sJ7771nWHbcuHFGyw0cOJAvv/yS3bt3m5x8S8%2B3EEIIIYT4n3T//fdja2vLmTNnDNPOnj2Lra0tzZs3r/Y%2B%2B/bt47HHHqN79%2B6sW7eOe%2B%2B91zBv3bp1HDhwwGh5nU6Hvb29yWOS5FsIIYQQQpjMEidcWoqjoyP9%2B/cnJiaG3NxccnNziYmJYcCAATg4OFRZ/pdffmHixInMnDmTyMhIbGyMm0QuXbrEa6%2B9RkpKCqWlpWzZsoXExESGDBli8pgk%2BRZCCCGEEP%2Bz5s2bR/PmzQkNDaVfv340btyYuXPnGuaHhIQQGxsLQGxsLKWlpSxcuBBvb2/DrbLdZPr06QQGBjJixAj8/Pz4%2BOOPWbt2Lc2aNTN5PNLzfRf4448/anRQCCGEEEJcz532JTtOTk5ERUURFRVV7fwdO3YYfq9Mwq/Hzs6OWbNmMWvWrFsej2qV71atWvH888%2BjKIrR9G3btlU5e1UtwcHBbNu2zSKxTbFz5066dOmCr68v33//fbXLHD9%2BnIiICLp27YqPjw/9%2B/cnLi6O0tJS1caRmppKq1atSE1NBcDb25uff/4ZgCVLlrBmzZrr3jc4OJiHHnrI8MmuY8eOdOvWjSVLllB%2Bi8%2Bumz3mM2bMYMaMGbcUWwghhBC3153UdvJPpGrbyb59%2B4iPj1cz5D/aJ598QkhICEePHq32%2Bo5fffUVo0ePxt/fn6%2B//pqjR4/y5ptvsn37dqZOnWqxcSUmJuLn5wdAXl7eTZd/7bXXSExMJDExkV9%2B%2BYV169bx2WefVbnephBCCCGEMI%2BqyfeoUaNYvnw5x44dq3b%2B3yu0ACtXrmTUqFFARcV0xIgRLFmyhE6dOtG5c2fef/99Nm/eTFBQEL6%2BvkY9OgBJSUkMHTqUTp068eyzz3LhwgXDvIsXLzJhwgQCAgIICgpi2bJl6HQ6w7qGDh3K2LFj8fPzY/v27VXGm5eXx5w5c%2BjWrRsBAQGMHz/eEH/48OEcPHiQjz/%2BmN69e1e5b0lJCfPmzWPixImMGjUKJycnNBoNbdu2JSYmBkVR%2BPPPPw37JDo6Gn9/f1577TWg4l8goaGh%2BPr6MnToUH788UdD7MLCQiIjI/H19aV79%2B58/vnnRutu1aoVhw4d4u2332b79u1s376dgQMHXu9hq6JVq1b4%2B/tz8uRJoOJxnTFjBkFBQfTs2ZPCwkJ%2B//13nnvuOTp16kRgYCDz58%2BnoKDAEKO0tJQlS5bQtWtXevfuTXx8fJX/ilS60baOGjWKFStW8OSTT9KxY0cGDhzI8ePHmTp1Kj4%2BPgQHB7N3717DOufPn8/DDz9MQEAAI0aM4OjRoyZvtxBCCCFuTirf5lG157tPnz4oisKUKVP47LPPcHZ2rnGMo0eP8sgjjxgS2wULFtC/f3927tzJmTNnCAsLIzQ0FH9/fwC%2B/fZb1q5dS/PmzVm0aBHjx49nx44d6HQ6xowZQ0hICMuXLyc3N5eIiAjKy8sNVeekpCSio6OJjY2ttsUiIiICKysrPv30U%2BrVq8fy5csZM2YMX375JVu2bGHUqFF06tSp2m9fOnbsGH/%2B%2BScDBgyoMq9169asWLECqEikoeJC7//5z3/QarXs27ePefPmsWbNGnx8fPjhhx8IDw9n8%2BbNtGzZktdff52LFy/y9ddfY2Vldd0q%2BsSJE0lJSQEgOjrapP2v1%2Bs5duwYBw8eNNqun376iU8%2B%2BQRHR0f0ej2jR49m6NChrFy5koKCAqZNm8b06dMNLS4ZGRlYWVmxd%2B9eTp06xbPPPourqyuDBw82Wt/NthUqvvXq3XffpWnTpowdO5YRI0bw1ltvER0dzdKlS4mKiqJnz558/vnnJCYmsmvXLurWrcuKFSt47bXX%2BOKLL0za9szMTLKysoymubo2vOXrjoo7nJXK56NXxlM7LoCNyqfvWFsb/7zbeHurG691a%2BOfKrK1VTde5aGk9iHF1ddz1TRtavxTTU2aqBerUSPjn0JggRMuIyMjSUxMZMaMGTfsNb6eOnXq8PTTT6PRaOjWrRtlZWU8%2B%2ByzODo68tBDD%2BHm5kZaWpoh%2BR47diytWrUCKnqJ/fz8OH78OJcvX0an0zFlyhQ0Gg0eHh5MmjSJiIgIQ7Jqa2vLoEGDsKrmzTAlJYXDhw%2BzY8cOwzcsTZs2je3bt7Nv3z5CQkJuuB25ubkAuLq6mrTdgwcPxs7ODjs7OxISEnjyyScN2xgUFERwcDAff/wxkZGR7Nq1i9jYWFxcXICKM28HDRpk0nqq89prr7Fo0SLD3%2B7u7jzzzDOMHDnSMC0wMJBGV188tmzZgq2tLdOmTcPa2hoHBwfmzJlDSEiIIXmtX78%2BU6ZMwdramvbt2xMWFsYXX3xRJfm%2B0bbOmTMHqPiq1wcffBAAPz8/8vPzDf9tCAwMZMOGDQA4ODiQmprKli1bCAwMZNKkSUyePNnk/VDdV9tOnPgSERE3/2rbmtJoVI%2BodsBrQqsb21L5nOpx69VTOeBVV7/k4Y5wCwWUG7FUKq/6Y3%2Bd/96a7cMPVQ9pqZTu6tuLeizVkvq3/4b/Y40de7tHoKq7rVKtNtWTbzs7O9566y2GDBnC%2BvXrqV%2B/fo3u7%2BzsjObqm31lUnzPPfcY5ltZWRlVqRs3bmz43dHREWdnZzIyMkhLSyM3N9eQ1AEoioJerycnJweo%2BNrS6hJvgOzsbACaXPMJ2NraGg8PD9LS0m66HZUJe1ZWFvfdd1%2BV%2BVlZWUZfm3ptdTUtLY3Dhw/z0UcfGaaVlZXRuXNn8vLy0Ol0eHh4GOY1MfNT%2Brx58xg6dOgNl7l2fDk5Odx3331YX/OOV/k4VO4bDw8Po/keHh7s2bOnStwbbWula/%2BDYm1tbXSxeysrK0M7S0hICHq9nk8%2B%2BYSlS5fi4uLChAkTePLJJ2%2B8A66q7qttXV0bcp1umVum0aB%2BTFQOaAis/mDLytX/oGBtDWVlKse8UnDzhWrCyqoi8S4qUv%2Bd62o7nWqsrSsS7z//VHXHljmrndFZ6LH391E3YOvWFYn3iBGQnKxq6Ixd6n5QsLGpSLxzckDF6wLQ6NVxN1%2BoJpo2rUi8X38dLl5UN3aLFurFatSoIvFevx4yMtSLCzBzprrxakCSb/NY5FKDTZs2JSoqiunTpxsldZXJmF6vN0z7%2BwmBmhpW2TIzMw2/FxYWkpeXh6enJ6WlpTRt2pSvvvrKaH5OTg4NGjS46bo8PT2Bir7xyvaHsrIy0tPTjZLm6%2BnYsSPOzs7s3LmzyleRJicnM2jQID7%2B%2BGNDrGvH4u7uzuDBg3n%2B%2BecN09LT03FwcMDJyQl7e3tSUlJ44IEHALh8%2BfJNx2Oua8fn6elJeno6ZWVlhsf04tUXv4YNG3Lu3DmysrJQFMVwv5SUFMM%2BvdaNtrW6dd/I%2BfPnadeuHYMHD0ar1fLVV18RGRmJn5%2Bf4TG8keq%2B2lbtJFncQSz17mKJBkc1s6RrlZVZLvY/WWKiZeImJ6se%2B5q3U1WVlqoc%2B/RpFYNd4%2BJF9WPb2akbDyoS76ttoEJY7Et2Hn30UYYNG8amTZsM01xcXLj33nvZsWMHiqKQlJRklBzfivXr13Pu3DmKi4tZuHAhbdq0oX379gQFBVFUVER8fDw6nY78/HwiIyOZPHmyScmcm5sbPXr0YMGCBWRlZaHVaomJiaGsrKzaK5v8nZ2dHbNnz2bVqlV88MEHFBUVUVZWxs8//8ykSZPo27cv3tfpK3z88cd57733OH78OAC//fYbQ4cO5csvv8TOzo7BgwezfPlyLl%2B%2BTEFBAf/%2B979vOI5rT4RUQ48ePQCIiYlBq9WSlZXFwoUL6dy5syHBzsrKYs2aNeh0OhITE/nkk0944oknarStNfX999/z0ksvkZqaioODA87OztjY2FDPUu0DQgghxF1ITrg0j0W/ZGfWrFn8%2Buuv5OfnAxWJYFRUFCtWrGDdunW0b9%2Bexx9/3KwrUvTu3ZsJEyaQl5eHv78/q1evxsrKCicnJzZu3Eh0dDTx8fGUl5cTEBBQoz70N954g5iYGIYMGcKVK1fo2LEj7777rsknkoaGhlK/fn3Wr1/PypUrKSkpwcPDg2HDhvHMM89c9379%2BvXjypUrzJo1i/T0dJydnRkzZozhqjCvvvoqixcvJjQ0FBsbG0aPHn3d64w/%2BuijTJ48mZ49exquCmKuevXqsWHDBqKjow2JeK9evZg%2Bfbphmcqr2gQEBNCwYUOmT59e7bW/b7atNTF69GgyMjJ44oknKCwsxNPTk2XLluHu7n7rGyuEEEIII3dbsqw2jXK9678JISzSdiI933dIz3fhX%2BoGtLKqOImzoED9dy6tVt14Fmr8LXNV//RAizz2Niofo97eFSdx%2Bvio3naSmqLu89PWtqJNOSND3baTxk/1UC8YVFw9JT4exo1Tv%2B2kXTv1YjVpUtGbvXix%2Bm0nq1erG68Gtm5VP%2BawYerH/KeSr5cXQgghhBAmk8q3eSzW8y2EEEIIIYQwJpVvIYQQQghhMql8m0eSbyGEEEIIYTJJvs0jbSdCCCGEEELUEql8CyGEEEIIk0nl2zxS%2BRZCCCGEEKKWSOVbCCGEEEKYTCrf5pHkWwghhBBCmEySb/NI24kQQgghhBC1RCrfQgghhBDCZFL5No9UvoUQQgghhKglUvkWQgghhBAmk8q3eST5FkIIIYQQJpPk2zzSdiKEEEIIIUQt0SiKotzuQQjxj2WJp4dGo3pcBY2q8SpZYKhodnypbsB77oHAQPjhB8jPVy%2Buh4d6sQAcHaFtWzh5EoqLVQ1d0t5X1XgaDdjZgU6n7uNvf%2ByAesEA6taFDh3g%2BHEoKlItbGqTLqrFArC1hUaNICMD9HpVQ9O4icrPfW9vOHYMfHwgMVG1sH9cUPeFxM6u4il66VLFcaqmxo3VjWdtDWVl6sasjHu7xMWpH3P8ePVj/lNJ5VsIIYQQQohaIj3fQgghhBDCZNLzbR5JvoUQQgghhMkk%2BTaPtJ0IIYQQQghRS6TyLYQQQgghTCaVb/NI5VsIIYQQQohaIpVvIYQQQghhMql8m0eSbyGEEEIIYTJJvs0jbSdCCCGEEELUEql8CyGEEEIIk0nl2zxS%2BRZCCCGEEKKWSOVbCCGEEEKYTCrf5pHkWwghhBBCmEySb/NI24kQQgghhBC1RCrfQgghhBDCZFL5No9Uvi3swoULt3sIN5WZmcmVK1du9zCEEEIIIf7n3bHJ9/nz54mMjCQwMBBvb2969%2B5NTEwMRUVFt3toBidPnmTAgAE3XEan0xEXF0doaCi%2Bvr507dqVF154gaSkJFXHMmPGDGbMmAFAbGws48aNAyA7O5u%2BffuSm5tb7f1WrlxJmzZt8Pb2xtvbm3/961888sgjfPDBB7e0biGEEELc2crL1b9Z0pUrV5g5cyYBAQH4%2Bvoyffr0G%2BaL8%2BbNo3379obcx9vbm02bNhnmv/POOwQGBtKxY0dGjRrFuXPnajSeOzL5PnbsGEOGDMHT05PPPvuMxMRE3nnnHX799VfGjh1LWVnZ7R4iAAUFBej1%2BuvOLykpYeTIkezfv58lS5Zw5MgRvvnmGzp06MDIkSM5fvy4RcY1YcIE4uPjAdBqtTetevv5%2BZGYmEhiYiK//PIL8%2BfPZ/HixRw8eNAi4xNCCCHEP9edlnxHRUVx6dIldu/ezddff82lS5eIiYm57vK//fYbUVFRhtwnMTGRsLAwAD799FPef/991q1bx6FDh2jXrh0REREoimLyeO7I5Hvu3LkMHjyYiIgIGjRoAMD999/PsmXLcHFxISUlBYBWrVpx6NAhw/22bdtGcHAwAIcOHaJHjx5MnToVPz8/1q5dy4wZM4iIiKB///507tyZixcvkp2dzbRp03j44Yfp1q0bc%2BfOpbCw0BAjODiYNWvW0L17dzp16kR4eDiFhYWkpKTw3HPPAeDt7U1iYmKV7Xj//fdJTU0lNjaWtm3bYmVlRd26dXnhhRd44oknOHXqFECNxwWwZ88eQkJC6NixI%2BPHjycvL88wb%2BXKlYwaNYqysjJDZX7AgAHs3Lnzpvteo9HQtWtXvLy8OHHiBACKorB27VpCQ0Px8/PD39%2BfqVOnotVqq9xfp9OxZMkS%2Bvfvj7e3N126dCEqKspw0I4aNYo333yTp556Cm9vb/r37280rpSUFCZMmICvry9dunRh/vz56HQ6AC5evMiECRMICAggKCiIZcuWGeYJIYQQ4u5TXFzM9u3biYiIwNnZGRcXF6ZNm8a2bdsoLi6usrxOp%2BPUqVO0b9%2B%2B2nibN29mxIgRtGzZEnt7e6ZOnUp6erpRvnkzd9wJlxcvXuT06dPMnz%2B/yjxXV1dWr15tcqzLly/zwAMPEB0dTUlJCQsWLGD//v1s2rQJd3d3nJyceOKJJ2jevDm7d%2B9Gr9czc%2BZM5s6dy9KlSwFIS0sjIyODb775hoyMDJ566ik%2B/PBDnn/%2Bed555x1Gjx5dbeIN8N1339GzZ0%2BcnJyqzIuMjDT6uybjOnfuHJMmTWLRokU8%2Buij7N27l4iICAYOHGgU09rami%2B//JJevXrx5Zdf0rhx45vuM0VROHLkCKmpqfTo0QOAXbt28d5775GQkEDz5s05e/YsI0aMYPv27Tz22GNG93/33XfZv38/7777Lm5ubiQmJjJy5Eh69%2B5Nly5dgIoDe8OGDTz44IO8/fbbzJ07l169emFtbc2zzz5LQEAAP/zwA1qtlmeffZaVK1fywgsvMGbMGEJCQli%2BfDm5ublERERQXl7O1KlTb7pdUNH7npWVZTStoasrbm5uJt1fmOiee9SNV/n8qeZ5ZBZHR3XjOTgY/1SRRmOZeGrHpW5ddeNVPkYqP1a2tqqGw8bG%2BKeqvL3Vjde6tfFPldjZqRrOsvtU3JQlKtXVvgc3bGjSe7BWqyUjI6PaecXFxej1ery8vAzTWrRogVar5cKFC7Rp08Zo%2BeTkZEpLS1mxYgVHjx6lXr16DBs2jHHjxmFlZcWZM2cMxVUAW1tbmjdvTnJyMp07dzZpW%2B%2B4w7ayN9nV1VWVeMOHD8fW1hbbq6%2B2HTt2NDxAx48fJykpiQ0bNlD36ptGZGQk/fr1Y86cOYYYEydOxMHBgWbNmhEQEMD58%2BdN3hZ/f3%2BTlq3JuHbu3En79u0NyXbv3r0JCgoyaT3VOXr0KH5%2BfkDFAa7X6xk4cCDNmjUDIDAwEB8fH9zd3cnNzSUvLw9nZ%2BdqnwiPP/44Q4YMwcXFhczMTLRaLXXr1jVatm/fvrRt2xaAIUOGEBsbS05ODqmpqaSlpTFr1iwcHR2pW7cuq1atory8nL1796LT6ZgyZQoajQYPDw8mTZpERESEycn3pk2bWLVqldG0lyZOJDwi4pb22w2pnNWonSMZxVY7eGCgygGv8vGxTFy1PfCA6iFVzmsM1E5C6dBB5YBXtWyparhGqkb7fy4uFgh67JgFggIffqhqOA9Vo/2/hg0tFFhl1ta3ewT/fNW%2BB7/0EuHh4Te976%2B//sro0aOrnTdp0iQA6tSpY5jmePUDe3V93wUFBXTq1IlRo0axdOlS/vvf/zJx4kSsrKwYN24cRUVFhvtXcnBwqNGFK%2B645Lvh1WdaVlYWzZs3rzI/Ozu7Ron53z9RXft3amoqZWVlhgpvJTs7O0Nry7VjgopPQKb2/TRs2JDMzMxq5/311184Ojpid7VcUJNxZWRkcN999xnNa9q0qVHrSU34%2Bvry/vvvG/4%2BdeoU06ZNY9q0aaxYsQJFUVi2bBnff/89DRo0oE2bNuj1%2Bmr3Q3FxMa%2B//jpHjhzB3d2dtm3boigK5dd8jL52f9pcLWuUl5eTlZVF/fr1jQ76ymr97t27q3yYURQFvV5PTk4OLia864WFhRnakgxjcXWFGvRxmUSjUT2mYqH02wJDRbP/B3UDOjlVJN7HjsE1rVdmU%2BkDvoGDQ0Xife4cVNOSZQ7dg21VjafRVCTeer26j79dssrnsTg6ViTep09DNf8%2BvlUZjdT9kGBjU5F45%2BRAaamqoWnUX%2BUPna1bVyTeI0ZAcrJqYS/tUPdDgo1NReKdlaX%2BPlX7n53W1mCJU9FuZ0Jvicp3te/BJn66CggI4Pfff6923smTJ1m%2BfDnFxcWGgmVlu0l1nQcPP/wwDz/8sOHvDh068PTTT7Nz507GjRuHo6NjlbbaykKiqe645NvT0xMvLy927txZpWqck5NDUFAQixcvZsCAAVhZWRmd8Fhd8qn5W1nv2r/d3d1xcHDg0KFDWF89ynU6HSkpKTRr1oyjR4%2BatS3BwcHEx8dTWFhY5QB49dVXKS4uZt26dTUel7u7O3v37jWKd/nyZezt7c0abyUvLy8ee%2Bwx3nzzTQBiYmJIT0/nu%2B%2B%2BM2xHaGhotfedPXs29957Lz/%2B%2BCP29vaUl5ebXP13d3cnLy%2BP4uJiQwL%2B888/c%2BLECdzd3WnatClfffWVYfnCwkJycnIM5wXcjJubW9V/b6mdeQrIz7dM3MJCdWOr3SJRSatVNVEEyx2miqJybEtdjaq4WNXYNzhP3iylpRaIfZ22RrMlJ6sa21Kn35SWWi62uD5LJN/Vvger4P7778fW1pYzZ87wr3/9C4CzZ88a2kX%2B7ttvvyU7O5snnnjCME2n0%2BFwtWWwZcuWnD592tBRoNfruXDhglFby83ckSdczpkzh61bt7Jq1Sry8vJQFIX//ve/TJgwgXbt2tG3b1%2Bgoqdn9%2B7dlJaWcvHiRbZs2VKj9XTo0IFmzZoRHR1NUVERWq2WRYsWMWbMGJOuqFKZ7BYUFFQ7f8SIEbi6uvLCCy%2BQnJyMoijk5eXx5ptv8p///IeI67Q73GxcAwcO5NSpU2zevJnS0lJ%2B/PFHvvnmmxuOsbAGFcPLly/zxRdf4Ovra7ivvb091tbWlJSUsH79ek6dOlXtlV4ql7WysqKwsJA33niDwsLCG14V5trtbt68OUuWLKG4uJjs7GwWL15Mbm4uQUFBFBUVER8fj06nIz8/n8jISCZPnlzlA5YQQggh7g6Ojo7079%2BfmJgYcnNzyc3NJSYmhgEDBhgS6mspisLixYs5cOAAiqKQmJjIe%2B%2B9Z7jaybBhw0hISCA5OZmSkhLefPNNXF1dDe25prgjk%2B9OnTqRkJDAyZMnCQkJwcfHh4iICDp37kx8fLyhf3vevHkkJSXRqVMnXn75ZYYPH16j9djY2BAXF0d2djaPPPII3bp14%2BLFi2zYsMGkKrKXlxe%2Bvr50796dffv2VZlvb2/PBx98QPv27YmIiMDX15eQkBDOnj1LQkKC4RNaTcfVpEkTYmNj%2BeCDD/D19WX16tX06dOn2liurq706dOVDM/1AAAgAElEQVSHsLAwPvroo2qX%2Bfnnn42udTl06FAefPBBQ%2BX75ZdfRqvV0rVrV4KDg/nll18YNGiQ4Wot15o9ezbJycl06tSJfv36UVhYSPfu3atd9u9sbW2JjY0lIyODnj17MmjQIPz9/YmIiMDJyYmNGzdy6NAhAgMD6d27N1ZWVqxZs%2BamcYUQQghhujvtUoPz5s2jefPmhIaG0q9fPxo3bszcuXMN80NCQoiNjQWgT58%2BzJw5k/nz5%2BPt7c0rr7xCeHg4gwYNAirOFRwzZgwTJ06kc%2BfOnDx5kri4OEPuaQqNUpMLEwpxt7HE0%2BNu7/ne8aW6Ae%2B5p%2BIkzh9%2BULftxEPlU8QcHaFtWzh5UvW2k5L2vqrG02gqrk6h06n7%2BNsfO6BeMKhoDerQAY4fV7XtJLVJF9ViQUX/fKNGkJGhfttJ4yYqP/e9vSvOn/DxUbXt5I8L6r6Q2NlVPEUvXVK/7cSEC3/VyP9iz/err6ofc%2BFC9WP%2BU91xPd9CCCGEEOL2sXSl%2Bn%2BdJN9CCCGEEMJkknyb547s%2BRZCCCGEEOJOJJVvIYQQQghhMql8m0eSbyGEEEIIYTJJvs0jbSdCCCGEEELUEql8CyGEEEIIk0nl2zxS%2BRZCCCGEEKKWSOVbCCGEEEKYTCrf5pHkWwghhBBCmEySb/NI24kQQgghhBC1RCrfQgghhBDCZFL5No9UvoUQQgghhKglUvkWQgghhBAmk8q3eST5FkIIIYQQJpPk2zwaRVGU2z0IIf6xLPH00GhUj6ugUTVeJQsMlaIideNZWUGdOnDlirpvCE5lf6kXDCoGWq8eFBSo/86Vn69uPFtbcHeHy5dBr1ctrN69iWqxKtnaqjrEipi9e6gbsGVLiI%2BHcePg9GlVQ//x3j5V49nZgYcHXLoEOp16cZs1V/k1ytsbjh0DHx9ITFQ3dmGherGsrMDREYqL1X/e162rbrwaGD9e/ZhxcerH/KeSyrcQQgghhDCZVL7NIydcCiGEEEIIUUuk8i2EEEIIIUwmlW/zSPIthBBCCCFMJsm3eaTtRAghhBBCiFoilW8hhBBCCGEyqXybRyrfQgghhBBC1BKpfAshhBBCCJNJ5ds8knwLIYQQQgiTSfJtHmk7EUIIIYQQopZI5VsIIYQQQphMKt/mkcq3EEIIIYQQtUQq30IIIYQQwmRS%2BTaPJN9CCCGEEMJkknybR9pOhBBCCCGEqCVS%2BRZCCCGEECaTyrd5pPItbosLFy7c7iEIIYQQQtQ6Sb7vEK1ataJDhw54e3vTsWNH/P39eeGFF7h06ZIq8bdt20ZwcLAqsW7m5MmTDBgwwKRlx40bR2xsrIVHJIQQQghTlZerf7ubSNvJHeSdd94hICAAgMLCQqZNm8Yrr7xCQkLCbR5ZzRQUFKDX601aNj4%2B3sKjEUIIIURN3G3Jstok%2Bb5DOTk58fjjjzNlyhTDtLNnz/LGG2/w%2B%2B%2B/k5ubS%2BPGjXnllVcICgoiNTWVXr16sWDBAtasWcNff/1Fhw4dWLx4Me7u7kaxdTodEydO5MqVK8TFxbFhwwYSExP566%2B/SElJ4e233yYyMpKXXnqJoUOHAnDo0CFGjx7N77//bljX7NmziY2NRavV/h97dx5XU/rHAfxz2yNbaaMsEya70iJLJcmSENKIyDQhS7LvWSolOyGTsoZmspV9MEKIIftYyiDFLWXotmi7vz%2Bazjjd4vq5t3My3/fr1cvcc66nz1zd2/c851lgZ2eHxYsX4%2B3bt/Dy8gIAmJiYIDIyEu3bt8emTZtw8OBB5OTkoHXr1li0aBGMjY3h7u4OCwsLTJkyBWKxGLt370ZUVBSysrLQqlUrzJ8/H%2B3atQMAnDp1Chs2bMDr16%2Bho6MDJycnTJw4UerXNCMjA5mZmaxj2g0bQkdH5//6NyKVU5Dx/TaB4N8/Zdq2WMZBy8PJ%2BgUAAGVl2banpMT%2B87%2BmZUvZttekCftPGVJRkW17cvunNzGRbXvGxuw/ZUmW71G5fUCRmuw/%2Bsla87179w7Hjh2Dg4MDc2zKlCno1asXQkNDIRaLsWrVKixZsgQ9e/ZknnP%2B/HkcPnwYhYWFGDt2LDZv3oxly5Yx5wsKCjBp0iQIBAJERERATU0NAHDlyhVERkaiQ4cOUFVVlSrj6dOnERcXh5KSEkyaNAlLly7FypUrER4ejtGjRyMpKQkAsHHjRhw9ehQRERFo3rw5QkNDMX78eJw7d47V3t69e7F9%2B3Zs2bIFRkZGOHLkCMaOHYsTJ05AQ0MDs2bNYu4OPHjwACNHjkT37t3RoUMHqfJGR0cjNDSUdWzypEmY4uMj1d//IuUfyLJqTqatVWhbxo3XqiXb9sqpq8u6xTqybrBM7dqyb7OOnLI2bCjT5mR8ifBvu7JuWF533Pz8ZN6kvsxbLKOtLeMGb96UcYP/2LtXPu3K2j%2B/S78V1PP9daj4rkEmTJgARUVFlJaWIjc3F3Xq1MHWrVuZ81u3boWuri7EYjHS0tJQt25dCIVCVhteXl6oW7cuAMDOzo4pgIGyHu8JEybg7du3%2BPXXX6HyUZeKoaEhrKysvijvvHnzoKmpCQDw8fGBt7c3AgMDJZ536NAhjB8/Hi1atAAAeHt7w8bGBmKxmPW8qKgojB8/Hsb/9HQMGzYMMTExiI2NhZubG9TU1BATE4PS0lKYmprixo0bUPiCngZXV1eJce/aDRsCFXJ8NYFA5m2K5VR%2ByyEq8vNl255AUFZ45%2BfLNmutkhzZNQaU9XrVrg3k5sr%2BN1durmzbU1IqK7zfvAGKi2XWbJGW3uef9IWUlQEpR7FJ36b3T7JtsEmTssJ72TLgxQuZNv3KX7YXCkpKZYV3ZqZM/%2Bmh72gqu8aAsh7vvXsBNzfg4UPZtp2QILu2BIKywrugQPYfprLvcSDVhIrvGiQsLIwZ811QUICoqCiMGTMG0dHRaNu2LR4%2BfIiJEyciMzMTRkZG0NTUlChgG37Uk6WkpMQ6n5mZCWNjY6SkpODevXswNf33w/L/GXrRtGlT5r/19fVRWFiIv//%2BW%2BJ5mZmZaNSoEfNYRUUFnTp1knheWloaVqxYgVWrVjHHiouL0a5dO6ipqWHfvn3YvHkzZsyYAZFIhD59%2BmDhwoWoV6%2BeVHl1dHQk/z9l/WFJZF53ll9ficUyblteXTvymF0k6%2BqzXHGx/NrmsydP5NPuixcyb7uwUKbNMYqLZdz2Rx09MvXwoezbluX7U24fUNz6hv5XOEEDkGooNTU1eHp6onbt2rh8%2BTKEQiGmTp2KadOm4erVq4iKipJ6RZFyOjo6CA8Ph7u7O%2BbOnYu8vDzmnKDC2AMFBQXWpMm3b99KtPdxr/vLly%2Bhrq6OBg0aSDxPX1%2BftWpLUVERli9fjoyMDNbz9PT0EBAQgD/%2B%2BIP5io2NhY%2BPD0QiETIyMrB69WpcvnwZ0dHRuHfvHq2UQgghhMgYrXbydaj4rqGKi4tx4MABvH//Hp07d0Zubi5KSkqg/s9tqOTkZGzatAlA2XASaSgrK0MgEMDX1xcKCgpYsWJFlc81MjLC2bNnUVBQgMzMTOzatUviOatXr4ZIJIJQKMSGDRswaNAgKCsrM2PGc3LKbusPGTIEERER%2BOuvv1BcXIytW7fizJkzEoX68OHDsWXLFqSkpAAALl68CEdHR1y/fh25ubnw8vJCXFwcxGIxdHR0oKCgUGmxTwghhBDCFRp2UoN4eXlBUVERQFlPdLNmzbBmzRpmeMjs2bMxa9Ys5OfnQ09PD8OHD8fKlSvx%2BPFj1K9fX%2Brvo6qqiqCgIIwcORK9evWq9DkzZ87EkiVL0K1bN%2Bjo6GDMmDG4ceMG6zlNmjTBgAEDkJ%2BfDycnJ8yaNQsA0KpVK3Tu3Bk9evTA%2BvXr8dNPP6G4uBienp549%2B4d2rdvj/DwcChXmEXl4eEBsViMiRMnIiMjA7q6uvDz82MybtiwAevWrYOfnx/U1NTQv39/eHh4SP3/TQghhJDP%2B6/1VMuaQFxxUDAhX6l8qcGzZ8/CwMCA6zhfRx5vj//4hEtZzw1UUChbQSUvT7a/EDRK3smuMaAsaJ06QE6O7H9zvX8v2/aUlQE9PeD1a5mO%2BS7SM5RZW%2BXkMuHS3ka2DbZsWbaCyk8/yXzM9/Nd8TJtT0UF0NcHXr2S7Zjvps1k/BllYlK2goqpqezHfItEsmtLQeHfGeGyft/LY%2BUkKfXpI/s2T52SfZt8RT3fhBBCCCFEajWt5zsvLw/%2B/v44d%2B4ciouL0atXLyxevBi1K7mA8fPzQ1xcHOtYQUEBunbtioiICJSWlqJz584Qi8Ws%2BXAJCQmoJeVaulR8E0IIIYQQqdW04tvf3x%2BvXr3CqVOnUFJSAl9fX6xatQqLFy%2BWeO6yZctY%2B59cunQJM2bMwNy5cwGUzakrKirCzZs3WUsyfwmacElkzsDAAI8ePar5Q04IIYQQUqPl5%2BcjLi4OPj4%2BqF%2B/PrS0tDBz5kwcPHgQ%2BZ/ZeCI7OxszZ87EggUL0PKfnW/v3r2L77///v8uvAHq%2BSaEEEIIIV9AHj3fGRkZyMzMZB3T1taWap%2BRgoICiU0Fy%2BXn56OoqAitWrVijhkZGaGgoADPnj1D69atq2x31apVaNeuHQYOHMgcu3v3Lj58%2BIChQ4ciLS0NRkZGmDFjBmtvlM%2Bh4psQQgghhEhNHsV3dHQ0QkNDWccmT56MKVOmfPbv3r59G6NHj6703NSpUwGANR67fFnm3E%2BsAJCamorY2Fj8%2BuuvrONqamro0KEDpk6dinr16iEqKgqenp6IjY2FoaF0k8qp%2BCaEEEIIIZxydXWFnZ0d65i2trZUf9fS0hKPHj2q9NyDBw%2Bwfv165OfnMxMsy4ebaGhoVNnmgQMHYGJiItEzXj72u5ynpycOHjyI%2BPh4jBo1Sqq8VHwTQgghhBCpyaPnW0dHR6ohJl%2BqefPmUFZWRnJyMjp27AgASElJgbKyMpo1a1bl3zt9%2BjR%2B/PFHieNr165Fnz590KZNG%2BZYYWEhs4GgNGjCJSGEEEII%2BSapq6ujX79%2BWLVqFbKzs5GdnY1Vq1ZhwIABUFNTq/TvvH37FikpKTA3N5c49/jxYwQGBiIzMxOFhYUIDQ2FSCRC7969pc5ExTchhBBCCJFaaansv%2BRp8eLFaNasGZycnNC3b18YGBjAz8%2BPOe/o6IiwsDDm8cuXLwEAurq6Em0FBQWhSZMmGDRoECwtLXHt2jVs3779i3YSp2EnhBBCCCFEajVtnW8NDQ34%2B/vD39%2B/0vPHjh1jPW7fvn2VY8jr16%2BPoKCgr8pDPd%2BEEEIIIYRUE%2Br5JoQQQgghUqtpPd98Qz3fhBBCCCGEVBPq%2BSaEEEIIIVKjnu%2BvQ8U3IYQQQgiRGhXfX4eKb0I%2BQQyBzNsUyKFdAcQybe/jlmXdtoZigUzbg0AAQA21FAoAgQyzqtb6/HP%2BH1WsK/tV6taVfZsAUMkyW19DWS4/pwIoK8m43bZtZdte%2BZbTRkaAiopMmzYwkGlzDJnvdSISybY9hX9GzSYkyL4S/MSuh1/MxAS4eRPo1g1ISpJduwAgltfnPpE3Kr4JIYQQQojUqOf769CES0IIIYQQQqoJ9XwTQgghhBCpUc/316HimxBCCCGESI2K769Dw04IIYQQQgipJtTzTQghhBBCpEY931%2BHer4JIYQQQgipJtTzTQghhBBCpEY931%2BHim9CCCGEECI1Kr6/Dg07IYQQQgghpJpQzzchhBBCCJEa9Xx/Her5JoQQQgghpJpQzzchhBBCCJEa9Xx/HSq%2BCSGEEEKI1Kj4/jo07IQQQgghhJBqQj3fhBBCCCFEatTz/XWo5/s/yM/PDyYmJjAxMUH79u1hbGzMPDYxMcEff/wh0%2B9nbW2NI0eOVHru0KFDGDhwoEy/HyGEEEIIX1HP93/QsmXLsGzZMgDAwYMHERoainPnznGSxdnZGc7Ozpx8b0IIIYR8Oer5/jrU800qlZOTg/nz56N3797o1KkTrK2t8fPPPwMAnj59ChMTE0RHRzPP7dWrF9atW/fF3%2BfXX39F7969mcd3796Fu7s7zM3N4eDggJ07d0IsFgMA1q5dC19fX8yYMQOdO3eGjY0N1q5dy/zdq1evYsiQITAzM4ODgwOCg4NRUlLyNS8DIYQQQiooLZX9138J9XyTSoWEhEAoFOLgwYPQ0NDAiRMnMH36dPTv3x/fffcdFixYgMDAQHTv3h0hISFo1KgRpkyZ8lXf8/Xr1xgzZgxmz56N7du34%2BnTp5g4cSJq1aoFFxcXAMDJkyexcuVKhISEID4%2BHt7e3rC3t0f79u0xa9YszJw5E4MGDUJqaipGjBgBMzMz2NvbS/X9MzIykJmZyTrWsKE2dHR0vur/i1QgEMinPVm3S/67DA1l256uLvvP/yIFGff1ffy%2Bl3XbJiaya8vYmP0nIaDim1Rh6tSpUFJSQu3atfHq1SuoqKhALBYjIyMDBgYGGDZsGC5fvgx3d3d8%2BPABhw4dgqKi4ld9z8OHD8PY2Bg//PADAKBVq1YYO3YsoqKimOK7RYsWcHJyAgDY2dlBS0sLz549Q/v27aGuro4TJ06gXr16MDc3x4ULF6DwBR/K0dHRCA0NZR2bNGkyfHy%2B7qKiMrKvE%2BVYeMo6rJqabNsrp6oqn3ZlTVmZ6wTSqykXNLLOOW%2BebNsr9%2BOPMm/y6z51P9GurBtWV5dxg/%2BQx%2BfJzZuyb3PvXtm3yaH/Wk%2B1rFHxTSr15s0bLF%2B%2BHH/%2B%2BScMDQ3Rtm1bAEDpR%2B%2B4UaNG4dixYxg6dKhMeofT0tJw584dmJmZMcdKS0uhoqLCPG7YsCHr7ygpKTGZdu3ahY0bN2Lx4sXIyspCjx49sGTJEuhK2dvk6uoKOzs71rGGDbXxz6gXmREIIPs2IeMGmYblEPbDB9m2JxCUFd4fPsg2q8yrD5QV3kVFsm9XSQ4f5fL4t5cHeeQMDpZte7q6ZYV3ZCQgFMq06ZLZsr9QUFQEZD1iT7EwX7YNCgRlhXdBgez//bt1k11bxsZlhbebG/DwoezaBeRzkUCqBRXfpFI%2BPj7o168fIiMjoaSkhDdv3uCXX35hzn/48AGLFy/GwIEDcezYMfTr1w89evT4qu%2Bpq6uLbt26YevWrcyx7Oxs5Od//kO7oKAAKSkpWLZsGRQVFfH06VMsWLAAK1aswJo1a6T6/jo6OhIXETWh9qhx5PWiisX0D0ZkIzVVPu0KhfJrm%2B9k3VVafldTLJZ920lJsm0PKCu85dEuR6jn%2B%2BvQhEtSqZycHKiqqkJRURFZWVkICAgAABT902sXEhICBQUFBAYGwtfXF3PnzkVWVlaV7b1//x6vX79mfRUWFrKeM2jQIFy/fh3Hjh1DcXExhEIhxo8fj5CQEKkyT5s2DTt37kRJSQm0tbWhpKSEBg0a/J%2BvACGEEEIqQxMuvw4V36RSwcHBiI2NhampKYYNGwYDAwN8//33ePz4MX7//Xf88ssvWLFiBVRUVDBmzBg0b94cc%2BfOZVYmqSggIAA2Njasr4rriRsaGiI8PBxRUVHo2rUrBg8ejJYtWyIwMPCzedXU1LB582acPHkSFhYWsLe3h76%2BPqZNmyaT14MQQgghRBYE4qqqJUKIXEYx/OfHfBcUyLY9eY39lMc4ahrzLXvyyDlpkmzbMzQsm8QZFCTzYSclGzfLtD1ATmO%2BC3Jl26CCQtkkzvx82XebamjIri0Tk7Kx2aamsh92wuH7U0tL9m1%2B4ub5N4d6vgkhhBBCCKkmNOGSEEIIIYRI7b82RlvWqPgmhBBCCCFSo%2BL769CwE0IIIYQQQqoJ9XwTQgghhBCpUc/316HimxBCCCGESI2K769Dw04IIYQQQgipJtTzTQghhBBCpEY931%2BHer4JIYQQQgipJtTzTQghhBBCpEY931%2BHim9CCCGEECI1Kr6/Dg07IYQQQggh37z8/Hy4urri4MGDn3ze7du34eLiAhMTE9jZ2eHXX39lnT906BB69%2B6NTp06YciQIUhKSvqiHFR8E0IIIYQQqZWWyv5L3p48eYKRI0fi1q1bn3zeu3fvMG7cOAwePBjXr19HYGAggoKCcOfOHQBAYmIi/P39ERwcjOvXr2PgwIHw9vZGfn6%2B1Fmo%2BCaEEEIIId%2BsK1euYMyYMXB2dkajRo0%2B%2BdzTp0%2Bjfv36GDlyJJSUlGBlZQUnJydERUUBAH799Vc4Ojqic%2BfOUFZWhoeHBxo0aIDjx49LnYfGfBNCCCGEEKnJo6c6IyMDmZmZrGPa2trQ0dH57N8tKCiAUCis9Jy2tjaMjY3x%2B%2B%2B/Q1VVFdu3b/9kW0%2BePEGrVq1Yx1q0aIGYmBgAQHJyMoYOHSpx/uHDh5/NWY6Kb0I%2BQSCQbXsZGRmIjo6Gq6urVB8o0pNxUMgxq7q67NrCPznDw%2BXwmsqW/P7tZa%2BmZJVbzs2bZdcW/sm5cSNcPT1l/noqyrQ1Ob6mtWvLri38k3PbNvn8jIrFMmuK%2Bbc/eZLX76UvJcOXiLFxYzRCQ0NZxyZPnowpU6Z89u/evn0bo0ePrvTcpk2bYG9vL3WO3NxcqFf4PaWmpoa8vDypzkuDhp0QUo0yMzMRGhoqcXXPRzUlK%2BWUvZqSlXLKXk3JSjm/PeUTIT/%2BcnV1lervWlpa4tGjR5V%2BfUnhDQDq6uooKChgHSsoKEDtfy4gP3deGtTzTQghhBBCOKWjo8OLuwOtWrVCQkIC61hycjJatmwJAGjZsiWePHkicd7a2lrq70E934QQQgghhADo3bs33rx5gx07dqCoqAhXr15FXFwcM8572LBhiIuLw9WrV1FUVIQdO3YgKysLvXv3lvp7UPFNCCGEEEL%2BsxwdHREWFgYAaNCgASIjI3Hy5ElYWlpi4cKFWLhwIbp06QIAsLKywuLFi7FkyRJYWFjg2LFjCA8PR/369aX%2BfopLlixZIo//EUJI5WrXrg0LC4svGh/GlZqSlXLKXk3JSjllr6ZkpZzk/zFmzBi0bt2adWzkyJEwMzNjHuvq6mLYsGEYP348Ro8eLfF8Y2NjjBo1ChMmTMDw4cOhp6f3RRkEYrE85qwSQgghhBBCKqJhJ4QQQgghhFQTKr4JIYQQQgipJlR8E0IIIYQQUk2o%2BCaEEEIIIaSaUPFNCCGEEEJINaHimxBCCCGEkGpCxTchhBBCCCHVhIpvQgghhBBCqgkV34QQQgghhFQTKr4JkSNvb%2B9Kj48aNaqakxBStdu3b1d6/MKFC9Wc5MuIRCIUFhZyHeOzUlJSIBQKuY7xWdnZ2VxHIOQ/gYpvQmTs5cuXCA0NRWhoKC5dusT8d/lXcHAwHj16xHXMSqWkpCAgIACTJ0/G27dvsWfPHq4jVeqXX36Bk5MTLC0tkZ6eDh8fH%2BTm5nIdS4KHhwfi4uLw4cMHrqN80tixYyWOiUQiTJ06lYM0VUtJScGkSZMAAL/99hu6dOmCHj164MaNGxwnY7t58yYGDx4MANi/fz8cHR3Rq1cvnDlzhuNkkoqLi7F27Vp07twZdnZ2SE1NxdChQ5GRkcF1tBpJLBbj3LlzAAChUIgZM2YgMDCQl59PhDtUfBMiY40aNcKTJ0%2BQmJiIkpISJCYmsr6Sk5OxePFirmNKSEhIwPDhw/H27VtcvnwZBQUF2LRpE37%2B%2BWeuo7Hs2LEDERERcHd3R0lJCWrXro2MjAwEBQVxHU1C165dERYWhu7du8PPzw937tzhOhLj%2BfPnaNeuHVq3bo28vDy0bt2a9WVubo42bdpwHZNl%2BfLlqFu3LsRiMdasWQMfHx/4%2BPggODiY62gsq1evhq2tLcRiMbZu3Yrg4GCEhoZi/fr1XEeTsHHjRly9ehXr16%2BHsrIytLS0oKenh8DAQK6jVerevXsAgPfv32PlypWIiIhAcXExx6n%2BFRISwny%2BL126FK9evcLDhw8REBDAcTLCK2JCiNwsWLCA6whSGzJkiPj8%2BfNisVgsNjMzE4vFYvGdO3fEdnZ2XMaS4ODgIE5OThaLxWKxubm5WCwWi4VCobhr165cxvqk27dvi5csWSLu0qWLuH///uLIyEjxmzdvuI4lfvDggfjq1aviDh06iBMTE1lft27dEufl5XEdkaVbt27iwsJCcWpqqrhNmzbinJwccWlpqdjExITraCxdunQRl5aWipOTk8Xt2rUTf/jwQSwWi8WdOnXiOJmknj17il%2B/fi0Wi/99P717905sYWHBZaxKbd68WWxqaioWi8XiWbNmifv16yd2dHQUBwQEcJzsXw4ODuLU1FRxbm6uuG3btuK//vpL/P79e7GlpSXX0QiPKHFd/BPyLQsICEBhYSGys7NRWlrKOteoUSOOUlXu%2BfPnsLa2BgAIBAIAQPv27fHu3TsuY0l4%2B/YtmjdvDqDsFi8AaGlp8ar3q6IOHTqgXbt2sLOzw9q1a7FixQqsW7cOdnZ2mDNnDvT09DjJ1bp1awDA0aNHYWhoyEmGL1FcXAyxWIyEhAS0bdsWGhoayM7OhqqqKtfRWBQVFZGbm4sLFy6gU6dOUFFRQVpaGjQ0NLiOJiEvLw%2BampoA/n0/qampQUGBfzfGjx49iqioKBQWFuLUqVOIjo6GtrY2Bg4ciAULFnAdD0DZ55OBgQHi4%2BOhra2NZs2aobS0lNefT6T6UfFNiBydPHkSixYtgkgkYo6JxWIIBAL8%2BeefHCaT1KhRI9y8eROdO3dmjt29exf6%2BvocppJkbGyM6OhojBgxgrlIOH78OFq2bMlxsso9ePAAR44cwbFjx1BcXIwBAwYgICAAenp6WLVqFSZMmIDDhw9zmlFTUxPh4eF49uyZxEUin4bzdO3aFVOmTMHDhw/h6emJ1NRUzJ49GzY2NlxHY7G3t8eoUaOQlpaGhQsXIjk5GZMmTcKAAQO4jiahU6dOCA0NxbRp05j30%2B7du9G%2BfXuOk0nKyMiAsbExrly5gjp16sDY2BgAkJ%2Bfz3GyfxkYGCAuLg7Hjx9H9%2B7dISSOF7UAACAASURBVBaLsXPnThgZGXEdjfCIQFx%2BqUsIkbn%2B/fvDwcEBzs7OUFJiX%2Bs2btyYo1SVO3bsGJYuXYoRI0Zg165dmDhxInbv3o3p06czk8f44P79%2B/Dw8ICRkRHu3bsHKysr3Lp1C9u2bUPHjh25jscyYMAA/PXXX7CyssKQIUNgb28PFRUV5vyTJ0/www8/cD5h0MfHB0lJSbC0tISysjLrHJ%2BK79zcXERGRkJVVRXjxo3Dw4cPERMTgxkzZkBdXZ3reIySkhIcPnwY6urq6N%2B/P549e4bff/8do0ePhqKiItfxWFJTUzFmzBgUFxcjKysLTZs2RW5uLrZv347vvvuO63gsAwYMwOLFixETE4PS0lKsXLkSR48eRXh4OI4cOcJ1PADA1atXMXv2bKirq2PXrl1ISUnBtGnTsGXLFpiamnIdj/AEFd%2BEyJGJiQmuX78uUXjzVXx8PKKiopCWlgY9PT0MHz4cffr04TqWBKFQiNjYWKSnp0NPTw9OTk68G8YDAFu2bMGQIUOgq6tb6fnCwkLk5%2BejXr161ZyMzdLSEjExMbwfehIREQFPT0%2BJ4%2BvWrYOvry8Hib4N%2Bfn5OH/%2BPPO%2Bt7W15eUQmVOnTmH27NlQU1PDvn37IBQKMW7cOGzcuBG2trZcx6tU%2BUpHfBsaRbhFxTchcjRq1CgsXLiQuT3KZ/7%2B/pg2bRovf%2BnWVF27dsXp06d5/5paW1vjzJkzrF55vsjOzkZKSgoAwMvLC9u2bcPHv7ZycnIwY8YMJCUlcRVRQnx8PAICApCWloaKv2L5NtyssLAQmzZtwrBhw2BoaIidO3fi7du38PHx4eW474%2BLWZFIhLy8POjo6HCciu3%2B/fuVDuFycnLiKBHhm5rRHUdIDWVqagoPDw/07dsXDRs2ZJ2bPHkyR6kqFxcXh3nz5nEd47NqUmFTr149ZGRk8L74dnNzQ3BwMCZPnsxMvuMLFRUV%2BPj44O3btwAkN6hSUVGBq6srF9GqtGzZMjg4OMDGxoaXBezHgoKCcOvWLeY1bNu2LYKDg1FYWIjZs2dznE5Sbm4uYmNjkZaWhqlTp%2BL%2B/fu8Kr7XrVuHsLAwaGlpse54CgQCKr4Jg3q%2BCZEjd3f3So8LBALs2rWrmtN82ooVK5CbmwtnZ2fo6Ogwk68Afq3M0qtXryoLGwsLC45SVc7X1xeXLl2CqampxGvq7%2B/PYTI2Ozs7pKens/KV49MFTd%2B%2BfXHy5EmuY3xW586dce3aNd6N765Mt27dEBcXx7roevPmDQYPHoxLly5xmEzS/fv3MXbsWHz33Xd49OgRYmNj4ejoiMWLF2Po0KFcxwMA9OzZE35%2BfujZsyfXUQiPUc83IXK0e/duriNIbfv27QDKdo8Eyi4Q%2BLgyy99//42ZM2fWiMJGWVmZ%2BSXM510u%2BbZJTVVqQuENlBVg8fHxsLOz4zrKZ3348AG1atViHdPQ0ODl0nhBQUGYO3cuhgwZAnNzcxgaGmLTpk0ICgriTfGdk5PD2/HnhD%2Bo55sQOfrUEnJ8WkEEANLS0qo8x6eVWWbOnIn%2B/fvXiMKmpnn37h1SU1PRpk0bFBcX824M%2BJMnTxASElLpeNqzZ89ylErSnTt34ObmhhYtWqBu3bqsc3y74zVhwgTo6upiwYIFUFFRwYcPH7BixQq8fv0amzdv5joei4WFBa5cuQJFRUVYWFjg2rVrAMruNHC9YlC5GTNmoFevXujfvz/XUQiPUc83IXK0YcMG1uN3794hPz8fnTt35l3x3bhxY%2BTm5iI%2BPh5paWnQ0dFBz549JYoHro0ePbrGFDYAEBUVhf379yMtLQ3a2toYNmwYvLy8uI7FkpubCz8/Pxw7dgxqamo4ePAgxo4dy7vl5vz8/KCuro5x48bxegUhPz8/mJiYwMzMjPd3aBYsWICffvoJpqamaNCgAbOJVVhYGNfRJGhqauLp06esNf2fPn0qMZ%2BGS6WlpZg5cya2bNkCbW1t1rnIyEiOUhG%2B4e%2BnFyHfgHPnzrEei8VihIeH4%2B%2B//%2BYoUdWeP38ODw8PFBUVoVGjRkhPT8eKFSuwc%2BdOXm1gU5MKm927dyM8PBxeXl4wMDDA8%2BfPERkZCYFAgJ9%2B%2BonreIyQkBDk5eXhxIkTGD58OAwNDdGzZ08EBgYiIiKC63iMR48e4cKFC7yfwPr8%2BXNcu3ZNYs10PjI0NMTx48dx48YNvHnzBnp6eujQoQMvL27c3Nwwfvx4TJgwAcXFxTh%2B/Di2bNnCqwm3TZs2xbhx47iOQXiOhp0QUs1KSkpgbW2NhIQErqOwTJgwAc2bN8esWbOgoKDAbGLx%2BPFjXhVgJiYmNaaw6devH1auXIl27doxx%2B7duwdfX1%2BcOXOGw2Rs1tbWiIuLQ7169Zjb%2BQUFBbC2tmZu7fNB3759sXfvXt6tyFKRm5sbAgICeHXX4FMKCwuRnZ0tMZSHTxOty0VFRWHv3r1IS0uDrq4uXF1d4eHhwftVZQj5GP8ubQn5xv3111%2BVrirBtdu3b2PDhg3MLzEFBQVMnToV3bt35zgZW%2BvWrZGamlojCpuMjAy0adOGdaxNmzbMsnl8UVpayozvLu%2BP%2BfgYX4waNQqTJk3C6NGjJYYamJubc5RKkpWVFUaPHo2%2Bffuifv36rHN8W2L0xIkT8PPzg0gkYo7xcaJ1uZEjR2LkyJFcx/ikAwcOYM%2BePcjIyEBMTAxCQkIQGBgoMbGV/HdR8U2IHLm7u7MK7aKiIjx69AgDBw7kMFXlFBUVIRKJWL2KIpGIV9t2AzWrsGnatCnOnTsHe3t75tjZs2fRtGlTDlNJ6tKlC5YtWwY/Pz/m53XdunW8W7oxICAAACQ21OFboXjt2jU0b94cjx49Yh3n40X3xo0bMXLkSDg7O/NyqAkA/Pzzzxg3bhxCQ0OrfA5f3vu7du3Cnj174OHhgTVr1kBdXR1paWkICgri1fKihFs07IQQOar4y0JBQQFGRkawt7fn3XjlRYsW4eXLl1i0aBEMDAyQmpqKgIAAGBoaYtmyZVzHY9SktdNPnz6N6dOno2/fvjA0NMSLFy9w%2BvRprF27llWQcy0rKwve3t548OABSkpKoKamhmbNmiEsLAy6urpcxyNyZGJiguvXr/O28AbKdjYNDw%2BvEe/9Pn36YNOmTWjRogUzhEsoFGLIkCG8G2pIuEPFNyHVJCsrC/Xq1ePtL7m///4bU6ZMwfXr15k1vm1sbLBy5UrerXhSkyQkJODgwYPIyspC48aNMXToUJiamnIdS4JYLMbdu3eRlpbGTLrj2wVienp6lef4Nj45JSUF%2B/btw%2BvXr%2BHv749jx45J7M7JB6NGjcLChQthbGzMdRSpiMVilJaWQlFREZmZmdDU1OTVz6mFhQUSExMhEAhgbm6O69evo6SkBF27dkViYiLX8QhP8LMKIOQbUVRUhJUrV%2BLXX39FQUEBVFRUMHDgQCxatIh342nr16%2BP3bt3IzU1lSkUKy6VxRdnzpxBdHQ0a/k%2BPm7dvGPHDnh4eKBbt26s4xs3bsSUKVM4SiWpvKht2LAhM5ZaKBQC4FdRa2dnx1wYAuxhHHwadpKQkIApU6agZ8%2BeuHz5MgoKCrBp0ybk5eXxbiUMU1NTeHh4oG/fvhLj6PkylKPcw4cP4e3tjfXr16NDhw7Ytm0bzpw5g23btqF58%2BZcxwMAfP/994iJiYGLiwvz83nq1Cm0aNGC42SET6jnmxA5Wr9%2BPc6dO4fp06fDwMAAL168wNq1a9G9e3fMnj2b63gs6enpmD59OhYtWoS2bdtixYoVuHXrFjZs2MCrIjwuLg5Lly6Fq6sr85r%2B8ssvmDt3LlxcXLiOh7dv3%2BKvv/4CAHh6eiIyMhIff8zm5OTA19dXYtwyl4yNjascj8ynorbiRlDZ2dnYtm0bevXqxat5FEOHDoWPjw9sbGyY3s%2B7d%2B/C19eXV5sBATVrGJe7uzvMzc0xceJEKCkpobi4GGFhYbh58yZv1tC%2Be/cuPDw80Lp1a9y6dQvdu3fHH3/8gfDwcJiYmHAdj/AEFd%2BEyJG9vT22b98OQ0ND5tiLFy8wcuRIXLx4kcNkksaPHw8tLS3Mnz8fGhoayM7Oxtq1a/Hu3TuJzYK4NHDgQMyfPx9dunRhjl29ehXLli3D8ePHOUxW5v379%2BjduzfevXtX6XlFRUW4urrCz8%2BvmpNVraYUtZXJycmBs7Mzr5ZuNDMzY4ZvfbwTo5mZGf744w%2BO09VcH7%2Bu5UpKStClSxdcv36dw2Rsr1%2B/xuHDh5Geng5dXV0MHDiQ9TuAEBp2QogcvXv3Dvr6%2Bqxj%2Bvr6KCgo4ChR1ZKSkpCQkMCsn62pqYmFCxfC2tqa42Rs6enpsLS0ZB2zsLDA69evOUrEVrduXVy9ehUlJSXo168fTp48yTrPp/Gp5Ro3bizxOCAgAM7OzrwvvoGyCx4%2BadSoEW7evInOnTszx%2B7evSvxWcAXV69ehVAoZO7QlK/KtHDhQo6TsWloaOCvv/5iLTOamprKuzkpenp6mDBhAtcxCI9R8U2IHH3//ffYv38/a6LV/v370apVKw5TVU5JSQnZ2dms1S3evXsHNTU1DlNJ0tPTw/Xr11nL4F2/fp1XY5MFAgGUlJTw22%2B/obS0lFk7PSEhAZqammjdujXHCaXDt6K24upBRUVFuHjxIjp16sRRosqNHz8e3t7eGDFiBIqKihAeHo7du3dj%2BvTpXEeTEBAQgP3796N27doAynqSc3Nz0aNHD46TSXJ2doa3tzd%2B%2BuknZhfeiIgIDBkyhOtoGDx4MA4fPgwHB4cqh3CdOnWqmlMRvqLimxA58vX1xY8//ojY2Fhmqbnk5GRe7RhZrm/fvvDx8YGvry/09fXx6tUrbNiwAX369OE6GsuYMWMwadIkuLq6Mq9pdHQ05s2bx3U0CefPn8fChQtx6dIlhIWFYdOmTQAAPz8/XoxPL1dTitqKq0UoKirCxMQE48eP5yhR5RwdHaGhoYGoqCg0atQIV69exYIFC3j3XgLKNtnZs2cP8vPzERsbi%2BXLl2PFihXIy8vjOpqEyZMnQ0FBAWFhYcjMzIS%2Bvj6GDBkCLy8vrqPBw8MDAHiRhfAfjfkmRM6ePn2KuLg4ZGVlwcDAAI6OjhK3%2BfkgPz8fS5cuxfHjx1FYWAgVFRUMHjwY8%2BbN491GOwcPHsTBgwfx5s0bNG7cGC4uLujbty/XsSS4uLjA2dkZP/zwA3r06IHAwEBoampi1qxZvOoFqzjpTlFREUZGRhg/fjx0dHQ4SkWqg6mpKW7evInMzEx4enoiNjYWIpEI/fv3x4ULF7iOx3L79m107NhR4viFCxd4NzzuY4WFhbhx4wasrKy4jkJ4gopvQghLUVER3r17By0tLV7uyAeUraGsq6sLDQ0NJCUloW7dujAyMuI6lgRLS0skJibizz//hJubG7OZiYmJCa9WO6lJ%2BLzMpDR3X4KCgqohifT69%2B%2BP3bt3Q0tLCxYWFkhISGAmit68eZPreCzlFwofE4lE6NGjB6/fT0KhELa2trxaOYhwi4adECJH8fHxCAgIQFpaGipe5/Lpg1gkEiEzMxPNmzeHsrIy4uPj8eeff6J3794Skxu5duLECcyePRv79u1Du3btcOvWLWzcuBFr166FjY0N1/FY1NTUkJ2djXPnzsHU1BRKSkp4/PgxGjRowHU0lsOHD0v1vMGDB8s5yad9vMyknZ0dXrx4gSVLlqCgoIBXw3hqEhsbG3h4eGDnzp0wNzfH/PnzoaqqimbNmnEdDQDw/PlzODo6oqSkBGKxuNL5EnzctKoi6uckH6Oeb0LkqFevXnBwcICNjQ0z6a7cxxMGuZSSkgJ3d3f07NkTgYGB2LFjB9asWQNbW1skJiZi9erV6N69O9cxGY6Ojpg7dy5rQtjFixexcuVKxMbGcphM0rp163Do0CH8/fffWL9%2BPbS1teHl5YXRo0fzajWEkSNHIikpCfXr14ehoSGEQiGEQiF0dHSY1VkEAgHna1TzfZnJmqioqAg7d%2B6Eq6sr8vLysGDBAohEIma9fz74888/8f79e4wbNw7h4eGsc6qqqmjVqhXvhsZ9jHq%2BSUVUfBMiR507d8a1a9d4ubxcOR8fH%2Bjp6WHOnDlQVFSEtbU1PDw88OOPPyI%2BPh7btm3D7t27uY7JqOzWs1gshrm5OS/XUE5ISICqqirMzMyQnp6OW7duoX///lzHYlm2bBlUVVUxc%2BZM5md169atePXqFZYsWcJtuI9Uts5zaWkpzMzMeDdEIjY2FkeOHEFGRgYaN26MESNG8O7OTE2TmpoKQ0NDZmhcgwYNeP3ZWo6Kb1IRDTshRI569uyJ%2BPh42NnZcR2lSn/88QdOnz4NRUVFPHv2DJmZmejduzeAsjHLM2bM4DghW%2BPGjXHx4kVWz/eVK1d4tdTgxz7eWr5Ro0a8zBkXF4eEhARWIePp6YkePXrwqviuCctMAkBERATCw8Ph6uoKfX19vHjxArNmzcKcOXMwdOhQruMBqJnj0zU1NTFnzhycPHkShYWFUFNTg7OzM%2BbOnQsVFRVOs8XFxVV5jm9LdhLuUfFNiByNHj0abm5uaNGihcRGEHzZurmgoAAaGhoAylYT0NTUZHZjU1BQQElJCZfxJIwbNw6TJk2Cg4MDGjdujPT0dPz2229YsWIF19EY5bsatm3btspJq/fu3avmVFVTU1PD06dPYWxszBy7d%2B8e6tWrx2EqSTVlmcno6GhERESwhm307t0bc%2BfO5U3xXRMtXboUz58/x%2BbNm6Gvr4/U1FRs3LgRq1atwvz58znNtmrVqk%2Bep1WDyMeo%2BCZEjvz8/GBiYgIzMzPe3h7V0tLCq1evoK%2Bvj6tXr8Lc3Jw59/DhQ9790nBycoKOjg4OHz6M%2B/fvQ19fH5GRkbyadFW%2BbnZ4eDhvV4z52MiRI%2BHp6QkXFxc0atQIqamp%2BOWXXzgvaCpycXGBoqIiDh48iDNnzjA7cfJtmcnc3FyJjbTatm2LzMxMjhJJ4luvtjR%2B//13nDx5ElpaWgCA7777DsbGxhg0aBDnP6vx8fGcfn9Ss1DxTYgcPX/%2BHNeuXWO2bOejvn37Yvbs2ejRoweOHTuGDRs2AACSk5MRHBwMe3t7jhNKsrS05N0qLB8rHxbRtWtXjpNIZ8KECdDS0kJsbCxOnz4NQ0NDhISE8HKMcseOHeHg4MBaZpJvBg4ciI0bN2LatGnMxVdkZCTvxvoDZWtQx8XFQSgUorS0FEDZJMzHjx9jy5YtHKdjU1VVlejEqF27Nq8nWxJSGZpwSYgcubm5ISAgAN999x3XUapUWFgIf39/3Lx5E46Ojpg4cSIAoEOHDmjXrh1%2B/vlnZlgKHwiFQmzZsgXPnj1jioVyfBnKM3bs2M/2eEdGRlZTmm9HxWUmt2/fzqtlJu3s7CAQCFBcXAyhUAhNTU3o6ekhMzMTmZmZMDY2lnpZx%2Boyc%2BZMXLx4EQ0aNEBRURFq1aqFJ0%2BeYPDgwQgODuY6HsuePXtw%2BvRpzJ8/H02bNoVQKMTq1avRpEkTjBw5knke3%2BYAEFIRFd%2BEyNHGjRsRHR2Nvn37on79%2BqxzkydP5iiVdFJSUni5cc2PP/6IN2/eoGfPnhJ3FPjymq5bt4757%2B3bt2Ps2LESz/H19a3OSJ%2BUm5uLvXv3VnpBw6fhCXxfZvLQoUOffY6zs3M1JJGepaUl9u3bh%2BzsbOzbtw%2BrV69GZGQk7ty5w/o55oOP5yQIBALW2tnljwUCAa0qQniPim9C5Kjitt3lBAIBb3ppaxpzc3OcOnUKmpqaXEeRirm5Oa5fv851jE/y8fFBUlISLC0tJS5o%2BFR817RlJrOyspidOPX19bmOU6nyn8/s7GyMGjUKx48fx4cPH9CrVy9cunSJ63gsaWlpUj2vcePGck5CyNehMd%2BEyFFV62M/fvy4mpN8O%2BrUqcP5smJfoiZMuExMTERMTAyzyg1f1ZRlJkUiEebMmYNz584xvbFWVlZYt24d78ao6%2BnpMetnZ2VlIS8vDwoKCsjNzeU6moSaUFRv2LABU6ZMYb3vs7OzMW/ePGzdupXDZIRPqPgmpBpdvnwZERERuHz5Mt0a/T9NnDgR8%2BbNg5eXFxo2bMg6x7cirKZQVVWFrq4u1zE%2BqyYsMwkAq1evRm5uLo4ePQoDAwM8f/4cy5cvx8qVK%2BHv7891PBYnJye4ubkhJiYGtra28Pb2hqqqKtq1a8d1NAnGxsZVXszy5fM0NjYWN2/exOrVq6GlpYWEhATMmTMHzZs35zoa4REadkKInBUXF%2BPo0aPYvn07kpOTYW1tjR9%2B%2BIEXE8SkIRKJeDXhsuK4TwC8HutZvuY3n4WFhSEjIwOTJ0/m/XCexMREHD58GJmZmdDX14ezszOvlpkEAFtbWxw4cIBZEg8AMjMzMXDgQFy5coXDZJU7ceIEbGxsUFpaipUrV0IkEsHX15d3d0Iqvo%2Bys7Oxe/duDBo0CMOHD%2BcoFVtOTg4WLlyIGzduwNbWFseOHcPUqVMxZsyYGnEXjFQPKr4JkZOcnBzs378fe/bsgUAgQHZ2Nn755RdW8cgnVRWJZmZmvBpP%2B6lxn3y5Lf3xuGQvLy9s27YNFT9q%2BVQw2tnZIT09vdLigG8XNAkJCWjTpg0aNGiA%2BPh4KCsr825JR0tLS1y8eJE1POrDhw%2BwtrZGYmIih8m%2BPZmZmfDw8MCxY8e4jsJIT0/HqFGjkJ6ejkGDBiEwMBBKSjTQgPyLfhoIkYPly5fjwIEDaNWqFebMmQMHBwd0794dDRo04Doay/Pnz%2BHn5wexWAyRSITRo0ezzotEIt6NUeVLgf0pbm5urMcjRoxgPeZbLz3flpSrSlRUFNauXYu9e/eiQYMGyMrKQnBwMObPn4/BgwdzHY/RsWNHrF%2B/HjNnzmRW4Vi/fj3at2/PdTSWa9eu4d69e7CxsUGTJk0wY8YMXLx4Eebm5li1ahXv3vuVqVu3LoRCIdcxGL/%2B%2BiuCg4Nha2uL1atXY/HixXBxcUFISAhatmzJdTzCE9TzTYgcGBsbw83NjXUbv0uXLjhy5AjvxtZGRUXh7du3CAsLw4QJE1jnVFRUYGdnhxYtWnCU7l/u7u6fvW3LlxVkSkpKPvscvu54ymf29vZYv349a9v2e/fuYcaMGTh16hSHydgePXqE0aNHQ0VFBY0bN0ZaWhoEAgG2b9/Om%2BU79%2B7di%2BXLl6NVq1ZIS0uDra0tHj58CBcXF8TGxqJly5YIDAzkOiZLxTXSi4qKcPbsWeTm5lY5ub26mZiYYOHChRg6dCiAsn0UVqxYgZiYGNy%2BfZvjdIQvqOebEDkICwtDVFQUbG1t4eDggNGjR/N2vF/55hQGBga86j2siM87WlZUUwprJycnxMXFMZvDVObs2bPVnKpqWVlZaN26NetYmzZtkJWVxVGiyhkaGuLUqVM4e/YssrKy0LhxY9jY2PBq7sTOnTsRHh4OKysrXLt2DWPGjEFcXBxatGgBe3t7DBs2jOuIEsp33y2nqKgIIyMjLF68mKNEkg4ePMiaXKmiooJFixaxVughhIpvQuTA1tYWtra2eP78OaKiouDp6QmRSITDhw/DxcWFV5Pajh49igEDBgCQ7Fkqx4einC8b6HxLxo0bB6DsteXrxeHHWrRogSNHjrA2qomLi%2BPdDrIDBgxAbGws0/vJRxkZGbCysgJQNt9DSUmJucOlp6eH/Px8LuNVKiQkBCYmJry%2BuG3evDnS09ORkZHBbFhVVFSE1NRUjpMRPqFhJ4RUg/z8fBw6dAj79u3Ds2fPYGtri40bN3IdC0BZoXD06FHY2dlVel4gEPCq95P8dyUkJMDb2xtt27ZFo0aN8OrVKzx48AA///wzLCwsuI7HsLOzQ3R0NLS1tbmOUqWKGxZVnHBd2YZGXLO0tMT58%2Behrq7OdZQqhYeHY82aNczj8pWYvv/%2B%2Byo7N8h/D/V8E1IN1NXV4ebmBjc3N1y5cgV79%2B7lOhLj6NGjAIBz585xnIRUt5o0jh4AunXrhtjYWBw9ehSZmZmwtrbGihUreLcknqWlJVxcXGBtbQ0dHR3WObqD8/8zNDTE3bt3eXWhVVFUVBRWr14NFRUVXLhwAVOnToW/vz%2BaNGnCdTTCI9TzTch/nDRbn5ubm1dDkm/PlClTKr3D4eHhgR07dlR/oApCQ0M/%2Bxy%2BF4u3bt1CZGSkxHhgLrm7u1d6XCAQ8OZipk2bNjAzM2Me37hxA507d2Y9vn//PhfRquTp6YmrV6/CwMAAOjo6rAtHvryuJiYmSEpKwqtXrzB58mQcOHAAWVlZcHFxoQ4OwqCeb0L%2B48oLhY9/kdWrVw85OTkoLS1F/fr1ebkxCF%2B9fPmSuZsQHx%2BPsLAw1vmcnBzcu3ePi2gS%2BF5Yf8pvv/2GyMhIJCUl8W4JP76svPEpEydOZD2u2JvMx95lExMTmJiYcB3jk7S1tZGbmws9PT2kpqZCLBZDS0sL79694zoa4REqvgn5j3v48CEAICIiAo8fP8bChQtRp04d5OXlITg4GPXq1eM4YRlpxkvyYWKovr4%2B7t27h%2BzsbBQXF%2BPChQus86qqqli0aBFH6ar2yy%2B/YPfu3cjIyMChQ4cQHByMoKAg1K5dm%2BtojA8fPiAmJgY7duzAy5cv4ezsDD8/P4kVULgUGhqK%2B/fvo3v37sxKQnxUEy%2B8xo4dW%2BnP46VLlzhIUzkzMzNMnToVa9asQevWrbF%2B/XqoqalJDD8i/2007IQQAgDo2rUrzp07BzU1NeYYn3blq2pCaDk%2BTgydN28egoKCuI7xWTt27MC%2Bffvg6emJkJAQnD17FuPGjUPLli0REBDAdTxkZWVh165d2L9/P7S1tTFq1CisWbMGcXFxvFo3PyQkBIcPH4aZmRkSExPh6enJrChDvp67uzsiIiKYnUMLCgoQHByMmJgY3txNEolECAkJga%2BvLzIzM%2BHj4wORSITg4GBabpAwqsdNCAAAIABJREFUqPgmRM4yMjLw4sULie3F%2BTaOukuXLjhw4ABrB8mUlBS4u7vj8uXLHCareTIzM6Gtrf3Jnff4VDT26dMHmzdvhpGREbPqRUZGBpydnZGQkMB1PHTs2BHW1tYYMWIEs5U8Hzetsra2RkREBFq2bInExEQEBAQgLi6O61jfDC8vLygoKGDTpk24d%2B8e5syZAwUFBQQFBaFTp06cZqs4Zp6QT6FhJ4TI0e7duxEcHCyx4yHfthcHgEGDBsHT0xM//fQT9PX1kZqaim3btuGHH37gOpqE1NRUCIVC5oKmqKgIjx8/hoeHB7fB/tGnTx/cvHkTNjY2EquJlC89xqd//7dv3zIbg5S/plpaWiguLuYyFqNly5ZISkqCnp4eGjVqhGbNmnEdqVI5OTnMFuKdO3fm1bbn34JNmzbB29sbLi4uSE5OxqhRozBt2jSmJ5xLXl5evFuakfAXFd%2BEyNHOnTvh5%2BeHoUOHQkmJ32%2B3WbNmoVatWtiyZQuEQiH09fUxfPhweHl5cR2NZevWrVi7di1T1JYXs61bt%2BZN8X3kyBEAwKlTp2rE5jXGxsaIjo7GiBEjmLzHjx9nCkmuxcTE4M6dO9izZw8GDx4MCwsLfPjwQeJuEtcUFBSY/%2Bb7%2B73ciRMn0K9fP4nj0dHRcHV15SBR1VRUVLB582ZMmDABVlZWmDNnDteRGHz7WST8RsNOCJEjU1NT/PHHH6xfyuTr2NjYYMGCBVBRUcG5c%2Bcwffp0%2BPv7Q19fHzNnzuQ6Xo10//59eHh4wMjICPfu3YOVlRVu3bqFbdu2oWPHjlzHY8nOzsb%2B/fsRHR2NoqIiDBw4EM7Ozvj%2B%2B%2B%2B5jvbZjWv4Ij8/H2/fvgUAODo64vjx46ziMScnBz/88AOSkpK4ishiZ2fHuogtLCxEZmYmdHV1mYscrud78HFTIsJfVHwTIkcTJkzAmDFjmG2c%2BS4hIQF79uyBUCjE1q1bERkZiRkzZvCqF698Hd3Xr19j4sSJOHjwILKzszFs2DDerKPbtm3bz/Z482WCWDmhUIjY2Fikp6dDT08PTk5OaNSoEdexqlRSUoLTp08jKioKN27c4MUwng4dOmDZsmXM46VLl2Lx4sWs5/BhRZ7MzEw4ODigoKBA4lz5nSR7e3ve7MJ76NChzz7H2dm5GpJUrXXr1p99v3B9gUD4gz%2B/UQn5Bunq6mL8%2BPGwtLREw4YNWef4tgpGXFwcgoKC4OLiwvTWnTt3DgKBALNnz%2BY43b90dHQgEomgq6uLly9fQiwWQ1NTk1fr6G7btg0AcOXKFZw/fx6TJ09GkyZN8OrVK2zatImXqx7o6urybojRpygqKqJfv37o168fHj16xHUcAEDDhg1Zm/00aNCA9VggEPCi%2BNbW1saZM2eQn58PJycnZl36cqqqqhKfV1ziurCWhrKyco1cvpFwg3q%2BCZGjefPmVXmOb8W3k5MT/P390alTJ5ibm%2BP69et49uwZRo8eLbFWNZcWLlyI9PR0rFu3Dj4%2BPmjfvj1UVVVx/PhxHD9%2BnOt4LA4ODti5cyf09fWZYxkZGXB1dcXvv//OYbIyFW/nV4Z6675tpaWlNWZYnFAoxJYtW/Ds2TOUlpayznG9wyUNOyFfgnq%2BCZEjvhXYn/L69WtmfG95Qda0aVPk5eVxGUvC3LlzsXr1ahQXF2P%2B/Pnw9fVFTk4OL1/rrKws1K9fn3VMXV0d79%2B/5ygR25QpUwCUjfk%2Be/Ysxo4dy/TQb9%2B%2BHb169eI4IZGXcePG4eeff8aYMWOqvADjuqCtaN68eXjz5g169uwJZWVlruOwUD8m%2BRJUfBMiR4WFhYiLi4NQKGR6asqXxduyZQvH6diaNWuGs2fPwt7enjl2%2BfJlNG3alMNUkjQ0NJhxtJqamrzr7f6YmZkZ5s2bh9mzZ0NPTw8vX77E8uXLeTPspPx2/vbt27Ft2zYYGRkx57p27Ypx48bxakUJIjvla1JbWFjUiBV5AODu3bs4deoUNDU1uY4iYeDAgVxHIDUIDTshRI5mzpyJixcvokGDBigqKkKtWrXw5MkTDB48GMHBwVzHY7l8%2BTImTpyIXr164cyZM3B2dsbRo0exevVq2NjYcB2PERoaWuU5vo25FAqFmDp1Km7dusUUOJaWlli/fj3q1avHcbp/mZiY4Nq1a6zexIKCAlhZWfFmxQtC7OzsEBsbCw0NDa6jEPJVqPgmRI4sLS2xb98%2BZGdnY9%2B%2BfVi9ejUiIyNx584drFu3jut4Eh4%2BfIjo6GikpaVBT08Pw4YNQ4cOHbiOxeLu7s56/PfffyMlJQV9%2B/bFmjVrOEr1aeWbAunp6cHAwIDrOBLc3d3x/fffY/bs2VBRUUF%2Bfj4CAgIgFAqZyaN8wOcxvzXNp%2BajlOPbUK6YmBjEx8fDy8tLYkIon1fmIaQiGnZCiByVlpbiu%2B%2B%2BQ/369Zml0EaOHInIyEiOk0ny9vbGypUrJZZG45vdu3dLHDty5AgSExM5SPN5f//9N86fP4/09HRMmjQJFy5cgLW1NdexWJYuXYrx48dj//79aNCgAbPj5c8//8x1NBY%2Bj/n92ODBg3H48GGJ43Z2drxZDrPc27dvcfHiRfTs2ROGhoYQCoX47bff4ODgwHU0CQsXLgQA/PbbbxKbbPFhqUlCpEXFNyFypKenh9TUVBgaGiIrKwt5eXlQUFBAbm4u19EkJCUl8WKb5v/HoEGDsHz5cq5jSHjw4AEziTE5ORlubm6YNGkS/P39ebHkXLnvvvsOJ06cQFJSEtNDb2pqyrtVMPg85vfFixfMPI7k5GSJnmWRSFTputpcKe/VnjBhAjZs2MCaXHvp0iWEhYVxFa1KtPIO%2BVZQ8U2IHDk5OcHNzQ0xMTGwtbWFt7c3VFVV0a5dO66jSRgwYAB8fHzg5OQEbW1t1iQsc3NzDpN93rVr11CrVi2uY0gICgrCzJkz4eLiAnNzcxgaGiI0NBQhISG8Kr6Bsu3Q%2Bf7vXKdOHd5eIDZp0oS5a1AZTU1NrF27tppTfV5iYiI2b97MOmZlZcWshMMnjRs3ljhWXFyMx48fV3qOEL6i4psQORo3bhwMDQ1Rp04dLFq0CCtXroRIJMKiRYu4jiZhz549AIDz58%2BzjvPtlm7FtamLiorw5s0beHt7c5iqco8ePcKQIUMA/Lt8o42NDaZPn85lrBpr4sSJmDdvHm/H/JZvRmVoaIiJEydynEY6jRs3xokTJ%2BDo6MgcO3jwIO9WOQLKPpuWLl0KoVDIWtpPSUkJd%2B/e5TAZIV%2BGJlwSUg2ysrKQlpYGbW1t1oYr5MtV3GpaQUEBRkZGvLyb0KdPH2zatAktWrSAhYUFrl27hmfPnmH8%2BPE4deoU1/FqHGNjY9ZjgUDAqzG/N27cQOfOnXH9%2BvUqn8O3uwtnz57F1KlT0aFDB%2Bjr6%2BPly5d4/PgxwsLCYGlpyXU8lgEDBqBbt26oW7cuHj16hAEDBmDTpk0YNmyYxERsQviMim9C5EgkEmHOnDnMWEWBQAArKyusW7cOdevW5Tjdv8RiMVJTU9GkSRPm2PHjx9GnTx8oKipymKxm27FjB/bs2QNvb28EBgYiODgYmzdvxoABA/DTTz9xHe%2BzRCIRr5Z1S0tLq/IcH4YdlO9yWPEioRxfLhIqevr0KY4fP46MjAzo6enByckJhoaGXMeS0LFjR9y4cQMvX77EokWLsHv3biQnJ2PatGmIi4vjOh4hUqPimxA5Wrp0Kf766y8sWrQIBgYGeP78OZYvXw5DQ0P4%2B/tzHQ8AkJeXhx9//BENGzZk1tDOyspCz5490a5dO2zbto1X46lr0nJzYrEYu3btwt69e5Geng49PT24uLjAy8uLVxublPfKV2RmZoY//viDg0Sf9uDBA7x8%2BRK2trbIycmBlpYW15FqvHfv3iE1NRWtW7dGSUkJL8fW9%2BzZE2fPnkVxcTFsbW1x%2BfJlAGV3Ez51t4EQvqEx34TI0e%2B//44DBw4wxUGrVq2wcuVKDBw4kDfF9//au/e4mu8/DuCvE11dKqlJJWZMM5eFwqLLVi5js6QNa2aYkLCfptyVhlxzbUVNJBu5LCVsElZK2VzGfvxs7MgUlVmldf394dH5OU6x/R7O%2BXxPvZ6PR3%2Bc77c/Xo9s9T7f83m/31u2bIGuri6WLFmiuGZmZobU1FRMmTIFX3zxBWbNmiUwoTJtGTcHPHry/d5772HcuHGio6i4efMmFi5ciJqaGhQXF%2BPDDz9Uul9cXCypT2eAR28Kp02bhkuXLkFXVxd79%2B6Fl5cXoqOj8dprr4mOh9u3bz/ze6RwNv1xJSUlWLhwIZKSkmBgYIB9%2B/Zh/PjxiImJwYsvvig6npKXX34Z4eHhmDZtGszMzJCWlgYDAwPo6%2BuLjkb0j7D4JlKjhw8fokWLFkrXWrZsqfLEVqQjR44gKipK5emhmZkZlixZgpkzZ0qq%2BJbyuLknbdmyRaWolQpbW1t4eHigqKgI586dg4ODg9J9PT09uLm5CUpXt88//xydO3dGTEwMBg4ciI4dO%2BKTTz5BWFgY4uPjRcdTaQYG/jeHupbUjp2EhYWhtLQUhw8fhre3N2xsbODq6orQ0FBs27ZNdDwlAQEB8Pf3h7e3N/z9/TF16lRUV1crGl2JtAWLbyI16tGjB8LDwzF79mxFc1h4eDi6desmOppCQUFBvZMN7OzscPfuXQ0nejopj5t7kpOTE7Zt2wYvLy9JvlkYO3YsAMDa2lpyow/rcubMGXz77bcwNDRUFLQTJ06UzNKq2t6OgwcPIicnBwEBAWjXrh1%2B//13rFq1Cj179hScUFVqaioSExNhbGwMmUwGXV1dBAYGSm4RFAB07NgRSUlJAB6d8U9NTUVJSQk6dOggOBnRP8Pim0iNZs%2BeDR8fH3zzzTewsrJCbm4uZDIZYmJiREdTaN68OYqKimBqaqpy7/79%2BzA0NBSQqn5SHzf3uB9//BHJyclYu3atSuPqpUuXBKVS5e7uji%2B//BIfffSRYkFMq1atEBwcjBdeeEF0PAVdXV2UlZXB0NBQMWqupKQEzZo1E5zskdqmz6%2B%2B%2BgrffPMNjI2NATwqGsPCwjB48GBMnjxZZEQV1dXVijeztT/Tx69J1ZUrV5Ceno7evXuLjkL0j7H4JlKjzp0748iRI/juu%2B9QUFAAKysrODs7S2qCRL9%2B/RAXFwc/Pz%2BVe7t27ZLc0zptWjEdGhoqOsLfEhISgitXruCjjz7C4sWL0bZtW%2Bjr62Px4sWKrY1S4ObmhoCAAMyfPx8ymQwFBQVYunQpnJ2dRUdTUlJSonK0rLS0FBUVFYIS1a9v374IDg7GwoULFf8/rVu3TuUYkkh37txBQEAALl26hMGDB8Pb2xs%2BPj5o1qwZ1qxZg7Vr18LDw0N0TKK/jdNOiDSsuLgYkZGRklm08uuvv8LT0xOenp4YOnQozM3NkZ%2Bfj8OHDyMhIQE7d%2B6U1AxtqY%2Bbe1x1dbXSiva7d%2B/C3NxcYKK6ubm5Yd%2B%2BfYpRmKmpqTAxMYGTk5OkpkiUlJQgKCgIR48eBfBodJ%2BzszNWrlyp0lsh0pw5c/Dbb7/B398flpaWkMvlCA8PR/fu3bFw4ULR8ZQUFBRgypQpuHz5MqqqqmBgYID27dsjIiJCMp96TJ06FTU1NfD29sahQ4dw6tQp%2BPr64uOPP0ZCQgLi4%2BOxd%2B9e0TGJ/jYW30QalpeXBxcXF0k9pT137hwWLVqEa9euKc6md%2B7cGQsWLJDcUhBtsXbtWty9exeff/45AKCoqAgDBgzAhAkTJNXACgCOjo7IzMxESkoK1q5diyNHjqC8vBxOTk51jiAUrbCwELdu3UKbNm1gYWEhOo6KkpISLFmyBCkpKSgvL4e%2Bvj7eeecdzJ8/X3LHOeRyOaytrXHx4kXk5uaiTZs26N69u6Tm%2Bzs6OuL48eNo1qwZ/vjjDzg6OuLChQvQ09NDVVUVHB0dJTkSk6g%2BPHZCRLC3t0diYiLkcjkKCwthbm4uufPTtTIzM7FkyRLcuHEDTz47kMobmj179mDfvn2KwhsAjI2NsWbNGixatAjt2rXDyJEjBSZU1qlTJ2zevBknT56Eq6sriouLsW7dOnTt2lV0NBVnzpzBwYMHcffuXbRt2xZeXl7o3r276FhKmjVrhrCwMCxduhT379%2BHqampZMdivvfeezh69Ci6d%2B8uuZ9jrfLycsW5fmNjYzRv3lzxJqZJkyYqvweIpI7FNxEp2NjYSHKz3eOWL1%2BOHj16YP78%2BWjaVJq/wuLj47Fq1Sql9dw6Ojrw8PBA06ZNsWnTJkkV34sXL8aSJUvQvHlz%2BPn54fLly8jMzMT69etFR1Py9ddfIyQkBB4eHrCzs8OtW7fg4%2BODVatWwd3dXXQ8JdevX0d8fDzu3LmDkJAQJCUl4YMPPhAdS4WJiQny8vIk1YfypCfHNz5%2BlAsAi2/SOtL8y0VEVI8bN25g9%2B7dkl6scevWrXob1gYOHIg5c%2BZoONHTvfTSS9ixY4fitYODgyTXdUdGRiIiIgKvv/664lpaWhrCwsIkVXx///33mD59OlxdXZGeno6ysjJs2rQJpaWl%2BOSTT0THU9KpUyd4e3ujZ8%2BeKkd4li1bJiiVsurqamRnZyuK7MrKSqXXUtqbQPR3sPgmUoOgoKB675WVlWkwScPTvn175OfnS/oJfZMmTVBRUVHn%2Bd4nmzCloLy8HImJicjLy1MUMhUVFbh69aqkpp0UFBSgb9%2B%2BStcGDBiAgIAAQYnqVjuBw9nZGX369IGlpSUiIyMxc%2BZMyRXfRkZGkp8UUlZWpvKpweOvn3wyTiR1LL6JNMzAwEArFppI1ZAhQzBx4kR4eXmpTA6Rys%2B1a9eu%2BPbbbzF06FCVe999953kloLMnTsXp06dgqmpKSoqKmBkZIRr165J5udZa8CAAdi5cyfGjRunuJaUlIT%2B/fsLTKXq5s2biiU1tYVht27d8Mcff4iMVSepPN1%2Bmp9//ll0BKLnisU3kRpowx80bbV7924AUFknXlRUJJli0cfHB5999pliRbuOjg6qq6tx/PhxBAcHY968eaIjKjl16hTi4%2BNRWFiI%2BPh4rF69GtHR0bhw4YLoaEqqqqqwfPly7N%2B/H7a2tsjLy8P58%2BdhZ2eHDz/8UPF9sbGxAlM%2BWvZ07tw59OrVS3Ht4sWLsLS0FJhK1aVLl3D16lV4enoCePRpx5QpUzBjxgxJbeElamhYfBORVjl%2B/LjS619%2B%2BQVffvklvvnmG0GJVDk7O2PSpEmYMWMG9PT0YGpqiqKiIlRUVGDatGkYNmyY6IhKqqur8eKLL8LExEQxMWbs2LGSWdtey87ODnZ2dorXnTp1gpOTk8BEdZs8eTKmTJmC0aNHo6KiAlFRUdixY4dkZvsDwOXLl%2BHj44MxY8Yorj18%2BBAGBgYYN24c4uLilH7WRPT8cM43EWml7OxsbNu2DWlpaejcuTNGjRqFsWPHio6lJC8vDydOnFCMbxwwYIBkFpc8bvjw4di8eTNsbGzg6OiI1NRU6OjooF%2B/fvjhhx9Ex9NKaWlpiIuLU8zO9vb2xqBBg0THUpg2bRq6desGX19flXurV6/Gr7/%2Bio0bNwpIRtTwsfgmIq1RXV2NlJQUxMTE4Nq1a6isrMSWLVswYMAA0dG0WmRkJHbs2IG9e/dizZo1uHPnDvT19fHw4UOlKSgiPXz4EJs3b0ZKSgry8/Nhbm6OQYMGYerUqYoZ0FIREhKCWbNmSXp8n5OTE44dOwZDQ0OVe/fv38ewYcNw%2BvRpAcmIGj5ptdwTNTDnz5%2Bv8/rJkyc1nET7bd%2B%2BHe7u7li5ciXc3d1x4sQJNG/eHJ07dxYdTet98sknmDt3Llq0aIEFCxagffv2aNGihdKSIJH%2B%2BusvjB49GikpKRg%2BfDiCgoIwaNAgHD58GKNHj5bcBKHExEQYGBiIjvFUZWVldRbewKPZ31L7mRI1JHzyTaRG9vb2OHfunNK14uJiDBgwgB/n/0NdunTBmDFjEBgYqBjh17dvXxw8eFCSRzno%2Bdm0aRMyMjKwdetWpaK2pKQEkyZNQv/%2B/eHn5ycwobIVK1agpKQE7777LiwsLJRG4Ullc%2Bzbb7%2BNsLAwdOnSReXev//9b/j7%2B%2BPIkSMCkhE1fCy%2BiZ6zmzdv4q233kJVVRVqamrqnEFrb2%2BPuLg4Aem0V1xcHHbt2oXCwkJ4e3tjzJgxGDFiBA4cOCC54vv69evo2LGj6BjP5OPj88wZyaInhwCPzqSvWLECr7zyisq9CxcuYO7cuTh06JCAZHV7vKCt/fnW/i6obWgV7YsvvsDp06cRGRmp9AS8tLQUU6ZMwauvviq5%2BelEDQWLbyI1uHLlCh48eIBPPvkEUVFRSvf09fXRuXPnej/ypafLyMjAzp07cerUKVRVVSE0NBTDhw9HkyZNREdTcHR0RGZmJiZMmIBt27aJjlOvv9NQJ4Unyr169UJOTk6d9yorK%2BHg4KDyCZNIubm59d6zsrLSYJL6lZeX44MPPsDt27fh4uKC1q1b4%2B7du0hLS4O5uTni4uJgZGQkOiZRg8Tim0iN5HK5pDcxarPc3Fzs2rULCQkJ0NHRwdtvv43AwEDRsQA8Ws/u7%2B%2BPlStXIjQ0FHX9mh0%2BfLiAZNrJwcEBR48ehYmJicq9oqIiDB06FBkZGQKS1e3Bgwdo2bKl4vX58%2BfRo0cPgYnqVl5ejtjYWKSmpiom8ri5uWHMmDF1bmcloueDxTeRGpWUlGDXrl24ceOGYm13LS7ieT7Ky8vxzTffYNeuXdi3b5/oOACA6OhoxMXF4ffff1fZwgk8Oopw4sQJzQfTUpMmTYKTk5PSZstasbGxSE9PR0REhIBkyqqqqjB79mxUV1cjPDwcAHDv3j04OTlh8ODBWL16taQ%2BoSEiMVh8E6mRv78/fvjhBzg6OkJXV1fpHovvhq9v3744c%2BaM6BhaLyMjA9OmTUNwcDAGDx6Mpk2bory8HPv370dYWBi%2B%2BOIL9O7dW3RMREZGIjExEatXr1aawvPzzz9jxowZ8Pb2xoQJEwQmJCIpYPFNpEaOjo7Yu3cvj540YjU1Nbh8%2BTJyc3NhYWGBHj16PLPJkVTFx8dj%2BfLlAABjY2MUFBRAV1cXCxYswMiRIwWne%2BStt97C6tWr65wgkp2djcWLF0uqMZSIxOB6eSI10tfXl9wkDtKcwsJC%2BPr64uLFi2jZsiUePHiAl156CVu3bpXsfxeFhYVo1aqV6BgqRo8eDXd3d5w8eRJ3796Fubk5XFxcJJU1Ly%2BvzsIbeDTh6Pfff9dwIiKSIi7ZIVKjMWPGYPny5SgsLBQdhQRYvnw5rKyskJWVhczMTGRkZKBjx46KJ7hSUVlZibVr16JXr15wc3ODXC7HyJEjkZ%2BfLzqaktatW8PT0xOTJ0%2BGp6enpApv4NGb7ZKSkjrvlZWVSbKJkYvAiDSPxTeRGn399dfYtWsXXn/9ddjZ2Sl9UcOXnp6OkJAQtGjRAsCjzYHBwcFIT08XnEzZhg0bcObMGYSHh0NXVxdmZmZo06YNQkNDRUfTKr169cKBAwfqvHfw4ME655SLNn78eJVrxcXFmDFjhoA0RI0Dj50QqZHUnnCSZlVVVamc79bR0ZHcxIvExETEx8fjhRdegEwmg5GREZYtWwZ3d3fR0bTKxIkTMW7cOPz111946623FLOzk5OTsWHDBmzatEl0RACqi8Dqehhgb28vIBlR48Dim0iNHBwcAAB//PEH5HI5XnnlFVRWVkry42d6/hwcHBASEoLFixfDwMAADx8%2BREhICPr06SM6mpLS0lLFEY7aHnwDAwPo6Ejjw9G0tDQ4OzuLjvFM3bt3x7Jly7B48WKsXLlScd3ExAQhISHo37%2B/wHT/Y2triz179jxzERgRqQennRCpUUlJCRYuXIikpCQYGBhg3759GD9%2BPGJiYvDiiy%2BKjkdqduvWLYwfPx537tyBmZkZCgoK0L59e0RGRsLS0lJ0PAVfX1%2B8/PLLmDVrFhwcHJCVlYVt27YhMzMTkZGRouOhT58%2BOHv2LDw8PHD06FHRcZ6pvLwcOTk5KCoqgrm5OXr27KkyalQquAiMSPNYfBOp0aJFi5Cfn4/PPvsM3t7eSE9PR2hoKORyuaTXjtPzU15ejrNnz%2BLevXuwsrJCz5490bSptD50lMvlGDduHCorK1FQUABbW1uUlJRI5k1i//798dZbbyE%2BPh6%2Bvr51fo%2Bfn5%2BGUzUMXARGpHnS%2BgtA1MCkpqYiMTERxsbGkMlk0NXVRWBgIAYOHCg6GmmInp4eXn/9ddExnsrGxgZJSUk4ceIEcnNz0aZNG7i4uKB58%2BaiowEAFixYgD179qCmpgaZmZkq9zk3/f8XFBRU7yIwIlIPFt9EalRdXa043137IdPj14ikoLy8HBEREfDy8sKQIUOwfft2bN26Ff7%2B/pI49z1kyBAMGTIEo0aNwo4dO0THaVAyMzO5CIxIw8T/ViVqwPr27Yvg4GA8fPhQ8XRu3bp1ikZMIilYtmwZTp48qZjC0rVrV5w%2BfRqrVq0SnEzZnj17UFJSguTkZERFReHgwYN48OCB6FgKaWlpoiP8Y1wERqR5PPNNpEYFBQWYMmUKLl%2B%2BjKqqKhgYGKB9%2B/aIiIjgHzySjNdffx2JiYlKS2vu3buHESNG4PTp0wKTKbt58yY%2B%2BugjVFRUoG3btrh9%2Bzaqq6uxfft2dOrUSXQ8rWsMBYCIiAjk5%2BfDz89PckuLiBoqFt9EaiSXy2FtbY2LFy8qztJ2795dcnOeST1qamqQmpoKNzc35OXlISwsDK1atcLMmTPRrFkz0fEUevfujdOnT8PAwEBxraysDC4uLjhz5ozAZMp8fX3RoUMHBAQEQEdHB9XV1Vi5ciWuXr0qiQZmbWwMdXNzw%2B3bt%2Bs8N3/lyhUBiYgaPhbfRGrUv39/HD16VDKNa6RZK1aswKFDh3Dq1ClMnToV9%2B/fR5MmTWBB3rENAAATtElEQVRtbS2pSRK%2Bvr544YUXMG/ePOjp6eGvv/7CihUrcOfOHWzevFl0PIV%2B/fohLS1NqWeirKwMTk5OyM7OFpjskcOHD2PPnj3IzMysc0mNTCZDbGysgGT1y8rKqvcej8cRqQcbLonUyMTEBHl5eSy%2BG6njx48jPj4epaWlOHnyJA4dOgQzMzPJbY6cN28eJk6cCHt7e5iamqKoqAgdOnRARESE6GhKmjRpguLiYqXjEcXFxTA0NBSY6n%2B0sTGUi8CINI/FN5EaderUCd7e3ujZsycsLCyU7knpySepR1FREaytrZGWlgZzc3O0b98e1dXVqKysFB1NiY2NDZKTk5GTk4N79%2B4pjkdJbR65q6sr/vWvf2HBggWwtraGXC7H0qVL4erqKjqaktrG0LS0NOTm5sLCwgKurq5o2bKl6GgquAiMSPM47YRIjYyMjODh4aFSeFPjYG1tjcTEROzevRtOTk6oqanB9u3b0bFjR9HRVFRVVaFdu3bo2bMn2rRpg/z8fNy%2BfVt0LCX/%2Bte/UFlZiaFDh6JHjx4YNmwY9PX1MXv2bNHRlNy8eRPDhg3D559/jmPHjmHlypUYPHgwrl27JjqairCwMJSWluLw4cPQ1dWFjY0NXF1dERoaKjoaUYPFM99EarR161aMHj1aUs11pDmZmZkICAiAoaEhYmNjcf36dcyaNQtbtmyp80ywKIcPH8bChQtRXFysuFZTUwOZTCbJpju5XI6CggJYWVnB3NxcdBwVUm8MfdzAgQMVi8AcHByQlZWFsrIyDBw48KnnwYno/yetzxSJGpjIyEiMHz9edAwSpLCwEMeOHYO%2Bvj6ARz0AJ0%2BeVLyWig0bNmDs2LF49913JXfUpC42NjaSXgpz/vx5rF%2B/XrGgSEdHBzNmzICTk5PgZKq4CIxI83jshEiNBgwYgKioKOTn54uOQgIsWrRIaUOkvr6%2B5ApvAPj999/h5%2BcHW1tbWFlZKX3RP1fbGPo4KTWGPo6LwIg0j8U3kRrl5ORg3bp1cHZ2hp2dndIXNXxdu3bVimUrXbt2xX/%2B8x/RMRqM2sbQX375BeXl5bh%2B/ToCAgIk1xgKAEFBQbh%2B/Tr69OmDP//8E6%2B99hrOnj2LOXPmiI5G1GDxzDeRGnGGbuPm7e2NixcvwsDAAObm5kqLTI4cOSIwmbI1a9bg66%2B/xuDBg9G6dWule1JaCpOUlAR3d3fJH4m4f/8%2Bpk%2BfjrNnzyr%2BzZ2dnREWFia5iSdcBEakeSy%2BiYjUZM%2BePfXeGzVqlAaTPJ2Pj0%2Bd16W2FMbBwQHff/89dHV1RUf5W6TeGApwERiRCCy%2BidTIzc2tzrXNAPDdd99pOA1JRVVVFZ8s/h8mTJiAt99%2BG%2B%2B8847oKA3G0KFDsWHDBkmOvyRqqFh8E6nR/v37lV4XFhYiISEBo0aN4hSURkAul2PLli3Iy8tTTJKoqKjAL7/8gu%2B//15wOuDQoUMYNmwYDhw4UO/3jBgxQoOJnm7kyJH46aefoKenh9atWyu9seWb2f/PjBkzcPr0aS4CI9Ig6c%2BUItJi7777rso1d3d3fPrppyy%2BG4F58%2BahoqICrVq1QkFBAbp06YLExESMGzdOdDQAQEREBIYNG4b169fXeV8mk0mq%2BP7ggw9ER2hwaheBEZHm8Mk3kYZVVVXB0dER2dnZoqOQmr322mtITU3F7du3sX79ekRERCAtLQ1RUVHYuXOn6HharbCwEK1atRIdo07a0hgKcBEYkQgcNUikRmfPnlX6Sk9Px5IlS9C%2BfXvR0UgDDA0NYWJiAltbW1y9ehXAo42C169fF5xMWXV1NY4dOwYAyMvLw8yZMxEcHKwyq1q0yspKrF27Fr169YKbmxvkcjlGjhyJu3fvio6mZMmSJfX2ekhNZGQkDAwMRMcgalRYfBOpkY%2BPj9LXxIkT8cMPPyAwMFB0NNKAdu3a4dSpU2jWrBkqKyuRm5uLe/fuobKyUnQ0JcuXL8fSpUsBPFoMdO/ePfzyyy8IDg4WnEzZhg0bcObMGYSHh0NXVxdmZmZo06aNIrtUdOvWDcnJyaJj/C1cBEakeTx2QkSkJt9%2B%2By0%2B/fRTJCUl4eDBg9i9ezeaNm0KBwcHhIWFiY6nMGjQIMTExMDY2BiOjo5ISkqCmZkZ3njjDWRmZoqOp%2BDm5ob4%2BHi88MILcHBwQFZWFh48eAB3d3dJ5dSmxlAXFxfcuXOnzif1V65cEZCIqOFjwyWRmtTU1EAul6Ndu3aKa8nJyRg0aBDHzDUSb775JlJSUmBhYQE/Pz%2B0a9cOxcXF8PLyEh1NSVFREdq2bYsTJ07AwsICtra2qKqqQlVVlehoSkpLSxXnvGufGxkYGEBHR1of4mpTY6iU3gQSNRYsvonUoLS0FB9//DFat26NjRs3AgAKCgoQGBiInTt3YuvWrTAyMhKckjShbdu2%2BPe//41bt25hyJAh%2BPPPPyXXiGdjY4MDBw4gJSUFTk5OqK6uRnR0NF566SXR0ZT07NkTGzduxKxZsxRPanfs2IFu3boJTqbs8SlHUm4MBbhpl0gEHjshUoPVq1fjxx9/xLp162BmZqa4XlBQgClTpqBfv36YNWuWwISkCYWFhfD398cPP/wAPT097N27F97e3oiOjkaPHj1Ex1M4e/Ys5syZAwMDA3z55Zf4z3/%2Bg08//RQRERHo2bOn6HgKcrkc48aNQ2VlJQoKCmBra4uSkhLExMTgxRdfFB1PobKyEhs2bMDOnTtRVVWFxMREzJw5ExEREZLbdMlFYESax%2BKbSA08PDwQFRUFW1tblXtXrlzBzJkzceTIEQHJSJNmz54NAwMDBAYGwtXVFWfPnsXGjRuRkZGBuLg40fHqVV5eDgCSe0IPAA8fPsSJEyeQm5uLNm3awMXFRXKr0deuXYszZ85g%2BvTpmDVrFtLS0hAQEICmTZsiPDxcdDwlXARGpHk8dkKkBrVP5epiZ2cnudFopB4ZGRk4duwYjIyMFE8XJ0%2BejO3btwtO9nRSLLpr6evrw9LSEjo6OrCyspJc4Q0AiYmJisZQmUwGIyMjLFu2DO7u7qKjqeAiMCLNY/FNpAbNmzdHUVERTE1NVe7dv38fhoaGAlKRpjVt2hTl5eUwMjJSNAiWlpbyvP//6ebNm5g8eTJu3boFExMTFBUV4ZVXXsGmTZtUVqOLpC2NofWxsrLCjRs3RMcgarC04zcBkZbp169fvccKdu3aJalztKQ%2Brq6umDNnDuRyOWQyGe7fv4/g4GAMHDhQdDStFBISgr59%2ByI7OxunT59GZmYmXnrpJcnNI69tDAUg6cZQgIvAiETgmW8iNfj111/h6ekJT09PDB06FObm5sjPz8fhw4eRkJCAnTt34tVXXxUdk9SsuLgYc%2BbMUTSuyWQyODk5YfXq1WjZsqXgdNrH0dERp06dUjoW8/DhQ7i4uEhqzre2NIYCQJcuXZRe6%2BjooGPHjli0aBF69%2B4tKBVRw8bim0hNzp07h0WLFuHatWuQyWSoqalB586dsWDBAvTp00d0PNKg/Px8RYOgpaWl6Dgq7t69i6ioKMydOxfZ2dmYPn06WrVqhfDwcEmNG/T09ERYWJhSpl9//RW%2Bvr6Sa2DWhsZQIhKDxTeRmsnlchQWFsLc3Bxt27YVHYc0wNfXFytXrkSLFi1ER/lbpk%2BfjtLSUmzduhUjR46Evb09DA0NceHCBUk0hx44cAAAcOnSJXz33XeYMGECrKyskJ%2Bfj%2BjoaLz55psICAgQnFJZdXU1Lly4gLy8PFhZWUnyky4uAiMSg8U3EdFz5u3tjYKCAqxfvx5du3YVHeeZXFxckJycjOLiYjg7OyM9PR0tWrSAo6MjcnJyRMeDm5vbU%2B/LZDJJzaTWhsbQ%2BhaBubq64tVXX%2BUiMCI1YvFNRPScVVVVYf369YiNjcWcOXPw/vvvi470VI6OjsjIyEBiYiKio6Nx8OBBFBcX44033pDUWWptMXHiRFhbWyMwMBAGBgYoLi5GaGgo/vzzT0WhKxoXgRGJw%2BKbiEhNsrKyEBQUBHt7e8yYMUNp1JyUjiBNmjQJlpaWyMnJwZAhQ/D%2B%2B%2B8jODgYNTU12LBhg%2Bh4SrKzs5Gbm4sn/3SNGDFCUCJV2tAYykVgROJwzjcRkZo4ODhg06ZNeP/993Ho0CEAj87ZymQyXLlyRXC6/wkNDcWaNWvQu3dvTJ48GZcvX0Z5eTmWLl0qOpqSRYsWYe/evbCwsFBaiS6TySRVfFtZWeG3335Tagy9c%2BcOTExMBKZSxkVgROKw%2BCYiUpO4uDisWrUKgwYNgp%2Bfn2SXrFhYWGD58uWK1z169EBERITARHVLTk7GV199JcnmReB/jaH29vaYNGlSnY2hUsFFYETi8NgJEdFzVlhYiLlz5yIrKwsLFy6U1FPZupSUlCAuLg5yuRyVlZVK95YtWyYolSo3NzekpKQoHeeQEm1qDA0MDIS1tTX8/PxU7m3evBk//fQTNm3aJCAZUcPHJ99ERM/Z22%2B/DXNzcyQkJKBDhw6i4zxTUFAQzp8/j969e0u2sAWAKVOmYN68eZgwYYLKkiIpnKE/fvy46Ah/2%2BTJk%2BHp6YmioqJ6F4ERkXqw%2BCYies7c3d0RFBQk6UL2cadOncKRI0ckMwavPn/99ReSk5MV5%2BcBaZ6hB6TfGNqhQwds27YNixYtQlxcnNIisKioKMke7SFqCHjshIiokfPw8EBSUhJ0dXVFR3mq/v37Y/r06XByclI5P29lZSUolaqnNYZK5djJ47gIjEizWHwTETVy0dHRuH37Nvz9/VWOc0iJo6OjZEb1PU2fPn0QExPDp8dEVCcW30REjVSXLl0Uxw0AKD2lrSWl4xwrVqyApaUlPvzwQ9FRnkrqjaFEJBaLbyKiRiozM7POgvtxDg4OGkrzbGPHjkVOTg6aNWsGY2NjpexSOs6xZ88eZGVlSbYxlIjEYsMlEVEj5ejoCABYunQp5s%2Bfr3L/s88%2Bk1Tx7eXlBS8vL9ExnkmbGkOJSPNYfBMRNUJ5eXnIyMgA8OhJ7ZPnk//8808cO3ZMRLR6vfvuu6Ij/C2bN2/G/Pnz62wMJSJi8U1E1AiZmppi586dKCwsRHl5OdavX690X19fv84FLCL5%2BPjUe0wmNjZWw2nqV1VVhdGjR4uOQUQSxeKbiKgR0tPTw969ewEAEyZMwLZt2wQnerbaYzK1ioqKkJKSgvfee09Qorp5enoiNjZW8o2hRCQGGy6JiEhr/fTTTwgLC8P27dtFR1HQlsZQIhKDT76JiBq5rKwsLF68GDdu3FDZyCj1BsGuXbvi0qVLomMo0ZbGUCISg8U3EVEjt2zZMvTo0QPz589H06bS/bNw%2B/ZtpdcVFRVISkqCpaWloER105bGUCISQ7q/ZYmISCNu3LiB3bt3Q19fX3SUp3Jzc1M6wlFTUwNjY2MsXbpUYCpV2tIYSkRisPgmImrk2rdvj/z8fNjY2IiO8lRPnpdu0qQJzMzMoKurKyhR3bSlMZSIxGDDJRFRIxcZGYmEhAR4eXnB3Nxc6d6IESMEpWpYpNgYSkRisPgmImrk3Nzc6rwuk8kkMZ3jyeMmT5LJZPj22281mOj/06tXL%2BTk5IiOQUSC8dgJEVEjd/z4cdERnmr69Ol1Xv/xxx/x1Vdf4ZVXXtFwoqfTlsZQIhKDT76JiAiXLl3C3r17kZubC3Nzc3h6eqJ3796iY9UrOjoaa9aswahRoxAUFAQ9PT3RkRS6dOlSb2Oou7u7wGREJAUsvomIGrnTp09j6tSpcHNzg7W1NX777TekpqZi7dq1ePPNN0XHU/LgwQPMmTMH2dnZCA4OxpAhQ0RHUpGbm6v0WqqNoUQkBotvIqJGztvbG%2BPHj1cqZA8fPoyoqCjs27dPYDJlP/74I2bNmgVTU1OEh4dLfjoLEVFdWHwTETVyffr0QWZmJnR0dBTXqqur0bt3b5w7d05gsv/ZunUrwsPD8d577%2BGzzz6T1DGTWg2lMZSI1IsNl0REjZyJiQmuXr2KLl26KK79/PPPKmMHRfH19UVaWho%2B%2BOADeHh44Pz58yrf06dPHwHJlGlbYygRicEn30REjVxkZCTi4%2BMxefJkxZnvqKgojBkzBpMmTRIdT%2BlNQV1kMhmuXLmioTT/jJQbQ4lIDBbfRESNXE1NDTZu3Ih9%2B/bh3r17sLKywqhRozB%2B/Hiloyj092lDYygRicHim4iI6DliYygRPQ3PfBMRNVIbN2585vf4%2BflpIEnDoQ2NoUQkFp98ExE1Ul26dEGLFi1gZ2eHuv4UyGQyxMbGCkimnZ5sDK2LFBpDiUgsFt9ERI1UTEwM9u3bh4qKCowaNQojRoyAmZmZ6FhaS5sbQ4lIc1h8ExE1chcuXEBCQgKOHj0Ke3t7jBo1CgMHDmSzJRGRGrD4JiIiAEBZWRlSUlKwf/9%2B3LhxA%2B%2B88w4%2B/fRT0bGIiBoUFt9ERKRQUlKC5ORkbN%2B%2BHb/99hsuXLggOhIRUYPCaSdERIT09HQkJCTg%2BPHj6NChA95//30MGzZMdCwiogaHT76JiBqpGzduYP/%2B/Th48CAqKiowbNgweHp64uWXXxYdjYiowWLxTUTUSNnZ2cHU1BTDhw%2BHi4sLmjZV/TCUo/GIiJ4vFt9ERI0UR%2BMREWkei28iIiIiIg3hEFciIiIiIg1h8U1EREREpCEsvomIiIiINITFNxERERGRhrD4JiIiIiLSEBbfREREREQawuKbiIiIiEhDWHwTEREREWnIfwFghnYh3X0hHQAAAABJRU5ErkJggg%3D%3D" class="center-img">
    <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAt8AAAKTCAYAAADBkGTTAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAPYQAAD2EBqD%2BnaQAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAIABJREFUeJzs3Xt8zvX/x/HHtZPNccxmMXIcJWXMzJlRDiGHZSFCKWTkR9GBJIcpURHJWVKToXxTyTeHVKwyKufmsDntZMzMztfvj7Xr67Lh0j6b0fN%2Bu%2B122efw%2Brw/7%2Bv62Ovzut6fz8dkNpvNiIiIiIhIobO73Q0QEREREfm3UPItIiIiIlJElHyLiIiIiBQRJd8iIiIiIkVEybeIiIiISBFR8i0iIiIiUkSUfIuIiIiIFBEl3yIiIiIiRUTJt4iIiIhIEXG43Q0QERFrhw4dYu3atfz888/ExMSQlpZGhQoVqFOnDm3btiUwMBBnZ%2Bfb3UwREfkHTHq8vIhI8fH%2B%2B%2B%2BzYMECsrOzKV26NNWqVcPR0ZG4uDjOnDkDwD333MMHH3xA/fr1b3NrRUTkVin5FhEpJsLCwnjllVcoWbIkM2bM4OGHH8be3t4yPzIykldeeYW9e/dSvnx5Nm3aRIUKFW5ji0VE5FZpzLeISDHx4YcfAvDSSy/RqVMnq8QboFatWixYsAA3NzcSExNZuXLl7WimiIgUgJJvEZFiICkpiaioKAAeeuih6y5XoUIFOnToAMDvv/9eJG0TERHj6IJLEZFiwMHhf/8db926lfvvv/%2B6ywYHBzNw4EDc3Nws0yZMmMD69et5%2BeWXadWqFXPmzOGXX34hPT2de%2B%2B9l549e/LEE09QokSJfGP%2B8ssvfPzxx%2BzZs4cLFy5QtmxZGjZsyIABA2jWrFm%2B6yQlJfHZZ5%2Bxfft2/vrrL5KTk3FxcaFatWq0a9eOgQMHUq5cOat16tatC8CPP/5ISEgI//3vf7Gzs6N%2B/fosXbqU1157jfXr1zN16lSaNGnC3Llz2bVrF5cuXcLLy4vHH3%2BcQYMGYTKZ2Lx5MytWrODgwYNkZ2dTr149hg8fTps2bfK0NTU1lbCwMLZs2cLhw4dJSkrCycmJypUr07JlSwYPHkylSpWs1gkICOD06dNs2rSJhIQEFi9ezL59%2B0hJScHLy4vOnTvz9NNPU6pUqeu%2BVyIi19KYbxGRYqJv377s2bMHk8nEY489RmBgII0aNcoz/CQ/ucl3r169%2BPbbb0lJSaFOnTpkZmZy7NgxABo3bszChQspU6aM1bqzZs1i0aJFAJQrVw4vLy9iY2OJi4sD4JlnnuHFF1%2B0WufEiRMMGjSIs2fP4uDgQLVq1XBxceH06dNcuHABgBo1ahAWFmaVnOYm340aNSIiIgJvb2/Onz9P06ZNeeedd6z24%2BuvvyYzM5NatWqRkJBgac%2Bzzz6LyWRi4cKFlC1blqpVq3L8%2BHFSUlIwmUx89NFHtG7d2rLN8%2BfP89RTT3HkyBFMJhPVqlWjTJkyxMTEWGK6ubmxbt06PD09LevlJt%2BDBw9m%2BfLlODk5Ub16dS5evMi5c%2BcA8PHx4ZNPPrHpPRIRAcAsIiLFwv79%2B80NGzY0e3t7W34aNWpkHjp0qHnhwoXmvXv3mrOysvJdd/z48ZZ12rVrZz5w4IBl3p49e8zNmzc3e3t7mydOnGi13qeffmr29vY2%2B/r6mr/44gvL9OzsbPNXX31lac%2BaNWus1nvyySfN3t7e5j59%2BphjYmKs1lu/fr25Xr16Zm9vb/OqVaus1stt4wMPPGAODw83m81mc1ZWljkxMTHPfvTt29ccGxtrWWbChAlmb29vc7169cx169Y1L1myxNIf58%2BfN/fo0cPs7e1tfvLJJ/Ptm4cffth8/Phxq3k7duwwP/TQQ2Zvb29zSEiI1bx27dpZ2jJhwgRzUlKSZR9XrVplmffdd9/l%2B56IiORHY75FRIqJ%2B%2B%2B/n88//5zGjRtbpiUnJ7N9%2B3beeecd%2BvTpQ8uWLZkzZw5XrlzJN4adnR3z58/nvvvus0zz8fFh5syZAHz%2B%2BefExMQAkJ6ezty5cwGYPn063bt3t6xjMpno0qWLpeI9d%2B5cMjMzAUhISODo0aMAvPnmm3h4eFit16NHD/z8/AA4fPhwvu3s3LkzTZo0sbTZ1dXVar6DgwOzZ8/G3d3dssyzzz4LQHZ2No899hhDhgzBzi7nz1j58uUZOHAgAAcOHLDEyczM5Ndff8VkMvHyyy9TvXp1q%2B20atWKLl26AHDkyJF821qvXj2mT59u%2BcbAZDLRv39/SxX/t99%2By3c9EZH8KPkWESlGateuzerVq9mwYQMjR47Ex8cHR0dHy/yEhAQ%2B/PBDunfvbhn6cDV/f3/q1auXZ3rLli3x8vIiOzubrVu3AhAREUF8fDylSpWiffv2%2Bbane/fu2NnZERMTY0lq3dzc2LVrF/v27cPb2zvPOllZWZQuXRrIGWudn6tPMPJTt25dqyEgAFWqVLH8O79x3bknAcnJyZZpDg4ObNmyhX379tG2bds865jNZkqWLHnDtrZt2xaTyZRnes2aNQG4dOnSDfdFRORquuBSRKQYuu%2B%2B%2B7jvvvsIDg7mypUr7Nmzh507d/LFF1%2BQkJBAVFQUo0ePJjQ01Gq9Bx988Lox69aty6lTpzhx4gSApXqdkZFB//79r7uevb092dnZHDt2zCq%2Bs7MzZ8%2BeZd%2B%2BfURFRREdHU1kZCQHDx4kJSUFyKlS5ye3on0999xzT55pTk5Oln%2BXL18%2Bz/yrL1q9VokSJUhISGDv3r2cOHGCU6dOcezYMQ4ePMjFixdv2NarK/tXy33KaFZW1vV3RETkGkq%2BRUSKORcXF1q0aEGLFi0YPXo0r7zyCl999RV79%2B5l//79Vk%2B6vPbuIlfLrfAmJSUB/6vYpqens2fPnpu2I3c9gGPHjvHWW2%2Bxfft2q6S1dOnS%2BPr6Ehsby6FDh64bKzdxvR4XF5cbzs8dbmKLuLg4Zs6cyTfffENGRobVNho0aEBWVtYNh45cnfTnx6z7FojILVDyLSJSDEyaNIldu3bRs2dPhg8fft3lnJ2dmTJlCps3byYjI4Pjx49bJd%2B5Fef85A7HyL1FYW6CW79%2BfdatW2dzWxMSEnjyySdJSEigcuXK9OnTh/vvv5%2BaNWvi5eWFyWRi7NixN0y%2Bi0paWhpPPfUUkZGRuLq60rdvXx544AFq1apFtWrVsLe3Z86cORq3LSJFRsm3iEgxkJaWxsmTJ9myZcsNk2/IqS6XKlWKCxcu5Hm8fO5QkvzkJsO1a9cGcm4FCDm3DczMzMx32IbZbGb37t14enpSuXJlnJycCAsLIyEhAVdXV8LCwvJ9xH3uRZ2325YtW4iMjMTBwYHQ0NA8F1wC%2BY6dFxEpLLrgUkSkGMi908iff/550yr0zp07uXDhAq6urnmehrljxw7LvauvtnXrVs6ePYuTkxMBAQEANGnShDJlynD58uXrbnPjxo089dRTdO7c2ZKknjp1CoDKlSvnm3j/9ddf7N27F7j946Fz21qqVKl8E%2B/4%2BHi2bdsG3P62isi/g5JvEZFioEWLFnTs2BGA1157jWnTplkSx1xpaWmEhYXxwgsvADB69Og8T1dMSUlhxIgRnD171jJt9%2B7dvPzyy0DOA2pyb5lXsmRJy%2B37pk2bRlhYmNX47S1btvD6668DObcGrFatGvC/u3wcOnSIb7/91rK82Wxmx44dPPPMM5ax1de7JWJRyW3rxYsXWbFihdX47L179zJ48GDLQ4Fud1tF5N9Bw05ERIqJWbNmUbJkSTZs2MDKlStZuXIllStXxs3NjbS0NE6cOEF6ejqOjo6MHTuWfv365YlRvXp1Dh48SIcOHfD29iYlJcVyd5OuXbvy3HPPWS0/dOhQoqOjWbNmDa%2B88gpvv/02Xl5exMTEEBsbC%2BQ8jXLq1KmWdQIDA1m9ejUnT55k1KhRVKlShfLly3P27FkSEhJwdHTEz8%2BP8PDw2z78JCAgAB8fHyIiIpg%2BfTqLFi2iUqVKxMXFERMTg8lkonnz5vz000/ExsZiNpvzva2giIhRlHyLiBQTTk5OhISE0L9/fzZt2sTu3buJiYnh0KFDuLi4UKNGDVq2bElgYKClonutBg0aMGvWLN5//31%2B%2B%2B03HBwc8PPzo2/fvpaHyVzNZDLx5ptv0rFjRz777DP27t3LwYMHKVGiBA0bNqRr164EBQVZ3fGjdOnSrF27lkWLFrF161ZOnTpFfHw8np6etG3blqeeeoqSJUvSoUMHDh06xJkzZ6hcuXKh9duN2Nvbs3z5cj7%2B%2BGO%2B%2BuoroqOjOXLkCO7u7nTp0oX%2B/ftTv359mjZtyoULF9izZ89N70EuIlIQJrPukSQicsebMGEC69evp1u3bsyaNet2N0dERK5DY75FRERERIqIkm8RERERkSKi5FtEREREpIgo%2BRYRERGRu8L58%2Bd5%2BOGH2b1793WX2b59O926daNhw4Z07tyZrVu3Ws1ftGgRrVu3pmHDhgwYMIBjx44Z2kYl3yIid4GQkBAOHz6siy1F5F/rt99%2BIygoiKioqOsuc%2BLECYKDgxk9ejS//vorwcHBvPDCC5bboq5fv56PP/6YJUuWsHv3burXr8%2BoUaMw8v4kSr5FRERE5LaKjY1l//79Vj%2B5zxqwxfr16xk3bhxjxoy56XK%2Bvr506NABBwcHunTpQpMmTQgNDQVgzZo19OvXjzp16lCiRAnGjh3LmTNnblhJv1W6z7fIjRj9sI0aNeDoUahTB44fNyxszDnj7xhqbw9ubpCQAEY%2BdbvSd6uMCwZQujR07w5ffgnJycbFbdbMuFgADg5QrRpERUFmpqGh07xqGRoPwMkJ0tONjVni2EFjAzo6Qq1aEBkJfz9R0wiJnvcZFgvAzg7KloWkJLjqAaKGKP/Np8YGLFUKunaF//wHLl82LGxip76GxYJC7lPXO%2BQOzLfzYVCFsO3Q999n3rx5VtNGjhxJcHCwTeu3bNmSbt264eDgcMME/K%2B//sLb29tqWu3atTl06JBl/tChQy3zHB0dqV69OocOHcLf39/W3bkhJd8iRcnVNSerdXW93S25KZPpfz/FmpNTzl/iqx4CUyzZ2eV0pl3x/8Lx6ve%2BWD8Jwt4%2Bp5H29oYm30a7Y44lsD6eDEy%2BjXZH9WmxP5CKh6CgIAICAqymubu727y%2BrctevnwZFxcXq2nOzs6kpKTYNN8ISr5FRERE5Lby8PDAw8Oj0Lfj4uJCamqq1bTU1FRKlSpl03wjFP8SjIiIiIgUH3Z2xv8UEW9vb44ePWo17a%2B//qJOnToA1KlTx2p%2BRkYGJ06cyDNUpSCUfIuIiIiI7e7g5Lt79%2B6Eh4ezadMmMjMz2bRpE%2BHh4Tz22GMA9O7dm1WrVnHo0CHS0tJ45513qFixIr6%2Bvoa1Qcm3iIiIiNy1fHx8%2BPLLLwGoVasWH3zwAQsXLqRJkybMnz%2BfuXPnUqNGDQACAwMZNGgQzz//PP7%2B/hw4cICFCxfi6OhoWHs05ltEREREbFfMLxw/fPiw1e8RERFWv7dq1YpWrVrlu67JZGLIkCEMGTKk0NpXvHtPREREROQuosq3iIiIiNiumFe%2Bizsl3yIiIiJiOyXfBaLeExEREREpIqp8i4iIiIjtVPkuECXfIiIiImI7Jd8Fot4TERERESkiqnyLiIiIiO1U%2BS4Q9Z6IiIiISBFR5VtEREREbKfKd4Go926zEydO3O4m3JWysrKIjo6%2B3c0QERG5%2B9jZGf/zL3LX7u3x48cZP348rVu3xsfHhw4dOjBr1iwuX758u5tmceDAAbp27Xrd%2BRMmTGDChAlF2KKb27ZtG3Xr1mXq1Km3uyk3NGbMGDZs2HC7myEiIiJi5a5Mvvfs2UPPnj2pUqUKGzZsICIigkWLFrFv3z6GDBlCVlbW7W4iAJcuXSIjI%2BN2N%2BOWrFq1ir59%2BxIWFsbFixdvd3OuKzEx8XY3QURE5O6kyneB3JV7O2nSJHr06MGoUaOoUKECADVq1GDOnDm4ublZhiPUrVuX3bt3W9Zbt24dAQEBAOzevZs2bdowduxYfH19%2Beijj5gwYQKjRo2ic%2BfO%2BPv7ExUVRXx8POPGjaNFixa0bNmSSZMmkZycbIkREBDAggULaNWqFX5%2BfgQHB5OcnEx0dDRDhw4FwMfHh4iIiFvez8OHDzN06FD8/Pxo3bo1kydP5tKlSwCYzWY%2B%2BugjunXrhq%2BvL02aNGHs2LGkpqYCOVX1SZMmMWzYMHx8fGjfvj0rV6684fZOnjzJrl27GDlyJHXr1iU0NNRq/oABA3j//ffp27cvDRs2pHv37vz%2B%2B%2B%2BMHTuWRo0aERAQwLZt2yzL//rrr/Tv3x9fX18CAgJ49913SU9PB2Du3LkMGDDAKn5AQADr1q2zbOudd96hf//%2B%2BPj40LlzZzZt2gTAq6%2B%2Byq%2B//srChQsZNmzYLferiIiISGG56y64jIqK4ujRo0yePDnPvIoVKzJ//nybY507d46aNWsSEhJCWloaU6dO5YcffiA0NBRPT09Kly7NE088QfXq1fn222/JyMjg5ZdfZtKkScyePRuA06dPExMTw3fffUdMTAz9%2B/dn9erVPPvssyxatIiBAwf%2Bo8Q7MTGRgQMH0qtXL%2BbOnculS5cYN24cL730EgsWLODrr79m5cqVrFq1iurVqxMZGUm/fv3YuHEjjz/%2BOJBzsrFw4ULmzZvH2rVrmTJlCh07dqRSpUr5bnPVqlU88sgjVKxYkQEDBhASEsKgQYNwcnKyLBMaGsqKFSuoVq0aQ4YMoV%2B/frz77ruEhIQwe/Zs3nzzTdq2bcuxY8cYPHgw48aNY9myZZw9e9ZyYvLaa6/Z1Adr1qxh2bJl1K5dmw8%2B%2BIBJkybRvn17pk2bRlRUlOVkx1axsbHExcVZTXOvUQMPV1ebY9xUvXrWrwZxKIQj2d7e%2BtUwf58QG6ZsWetXo1z1uTaEo6P1q4FMpsKJZ3RcnJ2NjZf7Hhn8Xhn9mc8t6hVKca98eWPjFdLxdEf1qdycOr5A7rrk%2B/z580BOom2EwMBAHB0dcfz7D2bDhg3x9vYG4Pfff2f//v0sW7aMUqVKATB%2B/Hg6derExIkTLTGef/55nJ2duffee2natCnHjx8vcLv%2B%2B9//4ujoyLhx47C3t8fZ2ZmJEyfy6KOPEhcXR%2BvWrWnUqBGenp6cP3%2BexMREXF1diYmJscRo2rQpLVq0AKB37968/vrrREVF5Zt8p6SksH79epYsWQJAx44deeutt/jqq6/o2bOnZbmOHTtSu3ZtAHx9fUlKSqJDhw4AtG7dmmXLlgGwceNG6taty1NPPQXAvffey9ixYxk1ahSvvPKKTX3QsWNH7r//fgB69uzJhx9%2BSEJCApUrV76lvswVGhrKvHnzrKaNHD2a4NGj/1G8G1q92tBwboZGs2bkuQcAXboYHPBvLVsWTlyjeXoaHtLg0wQLw88TatQwOODfqlQxNJzBp3EWpUsXQtBOnQohKNC8uaHh7qg%2BxeizTgrhTPY2U/JdIHdd8u3u7g5AXFwc1atXzzM/Pj7%2BlhJzDw%2BP6/5%2B6tQpsrKyaNOmjdUyTk5OVnfayG0TgKOjI2az2ebtX09ukml/VTnBy8sLyKm216pVizlz5rB161YqVKjAfffdR0ZGhtW2r20XQHZ2dr7b27BhA5cuXeLZZ5%2B1TLt8%2BTJLly61Sr5dr8rU7O3tKVeunOV3Ozs7y/YTEhKoWrWq1Ta8vLxITU0lISHBpj64uv0Of5d%2Br9d%2BWwQFBVmGHVm20a0brFjxj2PmUa9eTuLdrx8cOmRY2ITv9hgWK5e9fU7ifeECGHmZhNvuTcYFg5wKXcuWsHMnJCUZF7dBA%2BNiQU4m6%2BkJ586Bwdd6pFeqevOFboHJlNPcjAww4L8rC6fTBS88WAd0ykm8T5%2BGv4esGSHJzdiTBDu7nCQxORkK8F9Uvsr%2B9I3BAcvmJN4//WTo8ZTU3NiThELt0zIGfugh54Ay8kC6Oq7cke665LtKlSp4e3uzadMmmjRpYjUvISGBdu3aMWPGDLp27YqdnZ3VBY/5XaRnuubDffXvnp6eODs7s3v3bksSnJ6eTnR0NPfeey%2B//fabkbtmpUqVKpw5c4asrCzLtqOiooCcpHTWrFmcOXOG77//ntJ/lwa6dev2j7e3evVqRo8eTa9evSzTEhMT6d27Nzt37qTl31XHa/vrRu3fvHmz1bSoqCicnJwoV65cnvcmOzubCxcu/OP228LDwyPPyRYGfEuRr0OH4B8MN7qezEzDQuWRlWVw/L%2B/nTJcUpKxsQ1M5qxkZBgeuzD%2BrufGNTT239ecGC493dDYhXVNfnZ2IcQurIvLk5IMjX1H9ancnCrfBXJX9t7EiRMJCwtj3rx5JCYmYjabOXjwIMOGDaN%2B/fp07NgRgFq1avHtt9%2BSmZlJVFQUa9euvaXtPPjgg9x7772EhIRw%2BfJlUlNTmT59OoMGDbLpjiolSpQAsFwkmZ8rV65w7tw5q5/k5GRLtX3WrFmkpqYSFxfHtGnT8Pf3p0qVKiQnJ1OiRAns7e1JS0tj6dKlHDly5B/dXeXnn3/mxIkTBAUF4enpafm57777aN26NUuXLr3lmI8%2B%2BiiRkZGsWLGC9PR0oqKimD17Nt26dcPJyYlatWpx%2BPBhjh49SmZmJosXLyYlJcXm%2BE5OTjfsVxEREZHb4a5Mvv38/Fi1ahUHDhzg0UcfpVGjRowaNQp/f38WL15sGWLx%2Buuvs3//fvz8/HjhhRcIDAy8pe04ODiwcOFC4uPjeeSRR2jZsiVRUVEsW7bMkljfiLe3N40bN6ZVq1Zs374932W%2B%2BeYb2rRpY/Xz4YcfUqZMGZYtW8aRI0do06YNXbt2pUqVKrz33nsAvPDCC6SmptK8eXMCAgLYu3cvjz32GEeOHLmlfQT45JNPaN26NW5ueUcWP/HEE/z4448cusUhFF5eXixevJhvv/2W5s2b069fP1q0aMGkSZMA6NChA926dWPQoEG0atWKxMREGjdubHP8Hj16EBYWRr9%2B/W6pXSIiInITutVggZjMRgxAFrlbGT2mzscH9uyBRo0MHXYSc874w9jBAdzcICHB2GEnlb5bZVwwyLl7SpcusGmTscNOmjUzLhbkjE%2BuWhWiow0fdpLmVcvQeCZTTnPT040ddlLi2EHjgkHO3VNq1MgZHmbgsJNEz/sMiwU510%2BULZszksPoIRLlv/nU4IDlcy7i/OYbQ4edJHbqa1gsKOQ%2BddWY75sqjIunC2uYZzH07zrVEBERERG5je66Cy5FREREpBD9y4aJGE29JyIiIiJSRFT5FhERERHbqfJdIEq%2BRURERMR2Sr4LRL0nIiIiIlJEVPkWEREREdup8l0g6j0RERERkSKiyreIiIiI2E6V7wJR8i0iIiIitlPyXSDqPRERERGRIqLKt4iIiIjYTpXvAlHviYiIiIgUEVW%2BRURERMR2qnwXiMlsNptvdyNEiquYGGPjOTiAmxskJEBmpnFxK3majAuWy8cH9uyBRo0gIsK4uKmpxsUCMJnAyQnS08HI/84uXDAuFhTemw9Qtqyx8UwmcHbOea8M7NMsJxfDYuWyt4esLGNjnj9vbDwHByhfHhITjX/rK1QwNh4UTp8mJRkbz94%2B52OflGR8W52djYtVSIcSAC7GH062a9zY%2BJi//WZ8zGJKpy4iIiIiIkVEw05ERERExHYadlIg6j0RERERkSKiyreIiIiI2E6V7wJR8i0iIiIitlPyXSDqPRERERGRIqLKt4iIiIjYTpXvAlHyLSIiIiJ3tISEBCZOnEh4eDj29vZ0796d8ePH4%2BBgneo%2B88wz/HbNPcVTUlIICgpiypQpxMfH06JFC0qWLGmZX758eb7//nvD2qrkW0RERERsVwwr3y%2B88AKVKlXihx9%2BID4%2BnuHDh7N8%2BXKeeeYZq%2BUWL15s9fvatWuZN28eI0eOBOCPP/6gSpUqhibb11LyLSIiIiK2K4TkOzY2lri4OKtp7u7ueHh43HTdkydPEh4ezo4dO3BxcaFq1aqMGDGCt99%2BO0/yfbVjx47x5ptvsmTJEst2/vjjDx544IGC7cxNKPkWERERkdsqNDSUefPmWU0bOXIkwcHBN1336NGjuLq6UqlSJcu0WrVqcebMGZKSkihbtmy%2B673xxhv06NEDX19fy7Q//viDixcv0rVrV%2BLj42nQoAHjx4%2Bndu3a/3DP8lLyLSIiIiK2K4TKd1BQEAEBAVbT3N3dbVr38uXLuLi4WE3L/T0lJSXf5PvXX39l3759zJo1y2p62bJlqV27NkOHDsXJyYn33nuPwYMHs2nTJsqUKXMru3RdSr5FRERE5Lby8PCwaYhJfkqWLMmVK1espuX%2BXqpUqXzXCQ0NpXPnznkS/Hfeecfq95dffpmwsDB%2B/fVX2rVr94/ad63iN2JeRERERIovOzvjfwqgTp06XLhwgfj4eMu0yMhIPD09861WZ2Zm8t///pfu3btbTU9OTmbmzJmcPn3aMi0rK4vMzEycnZ0L1MarKfkWEREREdsVs%2BS7evXqNG7cmOnTp5OcnEx0dDTz588nMDAw3%2BUPHz5MWloajRo1sppeunRpfvrpJ2bOnMmlS5e4fPkyb775Jl5eXlbjwgtKybeIiIiI3NHef/99MjMzad%2B%2BPX369KFVq1aMGDECAB8fH7788kvLstHR0ZQrV44SJUrkiTN//nyys7Pp0KEDrVq1Ii4ujkWLFuHo6GhYWzXmW/6xEydOUL169dvdDBERESlKxfA%2B3xUrVuT999/Pd15ERITV7506daJTp075LlulSpU8d10xWvHrPbHJ8ePHGT9%2BPK1bt8bHx4cOHTowa9YsLl%2B%2BbOh26taty%2B7duwF49NFHLWeOn3zyCRMnTrzueunp6bzzzjt06NABHx8f/P39CQ4OJjIy0tD2iYiISBErZsNO7jT/rr29S%2BzZs4eePXtSpUoVNmzYQEREBIsWLWLfvn0MGTKErKysQtnuV199Zbk44fz58zdc9s033yQiIoLly5cTERHB5s2b8fT0pH///iQlJRVK%2B0RERESKOyXfd6BJkybRo0cPRo0aRYUKFQCoUaMGc%2BbMwc3NjejoaCCbtQNgAAAgAElEQVSnaj116lSaNm3KsGHDAPjpp58IDAzE19fXqpINkJGRwYwZM2jatCn%2B/v55HsEaEBDAunXrWL9%2BPQsXLuTXX3%2B97gUIv/32G61atcLLywvIuW/mSy%2B9RLt27SxPsEpJSWHKlCk0a9YMX19fhg4darnCODExkYkTJ9KyZUuaNm3Kc889x4kTJwA4deoUdevWJSQkhCZNmvDGG28AOScH3bp1o3HjxvTq1YudO3ca0d0iIiJyNVW%2BC0Rjvu8wUVFRHD16lMmTJ%2BeZV7FiRebPn59n%2BW3btpGRkcGhQ4cYPnw4b7/9Nu3bt2ffvn2MGDGC8uXL06pVK%2BbPn8%2B2bdtYu3Ytbm5u%2BW4DoGfPnpw6dYrw8HA%2B/vjjfJd59NFHmTdvHsePH8ff35%2BHHnqIGjVqMGPGDMsyU6ZMITIyknXr1uHm5sbrr7/O//3f/xEaGsqoUaOws7Nj/fr1lClThvfee49Bgwbxn//8x7L%2B5cuX%2BfHHH0lNTWX79u28/vrrLFiwgEaNGrFjxw6Cg4NZs2YNderUsalv83u0rb29O%2B7u/%2By%2Bo/mxt7d%2BNYyPj8EBgXr1rF%2BNYjIVTjyj4zoY/N9job353Dl9eoe4k976O4XR%2B56bqxVGzmbkx/5ffijJdSj5vsPkDveoWLGiTct37doVFxcXXFxcmD17Nu3bt%2BeRRx4BoFGjRvTp04dPPvmEVq1a8cUXXzBs2DCqVq0KwGuvvWZVGb8Vzz//PPfddx8bNmxg5syZnD9/Hg8PD55%2B%2BmkGDRpEeno6X331FQsWLOCee%2B4Bcm5kf/LkSaKjowkPD%2Berr76y3Px%2B3LhxbNy4ke3bt/PQQw8B0KNHD5ycnHBycmLVqlX07duXJk2aANCuXTsCAgL47LPPbjg2/Wr5Pdr2%2BedHMmrUzR9te6tcXQ0OuGePwQGvsnp14cU2koFXogPg5mZsvFyGv/mFKJ87ARREYeWeRid25csbGy/XdZ5wXSwZ3aeFte%2BlSxdOXKMZfCjdfv%2BySrXRlHzfYXKT0bi4uHzvNBIfH2%2BVmF/9tKjTp0%2Bza9cuq6EiWVlZVKtWDcip/OYmwpAzVKRcuXL/uK0BAQGWR8VGRUWxefNmZs2aRalSpWjbti3p6elUrlzZansNGjSwXJWcexIAYG9vzz333MPp06ctyfe1%2BxYeHs6nn35qtW/%2B/v42tze/R9va27uTkHALO30T9vY5udeFC2Dk0Hy3hxvdfKFbVa9eTuLdrx8cOmRc3F27jIsFOSUlR0fIyACz2bi4ly4ZFwsK780HuM4T3P4xkyknW0hLM7RPsxyNe0hFLnt747vT6MtS7O1zks%2BkJOPbWhhJbWH0qcH3AsDOLifxTk6G7GxjYzs5GRerkA4lAAx85sutU/JdIEq%2B7zBVqlTB29ubTZs2Waq8uRISEmjXrh0zZsyga9euAJiu%2Bq7L09OTnj17MmXKFMu02NhYzH//j%2BDp6WkZLw45Y7Iv/YMEJDIykh49ehAWFoa3tzcA1apV45lnnmHfvn0cPHiQ3r174%2BTkxNmzZ6lZs6al/YsWLWLIkCFATsKeO2QkKyuLM2fOWD0G9tp969GjB88%2B%2B6xl2pkzZ27piVT5Pdo2JgYyM2%2BxA2yQlWVw3Gtuo2SoQ4eMjW/0X6Cr4xoZuzDeeCiEN587p0/vEHfSW3%2BnKKT7AJCdbXzswvjI/0sPJbkOnbrcgSZOnEhYWBjz5s0jMTERs9nMwYMHGTZsGPXr16djx475rhcYGMh//vMfdu7cSXZ2NidOnODJJ59k6dKlADz%2B%2BOMsXryYyMhI0tLSCAkJue6dU0qUKEFycrIlcb9azZo1qV%2B/PpMmTeL3338nLS2NK1eusH37dnbv3s3DDz%2BMnZ0dPXr0YO7cucTExJCWlsa7777L3r178fDwoE2bNkydOpW4uDhSU1OZNWsWWVlZtGvXLt/29OnTh5UrV/L7778D8Mcff9CrVy%2BrMeIiIiJiAF1wWSCqfN%2BB/Pz8WLVqFR9%2B%2BCGPPvooV65coWLFinTq1Innnnvuuk9heuihh5g9ezazZ89m9OjRuLi40LVrV/7v//4PgKFDh3LlyhWefPJJMjMz6dOnD67XGZ/arl07Pv30Uxo3bsy2bdsoe9V3nyaTiUWLFjF//nxefPFFYmJisLOz47777uPtt9%2BmWbNmAEyYMIE5c%2Bbw%2BOOPk5qaip%2BfH%2B%2B99x4Ab731FrNmzaJnz56kpKTQsGFDVqxYgaurK8nJyXna06lTJ1JSUnjllVc4c%2BYMrq6uDBo0iAEDBhSor0VERESMZDLnV7oUESBn2ImRHBxyruNLSDD26%2BdKnoVwKb2PT86FnI0aGTvsJDXVuFiQM6jSyQnS0439XvfCBeNiQeG9%2BWD8wF%2BTKWdAaWqqsWO%2BnVwMi5WrMMYn3%2BQxBrfMwSHnIs7EROPf%2Br/vNmuof/s4eiPHUhfSoQSAi/GHk%2B169zY%2BZliY8TGLKVW%2BRURERMR2/7JhIkZT74mIiIiIFBFVvkVERETEdqp8F4h6T0RERESkiKjyLSIiIiK2U%2BW7QJR8i4iIiIjtlHwXiHpPRERERKSIqPItIiIiIrZT5btA1HsiIiIiIkVElW8RERERsZ0q3wWi5FtEREREbKfku0DUeyIiIiIiRUSVbxERERGxnSrfBaLeExEREREpIqp8i4iIiIjtVPkuECXfIjdQ6btVxgasUAG6dMFt9yY4f964uKmpxsXKZTLlvO7aBWazcXGdnY2LBeDjA3v2gL8/REQYF/f7742LBVC6NLi5wbFjkJxsaOi4B9oZGs/BAco7Q%2BIVZzIzjYvrfmC7ccEgp08bN8Z%2B72%2BG9mlpvzaGxYL/HUouLsYeSgD2y5cYG9DNDXr0wH7jBkhIMCysXeDThsWC//WpyWR8HuiSfdm4YHZ2gAvO5iuQnW1cXABKGRzvFij5LhD1noiIiIhIEVHlW0RERERsp8p3gaj3RERERESKiCrfIiIiImI7Vb4LRMm3iIiIiNhOyXeBqPdERERERIqIKt8iIiIiYjtVvgtEvSciIiIiUkRU%2BRYRERER26nyXSBKvkVERETEdkq%2BC0S9JyIiIiJSRFT5FhERERHbqfJdIOo9EREREZEiosq3iIiIiNhOle8CUfItIiIiIrZT8l0g6j0RERERkSKiyreIiIiI2E6V7wJR7xUDn3zyCXXr1mX58uW3uykWAQEBrFu3Lt95c%2BfOZcCAAUXcIhERESkW7OyM/ymghIQERowYga%2BvL02bNmXatGlkZmbmu%2BwzzzxDgwYN8PHxsfzs2LEDgKysLGbOnEnz5s3x8fFh%2BPDhxMbGFrh9V1PyXQx88skn9O3bl5UrV173gyIiIiIi%2BXvhhRcoWbIkP/zwA2vXruXnn3%2B%2BblHzzz//ZMmSJURERFh%2BWrduDcCCBQv48ccfCQsL44cffsDZ2ZnXXnvN0LZq2Mlt9vPPP5OQkMCECRPYtm0b3377LY8%2B%2BiiQU30OCgri66%2B/5uTJk9x7771MmDABf39/Tp06Rfv27Zk6dSoLFizg4sWLPPjgg8yYMQNPT0/WrVvHvHnz%2BP777y3bGjBgAH5%2BfgQHB5OcnExISAjh4eHExsZSpkwZ%2Bvfvz7Bhw26p/TdrB8DGjRtZuHAhp0%2BfxtPTk%2BDgYLp06QLA559/zvLlyzl79ixVqlRh6NChdO/e3dLeJk2a8PPPP3Pw4EGqVavG1KlTWbFiBVu3bsXV1ZVJkybRtm1bAPbv309ISAiHDh2ifPny9OvXj6eeegqTyWTTvsTGxhIXF2c1zT07G4%2BKFW%2BpT26obFnrV6PYuI//KKbRsX18jI1Xr571q1FKlzY2XsmS1q8GcjD4f3J7e%2BtXwxjdpy4u1q8GMfojX1iHEgBubsbGK1fO%2BtUgRo9SyI1XKKMfjAx69Zt/Nw3VKIR9yfdvsLs7Hh4eN1335MmThIeHs2PHDlxcXKhatSojRozg7bff5plnnrFaNjo6mosXL3L//ffnG%2Bvzzz9n3Lhx3HPPPQC8%2BuqrtGzZkujoaKpWrfoP986aku/b7OOPP6ZPnz44OzvTr18/li5dakm%2BAcLCwli0aBEeHh688cYbTJ48mW%2B%2B%2BcYyf9u2bWzYsIH09HQGDx7M/PnzmTJlyk23O2vWLE6dOsXatWspU6YMmzdvZtSoUXTu3Jl77733lvfjeu3YvXs3r7zyCvPmzaNVq1bs3LmTESNG4O3tze%2B//05ISAjz5s3Dz8%2BP8PBwRo4ciYuLCw8//DAAoaGhrFixgmrVqjFkyBD69evHu%2B%2B%2BS0hICLNnz%2BbNN9%2Bkbdu2xMTE8NRTTzFmzBiWLl3KyZMnGTFiBM7OzjzxxBM27UNoaCjz5s2zmjby%2BecJHjjwlvvjplq2ND5mYXF0NDbenj3Gxsu1enXhxDVa/fqGhyxveMQcRp8j0rixwQH/dp0/ov%2BUs6HR/qdEiUII2qNHIQQF2rUzNFwZQ6P9T6lShRHV2JM5AJwL61N198j3b/DIkQQHB9903aNHj%2BLq6kqlSpUs02rVqsWZM2dISkqi7FX/mf3xxx%2BUKlWKMWPG8Mcff1CxYkUGDRpEYGAgly5d4ty5c3h7e1uWr1ixIuXKlePw4cNKvu8Gp0%2Bf5ocffmDSpEkA9OnThw8%2B%2BIDw8HD8/PwACAwMtCTD3bp1Y8OGDVYxhg4davlQBQQEEBERYdO2g4ODsbe3p3Tp0pw7d44Sf/9ViI2N/UfJ9/XasWHDBh555BHatGkDQOvWrVm9ejWVKlUiLCyMoKAgmjVrBkCzZs0ICgris88%2BsyTfHTt2pHbt2gD4%2BvqSlJREhw4dLLGWLVsGwJdffkmtWrXo378/ALVr1%2Bbpp59m1apVNiffQUFBBAQEWE1z/%2B032LTplvvjusqWzUm8d%2B6EpCTj4v7dJ4YymXIS74wMMJuNi%2Bvvb1wsyKl4r14N/frBoUPGxV240LhYkFPxrl8f9u%2BHlBRDQyfWbmJoPHv7nI9qUhJkZRkXt/yx34wLBjkV7/vvhwMH4MoVw8Km1jf2JMFkykm809KMPZQAnL/ZcPOFbkW5cjmJ99atcPGiYWEvtTf2JMHOLifxvnwZsrMNDU0ZB%2BM%2BS5hMOYl3aqrxb77B3/jckkKofOf7N9jd3aZ1L1%2B%2BjMs1/ZH7e0pKilXynZ6eTsOGDRkzZgx16tRh9%2B7dBAcHU6pUKXz%2B/ma25DXfUDo7O3P58uVb3qfrUfJ9G61evZrMzEwee%2Bwxy7TMzEyWLl1qSb4rXjXkwcHBAfM1B%2B/N5l9PQkIC06ZN48CBA3h5efHAAw8AkP0P/xe7XjtiY2PzfLXz4IMPAhAfH5/nLNLLy8tqqIyrq6vl3/b29pS76qtQOzs7y3ZOnz7N/v378fX1tczPzs7G/ha%2BN/fw8Mj79VZEBJw/b3MMmyUlGRvX6P/Ur41tZHwbTxBv2aFDxsZOTjYu1tVSUgyPXViXimRlGRy7sPr0yhVDYxfW4WT0oQRAQoLBAf928aKhsY1OkK%2BOa3hsIwPmJqlmc%2BF1wu1QCMl3vn%2BDbVSyZEmuXHMCnvt7qWu%2BHunRowc9rvrGqGXLlvTo0YOvv/6a5s2bW62bKzU1NU%2BcglDyfZukpaWxdu1apk2bZnmzAY4cOcKzzz5LZGRkgeLb2dmRnp5uNS0xMdHy79GjRxMQEMCSJUtwcHAgMTGRNWvWFGib%2Bbnnnns4c%2BaM1bSlS5fSsGFDvLy8iIqKspoXHR1tdaZr63htT09PmjZtypIlSyzTEhMTDT1TFRERkeKnTp06XLhwgfj4eEsxMDIyEk9PT8qUsR70tHbtWkqVKkXnzp0t09LT0ylRogTlypWjUqVK/PXXX5ahJ3FxcVy4cMFqKEpB3UWj/%2B8sGzduxGQy0a1bNzw9PS0/rVu3xtvbu8C3HaxVqxbx8fHs2rULs9nMF198YZXQX7p0CWdnZ%2Bzt7Tl//jxTp04FICMjo0DbvVbPnj357rvv2LlzJ9nZ2fzwww/MnTuXMmXKEBgYSGhoKD///DNZWVns2rWL0NBQevfufcvb6datG3v37uXLL78kMzOT2NhYhg0bRkhIiKH7IyIi8q9XzG41WL16dRo3bsz06dNJTk4mOjqa%2BfPnExgYmGfZ5ORk3nzzTQ4cOEB2djbbtm3jP//5D0FBQQD06tWLBQsWEB0dTXJyMtOnT8fPz49q1aoVqI1XU%2BX7Nlm9ejXdunXDMZ%2BL2YKCgpg5c6bNVd/8NGjQgOHDhzNhwgQuX75Mhw4d6Nixo2X%2BjBkzmD59OkuXLqVcuXJ06dKF%2B%2B%2B/nyNHjtDSwIsBGzduzMyZM5k5cyanT5%2BmSpUqzJ49mzp16lCnTh2Sk5OZOnUqZ86coVKlSrz00ktWXwfZqkqVKixevJhZs2YxdepU7O3tadu2La%2B%2B%2Bqph%2ByIiIiLF0/vvv8%2BUKVNo3749dnZ29OjRgxEjRgDg4%2BPDG2%2B8Qffu3XnqqadISUlh5MiRJCQkULVqVWbOnGkZtvr888%2BTmZlJ//79uXz5Mk2bNuXdd981tK0ms62DhEX%2BjVatMjZehQrQpUvORZxGjvl%2B/HHjYuUymcDJCdLTjR2oavRV/z4%2BOXdQadTI2DHfV117YIjSpaFJE/jlF8PHPsc9YOydKRwcoHx5SEw0dsy3%2B4HtxgWDnD5t3Bh%2B%2B83QPr3i18awWFDI19ytXnLzhW6Fm1vOHVQ2bDB0zPfFwKcNiwU5hdIyZeDSJeOHUpdzMHC4op1dzoWRV64Y39DCudWLbWbMMD7myy8bH7OYUuVbRERERGx3N92z/DZQ74mIiIiIFBFVvkVERETEdqp8F4h6T0RERESkiKjyLSIiIiK2U%2BW7QJR8i4iIiIjtlHwXiHpPRERERKSIqPItIiIiIrZT5btA1HsiIiIiIkVElW8RERERsZ0q3wWi5FtEREREbKfku0DUeyIiIiIiRUSVbxERERGxnSrfBaLeExEREREpIqp8i9xIs2bGxnNyynlt0ADS042Le%2BGCcbFyOTiAmxtcugSZmcbF/f5742IBlC6d87pwISQnGxc3IMC4WAA%2BPrBnDzz3HEREGBra5ZLZ0Hi5Ra0SJcDR0cDAlSsbGIycBgK4u0PZsoaFdUlJMCwWAPb24OyKc%2BoFyMoyNnb16sbGK1Mm57Vy5f/92wDlMguhT3GlTFYh9GlJ4z5LFg53WbqlyneB3GWfBhEREREpVEq%2BC0S9JyIiIiJSRFT5FhERERHbqfJdIOo9EREREZEiosq3iIiIiNhOle8CUfItIiIiIrZT8l0g6j0RERERkSKiyreIiIiI2E6V7wJR74mIiIiIFBFVvkVERETEdqp8F4iSbxERERGxnZLvAlHviYiIiIgUEVW%2BRURERMR2qnwXiHpPRERERKSIqPItIiIiIrZT5btAlHyLiIiIiO2UfBeIek%2BuKzMzk%2Bjo6CLb3sWLFzl//nyRbU9ERESkqN2RyffkyZNp0aIFCQkJVtMzMzPp06cPzz33HGaz%2BTa1zjZLly6lSZMmNGnShKNHj%2Ba7zPbt23n66afx9/fH19eXnj17smbNGkPb8dNPP3H//fcDEB0djY%2BPDzExMQCMHj2ajRs35rteZmYmdevW5ddff80zb86cOQwaNAiA3bt34%2Bvre9N2ZGdn88gjj3Ds2LF/uCciIiJSJOzsjP/5F7kj9/bll1%2BmYsWKvPzyy1bT586dS3x8PDNnzsRkMt2m1tlm1apVBAcH88svv1CnTp088xcvXsyLL75Iz5492bZtG7t372b8%2BPG8//77zJ49u1DaVLVqVSIiIqhUqRKAIVXopk2b5pugXys7O5sLFy4UeHsiIiJSyJR8F8gdubclSpRgzpw5/PLLL3z88ccAhIeHs3z5ct59911cXV0BSE5OZvLkybRu3ZpmzZoxduxYq2r5li1bCAoKolmzZjz00EMMGDCAqKgoAD7//HMef/xxBg0ahK%2BvL5s2bWLXrl306tULX19fHnnkEUJCQsjKysq3jdHR0YwaNQp/f39atGjBiy%2B%2BSHx8PJCTkJ45c4a3336bIUOG5Fn33LlzzJ49m6lTp9K1a1ecnZ2xt7fH39%2BfadOmERcXR2ZmJj/99BMBAQGMGTMGX19flixZQnZ2NsuXL6djx474%2Bvry5JNPsn//fkvsmJgYnnvuORo1akSHDh34%2BeefLfNOnjxJ3bp1OXfuHBMmTGDv3r3Mnz%2Bf559//h%2B/V1dX1gHeffddWrdujZ%2BfH4GBgWzduhWATp06AfD000%2BzbNkyADZv3kzPnj1p1KgRHTt2ZOXKlZZvNMaNG8fo0aPp1KkT/v7%2BzJ8/n0cffdRq2x999BEDBw78x20XERERMdode8FlzZo1mTRpEm%2B88Qa%2Bvr5MmDCBl156iQcffNCyzPjx40lPT2fDhg04OTkxffp0Ro0axSeffMLp06d54YUX%2BOCDD2jTpg3nz59nxIgRLFiwgBkzZgDw%2B%2B%2B/8/bbb/PRRx%2BRnZ3Nww8/zLhx43jssceIjo6mb9%2B%2B%2BPr60qFDB6u2paenM3jwYHx8fPjuu%2B8wm81MmjSJ4cOH89lnn7F7925at27N2LFjeeyxx/Ls27Zt23ByciIgICDPvDZt2tCmTRvL76dPn6ZPnz689dZbpKWl8fHHH7Ny5UoWLFhAzZo1Wb9%2BPYMHD%2Babb76hQoUKjB49Gg8PD3bs2MHFixcZNmxYvv0bEhLCyZMnadWqFSNGjLju%2BzB06FDs7e2tpqWlpdG4ceM8y/7444%2BsW7eOsLAwKlasyOrVq3n11VfZsWMH33zzDfXr12fJkiX4%2Bvry448/8n//93%2B88847tG/fnoMHDzJixAhMJhMDBgwA4IcffmDNmjV4eHiQkpLC3Llz%2BfPPP3nggQcA2LBhA88%2B%2B%2Bx1236t2NhY4uLirKa5p6Xh4e5uc4ybcnS0fjWKQyEcyrnv6zXvb4GVLm1svJIlrV%2BN4uNjbLx69axfDWR00Sj3i0OTyeDYJUoYGIzCO56M/swX1rEEUKaMsfEK63i6k/pUbu5fVqk22h2bfAP07NmTn3/%2BmSeeeIIOHTrQv39/y7yYmBi2bNnCd999R4UKFQB45ZVX8PPz49ChQ9SsWZNNmzZRrVo1kpOTOXfuHBUqVLCMdwZwdnamW7duliEsLi4ufP3115QrV44mTZqwY8cO7PL5AIaHh3Pu3DkmT55MqVKlAJgyZQp%2Bfn4cOHCABg0a3HC/zp8/T/ny5XGwMaEKDAzE0dERR0dHVq9ezfDhw6lbty4Affr0Yc2aNWzcuJF27doRERHBli1bKF26NKVLl2bkyJGMGTPGpu3kZ9GiRXnGdM%2BZM4d9%2B/blWbZEiRIkJiYSGhpKQEAATzzxBP369cNkMpGZmWm17Lp16%2BjYsSMdO3YEoEGDBgwdOpTQ0FBL8t2oUSNq164NQNmyZWnevDlffPEFDzzwAL///jsxMTGW9W0RGhrKvHnzrKaNfP55gkeNsjmGzTw9jY9ZWP7%2BJskwbm7GxstVv76x8fbsMTZertWrDQ9pcJpk4eJicMBq1QwO%2BLd77imcuEYzOlEG8PMzPibA30WMYq8w%2BrQwGH2CKHe0Ozr5Bhg5ciRffPEFo0ePtpp%2B%2BvRpAHr16mU13cHBgVOnTlG3bl2%2B/PJLQkNDsbe3x9vbm6SkJJydnS3Luru7W40dX7lyJXPnzuX1118nISGBVq1aMXnyZMsY6Vzx8fFUqFDBknhDTnJYrlw5Tp8%2BfdPk293dnfPnz5OZmZknAc/KyuLixYuWEwp7e3sqVqxotd/Tp09n5syZlmmZmZmcOXPGcmJxz1V/qKoV1h/DfPj6%2BvLee%2B%2BxatUqFi9ejIuLCwMHDsy3%2Bh4fH0/Dhg2tpnl5eVneVwAPDw%2Br%2Bb1792bq1KmMHz%2BedevW0aVLF1xuIXsICgrK822De1oaGHnHF0fHnMT73DnIyDAurtFVKsipKLm6woULcJ3hVf%2BI0RfVliyZk3jv3w8pKcbFfe4542JBTsV79Wro1w8OHTI0dMpOY08UTKacxPvKFTDy2vWS8VHGBYOc4%2Bmee%2BDsWWOPp7JljYsFOcdSmTJw6ZKxxxLAkSPGxitZMifx/vNPY48nb2/jYkHh9ulVf7sN4eho7Ofz6ri3iyrfBXLHJ9%2B5ledrK9Cef1cWN2/ebElUzWYzkZGRVKtWjY0bN/LZZ5/x6aefUrVqVQBef/11Tp48aYlxdeKdmppKZGQkU6ZMwd7enmPHjvHqq68yc%2BbMPBdAenl5cf78eS5fvmxJwC9cuMDFixdxt2EIQ%2BvWrcnMzGTr1q08/PDDVvP%2B%2B9//MmbMGL7//vt8161UqRIvvviiZQw1QFRUFOXLl7dc0Hjq1CmqV68O5IwvLyqnT5/Gw8ODpUuXkp6ezo8//khwcDAPPPAAzZo1s1q2SpUqeW5zGBUVZdV/115U26FDB9544w1%2B%2BuknvvnmGz788MNbap%2BHh0eehJ7ISEhPv6U4NsnIMDauk5Nxsa6VlQXXfDNRIMnJxsW6WkqKsbEjIoyLdbVDhwyPnZ1taDjL31Wz2eDYaWkGBrtKRoaxsY1O5q6Oa3TsS5eMjZcrJcXY2HdSn8rNKfkukLu29ypXrkzLli2ZNm0aFy5cICMjgw8%2B%2BIDHH3%2BcS5cucenSJezs7ChRogTZ2dls376djRs3knGDs9MxY8awYsUKsrKycHd3x8HBgfLly%2BdZ7qGHHqJ69epMnjyZ5ORkkpKSmDx5MjVr1sxTzc1PpUqVeP7553nttdfYtGkT6enpZGRk8P333zNp0iQGDx6cp9qeKygoiPnz53P8%2BHEg53aFXbp0Yc%2BePVStWhV/f39mzJhBUlISsbGxeYZZXK1EiRJcMvA/33379jF06FAOHz6Mk5MTbn8PP8gdYmNvb0/y38lT79692bx5M99%2B%2By1ZWVn8%2BeefLFmyhN69e183vpOTE127dmXOnDmUL1/epr4WERERKUp3fOX7Rt555x1mzZpF9%2B7duXz5Mt7e3ixZsov3M9UAACAASURBVAQ3NzcCAwOJiIigS5cu2NvbU6tWLQYOHEhoaGi%2BCbizszPz58/nrbfe4oMPPsDBwYE2bdrkO17a0dGRhQsXMnPmTB5%2B%2BGEyMzNp3rw5S5cuzXNx4vWMGDECLy8vVq5cyeTJk8nKyuLee%2B9l7NixPP7449dd7%2BmnnwbgueeeIy4uDk9PT9544w3LRZrvvvsukydPpm3btpQpU4YePXpw8ODBfGP16NGDKVOmsH//flauXGlTu2%2BkS5cunDhxgmHDhpGYmIi7uzsTJ060XCAZFBTE6NGjGTJkCKNHj2bOnDnMnz%2BfCRMmUL58eQYMGMAzzzxzw2306tWLVatW8eKLLxa4vSIiIpIPVb4LxGQu7k%2BjEbkF58%2Bfp02bNnz//fc2DfG5qcjIgse4mpMTVK2aM47cyGEnRt9BBHLuoOLmBgkJxg47OXDAuFiQs%2B9NmsAvvxg77CSfuw0ViI9PzkWcjRoZPuwk%2BZKx/43b2eUM/U1JMXbYSemz%2BT9Q7B8rUSLnIs6oKGOHnfw9VNEwhXX9BMDevcbGK1Mm5yLO8HBjh50Y/U1kYfap0WP%2B78Yx399%2Ba3zMW7hBwp3urq58y79HWloaUVFRLFu2jICAAGMSbxEREclLle8CUfItd4UrV64QFBRElSpVWLhw4e1ujoiIyN2rGCbfCQkJTJw4kfDwcOzt7enevTvjx4/P97bNn376KcuXLyc2NhYPDw8GDhxouV11dnY2jRs3xmw2W93Y4ccff6SkQXcWU/ItdwVXV1f2FNZ9mUVERKRYe%2BGFF6hUqRI//PAD8fHxDB8%2BnOXLl%2Be5VmzLli3Mnj2bRYsW8dBDD7F3716effZZKlasSMeOHfnrr7/IyMhgz549OBXSncSUfIuIiIiI7Qqh8p3vU6bd3fPeAjgfJ0%2BeJDw8nB07duDi4kLVqlUZMWIE/8/enYdFVbYPHP%2ByL2LiAkGaSya45SubuKKg5oK4kpS55ZKWgbm8auYaroWaYG6hZpFvmlKJa6Vp9pZLSpoYuSeLylosAjPA%2Bf2BzI8R1EEOqK/357rmGjjLfZ7zzIG5557nnPPBBx%2BUSr5v3rzJ2LFjdVdEc3FxwdPTkxMnTtCjRw9%2B//13nJ2dKy3xBkm%2BhRBCCCHEQ1bmXabfeovAwMD7rnvhwgVsbW31LsPcuHFjEhMTycjI4KkSJ9GWvBs6FA1XOXHiBO%2B88w4Av//%2BO3l5eQwaNIiEhAQaN27MlClTcHV1rcju6ZHkWwghhBBCGK4SKt9l3mXawIsnZGdnl7qjdfHvt27d0ku%2BS0pOTmbcuHG0bNmSPn36AEWXlm7VqhUTJ06kRo0afP7554wePZqdO3fqbspYUZJ8CyGEEEIIw1VC8l3mXaYNZG1tTU5Ojt604t%2BL7zR%2Bp99%2B%2B42JEyfi7u7O4sWLdSdmzpgxQ2%2B50aNHExkZyeHDhxk6dOgDte9Oj97pqkIIIYQQQhioSZMm/P3336SkpOimXbp0CQcHB6pXr15q%2Be3btzNy5EhGjBjBsmXL9MZ3r1ixgnN33I9Co9FgYWGhWnsl%2BRZCCCGEEIYzNlb/UQENGzbEzc2NRYsWkZWVRVxcHKtXr8bf37/Usvv372fevHmEhYUxatSoUvPPnz/PwoULSU5ORqPRsGrVKrKysujevXuF2liSJN9CCCGEEOKxFhoaSn5%2BPl27dmXw4MF06tSJN998Eyi6osnOnTsBWLVqFQUFBQQFBeHi4qJ7zJkzB4DFixdTv359%2BvXrh6enJ8ePH2fTpk3Y2tqq1lYZ8y2EEEIIIQz3CN5kp06dOoSGhpY5Lzo6WvdzVFTUPePY2tqyePFiVdt2J0m%2BhRBCCCGE4R7B5PtxIr0nhBBCCCFEFZHKtxBCCCGEMJxUvitEek8IIYQQQogqYqQoivKwGyHEoyovT914RkZgbg4aDaj5l2dRmHP/hcrLyAgsLSE3V9XGJmdZ3X%2BhcjA1hZo1IT0d8vPVi2ulbjMxNgZra7h1CwoL1Y1tU91I3YAuLnDqFLi6QokTlSoqK1Pdt5vK6lObzOvqBYOig9TODpKT1T1IAcXBUdV4UPSnr3ZmYJSYoG5AMzOwt4ekJNBq1Y39zDPqxquMDi2O%2B7CcPKl%2BTDc39WM%2BomTYiRBCCCGEMJwMO6kQ6T0hhBBCCCGqiFS%2BhRBCCCGE4aTyXSHSe0IIIYQQQlQRqXwLIYQQQgjDSeW7QiT5FkIIIYQQhpPku0Kk94QQQgghhKgiUvkWQgghhBCGk8p3hUjvCSGEEEIIUUWk8i2EEEIIIQwnle8KkeRbCCGEEEIYTpLvCpHeE0IIIYQQoopI5VsIIYQQQhhOKt8VIr0nhBBCCCFEFZHKtxBCCCGEMJxUvitEkm8hhBBCCGE4Sb4r5JHtvby8PG7cuPGwm/FYuXr16sNuwiNF%2BkMIIYQQj5pyJd/Ozs44Oztz%2BfLlUvM2bdqEs7MzYWFhqjRsyJAh/PzzzwAcO3YMZ2dnVeLei6%2BvLzt37qz07ZQUFhbGsGHDKhzn888/Z/bs2QYvHxkZiY%2BPj0HLlmzjzp078fX1faA2VqVz587Rp0%2Bfh90MIYQQ4n%2BPsbH6jydIufe2Zs2afPXVV6WmR0ZGYmNjo0qjANLT01WLZajdu3fTt2/fKt%2BuGtLS0qpkO3379mX37t1Vsq2KyMzMRKvVPuxmCCGEEELoKfeYbz8/P7755hsmTZqE8e1PKmfOnEGj0dC8eXPdcoWFhYSHh7Nt2zbS09Np1KgREydOpFOnTgD4%2BPgQEBDA3r17%2Beuvv2jQoAEzZsygbdu2jBo1isTERObOncvZs2fp0aMHABs2bOCLL74gOTkZLy8vFi1ahI2NDTdv3uTdd9/lzJkzWFpa0qpVK%2BbMmYO9vX2p9p84cYLFixdz7do1atasSZcuXZg%2BfTqmpqb4%2BPjw1ltvMXDgQIYNG0br1q05deoU586dw8HBgcDAQHr37g1AXFwcCxcu5MSJE5ibm9OjRw9mzpyJubk5165dY9GiRURHR2NtbU3fvn2ZMGEC5ubm9%2BxbRVH4%2BOOPiYqK4vr16xgZGeHl5cXChQuxtLTkwoULzJs3j/Pnz2NjY0ObNm2YPXs23333HevWraOgoAB3d3d%2B/fXXUrEvXbrEvHnzOHv2LPXq1cPT01NvfkxMDEuWLCE2NpaaNWsyZMgQRowYgZGRkd5ykZGRrFq1ioMHD3Ls2DHeeecdXnrpJbZs2UJeXh6enp4sXrwYGxsbFEVh3bp1REREkJOTQ9%2B%2Bffnzzz/x9/fX9XGbNm0IDAwEID4%2Bnq5du3LgwAHq1atHSkoKS5Ys4ZdffsHIyAgfHx%2BmTZuGjY3NPbednp7O2LFjAXBxcWHjxo24uLjcs%2B8BkpKSSE5O1ptWo4ZdmcfRgyruzju6Vb3AlRFT5dimKp9pYmKi/6wWtQsxJbtT9SKPAcd3uTRtqv%2BsksemT9U%2BSIvjqR33cWJmpm486dOH6wmrVKtOKQcnJyflp59%2BUtq2bascOXJEN3327NnK%2BvXrlaFDhyqhoaGKoihKaGio4uXlpZw9e1bRarXK7t27lZYtWyqnT59WFEVRvL29le7duytXr15Vbt26pUyfPl3p0aOHLqa3t7eyY8cORVEU5ejRo4qTk5Myf/58JTc3V7lx44bSqVMnZe3atYqiKMq0adOUd999V9FoNEpmZqby2muvKcHBwWXuQ5cuXZTIyEhFURQlLi5O6dixo7Jv375S2xw6dKjSpk0bJSYmRsnLy1OWL1%2BuuLm5Kbm5uYpWq1W6d%2B%2BuzJo1S8nKylJSUlKUfv36KSEhIUp2drbi7e2thISEKLm5uUpiYqLi7%2B%2BvhISElNme0NBQZejQoYqiKMru3buVDh06KFeuXFEURVEuXryotGnTRtm2bZuiKIry6quvKmFhYUphYaGSmpqq9OnTR9m4cWOpOHfSaDRK165ddf13/vx5pXPnzoq3t7eiKIpy48YNxc3NTYmIiFA0Go1y4cIFpXv37sp//vOfUrF37NihW6/4dZk7d66Sk5OjXL16VenQoYOybt06RVEUZdu2bUrbtm2Vs2fPKrm5ucqSJUsUZ2dnvT4uPl6KXw8nJyclLi5OKSgoUF566SXl3//%2Bt5KZmamkpaUp48aNUyZNmmTQtovnl0doaKji5OSk91i5MvT%2BKwohhBBPksRE9R9PkHJ/ZDQ1NcXPz4%2BvvvqKjh07kpuby/79%2B9m1axc//vijbrkdO3bw%2Buuv06JFCwB69%2B7N/v372b59O61atQLA39%2BfBg0aAEUV9a%2B//vqe2w4MDMTCwoKnn34aDw8Prl27BoCFhQUnTpxg9%2B7dtGvXjvDwcF1V/k4WFhbs3bsXW1tbPDw8OHz48F2X7dGjh66aP2DAANauXUtqairx8fEkJCQwc%2BZMrKysqFatGqtWraKwsJBDhw6h0WiYPHkyRkZGODo6MnHiRIKCgpgyZco998/LywtXV1ccHBxIS0sjPT0dW1tbbt68qWv7kSNHaNy4Me3ateObb765a9tLio6O5vr160ybNg0LCwuaNGnCa6%2B9xubNm4GicdyNGzfm1VdfBeD5559n9OjRRERE8PLLL983/oQJE7C0tKRBgwZ4enpy5coVAL755hsGDx6sOwamTJly39e42NmzZ4mJiWHTpk1Uq1YNgOnTp9OzZ0%2B9se132/aDCAgIKDUOvkYNOzSaBw5ZipFRUQFIqwVFUS%2BueWGuesGKGRmBhQXk5ana2PQcS9ViQVHF%2B6mnICMDCgrUi2thoV4sKOpOKyvIyVH3tQew7uiqbsCmTWHLFhgyBGJjVQt766dTqsWCyutT6%2Bzk%2By9UHqamULMmpKdDfr6qoZU6dqrGg6J%2BVfsYNUpOUjegqSnUqgVpaar3KXYq92lldGhxXPFYeqDvawYOHEhAQABZWVl8//33uLq6YnfHwZqSksKzzz6rN61evXrElvhHXqdOnf9viKkpyn0Ozpo1a%2Bp%2BNjMzo%2BD2O%2B2sWbNYt24dGzZsYMaMGTRt2pRZs2bh7u5eKsbmzZsJCwtj/vz5JCcn06lTJ%2BbNm4eDg0OpZUvuk%2Bntr7YKCwtJTk6mZs2aWFlZ6e0bwP79%2B0lLS8PDw0M3T1EUtFotqamp1K5d%2B677pygKK1as4IcffqBWrVo0a9YMrVar65cPP/yQsLAwVqxYweTJk3F1dWXevHk0adLknv128%2BZNatasiaXl/yc99evX1/2ckJBATEyMXn8VFhZiYuD3%2BCX7yczMTNfe1NRUHB0ddfNMTU1LHRN3Ex8fT0FBAZ07d9abbm5uTlxc3H23/SDs7e1LDTFROe/UURSV41ZGI0vGVjG%2B2u%2BTxQoK1I2t9rfkxZ%2BTFQUKC9WNTXS0ygFvi41VNbba%2B11pfVpZB2l%2BfuXFftRV1jk4%2BfmVF1vcnQw7qZAHSr6bNm3Kc889x969e4mKimLEiBGllqlbt65ekgRF46TVHD9b7Ny5cwQEBBAYGEhaWhofffQRb731FkePHtVbLi8vj4sXLzJv3jxMTU25cuUKs2bNYtGiRYSGhhq8PQcHB9LT08nJydEl4L/%2B%2Bitnz57FwcGB%2BvXrs2/fPt3yWVlZpKamUqtWrXvGDQkJITExkYMHD%2BpOXvXz8wOKkuFz584RGBjIzJkzuX79OosXL2bGjBns2LHjnnEdHR1JS0sjOztbV0UueRlHBwcHPD092bBhg25aeno62dnZBvdJWZ599lm9Y0BRFF0VH8DY2FjvpMiSJ9k6ODhgaWnJsWPHdB8CNBoNcXFxNGjQgJMnT1aobUIIIYR4QJJ8V8gD997AgQP55JNPuHLlSqnqJMBLL73E%2BvXriYmJoaCggL1793Lw4EEGDBhgUHxzc3MyMzMNWnbt2rUEBweTlZXFU089hZWVlV6VvJiRkRGTJ09m48aN5OfnY2dnh6mpaZnL3kurVq1o2LAhS5cuJScnh5SUFBYvXkxaWhre3t5kZ2cTHh6ORqMhIyOD6dOnM2nSpFInL94pKysLCwsLTExMyMvLY%2BPGjZw/fx6tVouxsTELFizgww8/JC8vj1q1amFhYaFru4WFBVlZWWVWfl1cXGjUqBELFiwgJyeHv/76i40bN%2Brm%2B/n58dtvv7Fz507y8/NJSkpi/PjxLFmypFz9cqdXX32Vbdu2cerUKbRaLevXr9dL%2Bhs3bsyRI0fIyMggMzOTjz/%2BWK%2BPGzRowJIlS8jOziY3N5dFixYxcuRI3Tce92Jxe8yAoceQEEIIIURVeODku0%2BfPvz111/07dtXNySjpNdee41XX32VSZMm4e7uzrp161i%2BfDlt2rQxKL6/vz8rVqxg6tSp9132vffeo7CwkK5du%2BLh4cHp06dZuXJlqeXMzc1Zs2YNBw4cwNPTEx8fH%2Bzs7AzaRklmZmasXbuWmzdv0qVLF/r164eHhwdBQUHY2NjwySefcOzYMby8vOjWrRvGxsasWbPmvnHffvttcnNzad%2B%2BPT4%2BPvz222/069eP8%2BfPA0XDTi5dukTHjh1p3749mZmZBAcHA%2BDt7c3ff/%2BNm5sbGRkZenFNTExYv349SUlJtG/fnjFjxtC1a1fd/Lp16xIeHs7WrVtp3749/fr147nnnqtw8t25c2feffdd3nnnHTp27EhCQoLeNx/jxo2jdu3adO3alX79%2BumNtzY1NWXdunWkpKTw4osv0rFjR65du8amTZt0ifW9ODk54ebmRqdOnTh8%2BHCF9kMIIYQQJch1vivESKnIIFkhyqnk5RwfB3l56sYzMgJzc9Bo1B2mbVGYo16wYkZGYGkJubmqNjY5y%2Br%2BC5VDZZ3LZqVuMzE2BmtruHVL/bHPNtVVPvHKxQVOnQJXV1XHfGdlqvt2U1l9apN5Xb1gUHSQ2tlBcrL6J1w6ON5/oXKqlBMuExPUDWhmBvb2kJSk/pjvZ55RN97/4gmXqanqx7zHOXH/a%2BQCmUIIIYQQwnBPWKVabZJ8CyGEEEIIw0nyXSGSfIsqdfDgwYfdBCGEEEKIh0aSbyGEEEIIYTipfFeI9J4QQgghhBBVRCrfQgghhBDCcFL5rhBJvoUQQgghhOEk%2Ba4Q6T0hhBBCCCGqiFS%2BhRBCCCGE4aTyXSHSe0IIIYQQQlQRqXwLIYQQQgjDSeW7QqT3hBBCCCGE4YyN1X9UUGpqKm%2B%2B%2BSbu7u54enqycOFC8vPzy1z28OHD%2BPn50bp1a3r16sUPP/ygN//jjz/Gy8uL1q1bM2zYMC5fvlzh9pUkybcQQgghhHisvf3221hbW3PkyBG2b9/OL7/8wieffFJquatXrxIYGMjEiRP59ddfCQwM5O233%2BbmzZsAfPXVV3z22Wds2LCBY8eO0aJFC4KCglAURbW2SvIthBBCCCEMVwmV76SkJGJiYvQeSUlJBjXnr7/%2B4vjx4/z73//GysqKZ599ljfffJPPP/%2B81LJfffUV7u7udOvWDVNTU3r37o2Hhwdbt24FYNu2bQwZMoQmTZpgYWHBlClTSExM5NixY6p1n4z5FuIeLC7/oW5AS0to1AjzhCuQm6ta2AKnZqrFKskEKDCzVDWm3bnDqsbDxgbc3Kh5%2BSRkZakX95ln1IsFYGEB9etjnXIN8vJUDZ2VqV5FBoreC62BWz%2BdorBQvbg21Y3UCwbg4gKnTmHd0RWio1ULW5Cvbn/C7b%2BlWnbqx/10s7oBa9UCPz%2BMdkVBWppqYbVDRqgWq5gZoK1pr37cwgJ1A5qYoOofUsm4/0O2bt3KqlWr9Ka99dZbBAYG3nfdCxcuYGtry9NPP62b1rhxYxITE8nIyOCpp57STb948SJOTk566z///PPExsbq5o8dO1Y3z8zMjIYNGxIbG0vbtm0faN/uJMm3EEIIIYQwmILKH6SBgIAAfHx89KbZ2Rn2gTU7OxsrKyu9acW/37p1Sy/5LmtZS0tLbt26ZdB8NUjyLYQQQgghDFYZhXx7e3vs7R/smwxra2tycnL0phX/Xq1aNb3pVlZW5N7xzXNubq5uufvNV4OM%2BRZCCCGEEI%2BtJk2a8Pfff5OSkqKbdunSJRwcHKhevbresk5OTly4cEFv2sWLF2nSpIkuVsn5Wq2Wq1evlhqqUhGSfAshhBBCCIMVFqr/qIiGDRvi5ubGokWLyMrKIi4ujtWrV%2BPv719q2b59%2B3L8%2BHH27NlDfn4%2Be/bs4fjx4/Tr1w%2BAQYMGERERQWxsLHl5eSxbtow6derg7u5esUaWIMm3EEIIIYR4rIWGhpKfn0/Xrl0ZPHgwnTp14s033wTAxcWFnTt3AkUnYn700UesW7cODw8PVq9eTVhYGI0aNQLA39%2BfkSNHMmHCBNq2bcu5c%2BdYt24dZmZmqrVVxnwLIYQQQgiDVcaY74qqU6cOoaGhZc6LvuNqSJ06daJTp05lLmtkZMSoUaMYNWqU6m0sJsm3EEIIIYQw2KOYfD9OZNiJEEIIIYQQVUQq30IIIYQQwmBS%2Ba4YqXwLIYQQQghRRaTyLYQQQgghDCaV74qR5FsIIYQQQhhMku%2BKkWEnQgghhBBCVBGpfAshhBBCCINJ5btipPIthBBCCCFEFZHKtxBCCCGEMJhUvitGkm/xWMvMzESr1VKrVq2H3RQhhBDiiSDJd8VU6rATZ2dnXn/9dRRF0ZseGRmJj49PpWzTx8eHyMjISoltiD179tCuXTvc3Nz44Ycfylzml19%2BYcyYMXh4eODi4oKvry%2BrVq0iNze3iltbmr%2B/Py%2B88ALJyckPuykG6d69OxcuXHjYzRBCCCGEMEilj/k%2BfPgw4eHhlb2ZR8aXX36Jr68vJ0%2BexNvbu9T8//znP7z55pt06NCB/fv3c/LkSZYuXcovv/xCQEAA2dnZD6HVRU6fPs2NGzfw8vIiIiLiobWjPNLT0x92E4QQQognSmGh%2Bo8nSaUPOxk2bBgrV67Ezc0NV1fXUvPj4%2BPp2rUrBw4coF69egCEhYVx/PhxPvvsMyIjI9m%2BfTv/%2Bte/2LFjB8bGxkyYMAELCwvWrFlDRkYGvr6%2BvPfee7qYMTExREREEB8fzwsvvMDs2bNp2LAhANeuXWPRokVER0djbW1N3759mTBhAubm5kRGRhIREYGtrS1nzpxh7ty5%2BPn56bU3PT2d5cuX88MPP6DVamndujXvvPMODRs2xN/fn5iYGE6cOMGhQ4f4/vvv9dZNTk5m8eLFBAcH069fP930li1bEh4ejp%2BfH6tXr%2Bbf//43YWFh/PHHH5iYmHDkyBFq1arFuHHjCAgIACArK4vly5dz4MABNBoNbdu25d1336VOnTq6Pl2wYAFr1qzhn3/%2BoVWrVixevBgHB4e7vlYRERH07NkTb29vJk%2BezPjx47GystLN/%2B9//8uKFSu4dOkSNWvWZNSoUQwdOhSAqKgo1q1bR0JCAg4ODgQGBtK7d2%2Bg6APJJ598wvXr16lbty5jx46lb9%2B%2BuuOjTZs2BAYGlnk8ODs7M2vWLCIiIkhKSsLZ2Zn58%2Bfj7OxMjx49ABg7diyBgYG88sorzJ49m59//hlTU1OaNm3KzJkzady48V33uaSkpKRSFX%2B77Gzs7ewMWt8g5ub6z08iGxt14xUfoyWOVVVYWKgbz8xM/1lFxiqXUYyM/v9Z1dguLioGA5o21X9%2BEqk95K5GDf1nIYT6lErk5OSkHD16VHnvvfeUzp07K%2Bnp6YqiKMqOHTsUb29vRVEUJS4uTnFyclLi4uJ064WGhipDhw7VLevk5KRs2rRJKSgoUD7//HOlWbNmyuTJk5Vbt24pZ86cUZo1a6YcP35cURRF8fb2Vry8vJTY2FglNzdXmTNnjvLiiy8qWq1Wyc7OVry9vZWQkBAlNzdXSUxMVPz9/ZWQkBC9bUVGRip5eXlKTk5OqX0aOnSoMnz4cCUpKUnJyclRlixZonTu3FnJzMzUzQ8NDS2zP3bs2KG0bNlSycvLK3P%2Bhx9%2BqPj4%2BOj6wMnJSdm4caOi0WiUI0eOKC1atFB%2B/vlnRVEUJTAwUBk1apSSkpKiZGVlKbNmzVICAgKUwsJCXZ%2B%2B%2Beabyj///KMkJycrffr0UWbPnn3X1yolJUV54YUXlIsXLyqFhYVKr169lM8%2B%2B0w3//Lly0rLli2VL7/8UtFqtcrvv/%2BuuLi4KD/%2B%2BKNy9OhRpWXLlsqhQ4eUgoIC5fDhw0qLFi2UCxcuKDt27FBcXV2Vn3/%2BWcnPz1d%2B/vlnxdXVVfn222/L7K87jwcnJyclICBASUpKUjIyMpSRI0cqo0aN0i1ffIwpiqKsXLlSGTNmjJKTk6Pk5eUp06dPV8aPH3/Xfb5TcZ%2BXfISuXGnw%2BkIIIcSTIDFR/ceTpEpOuJw%2BfTrR0dHMmDGDNWvWlHt9a2trRowYgZGRER07dqSgoIDRo0djZWXFCy%2B8gL29PQkJCXh4eAAwatQonJ2dAZgxYwbu7u6cOXOGGzduoNFomDx5MkZGRjg6OjJx4kSCgoKYMmUKAGZmZvTr1w/jMso9cXFxHD9%2BnN27d2N3uxo6depUoqKiOHz4ML6%2Bvvfcj6SkJGrUqIH5Xaqe9vb2JCUl6X53dnbmtddeA6Bjx4706NGDb775BicnJ/bv38/evXupXbs2ADNnzsTd3Z2YmBhsbW2BoorwU089BRSNhY%2BOjr5r27Zu3UqbNm10VeJhw4axYcMGhgwZgrGxMbt376ZFixb4%2B/sDRdX6LVu2YG9vzwcffMCLL75I586dAfDy8mLLli08/fTT7Nixg4CAANq1awdAu3btCAgI4IsvvqB79%2B737K9iw4YN0/V3r169WLduXZnLWVpaEhsby9dff02HDh1YtGhRma/j3QQEBJQ6F8EuOxuuXDE4xn2Zm0PdupCQABqNamEL6jdSLVZJJiZQUKByzN9OqhvQygqaN4dz5yAnR724an7jAUUVb0dHuH4dtFpVQ9%2BqU1/VeEZGRd2akwN3nLJTIdYdS3/7WSFNm8KWLTBkCMTGqha24MQp1WIVq4y/JQCTPVHqBqxRge7t1wAAIABJREFUA7y84Mcf4Z9/VAur7el3/4XKycxM9T%2BlorjGav/Tq6wX30T9mAZ60oaJqK1Kkm9zc3M%2B/PBDBgwYwMaNG6lZs2a51re1tcXo9vegxclUcVJZPK2wxJFQPHwFwMrKCltbW27evElCQgJpaWm6JB1AURS0Wi2pqakA2NnZ3TVhS0lJAeDZZ5/VTTMxMcHR0ZGEhIT77oednR2pqank5eVhUcZX2vHx8bokE9ANlSnm6OjIH3/8odvW4MGD9eabmJgQHx%2BvS77r1Kmjm2dqalrqxNdi%2Bfn5fPHFF2RkZODp6QlAYWEhGRkZfPfdd/To0YOkpCSeeeYZvfWa3v6qNykpiebNm%2BvNa9WqFVDUZyX7C4pen4MHD5bZlrIYuh9jx47F3Nyc7du389577/Hss88yZcoUXnzxRYO2Y29vj729vf7EP/6AyjgRVqOpnLiPg6ysyombk6Nu7BL/Y1Sl1UJenqoh1X4jLP4XqCgqx75HAaBCYmMrL/ajLi2tcuL%2B80/lxRbiCVdllxqsX78%2BwcHBTJs2jYEDB%2Bqmm9z%2B5KYt8fH1zpPoihNvQ5WsHmdlZZGenk7dunXJz8%2Bnfv367Nu3T29%2Bamqq7lJ199pW3bp1gaJx402aNAGgoKCAxMREvaT5bry9vTEzMyMyMpJXXnlFb152djZ79uyhZ8%2Beumk3b97UWyY%2BPh5HR0eefvppAPbu3au33YsXL/Lss8%2BW%2B0ol3333HRqNht27d%2BteD4CVK1eyadMmevTogaOjI4cPH9Zbb8eOHdSuXRtHR0cSExP15m3cuJHWrVtTr149rl27pjcvLi5O125jY%2BN7vvbl8eeff%2BLj48PIkSPJzMxky5YtTJo0iaNHj1K9evUHjiuEEEKI/yeV74qp0jtc9u7dm0GDBrF161bdtNq1a1OjRg12796NoijExMToJccPYuPGjVy%2BfJmcnBwWLlxIs2bNaNmyJd7e3mRnZxMeHo5GoyEjI4Pp06czadIkgxJ8e3t7OnfuzIIFC0hOTiY3N5eQkBAKCgrKvLLJnWrVqsWcOXN4//33%2BeSTT0hLS0Or1XLmzBnGjBlDtWrVmDBhgm753377jW%2B%2B%2BYaCggIOHz7MgQMHGDRoEE8//TRdunRh4cKFpKeno9VqWbNmDf7%2B/mRkZJS7vyIiIvDz86Nu3bo4ODjoHsOGDSM6OppTp07h6%2BvLuXPn%2BPrrrykoKODs2bMsWbIEU1NTBgwYwHfffcdPP/1EYWEhR44cISwsjOrVq%2BPv78/WrVv55ZdfKCgo4OjRo2zdupVBgwYB0LhxY44cOUJGRgaZmZl8/PHH5Wq7ubk5mZmZQNGJndOmTSM1NRUbGxtsbGywtra%2B6zAfIYQQQpSfXO2kYqr8JjszZ87k9OnTuiTR3Nyc4OBgQkND2bBhAy1btmTw4MGcPPng40K7devG%2BPHjSU9Px8PDg9WrV2NsbIyNjQ2ffPIJS5YsITw8nMLCQjw9Pcs1Dv39998nJCSEAQMGcOvWLVq3bs3mzZt1Qz3ux9/fn/r167Nx40bWrl1LXl4ejo6O9OzZkzFjxmBtba1btlmzZhw4cIAFCxZQp04dPvjgA1xuXy3g/fffZ9myZfTv35%2BsrCyaNGlCeHg4dnZ2xMfHG7w/sbGx/Prrr8yaNavUvObNm9OyZUs2btzIqlWrWL9%2BPcuWLSM4OJjatWszY8YMOnbsCMDSpUtZunQpCQkJ1K1bl%2BXLl9OkSROaNGlCVlYWCxYsIDExkaeffppp06bRv39/AMaNG8e7775L165dqV69OkFBQezfv9/g9gcEBDBlyhRGjhzJ5MmTee%2B99/D19SUvL4/nnnuO1atXlznERwghhBDiYTBS7jaAVjxUJS%2B3KB6iP/5QN56lJTRqVHQSp4pjvgucmqkWq6RKOeHyp8P3X6g8bGzAzQ1OnlR3zPcd5zhUmIUF1K8P166pPuY7y7GJqvGMjcHaGm7dUrciZVO9fEMI78vFBU6dAldXVcd8F%2BSr/7ZYaefcRWxWN2CtWuDnB1FRqo751g4ZoVqsYnLC5cM74VLN6xAUa1Q51w14JFXpsBMhhBBCCCGeZFU%2B7EQIIYQQQjy%2BnrQx2mqT5PsRVXzHRyGEEEKIR4kk3xUjw06EEEIIIYSoIlL5FkIIIYQQBpPKd8VI5VsIIYQQQogqIpVvIYQQQghhMKl8V4wk30IIIYQQwmCSfFeMDDsRQgghhBCiikjlWwghhBBCGEwq3xUjlW8hhBBCCCGqiFS%2BhRBCCCGEwaTyXTGSfAshhBBCCINJ8l0xMuxECCGEEEKIKmKkKIrysBshxKMqPV3deCYm8NRTkJEBBQXqxc3PVy9WMVNTqFmzqA/UjG9jo14sACMjsLSE3FxQ87%2BZ1a1U9YJB0Ytvawt//63uiw%2Bg0agbz9QU7OwgOVnVF7/A3lG1WMVMTNTvThNTI3UDurjAqVPg6grR0aqGjj6l7lu4lRU0bQqxsZCTo15cl4GN1AsG0KIF7NoFffpATIy6sefNUy9WrVrg5wdRUZCWpl5cgBEj1I1XDidPqh/TzU39mI8qqXwLIYQQQghRRWTMtxBCCCGEMJiM%2Ba4YSb6FEEIIIYTBJPmuGBl2IoQQQgghRBWRyrcQQgghhDCYVL4rRirfQgghhBBCVBGpfAshhBBCCINJ5btiJPkWQgghhBAGe9yS71u3bhEcHMzBgwfJz8%2Bna9euzJ07l2rVqpW5/P79%2B1m9ejVxcXHY2toycOBA3nzzTYyNiwaM9OrVi8TERN3vANu3b6dx48YGtUeSbyGEEEII8T8rODiY69evs3//fgoKCnj77bcJCQlh7ty5pZY9e/Ys06ZN48MPP6Rz585cuXKFsWPHYm1tzahRo8jKyuLKlSscOHCAunXrPlB7ZMy3EEIIIYQwWGGh%2Bo%2BkpCRiYmL0HklJSRVua05ODlFRUQQFBWFra0vt2rWZOnUqkZGR5JRxG9eEhARefvllvL29MTY2pnHjxnTv3p0TJ04ARcm5ra3tAyfeIJVvIYQQQgjxkG3dupVVq1bpTXvrrbcIDAy877q5ubncvHmzzHk5OTlotVqcnJx00xo3bkxubi5Xr16lWbNmesv36NGDHj166MU%2BdOgQfn5%2BAPz%2B%2B%2B9YWVkxdOhQLly4QN26dQkMDMTb29vgfZXkWwghhBBCGKwyxnwHBATg4%2BOjN83Ozs6gdU%2BfPs3w4cPLnDdx4kQArK2tddOsrKwAyM7OvmfcrKwsJk6ciKWlJSNHjgTAyMiIF154gcmTJ/PMM8%2Bwb98%2BAgMDiYiIoHXr1ga1V5JvIYQQQghhsMpIvu3t7bG3t3%2BgdT09Pfnzzz/LnHfu3DlWrlxJTk6O7gTL4uEmNjY2d415%2BfJlgoKCqF27Np9%2B%2Bqlu2TFjxugt17dvX3bt2sX%2B/fsNTr5lzLcQQgghhPif1KhRI8zMzLh48aJu2qVLlzAzM6Nhw4ZlrnP48GFeeuklOnXqxIYNG6hRo4Zu3oYNG/jll1/0ltdoNFhYWBjcJkm%2BhRBCCCGEwSrjhMvKYmVlRa9evQgJCSEtLY20tDRCQkLo06cPlpaWpZb/7bffmDBhAu%2B88w7Tp0/H1FR/kMj169eZP38%2BcXFx5Ofns337dqKjoxkwYIDBbZLkWwghhBBC/M%2BaO3cuDRs2xM/Pj549e1KvXj3mzJmjm%2B/r68vatWsBWLt2Lfn5%2BSxcuBAXFxfdo3i4ybRp0/Dy8mLIkCG4u7vzxRdfsH79eho0aGBwe2TM9xPgr7/%2BKtdBIYQQQghxN4/bTXZsbGwIDg4mODi4zPm7d%2B/W/VychN%2BNubk5M2fOZObMmQ/cHtUq387Ozrz%2B%2BusoiqI3PTIystTZq2rx8fEhMjKyUmIbYs%2BePbRr1w43Nzd%2B%2BOGHMpc5c%2BYMQUFBtG/fHldXV3r16sW6devIz89XrR3x8fE4OzsTHx8PgIuLC7/%2B%2BisAS5cuZc2aNXdd18fHhxdeeEH3ya5169Z07NiRpUuXUviAf133e81nzJjBjBkzHii2EEIIIR6ux2nYyaNI1WEnhw8fJjw8XM2Qj7Qvv/wSX19fTp48Web1Hfft28fw4cPx8PDg22%2B/5eTJkyxbtoyoqCimTJlSae2Kjo7G3d0dgPT09PsuP3/%2BfKKjo4mOjua3335jw4YNfP3116WutymEEEIIISpG1eR72LBhrFy5klOnTpU5/84KLUBYWBjDhg0DiiqmQ4YMYenSpbRp04a2bdvy2WefsW3bNry9vXFzc9MbowMQExPDwIEDadOmDaNHj%2Bbq1au6edeuXWP8%2BPF4enri7e3NihUr0Gg0um0NHDiQUaNG4e7uTlRUVKn2pqenM3v2bDp27Iinpyfjxo3Txff39%2Bfo0aN88cUXdOvWrdS6eXl5zJ07lwkTJjBs2DBsbGwwMjKiefPmhISEoCgKf//9t65PlixZgoeHB/PnzweKvgLx8/PDzc2NgQMH8tNPP%2BliZ2VlMX36dNzc3OjUqRPffPON3radnZ05duwYH330EVFRUURFRdG3b9%2B7vWylODs74%2BHhwblz54Ci13XGjBl4e3vTpUsXsrKy%2BPPPPxk7dixt2rTBy8uLefPmkZmZqYuRn5/P0qVLad%2B%2BPd26dSM8PLzUtyLF7rWvw4YNIzQ0lFdeeYXWrVvTt29fzpw5w5QpU3B1dcXHx4dDhw7ptjlv3jw6dOiAp6cnQ4YM4eTJkwbvtxBCCCHuTyrfFaPqmO/u3bujKAqTJ0/m66%2B/xtbWttwxTp48yYsvvqhLbBcsWECvXr3Ys2cPFy9eJCAgAD8/Pzw8PAD4/vvvWb9%2BPQ0bNmTRokWMGzeO3bt3o9FoGDlyJL6%2BvqxcuZK0tDSCgoIoLCzUVZ1jYmJYsmQJa9euLXOIRVBQEMbGxnz11VdUr16dlStXMnLkSHbt2sX27dsZNmwYbdq0KfPuS6dOneLvv/%2BmT58%2BpeY1bdqU0NBQoCiRhqILvf/3v/8lNzeXw4cPM3fuXNasWYOrqys//vgjgYGBbNu2jSZNmvDee%2B9x7do1vv32W4yNje9aRZ8wYQJxcXEALFmyxKD%2B12q1nDp1iqNHj%2Brt188//8yXX36JlZUVWq2W4cOHM3DgQMLCwsjMzGTq1KlMmzZNN8Tl5s2bGBsbc%2BjQIc6fP8/o0aOpU6cO/fv319ve/fYViu56tXnzZurXr8%2BoUaMYMmQIH374IUuWLGH58uUEBwfTpUsXvvnmG6Kjo9m7dy/VqlUjNDSU%2BfPns3PnToP2PSkpieTkZL1plpZ22Nk92HVHy2JsrP/8KDMx0X9Wi5FR5cRTO67qO15ZHQpgqvLpO8Xx1I77uHBxUTde06b6zyq6fa8Q1RRfLa0cV00zTIsW6sZr3Fj/WU21aqkXq/gSdSUuVSeE6v9Zp0%2BfTnR0NDNmzLjnWOO7sba2ZsSIERgZGdGxY0cKCgoYPXo0VlZWvPDCC9jb25OQkKBLvkeNGoWzszNQNJbY3d2dM2fOcOPGDTQaDZMnT8bIyAhHR0cmTpxIUFCQLlk1MzOjX79%2BGJeRCcXFxXH8%2BHF2796tu8PS1KlTiYqK4vDhw/j6%2Bt5zP9LS0gCoU6eOQfvdv39/zM3NMTc3JyIigldeeUW3j97e3vj4%2BPDFF18wffp09u7dy9q1a6lduzZQdOZtv379DNpOWebPn8%2BiRYt0vzs4OPDaa68xdOhQ3TQvLy%2BefvppALZv346ZmRlTp07FxMQES0tLZs%2Beja%2Bvry55rVmzJpMnT8bExISWLVsSEBDAzp07SyXf99rX2bNnA0W3en3%2B%2BecBcHd3JyMjQ/dtg5eXF5s2bQLA0tKS%2BPh4tm/fjpeXFxMnTmTSpEkG90NZt7adMOEtgoLuf2vb8rrHdf0fOU899bBbYBjVkwXL8hcPDFK9euXErQw1a6oarhI%2BdhTFVTvwXb69rbAtW1QPqX46X6RRI5UD7tqlcsDbVq6snLhq8/J62C1Q1ZNWqVab6sm3ubk5H374IQMGDGDjxo3ULOc/b1tbW4xul7CKk%2BKnSrz7Gxsb61Wp69Wrp/vZysoKW1tbbt68SUJCAmlpabqkDkBRFLRaLampqUDRbUvLSrwBUlJSAHj22Wd100xMTHB0dCQhIeG%2B%2B1GcsCcnJ/PMM8%2BUmp%2BcnKx329SSd3VKSEjg%2BPHj/Oc//9FNKygooG3btqSnp6PRaHB0dNTNK9nGBzF37lwGDhx4z2VKti81NZVnnnkGkxLveMWvQ3HfODo66s13dHTkwIEDpeLea1%2BLlfwGxcTERO9i98bGxrrhLL6%2Bvmi1Wr788kuWL19O7dq1GT9%2BPK%2B88sq9O%2BC2sm5ta2lpR0aGQasbxNi4KPHOylL3n1dBgXqxipmYFCXeGRnqxle7UmdkVJR45%2BXBXUY2PRDL3L/VCwZFHVq9OmRmqv%2BCabXqxjM1LUq809NBxZPDC2oZdqvo8jAxUb87TTxc1Q3YtGlR4j1kCMTGqho6dou6HxQsLIoS7ytXiv6m1NJ0aulvgSukceOixHviRLh0Sd3Y48apF6tGjaLE%2B8cf4Z9/1IsL4OenbrxykOS7YirlO8X69esTHBzMtGnT9JK64mRMW%2BKN4s4TAo3K%2Bd1xUlKS7uesrCzS09OpW7cu%2Bfn51K9fn3379unNT01Npdbtr5Tuta26desCRePGi4c/FBQUkJiYqJc0303r1q2xtbVlz549pW5FGhsbS79%2B/fjiiy90sUq2xcHBgf79%2B/P666/rpiUmJmJpaYmNjQ0WFhbExcXx3HPPAXDjxo37tqeiSravbt26JCYmUlBQoHtNr127BhR96Lh8%2BTLJyckoiqJbLy4uTtenJd1rX8va9r1cuXKFFi1a0L9/f3Jzc9m3bx/Tp0/H3d1d9xreS1m3tk1Pr5zEtrBQ3bgq5kelFBSoG1/NBPnOuKrGrowXvjiu2rEr6wDIz6/cg%2BtRFR1dOXFjY1WPffsu2arLy1M5dkyMisFKuHRJ/di3v7lW1T//VE5c8ViqtJGnvXv3ZtCgQWzdulU3rXbt2tSoUYPdu3ejKAoxMTF6yfGD2LhxI5cvXyYnJ4eFCxfSrFkzWrZsibe3N9nZ2YSHh6PRaMjIyGD69OlMmjTJoGTO3t6ezp07s2DBApKTk8nNzSUkJISCgoIyr2xyJ3Nzc2bNmsWqVav4/PPPyc7OpqCggF9//ZWJEyfSo0cPXO4yrnDw4MF8%2BumnnDlzBoDff/%2BdgQMHsmvXLszNzenfvz8rV67kxo0bZGZm8sEHH9yzHSVPhFRD586dAQgJCSE3N5fk5GQWLlxI27ZtdQl2cnIya9asQaPREB0dzZdffsnLL79crn0trx9%2B%2BIG33nqL%2BPh4LC0tsbW1xdTUlOqP09f8QgghxCNOTrismEo9m2bmzJmcPn2ajNvf25ubmxMcHExoaCgbNmygZcuWDB48uEJXpOjWrRvjx48nPT0dDw8PVq9ejbGxMTY2NnzyyScsWbKE8PBwCgsL8fT0LNc49Pfff5%2BQkBAGDBjArVu3aN26NZs3bzb4RFI/Pz9q1qzJxo0bCQsLIy8vD0dHRwYNGsRrr7121/V69uzJrVu3mDlzJomJidja2jJy5EjdVWHeffddFi9ejJ%2BfH6ampgwfPvyu1xnv3bs3kyZNokuXLrqrglRU9erV2bRpE0uWLNEl4l27dmXatGm6ZYqvauPp6YmdnR3Tpk0r89rf99vX8hg%2BfDg3b97k5ZdfJisri7p167JixQocHBwefGeFEEIIoedJS5bVZqTc7fpvQggMuEx6uVTWOOrKGBlQScN%2BVT/Z1MgILC0hN1fdYSdWt1LVCwZFL76tLfz9t/rDTm5fQlU1pqZgZwfJyeqO%2BbZ3vP9C5VQpY75NVb50jotL0Umcrq6qDzuJPqXuW7iVVdEQ9dhYdYeduAxU%2BQzOFi2KTuLs00f9YSfz5qkXq1atorHZUVHqDzsZMULdeOWwY4f6MQcNUj/mo%2BoJvY6UEEIIIYR4EFL5rpjH4GrDQgghhBBC/G%2BQyrcQQgghhDCYVL4rRpJvIYQQQghhMEm%2BK0aGnQghhBBCCFFFpPIthBBCCCEMJpXvipHKtxBCCCGEEFVEKt9CCCGEEMJgUvmuGEm%2BhRBCCCGEwST5rhgZdiKEEEIIIUQVkcq3EEIIIYQwmFS%2BK0Yq30IIIYQQQlQRqXwLIYQQQgiDSeW7YiT5FkIIIYQQBpPku2Jk2IkQQgghhBBVRCrfQtxDzX3/UTlgTejZk6d%2B3gfp6aqFLRj8imqx7vTUU%2BrGM/lkg7oBa9eG/v2x3Pc1pKaqF7dhQ/ViAVSvDm3awPnzkJmpamjFp6uq8QCMAKWOnaoxTT7drGo8atUCPz9M9kRBWppqYaNPKarFArCygqZA7JZT5OSoGhoXVyOVA7rAqVM0HeIK0dGqha20Pg3ZpXqfNm%2BuXiwjIzAHND38UNTtAizUDVcuUvmuGKl8CyGEEEIIUUWk8i2EEEIIIQwmle%2BKkeRbCCGEEEIYTJLvipFhJ0IIIYQQQlQRqXwLIYQQQgiDSeW7YqTyLYQQQgghRBWRyrcQQgghhDCYVL4rRpJvIYQQQghhMEm%2BK0aGnQghhBBCCFFFpPIthBBCCCEMJpXvipHKtxBCCCGEEFVEKt9CCCGEEMJgUvmuGEm%2BhRBCCCGEwST5rhgZdiKEEEIIIUQVkcq3EEIIIYQwmFS%2BK0Yq35Xs6tWrD7sJ95WUlMStW7cedjOEEEIIIf7nPbbJ95UrV5g%2BfTpeXl64uLjQrVs3QkJCyM7OfthN0zl37hx9%2BvS55zIajYZ169bh5%2BeHm5sb7du354033iAmJkbVtsyYMYMZM2YAsHbtWsaMGQNASkoKPXr0IC0trcz1wsLCaNasGS4uLri4uPCvf/2LF198kc8///yBti2EEEKIx1thofqPynTr1i3eeecdPD09cXNzY9q0affMF%2BfOnUvLli11uY%2BLiwtbt27Vzf/444/x8vKidevWDBs2jMuXL5erPY9l8n3q1CkGDBhA3bp1%2Bfrrr4mOjubjjz/m9OnTjBo1ioKCgofdRAAyMzPRarV3nZ%2BXl8fQoUM5cuQIS5cu5cSJE3z33Xe0atWKoUOHcubMmUpp1/jx4wkPDwcgNzf3vlVvd3d3oqOjiY6O5rfffmPevHksXryYo0ePVkr7hBBCCPHoetyS7%2BDgYK5fv87%2B/fv59ttvuX79OiEhIXdd/vfffyc4OFiX%2B0RHRxMQEADAV199xWeffcaGDRs4duwYLVq0ICgoCEVRDG7PY5l8z5kzh/79%2BxMUFEStWrUAaNSoEStWrKB27drExcUB4OzszLFjx3TrRUZG4uPjA8CxY8fo3LkzU6ZMwd3dnfXr1zNjxgyCgoLo1asXbdu25dq1a6SkpDB16lQ6dOhAx44dmTNnDllZWboYPj4%2BrFmzhk6dOtGmTRsCAwPJysoiLi6OsWPHAuDi4kJ0dHSp/fjss8%2BIj49n7dq1NG/eHGNjY6pVq8Ybb7zByy%2B/zPnz5wHK3S6AAwcO4OvrS%2BvWrRk3bhzp6em6eWFhYQwbNoyCggJdZb5Pnz7s2bPnvn1vZGRE%2B/btcXJy4uzZswAoisL69evx8/PD3d0dDw8PpkyZQm5ubqn1NRoNS5cupVevXri4uNCuXTuCg4N1B%2B2wYcNYtmwZr776Ki4uLvTq1UuvXXFxcYwfPx43NzfatWvHvHnz0Gg0AFy7do3x48fj6emJt7c3K1as0M0TQgghxJMnJyeHqKgogoKCsLW1pXbt2kydOpXIyEhycnJKLa/RaDh//jwtW7YsM962bdsYMmQITZo0wcLCgilTppCYmKiXb97PY3fC5bVr17hw4QLz5s0rNa9OnTqsXr3a4Fg3btzgueeeY8mSJeTl5bFgwQKOHDnC1q1bcXBwwMbGhpdffpmGDRuyf/9%2BtFot77zzDnPmzGH58uUAJCQkcPPmTb777jtu3rzJq6%2B%2BypYtW3j99df5%2BOOPGT58eJmJN8DBgwfp0qULNjY2peZNnz5d7/fytOvy5ctMnDiRRYsW0bt3bw4dOkRQUBB9%2B/bVi2liYsKuXbvo2rUru3btol69evftM0VROHHiBPHx8XTu3BmAvXv38umnnxIREUHDhg25dOkSQ4YMISoqipdeeklv/c2bN3PkyBE2b96Mvb090dHRDB06lG7dutGuXTug6MDetGkTzz//PB999BFz5syha9eumJiYMHr0aDw9Pfnxxx/Jzc1l9OjRhIWF8cYbbzBy5Eh8fX1ZuXIlaWlpBAUFUVhYyJQpU%2B67X1A09j05OVlvml1BAfZ16hi0vkGeekr/%2BUlUu7a68WrU0H9WS/Xq6sazttZ/fhLdLpaoppJeeysrVcNhYaH/rCoXF3XjNW2q/6ySx6lPjYzUj6VmzEdBZVSqy3wPtrPD3t7%2Bvuvm5uZy8%2BbNMufl5OSg1WpxcnLSTWvcuDG5ublcvXqVZs2a6S0fGxtLfn4%2BoaGhnDx5kurVqzNo0CDGjBmDsbExFy9e1BVXAczMzGjYsCGxsbG0bdvWoH197JLv4rHJdVRKiPz9/TEzM8PMzAyA1q1b616gM2fOEBMTw6ZNm6hWrRpQlBT37NmT2bNn62JMmDABS0tLGjRogKenJ1euXDF4Xzw8PAxatjzt2rNnDy1bttQl2926dcPb29ug7ZTl5MmTuLu7A0UHuFarpW/fvjRo0AAALy8vXF1dcXBwIC0tjfT0dGxtbcv8Qxg8eDADBgygdu3aJCUlkZubS7Vq1fSW7dGjB82bNwdgwIABrF27ltTUVOLj40lISGDmzJlYWVlRrVo1Vq1aRWFhIYcOHUKj0TB58mSMjIxwdHRk4sSJBAUFGZx8b926lVWrVulNe2vCBAKHDn2gfrun9u1VDWeiarQ7YqsdvH9/lQPeVoFjvErdpZpSEZX1vq56wuDnp3LA27y8VA2nbtr5/xo1qoSgp05VQlBgyxZVwz2g718vAAAgAElEQVRWfVoJbqcY4h7KfA9%2B6y0CAwPvu%2B7p06cZPnx4mfMmTpwIgHWJwofV7U%2BDZY37zszMpE2bNgwbNozly5fzxx9/MGHCBIyNjRkzZgzZ2dm69YtZWlqW68IVj13ybWdnB0BycjINGzYsNT8lJaVcifmdn6hK/h4fH09BQYGuwlvM3NxcN7SlZJug6BOQoeN%2B7OzsSEpKKnPeP//8g5WVFebm5uVu182bN3nmmWf05tWvX19v6El5uLm58dlnn%2Bl%2BP3/%2BPFOnTmXq1KmEhoaiKAorVqzghx9%2BoFatWjRr1gytVltmP%2BTk5PDee%2B9x4sQJHBwcaN68OYqiUFjiY3TJ/jQ1LTpECwsLSU5OpmbNmnoHfXG1fv/%2B/aU%2BzCiKglarJTU1ldoGVFsDAgJ0w5J0bYmOhn377ruuwZ56qijx/vlnyMhQLWxB956qxSrJxATUPoXCJOprdQPWqFGUeP/wA/zzj3px7/gbqjBr66LE%2B%2BxZUPnqQopHG1XjQVHiXY4hjIbF3BWlbsAaNYoS7x9/VPW1j22i7ocEC4uiJPHKFcjLUzU0TYe4qhywaVHiPWQIxMaqFjZ2i7ofEiqzT597Tr1YRkZFibdWq/7f0%2B304KGojMp3me/BJfKBe/H09OTPP/8sc965c%2BdYuXIlOTk5uoJl8XCTskYedOjQgQ4dOuh%2Bb9WqFSNGjGDPnj2MGTMGKyurUsNqiwuJhnrsku%2B6devi5OTEnj17SlWNU1NT8fb2ZvHixfTp0wdjY2O9Ex7LSj6N7ijtlPzdwcEBS0tLjh07hsnt8p9GoyEuLo4GDRpw8uTJCu2Lj48P4eHhZGVllToA3n33XXJyctiwYUO52%2BXg4MChQ4f04t24cQMLlb6fc3Jy4qWXXmLZsmUAhISEkJiYyMGDB3X74XeXCtesWbOoUaMGP/30ExYWFhQWFhpc/XdwcCA9PZ2cnBxdAv7rr79y9uxZHBwcqF%2B/PvtKJMpZWVmkpqbqzgu4H3t7%2B9Jfb505Aw/4oeWeMjIqJ%2B7jIDW1cuL%2B84%2B6sdUedlLs1i3IzKyc2I%2B6u1xVqcL%2B%2BUfV2GUMA1VFXl4lxL7LsMYKi41VNfbj1KdqJ8nFMSsj7sNSGcl3me/BKmjUqBFmZmZcvHiRf/3rXwBcunRJN1zkTt9//z0pKSm8/PLLumkajQZLS0sAmjRpwoULF3QjCrRaLVevXtUb1nI/j%2BUJl7Nnz2bHjh2sWrWK9PR0FEXhjz/%2BYPz48bRo0YIePXoARWN69u/fT35%2BPteuXWP79u3l2k6rVq1o0KABS5YsITs7m9zcXBYtWsTIkSMNuqJKcbKbeZc32iFDhlCnTh3eeOMNYmNjURSF9PR0li1bxn//%2B1%2BCgoIeqF19%2B/bl/PnzbNu2jfz8fH766Se%2B%2B%2B67e7ax5Mma93Pjxg127tyJm5ubbl0LCwtMTEzIy8tj48aNnD9/vswrvRQva2xsTFZWFu%2B//z5ZWVn3vCpMyf1u2LAhS5cuJScnh5SUFBYvXkxaWhre3t5kZ2cTHh6ORqMhIyOD6dOnM2nSpFIfsIQQQgjxZLCysqJXr16EhISQlpZGWloaISEh9OnTR5dQl6QoCosXL%2BaXX35BURSio6P59NNPdVc7GTRoEBEREcTGxpKXl8eyZcuoU6eObniuIR7L5LtNmzZERERw7tw5fH19cXV1JSgoiLZt2xIeHq4bvz137lxiYmJo06YNb7/9Nv7%2B/uXajqmpKevWrSMlJYUXX3yRjh07cu3aNTZt2mRQFdnJyQk3Nzc6derE4cOHS823sLDg888/p2XLlgQFBeHm5oavry%2BXLl0iIiJC9wnt/9i787ia8v8P4K/2GtlKGzWYMFlHacFQhKwhW2PP19hJ9j2GKNkJmRSG0IyxlH0wgwkxxFjG1gyTolImldJ2f3803XHd4vp1buc083o%2BHj2451yfXm7de9/3c97ncz40l5WVFYKDgxEeHo4WLVpg06ZN6NSpU4lj1ahRA506dYKnpyf27NlT4n1%2B%2BeUXhbUu%2B/Tpg3r16slnvn18fJCTk4PWrVvD1dUV169fR69eveSrtbxp/vz5uHv3LhwdHdGlSxdkZmaibdu2Jd73bTo6OggODkZSUhLatWuHXr16wcHBAd7e3jA0NMT27dsRExMDZ2dndOzYEZqamti8efN7xyUiIiLVVbSlBhcuXIg6derA3d0dXbp0gaWlJXx9feX7u3fvjuDgYABAp06dMGfOHCxatAi2traYMWMGJk2ahF69egEoOlfQy8sLEyZMQMuWLXHnzh1s2bJFXnuqQkP2IQsTEv3XlPKB5P%2BtenWgS5eiPnIB204KBgwUbKw3qaXne3uosAMaGxedxHnwoLBtJyUcjiyTypUBR0fg8mXB205krh0EHQ9QU8/3NzuEHdDIqOgkzqgoQdtOYpsNF2wsoGilDxubok4OoVskbO0EPrJna1t0EqednaBtJ7HXhP1lUudj%2Bvf5/oLQ0Cjqzc7NFf75pJbVc1Q0b57wYy5dKvyYUlXher6JiIiISDzqnqn%2Bt2PxTUREREQqY/FdNhWy55uIiIiIqCLizDcRERERqYwz32XD4puIiIiIVMbiu2zYdkJEREREVE44801EREREKuPMd9lw5puIiIiIqJxw5puIiIiIVMaZ77Jh8U1EREREKmPxXTZsOyEiIiIiKiec%2BSYiIiIilXHmu2w4801EREREVE44801EREREKuPMd9mw%2BCYiIiIilbH4LhsNmUwmEzsEkVS9eCHseFpaQJUqwMuXQEGBsGMLTV1ZNQVudtPUBCpXBjIyhH1DqJqfKtxgQNEDWq0a8Ndfwv/wc3KEHU9HBzA1BZKTgbw8wYbNM60l2FjFdHQEjVg0ZoO6wg7YuDFw%2BDDQowdw%2B7agQ8fu/0PQ8QwMABsb4O5dIDtbuHFt7TSEGwwAbG2Ba9cAOzsgNlbYsV%2B%2BFG4sTU2gUiUgK0v4irVyZWHH%2BwBjxgg/5pYtwo8pVZz5JiIiIiKVcea7bHjCJRERERFROeHMNxERERGpjDPfZcPim4iIiIhUxuK7bNh2QkRERERUTjjzTUREREQq48x32XDmm4iIiIionHDmm4iIiIhUxpnvsmHxTUREREQqY/FdNmw7ISIiIiIqJ5z5JiIiIiKVcea7bDjzTURERERUTjjzTUREREQq48x32bD4JiIiIiKVsfguG7adEBERERGVE858ExEREZHKOPNdNpz5JlE8evRI7AhERERE5Y7FdwXx6aefolmzZrC1tUXz5s3h4OCAcePG4enTp4KMv3//fri6ugoy1vvcuXMHPXr0UOm%2BX375JYKDg9WciIiIiFRVWCj8138J204qkJCQEDg5OQEAMjMzMX36dMyYMQO7du0SOdmHycjIQF5enkr33bp1q5rTEBER0Yf4rxXLQmPxXUEZGhpiwIABmDp1qnxbXFwcAgMDce/ePaSlpcHS0hIzZsxA%2B/bt8eTJE3To0AF%2Bfn7YvHkz0tPT0axZM/j7%2B8Pc3Fxh7NzcXEyYMAGvXr3Cli1bsG3bNsTGxiI9PR3x8fHYuHEjZs2ahYkTJ6JPnz4AgJiYGAwbNgz37t2Tf6/58%2BcjODgYOTk5cHV1xcKFC/HixQuMGjUKAGBra4uwsDA0bdoUGzduxP79%2B5GRkYGGDRtiwYIFsLGxwdChQ%2BHo6IhJkyZBJpNh586dCA8PR2pqKho0aIC5c%2BeiSZMmAIATJ05g/fr1ePbsGUxNTeHu7o7x48er/JgmJycjJSVFYZu%2BvglMTEz/Xz%2BjkmhqKv4pZerKqqEh7Hhqe0y1tNQzntDjAoCOjrDjaWsr/vlf07ixsONZWyv%2BKSADA2HH09NT/FMwtrbCjmdjo/inkIR8MalIL/pUbv6jr6wVX3p6Oo4cOQI3Nzf5tkmTJqFDhw4ICgqCTCbDypUrsWjRIrRv315%2Bn59%2B%2BgkHDx5Ebm4uRowYgU2bNmHx4sXy/Tk5OZgwYQI0NDQQGhoKfX19AMDFixcRFhaGZs2aQU/FV%2BWTJ08iKioKBQUFmDBhAr766iusWLECISEhGDZsGGJjYwEAGzZswOHDhxEaGoq6desiKCgIY8aMwZkzZxTG2717N7Zt24bNmzfD2toahw4dwogRI3Ds2DEYGhpixowZ8qMDd%2B7cweDBg9GmTRs0a9ZMpbwREREICgpS2DZhwkR4e09S6d9/CENDwYdUm4qStVIloUesJvSARSpXVs%2B46mBkJOhwAn9E%2BGdcoQc%2BfFjgAf%2B2bp3gQ6qh9AQA1K0r8IDXrgk84N9271bPuEIT%2BlOSyDjzXTYsviuQsWPHQktLC4WFhcjKykLlypWxZcsW%2Bf4tW7bAzMwMMpkMCQkJqFKlCpKSkhTGGDVqFKpUqQIAcHV1lRfAQNGM99ixY/HixQt899130NXVle%2BzsrJCq1atPijvnDlzYPT3m7e3tzfGjRuHpUuXKt3vwIEDGDNmDOrVqwcAGDduHFxcXCCTyRTuFx4ejjFjxsDm75mOfv36Yd%2B%2BfYiMjMSgQYOgr6%2BPffv2obCwEHZ2drh69So0P2C2wdPTU6nvXV/fBC9fftB/%2B500NYuK2cxM6b94qSurOma%2BK1UCsrKEzVm54C/hBgOKZrwrVwYyMoCCAmHHzs0Vdjxt7aLCOy0NyM8XbNi86sIdRSqmowOo2MWm%2Bpgeqp2TojJr66LCe/JkIC5O0KHvrhT2g4KeXlHh/ccfwOvXwo1rM8hOuMGAohnv3buBQYOAu3eFHfv8eeHG0tQsKryzs4V/0Rd%2BxoHKCYvvCiQ4OFje852Tk4Pw8HAMHz4cERERaNy4Me7evYvx48cjJSUF1tbWMDIyUipga9SoIf%2B7tra2wv6UlBTY2NggLi4Ot27dgp3dPy%2BWpqYf/qZZu3Zt%2Bd8tLCyQm5uLv/5SLmhSUlJQs2ZN%2BW1dXV00b95c6X4JCQlYvnw5Vq5cKd%2BWn5%2BPJk2aQF9fH3v27MGmTZswbdo0ZGZmonPnzpg/fz6qVq2qUl5TU1Ol/%2BeLF8LXSUDRa7A6xlUHobOq6%2Bir4CftqOsHVFAg/NhCV5/F8vPVN7aU3b6tnnHj4gQfOztb0OHkXr8WeOw3JnoEdfeu8GOrY2bkX3ZW4b/ovyIKNiFVUPr6%2Bhg5ciQqVaqECxcuICkpCZMnT8aUKVNw6dIlhIeHq7yiSDFTU1OEhIRg6NChmD17Nl69eiXfp/HWdKWmpqbCSZMvXrxQGu/NWfcnT57AwMAA1atXV7qfhYWFwqoteXl5WLZsGZKTkxXuZ25uDj8/P/zyyy/yr8jISHh7eyMzMxPJyclYtWoVLly4gIiICNy6dYsrpRAREQmMq52UDYvvCio/Px/ff/89Xr58iRYtWiArKwsFBQUw%2BLuv7OHDh9i4cSOAonYSVejo6EBDQwM%2BPj7Q1NTE8uXLS72vtbU1Tp8%2BjZycHKSkpOCbb75Rus%2BqVauQmZmJpKQkrF%2B/Hr169YKOjo68ZzwjIwMA0KdPH4SGhuKPP/5Afn4%2BtmzZglOnTikV6gMGDMDmzZsR9/dh2/Pnz6N79%2B64cuUKsrKyMGrUKERFRUEmk8HU1BSampolFvtEREREYmHbSQUyatQoaP29UoKGhgbq1KmD1atXy9tDZs6ciRkzZiA7Oxvm5uYYMGAAVqxYgfv376NaNdVPHtPT04O/vz8GDx6MDh06lHif6dOnY9GiRfj8889hamqK4cOH4%2BrVqwr3%2Bfjjj9GjRw9kZ2fD3d0dM2bMAAA0aNAALVq0QNu2bbFu3Tp8%2BeWXyM/Px8iRI5Geno6mTZsiJCQEOm%2BdReXl5QWZTIbx48cjOTkZZmZm8PX1lWdcv3491q5dC19fX%2Bjr66Nbt27w8vJS%2Bf9NRERE7/dfm6kWmobs7aZgojIqXmrw9OnTsLS0FDtOmZTQTVMmWlpAlSrAy5fS7/lWV1ahe741Nf85j1HIN4Sq%2BanCDQYUPaDVqgF//SX8Dz8nR9jxdHQAU1MgOVnQnu8801qCjVVMLSdcNhB4qY/GjYtWUOnRQ/Ce79j9fwg6noFB0bmMd%2B8K2/Ntayfwmda2tkUrqNjZCd/zLfRZ9uo4IxwQdeWkzp2FH/PECeHHlCrOfBMRERGRyirazPerV6%2BwZMkSnDlzBvn5%2BejQoQMWLlyISiWsGOPr64uoqCiFbTk5OWjdujVCQ0NRWFiIFi1aQCaTKZwPFx0djY8%2B%2BkilPCy%2BiYiIiEhlFa34XrJkCZ4%2BfYoTJ06goKAAPj4%2BWLlyJRYuXKh038WLFytc/%2BTnn3/GtGnTMHv2bABF59Tl5eXh2rVrCksyfwiecEmCs7S0xL179yp8ywkRERFVbNnZ2YiKioK3tzeqVasGY2NjTJ8%2BHfv370f2e3qr0tLSMH36dMybNw/169cHANy8eROffvrp/7vwBjjzTUREREQfQB0z38nJyUhJSVHYZmJiotJ1RnJycpQuKlgsOzsbeXl5aNCggXybtbU1cnJy8OjRIzRs2LDUcVeuXIkmTZqgZ8%2Be8m03b97E69ev0bdvXyQkJMDa2hrTpk1TuDbK%2B7D4JiIiIiKVqaP4joiIQFBQkMK2iRMnYtKkSe/9tzdu3MCwYcNK3Dd58mQAUOjHLl6WOSsrq9Qx4%2BPjERkZie%2B%2B%2B05hu76%2BPpo1a4bJkyejatWqCA8Px8iRIxEZGQkrK6v3ZgVYfBMRERGRyDw9PeHq6qqwzcTERKV/6%2BTkhHv37pW4786dO1i3bh2ys7PlJ1gWt5sYGhqWOub3338PW1tbpZnx4t7vYiNHjsT%2B/ftx9uxZDBkyRKW8LL6JiIiISGXqmPk2NTVVqcXkQ9WtWxc6Ojp4%2BPAhPvvsMwBAXFwcdHR0UKdOnVL/3cmTJ/G///1PafuaNWvQuXNnNGrUSL4tNzdXfgFBVfCESyIiIiL6VzIwMEDXrl2xcuVKpKWlIS0tDStXrkSPHj2gr69f4r958eIF4uLi4ODgoLTv/v37WLp0KVJSUpCbm4ugoCBkZmaiU6dOKmdi8U1EREREKissFP5LnRYuXIg6derA3d0dXbp0gaWlJXx9feX7u3fvjuDgYPntJ0%2BeAADMzMyUxvL398fHH3%2BMXr16wcnJCZcvX8a2bds%2B6EribDshIiIiIpVVtHW%2BDQ0NsWTJEixZsqTE/UeOHFG43bRp01J7yKtVqwZ/f/8y5eHMNxERERFROeHMNxERERGprKLNfEsNZ76JiIiIiMoJZ76JiIiISGWc%2BS4bFt9EREREpDIW32XD4pvoHapXk6lhVA1UqSzsuNk5GoKOBwAafw%2BpqwvIBIxrUFj65Xz/XzQ1ARigsna2sO8IH1URbqw3/X2FNUEZGQk/JgCoeHU5VekUFgg6XhEt6GgKPO6iRcKOV/zzGTMGSEsTdOg3rvMhiOLn/SefCPu8x8uXAg6Gv5/3AM6fF74SrCLgc9/WFrh2DWjbFoiNFW5cQOAfEJUnFt9EREREpDLOfJcNT7gkIiIiIionnPkmIiIiIpVx5rtsWHwTERERkcpYfJcN206IiIiIiMoJZ76JiIiISGWc%2BS4bznwTEREREZUTznwTERERkco48102LL6JiIiISGUsvsuGbSdEREREROWEM99EREREpDLOfJcNZ76JiIiIiMoJZ76JiIiISGWc%2BS4bFt9EREREpDIW32XDthMiIiIionLCmW8iIiIiUhlnvsuGM9//Qb6%2BvrC1tYWtrS2aNm0KGxsb%2BW1bW1v88ssvgn4/Z2dnHDp0qMR9Bw4cQM%2BePQX9fkRERERSxZnv/6DFixdj8eLFAID9%2B/cjKCgIZ86cESWLh4cHPDw8RPneRERE9OE48102nPmmEmVkZGDu3Lno1KkTmjdvDmdnZ3z99dcAgN9//x22traIiIiQ37dDhw5Yu3btB3%2Bf7777Dp06dZLfvnnzJoYOHQoHBwe4ublhx44dkMlkAIA1a9bAx8cH06ZNQ4sWLeDi4oI1a9bI/%2B2lS5fQp08f2Nvbw83NDQEBASgoKCjLw0BERERvKSwU/uu/hDPfVKLAwEAkJSVh//79MDQ0xLFjxzB16lR069YNn3zyCebNm4elS5eiTZs2CAwMRM2aNTFp0qQyfc9nz55h%2BPDhmDlzJrZt24bff/8d48ePx0cffYT%2B/fsDAI4fP44VK1YgMDAQZ8%2Bexbhx49CxY0c0bdoUM2bMwPTp09GrVy/Ex8dj4MCBsLe3R8eOHVX6/snJyUhJSVHYZlKjBkxNTcv0/yoPGhrqG1PwsTUF/sz/ZlChx6b/JiMjYcerWlXxTwEJ/fysMM/74vHU8Zy3tRVuLBsbxT%2BJwOKbSjF58mRoa2ujUqVKePr0KXR1dSGTyZCcnAxLS0v069cPFy5cwNChQ/H69WscOHAAWlpaZfqeBw8ehI2NDb744gsAQIMGDTBixAiEh4fLi%2B969erB3d0dAODq6gpjY2M8evQITZs2hYGBAY4dO4aqVavCwcEB586dg%2BYHvDBHREQgKChIYdvECRMwydu7TP%2BvEgn8zqavL%2BhwCvT0hB7RQOgBi6jzQRCSjo7YCVQndAVWxteIchv379cYwTk7Cz6kruAjFhH811S3ksAD/s1ADa8n164JP%2Bbu3cKPKaL/2ky10Fh8U4meP3%2BOZcuW4bfffoOVlRUaN24MACh84xk3ZMgQHDlyBH379hVkdjghIQG//vor7O3t5dsKCwuhq/vP20uNGjUU/o22trY80zfffIMNGzZg4cKFSE1NRdu2bbFo0SKYmZmp9P09PT3h6uqqsM2kRg3g77YXwWhoCD5mzmvhp741NIoK79evhY2rL8sWbjCgKKi%2BPpCTI2xQbTW8POroAHl5wo%2Brjqxq%2BD1Vyzu2lhYgdHvZ0aPCjle1alHhfe4ckJ4u6NC5nYX9oKCh8c%2BvqZA/ft28LOEGA4pmvA0MgOxs4X%2Bv2rYVbiwbm6LCe9Ag4O5d4cYF1PMhgcoFi28qkbe3N7p27YqwsDBoa2vj%2BfPn%2BPbbb%2BX7X79%2BjYULF6Jnz544cuQIunbtirZlfMEyMzPD559/ji1btsi3paWlITv7/cVaTk4O4uLisHjxYmhpaeH333/HvHnzsHz5cqxevVql729qaqr8IULo4kNN1BlTJhN4fKHfKIuPbshknI4hYaSlqWfc9HTBx1bXc1/yz/s3xxV67NhYYccDigpvdYwrEr7Ulg0bJKlEGRkZ0NPTg5aWFlJTU%2BHn5wcAyPt71i4wMBCamppYunQpfHx8MHv2bKSmppY63suXL/Hs2TOFr9zcXIX79OrVC1euXMGRI0eQn5%2BPpKQkjBkzBoGBgSplnjJlCnbs2IGCggKYmJhAW1sb1atX/38%2BAkRERFQSnnBZNiy%2BqUQBAQGIjIyEnZ0d%2BvXrB0tLS3z66ae4f/8%2BfvzxR3z77bdYvnw5dHV1MXz4cNStWxezZ8%2BWr0zyNj8/P7i4uCh8vb2euJWVFUJCQhAeHo7WrVujd%2B/eqF%2B/PpYuXfrevPr6%2Bti0aROOHz8OR0dHdOzYERYWFpgyZYogjwcRERGREDRkpVVLRKSeY7pq6KXNzlFPz7c6WqkNCitI76euGk5lY8%2B3sOMB6un53rVL2PGMjIpO4oyKErzt5PUXwwUdT0Oj6Fc/N1fYH79eboZwgwFFz/tKlYCsLOF/r6pUEW4sW9ui3mw7O%2BHbTkQs34yNhR/zHQfP/3U4801EREREVE54wiURERERqey/1qMtNBbfRERERKQyFt9lw7YTIiIiIqJywplvIiIiIlIZZ77LhsU3EREREamMxXfZsO2EiIiIiKiccOabiIiIiFTGme%2By4cw3EREREVE54cw3EREREamMM99lw%2BKbiIiIiFTG4rts2HZCRERERP962dnZ8PT0xP79%2B995vxs3bqB///6wtbWFq6srvvvuO4X9Bw4cQKdOndC8eXP06dMHsbGxH5SDxTcRERERqaywUPgvdXvw4AEGDx6M69evv/N%2B6enpGD16NHr37o0rV65g6dKl8Pf3x6%2B//goAiImJwZIlSxAQEIArV66gZ8%2BeGDduHLKzs1XOwuKbiIiIiP61Ll68iOHDh8PDwwM1a9Z8531PnjyJatWqYfDgwdDW1karVq3g7u6O8PBwAMB3332H7t27o0WLFtDR0YGXlxeqV6%2BOo0ePqpyHPd9EREREpDJ1zFQnJycjJSVFYZuJiQlMTU3f%2B29zcnKQlJRU4j4TExPY2Njgxx9/hJ6eHrZt2/bOsR48eIAGDRoobKtXrx727dsHAHj48CH69u2rtP/u3bvvzVmMxTfRu2hoCDpccnIyIiIi4OnpqdILiqoMDAQbSi45ORkhIcJnBSoJONbfj%2BnWrWrIKSx1/ezVQW1ZtbSEGwtqzDl8uHBj4e%2BcGzao5WevJ%2BhoanxM9SoLNxb%2BzhkWpp7nk0wm2FDyn/3x45J/3n8IAR8iuQ0bIhAUFKSwbeLEiZg0adJ7/%2B2NGzcwbNiwEvdt3LgRHTt2VDlHVlYWDN56U9XX18erV69U2q8Ktp0QlaOUlBQEBQUpfbqXooqSlTmFV1GyMqfwKkpW5vz3KT4R8s0vT09Plf6tk5MT7t27V%2BLXhxTeAGBgYICcnByFbTk5OahUqZJK%2B1XBmW8iIiIiEpWpqakkjg40aNAA0dHRCtsePnyI%2BvXrAwDq16%2BPBw8eKO13dnZW%2BXtw5puIiIiICECnTp3w/PlzbN%2B%2BHXl5ebh06RKioqLkfd79%2BvVDVFQULl26hLy8PGzfvh2pqano1KmTyt%2BDxTcRERER/Wd1794dwcHBAIDq1asjLCwMx48fh5OTE%2BbPn4/58%2BejZcuWAIBWrVph4cKFWLRoERwdHXHkyBGEhISgWrVqKn8/rUWLFi1Sx3%2BEiEpWqVIlODo6flB/mFgqSlbmFF5FycqcwqsoWZmT/j%2BGDx%2BOhg0bKmwbPHgw7O3t5bfNzMzQr18/jBkzBsOGDVO6v42NDYYMGYKxY8diwIABMP4rvO8AACAASURBVDc3/6AMGjKZOs5ZJSIiIiKit7HthIiIiIionLD4JiIiIiIqJyy%2BiYiIiIjKCYtvIiIiIqJywuKbiIiIiKicsPgmIiIiIionLL6JiIiIiMoJi28iIiIionLC4puIiIiIqJyw%2BCZSo3HjxpW4fciQIeWchKh0N27cKHH7uXPnyjnJh8nMzERubq7YMd4rLi4OSUlJYsd4r7S0NLEjEP0nsPgmEtiTJ08QFBSEoKAg/Pzzz/K/F38FBATg3r17YscsUVxcHPz8/DBx4kS8ePECu3btEjtSib799lu4u7vDyckJiYmJ8Pb2RlZWltixlHh5eSEqKgqvX78WO8o7jRgxQmlbZmYmJk%2BeLEKa0sXFxWHChAkAgB9%2B%2BAEtW7ZE27ZtcfXqVZGTKbp27Rp69%2B4NANi7dy%2B6d%2B%2BODh064NSpUyInU5afn481a9agRYsWcHV1RXx8PPr27Yvk5GSxo1VIMpkMZ86cAQAkJSVh2rRpWLp0qSRfn0g8LL6JBFazZk08ePAAMTExKCgoQExMjMLXw4cPsXDhQrFjKomOjsaAAQPw4sULXLhwATk5Odi4cSO%2B/vprsaMp2L59O0JDQzF06FAUFBSgUqVKSE5Ohr%2B/v9jRlLRu3RrBwcFo06YNfH198euvv4odSe7x48do0qQJGjZsiFevXqFhw4YKXw4ODmjUqJHYMRUsW7YMVapUgUwmw%2BrVq%2BHt7Q1vb28EBASIHU3BqlWr0K5dO8hkMmzZsgUBAQEICgrCunXrxI6mZMOGDbh06RLWrVsHHR0dGBsbw9zcHEuXLhU7Wolu3boFAHj58iVWrFiB0NBQ5Ofni5zqH4GBgfLX96%2B%2B%2BgpPnz7F3bt34efnJ3IykhQZEanNvHnzxI6gsj59%2Bsh%2B%2BuknmUwmk9nb28tkMpns119/lbm6uooZS4mbm5vs4cOHMplMJnNwcJDJZDJZUlKSrHXr1mLGeqcbN27IFi1aJGvZsqWsW7dusrCwMNnz58/FjiW7c%2BeO7NKlS7JmzZrJYmJiFL6uX78ue/XqldgRFXz%2B%2Beey3NxcWXx8vKxRo0ayjIwMWWFhoczW1lbsaApatmwpKywslD18%2BFDWpEkT2evXr2UymUzWvHlzkZMpa9%2B%2BvezZs2cymeyf51N6errM0dFRzFgl2rRpk8zOzk4mk8lkM2bMkHXt2lXWvXt3mZ%2Bfn8jJ/uHm5iaLj4%2BXZWVlyRo3biz7448/ZC9fvpQ5OTmJHY0kRFvs4p/o38zPzw%2B5ublIS0tDYWGhwr6aNWuKlKpkjx8/hrOzMwBAQ0MDANC0aVOkp6eLGUvJixcvULduXQBFh3gBwNjYWFKzX29r1qwZmjRpAldXV6xZswbLly/H2rVr4erqilmzZsHc3FyUXA0bNgQAHD58GFZWVqJk%2BBD5%2BfmQyWSIjo5G48aNYWhoiLS0NOjp6YkdTYGWlhaysrJw7tw5NG/eHLq6ukhISIChoaHY0ZS8evUKRkZGAP55Punr60NTU3oHxg8fPozw8HDk5ubixIkTiIiIgImJCXr27Il58%2BaJHQ9A0euTpaUlzp49CxMTE9SpUweFhYWSfn2i8sfim0iNjh8/jgULFiAzM1O%2BTSaTQUNDA7/99puIyZTVrFkT165dQ4sWLeTbbt68CQsLCxFTKbOxsUFERAQGDhwo/5Bw9OhR1K9fX%2BRkJbtz5w4OHTqEI0eOID8/Hz169ICfnx/Mzc2xcuVKjB07FgcPHhQ1o5GREUJCQvDo0SOlD4lSaudp3bo1Jk2ahLt372LkyJGIj4/HzJkz4eLiInY0BR07dsSQIUOQkJCA%2BfPn4%2BHDh5gwYQJ69OghdjQlzZs3R1BQEKZMmSJ/Pu3cuRNNmzYVOZmy5ORk2NjY4OLFi6hcuTJsbGwAANnZ2SIn%2B4elpSWioqJw9OhRtGnTBjKZDDt27IC1tbXY0UhCNGTFH3WJSHDdunWDm5sbPDw8oK2t%2BFm3Vq1aIqUq2ZEjR/DVV19h4MCB%2BOabbzB%2B/Hjs3LkTU6dOlZ88JgW3b9%2BGl5cXrK2tcevWLbRq1QrXr1/H1q1b8dlnn4kdT0GPHj3wxx9/oFWrVujTpw86duwIXV1d%2Bf4HDx7giy%2B%2BEP2EQW9vb8TGxsLJyQk6OjoK%2B6RUfGdlZSEsLAx6enoYPXo07t69i3379mHatGkwMDAQO55cQUEBDh48CAMDA3Tr1g2PHj3Cjz/%2BiGHDhkFLS0vseAri4%2BMxfPhw5OfnIzU1FbVr10ZWVha2bduGTz75ROx4Cnr06IGFCxdi3759KCwsxIoVK3D48GGEhITg0KFDYscDAFy6dAkzZ86EgYEBvvnmG8TFxWHKlCnYvHkz7OzsxI5HEsHim0iNbG1tceXKFaXCW6rOnj2L8PBwJCQkwNzcHAMGDEDnzp3FjqUkKSkJkZGRSExMhLm5Odzd3SXXxgMAmzdvRp8%2BfWBmZlbi/tzcXGRnZ6Nq1arlnEyRk5MT9u3bJ/nWk9DQUIwcOVJp%2B9q1a%2BHj4yNCon%2BH7Oxs/PTTT/Lnfbt27STZInPixAnMnDkT%2Bvr62LNnD5KSkjB69Ghs2LAB7dq1EzteiYpXOpJaaxSJi8U3kRoNGTIE8%2BfPlx8elbIlS5ZgypQpknzTrahat26NkydPSv4xdXZ2xqlTpxRm5aUiLS0NcXFxAIBRo0Zh69atePNtKyMjA9OmTUNsbKxYEZWcPXsWfn5%2BSEhIwNtvsVJrN8vNzcXGjRvRr18/WFlZYceOHXjx4gW8vb0l2ff9ZjGbmZmJV69ewdTUVORUim7fvl1iC5e7u7tIiUhqKsZ0HFEFZWdnBy8vL3Tp0gU1atRQ2Ddx4kSRUpUsKioKc%2BbMETvGe1WkwqZq1apITk6WfPE9aNAgBAQEYOLEifKT76RCV1cX3t7eePHiBQDlC1Tp6urC09NTjGilWrx4Mdzc3ODi4iLJAvZN/v7%2BuH79uvwxbNy4MQICApCbm4uZM2eKnE5ZVlYWIiMjkZCQgMmTJ%2BP27duSKr7Xrl2L4OBgGBsbKxzx1NDQYPFNcpz5JlKjoUOHlrhdQ0MD33zzTTmnebfly5cjKysLHh4eMDU1lZ98BUhrZZYOHTqUWtg4OjqKlKpkPj4%2B%2BPnnn2FnZ6f0mC5ZskTEZIpcXV2RmJiokK%2BYlD7QdOnSBcePHxc7xnu1aNECly9fllx/d0k%2B//xzREVFKXzoev78OXr37o2ff/5ZxGTKbt%2B%2BjREjRuCTTz7BvXv3EBkZie7du2PhwoXo27ev2PEAAO3bt4evry/at28vdhSSMM58E6nRzp07xY6gsm3btgEounokUPQBQYors/z111%2BYPn16hShsdHR05G/CUr7KpdQuUlOailB4A0UF2NmzZ%2BHq6ip2lPd6/fo1PvroI4VthoaGklwaz9/fH7Nnz0afPn3g4OAAKysrbNy4Ef7%2B/pIpvjMyMiTbf07SwZlvIjV61xJyUlpBBAASEhJK3SellVmmT5%2BObt26VYjCpqJJT09HfHw8GjVqhPz8fMn1gD948ACBgYEl9tOePn1apFTKfv31VwwaNAj16tVDlSpVFPZJ7YjX2LFjYWZmhnnz5kFXVxevX7/G8uXL8ezZM2zatEnseAocHR1x8eJFaGlpwdHREZcvXwZQdKRB7BWDik2bNg0dOnRAt27dxI5CEsaZbyI1Wr9%2BvcLt9PR0ZGdno0WLFpIrvmvVqoWsrCycPXsWCQkJMDU1Rfv27ZWKB7ENGzaswhQ2ABAeHo69e/ciISEBJiYm6NevH0aNGiV2LAVZWVnw9fXFkSNHoK%2Bvj/3792PEiBGSW27O19cXBgYGGD16tKRXEPL19YWtrS3s7e0lf4Rm3rx5%2BPLLL2FnZ4fq1avLL2IVHBwsdjQlRkZG%2BP333xXW9P/999%2BVzqcRU2FhIaZPn47NmzfDxMREYV9YWJhIqUhqpPvqRfQvcObMGYXbMpkMISEh%2BOuvv0RKVLrHjx/Dy8sLeXl5qFmzJhITE7F8%2BXLs2LFDUhewqUiFzc6dOxESEoJRo0bB0tISjx8/RlhYGDQ0NPDll1%2BKHU8uMDAQr169wrFjxzBgwABYWVmhffv2WLp0KUJDQ8WOJ3fv3j2cO3dO8iewPn78GJcvX1ZaM12KrKyscPToUVy9ehXPnz%2BHubk5mjVrJskPN4MGDcKYMWMwduxY5Ofn4%2BjRo9i8ebOkTritXbs2Ro8eLXYMkji2nRCVs4KCAjg7OyM6OlrsKArGjh2LunXrYsaMGdDU1JRfxOL%2B/fuSKsBsbW0rTGHTtWtXrFixAk2aNJFvu3XrFnx8fHDq1CkRkylydnZGVFQUqlatKj%2Bcn5OTA2dnZ/mhfSno0qULdu/eLbkVWd42aNAg%2BPn5Seqowbvk5uYiLS1NqZVHSidaFwsPD8fu3buRkJAAMzMzeHp6wsvLS/KryhC9SXofbYn%2B5f74448SV5UQ240bN7B%2B/Xr5m5impiYmT56MNm3aiJxMUcOGDREfH18hCpvk5GQ0atRIYVujRo3ky%2BZJRWFhoby/u3g%2B5s1tUjFkyBBMmDABw4YNU2o1cHBwECmVslatWmHYsGHo0qULqlWrprBPakuMHjt2DL6%2BvsjMzJRvk%2BKJ1sUGDx6MwYMHix3jnb7//nvs2rULycnJ2LdvHwIDA7F06VKlE1vpv4vFN5EaDR06VKHQzsvLw71799CzZ08RU5VMS0sLmZmZCrOKmZmZkrpsN1CxCpvatWvjzJkz6Nixo3zb6dOnUbt2bRFTKWvZsiUWL14MX19f%2Be/r2rVrJbd0o5%2BfHwAoXVBHaoXi5cuXUbduXdy7d09huxQ/dG/YsAGDBw%2BGh4eHJFtNAODrr7/G6NGjERQUVOp9pPLc/%2Babb7Br1y54eXlh9erVMDAwQEJCAvz9/SW1vCiJi20nRGr09puFpqYmrK2t0bFjR8n1Ky9YsABPnjzBggULYGlpifj4ePj5%2BcHKygqLFy8WO55cRVo7/eTJk5g6dSq6dOkCKysr/Pnnnzh58iTWrFmjUJCLLTU1FePGjcOdO3dQUFAAfX191KlTB8HBwTAzMxM7HqmRra0trly5ItnCGyi6smlISEiFeO537twZGzduRL169eQtXElJSejTp4/kWg1JPCy%2BicpJamoqqlatKtk3ub/%2B%2BguTJk3ClStX5Gt8u7i4YMWKFZJb8aQiiY6Oxv79%2B5GamopatWqhb9%2B%2BsLOzEzuWEplMhps3byIhIUF%2B0p3UPiAmJiaWuk9q/clxcXHYs2cPnj17hiVLluDIkSNKV%2BeUgiFDhmD%2B/PmwsbERO4pKZDIZCgsLoaWlhZSUFBgZGUnq99TR0RExMTHQ0NCAg4MDrly5goKCArRu3RoxMTFixyOJkGYVQPQvkZeXhxUrVuC7775DTk4OdHV10bNnTyxYsEBy/bTVqlXDzp07ER8fLy8U314qSypOnTqFiIgIheX7pHjp5u3bt8PLywuff/65wvYNGzZg0qRJIqVSVlzU1qhRQ95LnZSUBEBaRa2rq6v8gyGg2MYhpbaT6OhoTJo0Ce3bt8eFCxeQk5ODjRs34tWrV5JbCcPOzg5eXl7o0qWLUh%2B9VFo5it29exfjxo3DunXr0KxZM2zduhWnTp3C1q1bUbduXbHjAQA%2B/fRT7Nu3D/3795f/fp44cQL16tUTORlJCWe%2BidRo3bp1OHPmDKZOnQpLS0v8%2BeefWLNmDdq0aYOZM2eKHU9BYmIipk6digULFqBx48ZYvnw5rl%2B/jvXr10uqCI%2BKisJXX30FT09P%2BWP67bffYvbs2ejfv7/Y8fDixQv88ccfAICRI0ciLCwMb77MZmRkwMfHR6lvWUw2Njal9iNLqah9%2B0JQaWlp2Lp1Kzp06CCp8yj69u0Lb29vuLi4yGc/b968CR8fH0ldDAioWG1cQ4cOhYODA8aPHw9tbW3k5%2BcjODgY165dk8wa2jdv3oSXlxcaNmyI69evo02bNvjll18QEhICW1tbseORRLD4JlKjjh07Ytu2bbCyspJv%2B/PPPzF48GCcP39exGTKxowZA2NjY8ydOxeGhoZIS0vDmjVrkJ6ernSxIDH17NkTc%2BfORcuWLeXbLl26hMWLF%2BPo0aMiJivy8uVLdOrUCenp6SXu19LSgqenJ3x9fcs5WekqSlFbkoyMDHh4eEhq6UZ7e3t5%2B9abV2K0t7fHL7/8InK6iuvNx7VYQUEBWrZsiStXroiYTNGzZ89w8OBBJCYmwszMDD179lR4DyBi2wmRGqWnp8PCwkJhm4WFBXJyckRKVLrY2FhER0fL1882MjLC/Pnz4ezsLHIyRYmJiXByclLY5ujoiGfPnomUSFGVKlVw6dIlFBQUoGvXrjh%2B/LjCfin1pxarVauW0m0/Pz94eHhIvvgGij7wSEnNmjVx7do1tGjRQr7t5s2bSq8FUnHp0iUkJSXJj9AUr8o0f/58kZMpMjQ0xB9//KGwzGh8fLzkzkkxNzfH2LFjxY5BEsbim0iNPv30U%2Bzdu1fhRKu9e/eiQYMGIqYqmba2NtLS0hRWt0hPT4e%2Bvr6IqZSZm5vjypUrCsvgXblyRVK9yRoaGtDW1sYPP/yAwsJC%2Bdrp0dHRMDIyQsOGDUVOqBqpFbVvrx6Ul5eH8%2BfPo3nz5iIlKtmYMWMwbtw4DBw4EHl5eQgJCcHOnTsxdepUsaMp8fPzw969e1GpUiUARTPJWVlZaNu2rcjJlHl4eGDcuHH48ssv5VfhDQ0NRZ8%2BfcSOht69e%2BPgwYNwc3MrtYXrxIkT5ZyKpIrFN5Ea%2Bfj44H//%2Bx8iIyPlS809fPhQUleMLNalSxd4e3vDx8cHFhYWePr0KdavX4/OnTuLHU3B8OHDMWHCBHh6esof04iICMyZM0fsaEp%2B%2BuknzJ8/Hz///DOCg4OxceNGAICvr68k%2BtOLVZSi9u3VIrS0tGBra4sxY8aIlKhk3bt3h6GhIcLDw1GzZk1cunQJ8%2BbNk9xzCSi6yM6uXbuQnZ2NyMhILFu2DMuXL8erV6/EjqZk4sSJ0NTURHBwMFJSUmBhYYE%2Bffpg1KhRYkeDl5cXAEgiC0kfe76J1Oz3339HVFQUUlNTYWlpie7duysd5peC7OxsfPXVVzh69Chyc3Ohq6uL3r17Y86cOZK70M7%2B/fuxf/9%2BPH/%2BHLVq1UL//v3RpUsXsWMp6d%2B/Pzw8PPDFF1%2Bgbdu2WLp0KYyMjDBjxgxJzYK9fdKdlpYWrK2tMWbMGJiamoqUisqDnZ0drl27hpSUFIwcORKRkZHIzMxEt27dcO7cObHjKbhx4wY%2B%2B%2Bwzpe3nzp2TXHvcm3Jzc3H16lW0atVK7CgkESy%2BiUhBXl4e0tPTYWxsLMkr8gFFayibmZnB0NAQsbGxqFKlCqytrcWOpcTJyQkxMTH47bffMGjQIPnFTGxtbSW12klFIuVlJlU5%2BuLv718OSVTXrVs37Ny5E8bGxnB0dER0dLT8RNFr166JHU9B8QeFN2VmZqJt27aSfj4lJSWhXbt2klo5iMTFthMiNTp79iz8/PyQkJCAtz/nSumFODMzEykpKahbty50dHRw9uxZ/Pbbb%2BjUqZPSyY1iO3bsGGbOnIk9e/agSZMmuH79OjZs2IA1a9bAxcVF7HgK9PX1kZaWhjNnzsDOzg7a2tq4f/8%2BqlevLnY0BQcPHlTpfr1791Zzknd7c5lJV1dX/Pnnn1i0aBFycnIk1cZTkbi4uMDLyws7duyAg4MD5s6dCz09PdSpU0fsaACAx48fo3v37igoKIBMJivxfAkpXrTqbZznpDdx5ptIjTp06AA3Nze4uLjIT7or9uYJg2KKi4vD0KFD0b59eyxduhTbt2/H6tWr0a5dO8TExGDVqlVo06aN2DHlunfvjtmzZyucEHb%2B/HmsWLECkZGRIiZTtnbtWhw4cAB//fUX1q1bBxMTE4waNQrDhg2T1GoIgwcPRmxsLKpVqwYrKyskJSUhKSkJpqam8tVZNDQ0RF%2BjWurLTFZEeXl52LFjBzw9PfHq1SvMmzcPmZmZ8vX%2BpeC3337Dy5cvMXr0aISEhCjs09PTQ4MGDSTXGvcmznzT21h8E6lRixYtcPnyZUkuL1fM29sb5ubmmDVrFrS0tODs7AwvLy/873//w9mzZ7F161bs3LlT7JhyJR16lslkcHBwkOQaytHR0dDT04O9vT0SExNx/fp1dOvWTexYChYvXgw9PT1Mnz5d/ru6ZcsWPH36FIsWLRI33BtKWue5sLAQ9vb2kmuRiIyMxKFDh5CcnIxatWph4MCBkjsyU9HEx8fDyspK3hpXvXp1Sb%2B2FmPxTW9j2wmRGrVv3x5nz56Fq6ur2FFK9csvv%2BDkyZPQ0tLCo0ePkJKSgk6dOgEo6lmeNm2ayAkV1apVC%2BfPn1eY%2Bb548aKklhp805uXlq9Zs6Ykc0ZFRSE6OlqhkBk5ciTatm0rqeK7IiwzCQChoaEICQmBp6cnLCws8Oeff2LGjBmYNWsW%2BvbtK3Y8ABWzP93IyAizZs3C8ePHkZubC319fXh4eGD27NnQ1dUVNVtUVFSp%2B6S2ZCeJj8U3kRoNGzYMgwYNQr169ZQuBCGVSzfn5OTA0NAQQNFqAkZGRvKrsWlqaqKgoEDMeEpGjx6NCRMmwM3NDbVq1UJiYiJ%2B%2BOEHLF%2B%2BXOxocsVXNWzcuHGpJ63eunWrnFOVTl9fH7///jtsbGzk227duoWqVauKmEpZRVlmMiIiAqGhoQptG506dcLs2bMlU3xXRF999RUeP36MTZs2wcLCAvHx8diwYQNWrlyJuXPnippt5cqV79zPVYPoTSy%2BidTI19cXtra2sLe3l%2BzhUWNjYzx9%2BhQWFha4dOkSHBwc5Pvu3r0ruTcNd3d3mJqa4uDBg7h9%2BzYsLCwQFhYmqZOuitfNDgkJkeyKMW8aPHgwRo4cif79%2B6NmzZqIj4/Ht99%2BK3pB87b%2B/ftDS0sL%2B/fvx6lTp%2BRX4pTaMpNZWVlKF9Jq3LgxUlJSREqkTGqz2qr48ccfcfz4cRgbGwMAPvnkE9jY2KBXr16i/66ePXtW1O9PFQuLbyI1evz4MS5fviy/ZLsUdenSBTNnzkTbtm1x5MgRrF%2B/HgDw8OFDBAQEoGPHjiInVObk5CS5VVjeVNwW0bp1a5GTqGbs2LEwNjZGZGQkTp48CSsrKwQGBkqyR/mzzz6Dm5ubwjKTUtOzZ09s2LABU6ZMkX/4CgsLk1yvP1C0BnVUVBSSkpJQWFgIoOgkzPv372Pz5s0ip1Okp6enNIlRqVIlSZ9sSVQSnnBJpEaDBg2Cn58fPvnkE7GjlCo3NxdLlizBtWvX0L17d4wfPx4A0KxZMzRp0gRff/21vC1FCpKSkrB582Y8evRIXiwUk0orz4gRI9474x0WFlZOaf493l5mctu2bZJaZtLV1RUaGhrIz89HUlISjIyMYG5ujpSUFKSkpMDGxkblZR3Ly/Tp03H%2B/HlUr14deXl5%2BOijj/DgwQP07t0bAQEBYsdTsGvXLpw8eRJz585F7dq1kZSUhFWrVuHjjz/G4MGD5feT2jkARG9j8U2kRhs2bEBERAS6dOmCatWqKeybOHGiSKlUExcXJ8kL1/zvf//D8%2BfP0b59e6UjClJ5TNeuXSv/%2B7Zt2zBixAil%2B/j4%2BJRnpHfKysrC7t27S/xAI6X2BKkvM3ngwIH33sfDw6MckqjOyckJe/bsQVpaGvbs2YNVq1YhLCwMv/76q8LvsRS8eU6ChoaGwtrZxbc1NDS4qghJHotvIjV6%2B7LdxTQ0NCQzS1vRODg44MSJEzAyMhI7ikocHBxw5coVsWO8k7e3N2JjY%2BHk5KT0gUZKxXdFW2YyNTVVfiVOCwsLseOUqPj3My0tDUOGDMHRo0fx%2BvVrdOjQAT///LPY8RQkJCSodL9atWqpOQlR2bDnm0iNSlsf%2B/79%2B%2BWc5N%2BjcuXKoi8r9iEqwgmXMTEx2Ldvn3yVG6mqKMtMZmZmYtasWThz5ox8NrZVq1ZYu3at5HrUzc3N5etnp6am4tWrV9DU1ERWVpbY0ZRUhKJ6/fr1mDRpksLzPi0tDXPmzMGWLVtETEZSwuKbqBxduHABoaGhuHDhAg%2BN/j%2BNHz8ec%2BbMwahRo1CjRg2FfVIrwioKPT09mJmZiR3jvSrCMpMAsGrVKmRlZeHw4cOwtLTE48ePsWzZMqxYsQJLliwRO54Cd3d3DBo0CPv27UO7du0wbtw46OnpoUmTJmJHU2JjY1Pqh1mpvJ5GRkbi2rVrWLVqFYyNjREdHY1Zs2ahbt26YkcjCWHbCZGa5efn4/Dhw9i2bRsePnwIZ2dnfPHFF5I4QUwVmZmZkjrh8u2%2BTwCS7vUsXvNbyoKDg5GcnIyJEydKvp0nJiYGBw8eREpKCiwsLODh4SGpZSYBoF27dvj%2B%2B%2B/lS%2BIBQEpKCnr27ImLFy%2BKmKxkx44dg4uLCwoLC7FixQpkZmbCx8dHckdC3n4epaWlYefOnejVqxcGDBggUipFGRkZmD9/Pq5evYp27drhyJEjmDx5MoYPH14hjoJR%2BWDxTaQmGRkZ2Lt3L3bt2gUNDQ2kpaXh22%2B/VSgepaS0ItHe3l5S/bTv6vuUymHpN/uSR40aha1bt%2BLtl1opFYyurq5ITEwssTiQ2gea6OhoNGrUCNWrV8fZs2eho6MjuSUdnZyccP78eYX2qNevX8PZ2RkxMTEiJvv3SUlJgZeXF44cOSJ2FLnExEQMGTIEiYmJ6NWrF5YuXQptbTYa0D/420CkBsuWLcP333%2BPBg0aYNasWXBzc0ObNm1QvXp1saMpePz4MXx9fSGTyZCZmYlhw4Yp7M/MzJRcj6pUCux3GTRokMLtgQMHKtyW2iy91JaUK014eDjWrFmD3bt3o3r16khNTUVAQADmzp2L3r17ix1P7rPPPsO6deswffp0%2BSoc69atQ9OmTcWOpuDy5cu4desWXFxc8PHHH2PatGk4f/48HBwcF/LfTAAAIABJREFUsHLlSsk990tSpUoVJCUliR1D7rvvvkNAQADatWuHVatWYeHChejfvz8CAwNRv359seORRHDmm0gNbGxsMGjQIIXD%2BC1btsShQ4ck11sbHh6OFy9eIDg4GGPHjlXYp6urC1dXV9SrV0%2BkdP8YOnToew/bSmUFmYKCgvfeR6pXPJWyjh07Yt26dQqXbb916xamTZuGEydOiJhM0b179zBs2DDo6uqiVq1aSEhIgIaGBrZt2yaZ5Tt3796NZcuWoUGDBkhISEC7du1w9%2B5d9O/fH5GRkahfvz6WLl0qdkwFb6%2BRnpeXh9OnTyMrK6vUk9vLm62tLebPn4%2B%2BffsCKLqOwvLly7Fv3z7cuHFD5HQkFZz5JlKD4OBghIeHo127dnBzc8OwYcMk2%2B9XfHEKS0tLSc0evk3KV7R8W0UprN3d3REVFSW/OExJTp8%2BXc6pSpeamoqGDRsqbGvUqBFSU1NFSlQyKysrnDhxAqdPn0Zqaipq1aoFFxcXSZ07sWPHDoSEhKBVq1a4fPkyhg8fjqioKNSrVw8dO3ZEv379xI6opPjqu8W0tLRgbW2NhQsXipRI2f79%2BxVOrtTV1cWCBQsUVughYvFNpAbt2rVDu3bt8PjxY4SHh2PkyJHIzMzEwYMH0b9/f0md1Hb48GH06NEDgPLMUjEpFOVSuYDOv8no0aMBFD22Uv1w%2BKZ69erh0KFDCheqiYqKktwVZHv06IHIyEj57KcUJScno1WrVgCKzvfQ1taWH%2BEyNzdHdna2mPFKFBgYCFtbW0l/uK1bty4SExORnJwsv2BVXl4e4uPjRU5GUsK2E6JykJ2djQMHDmDPnj149OgR2rVrhw0bNogdC0BRoXD48GG4urqWuF9DQ0NSs5/03xUdHY1x48ahcePGqFmzJp4%2BfYo7d%2B7g66%2B/hqOjo9jx5FxdXREREQETExOxo5Tq7QsWvX3CdUkXNBKbk5MTfvrpJxgYGIgdpVQhISFYvXq1/HbxSkyffvppqZMb9N/DmW%2BicmBgYIBBgwZh0KBBuHjxInbv3i12JLnDhw8DAM6cOSNyEipvFamPHgA%2B//xzREZG4vDhw0hJSYGzszOWL18uuSXxnJyc0L9/fzg7O8PU1FRhH4/g/P9ZWVnh5s2bkvqg9bbw8HCsWrUKurq6OHfuHCZPnowlS5bg448/FjsaSQhnvon%2B41S59LmDg0M5JPn3mTRpUolHOLy8vLB9%2B/byD/SWoKCg995H6sXi9evXERYWptQPLKahQ4eWuF1DQ0MyH2YaNWoEe3t7%2Be2rV6%2BiRYsWCrdv374tRrRSjRw5EpcuXYKlpSVMTU0VPjhK5XG1tbVFbGwsnj59iokTJ%2BL7779Hamoq%2BvfvzwkOkuPMN9F/XHGh8OYbWdWqVZGRkYHCwkJUq1ZNkhcGkaonT57IjyacPXsWwcHBCvszMjJw69YtMaIpkXph/S4//PADwsLCEBsbK7kl/KSy8sa7jB8/XuH227PJUpxdtrW1ha2trdgx3snExARZWVkwNzdHfHw8ZDIZjI2NkZ6eLnY0khAW30T/cXfv3gUAhIaG4v79%2B5g/fz4qV66MV69eISAgAFWrVhU5YRFV%2BiWlcGKohYUFbt26hbS0NOTn5%2BPcuXMK%2B/X09LBgwQKR0pXu22%2B/xc6dO5GcnIwDBw4gICAA/v7%2BqFSpktjR5F6/fo19%2B/Zh%2B/btePLkCTw8PODr66u0AoqYgoKCcPv2bbRp00a%2BkpAUVcQPXiNGjCjx9/Hnn38WIU3J7O3tMXnyZKxevRoNGzbEunXroK%2Bvr9R%2BRP9tbDshIgBA69atcebMGejr68u3SemqfKWdEFpMiieGzpkzB/7%2B/mLHeK/t27djz549GDlyJAIDA3H69GmMHj0a9evXh5%2Bfn9jxkJqaim%2B%2B%2BQZ79%2B6FiYkJhgwZgtWrVyMqKkpS6%2BYHBgbi4MGDsLe3R0xMDEaOHClfUYbKbujQoQgNDZVfOTQnJwcBAQHYt2%2BfZI4mZWZmIjAwED4%2BPkhJSYG3tzcyMzMREBDA5QZJjsU3kZolJyfjzz//VLq8uNT6qFu2bInvv/9e4QqScXFxGDp0KC5cuCBisoonJSUFJiYm77zynpSKxs6dO2PTpk2wtraWr3qRnJwMDw8PREdHix0Pn332GZydnTFw4ED5peSleNEqZ2dnhIaGon79%2BoiJiYGfnx%2BioqLEjvWvMWrUKGhqamLjxo24desWZs2aBU1NTfj7%2B6N58%2BaiZnu7Z57oXdh2QqRGO3fuREBAgNIVD6V2eXEA6NWrF0aOHIkvv/wSFhYWiI%2BPx9atW/HFF1%2BIHU1JfHw8kpKS5B9o8vLycP/%2BfXh5eYkb7G%2BdO3fGtWvX4OLiorSaSPHSY1L6%2Bb948UJ%2BYZDix9TY2Bj5%2BflixpKrX78%2BYmNjYW5ujpo1a6JOnTpiRypRRkaG/BLiLVq0kNRlz/8NNm7ciHHjxqF///54%2BPAhhgwZgilTpshnwsU0atQoyS3NSNLF4ptIjXbs2AFfX1/07dsX2trSfrrNmDEDH330ETZv3oykpCRYWFhgwIABGDVqlNjRFGzZsgVr1qyRF7XFxWzDhg0lU3wfOnQIAHDixIkKcfEaGxsbREREYODAgfK8R48elReSYtu3bx9%2B/fVX7Nq1C71794ajoyNev36tdDRJbJqamvK/S/35XuzYsWPo2rWr0vaIiAh4enqKkKh0urq62LRpE8aOHYtWrVph1qxZYkeSk9rvIkkb206I1MjOzg6//PKLwpsylY2LiwvmzZsHXV1dnDlzBlOnTsWSJUtgYWGB6dOnix2vQrp9%2Bza8vLxgbW2NW7duoVWrVrh%2B/Tq2bt2Kzz77TOx4CtLS0rB3715EREQgLy8PPXv2hIeHBz799FOxo733wjVSkZ2djRcvXgAAunfvjqNHjyoUjxkZGfjiiy8QGxsrVkQFrq6uCh9ic3NzkZKSAjMzM/mHHLHP95DiRYlIulh8E6nR2LFjMXz4cPllnKUuOjoau3btQlJSErZs2YKwsDBMmzZNUrN4xevoPnv2DOPHj8f%2B/fuRlpaGfv36SWYd3caNG793xlsqJ4gVS0pKQmRkJBITE2Fubg53d3fUrFlT7FilKigowMmTJxEeHo6rV69Koo2nWbNmWLx4sfz2V199hYULFyrcRwor8qSkpMDNzQ05OTlK%2B4qPJHXs2FEyV%2BE9cODAe%2B/j4eFRDklK17Bhw/c%2BX8T%2BgEDSIZ13VKJ/ITMzM4wZMwZOTk6oUaOGwj6prYIRFRUFf39/9O/fXz5bd%2BbMGWhoaGDmzJkip/uHqakpMjMzYWZmhidPnkAmk8HIyEhS6%2Bhu3boVAHDx4kX89NNPmDhxIj7%2B%2BGM8ffoUGzdulOSqB2ZmZpJrMXoXLS0tdO3aFV27dsW9e/fEjgMAqFGjhsLFfqpXr65wW0NDQxLFt4mJCU6dOoXs7Gy4u7vL16Uvpqenp/R6JSaxC2tV6OjoVMjlG0kcnPkmUqM5c%2BaUuk9qxbe7uzuWLFmC5s2bw8HBAVeuXMGjR48wbNgwpbWqxTR//nwkJiZi7dq18Pb2RtOmTaGnp4ejR4/i6NGjYsdT4Obmhh07dsDCwkK%2BLTk5GZ6envjxxx9FTFbk7cP5JeFs3b9bYWFhhWmLS0pKwubNm/Ho0SMUFhYq7BP7CpdsO6EPwZlvIjWSWoH9Ls%2BePZP39xYXZLVr18arV6/EjKVk9uzZWLVqFfLz8zF37lz4%2BPggIyNDko91amoqqlWrprDNwMAAL1%2B%2BFCmRokmTJgEo6vk%2Bffo0RowYIZ%2Bh37ZtGzp06CByQlKX0aNH4%2Buvv8bw4cNL/QAmdkH7tjlz5uD58%2Bdo3749dHR0xI6jgPOY9CFYfBOpUW5uLqKiopCUlCSfqSleFm/z5s0ip1NUp04dnD59Gh07dpRvu3DhAmrXri1iKmWGhobyPlojIyPJzXa/yd7eHnPmzMHMmTNhbm6OJ0%2BeYNmyZZJpOyk%2BnL9t2zZs3boV1tbW8n2tW7fG6NGjJbWiBAmneE1qR0fHCrEiDwDcvHkTJ06cgJGRkdhRlPTs2VPsCFSBsO2ESI2mT5%2BO8%2BfPo3r16sjLy8NHH32EBw8eoHfv3ggICBA7noL/a%2B/Ow2rM3z%2BAv0%2B0iFSSKZXsU2OdqGOJlpmyxZBqBtMYY6lI5CsJoZKlbFmbIiMlM8qWFmvCRCn7MGPnVKNoGSpN6%2B8PV2c8TmHm55zPc%2Bp%2BXVd/nOfpj/eVmbrPcz73faelpWHmzJn44osvcPLkSYwbNw5Hjx7FunXrYGFhwTqe2JYtWxq8x7czl3l5eZgzZw6uXr0qLnCEQiFCQkKgrq7OON0/Pv/8c2RkZHCeJpaXl2PgwIG8mXhBiLW1NY4cOYJWrVqxjkLI/wsV34RIkVAoRExMDAoLCxETE4N169YhIiIC169fx8aNG1nHk/D777/j559/Rk5ODnR0dODg4IDevXuzjsXh7OzMeV1cXIz79%2B9j%2BPDhWL9%2BPaNU71a3FEhHRwf6%2Bvqs40hwdnbGp59%2BigULFkBJSQmvXr3CihUrkJeXJ24e5QM%2Bn/mVN%2B/qR6nDt6NcsbGxSE1NxfTp0yUaQvk8mYeQt9GxE0KkqKamBp07d4aGhoZ4FNqkSZMQERHBOJkkNzc3BAcHS4xG45s9e/ZIXDt8%2BDDS09MZpHm/4uJinDlzBrm5uZg1axbOnj2LoUOHso7F4efnBxcXF%2Bzbtw%2BamprijZdhYWGso3Hw%2Bczvm8aOHYtDhw5JXLe2tubNOMw6RUVFOHfuHKysrGBgYIC8vDycOHECtra2rKNJWLJkCQDgxIkTEku2%2BDBqkpAPRcU3IVKko6MDkUgEAwMDFBQUoKysDAoKCigtLWUdTcKVK1d4sab5v/jqq6%2BwcuVK1jEk3Lp1S9zEeO/ePUycOBGzZs1CQEAAL0bO1encuTOSkpJw5coV8RN6ExMT3k3B4POZ3ydPnoj7OO7duyfxZLmkpKTeudqs1D3VdnV1xaZNmzjNtefPn0doaCiraA2iyTuksaDimxApGj16NCZOnIjY2FhYWlrCzc0NysrK6NmzJ%2BtoEuzs7ODh4YHRo0dDW1ub04RlamrKMNn7ZWRkQFVVlXUMCatWrcL8%2BfPh6OgIU1NTGBgYYMuWLQgKCuJV8Q28XofO939nNTU13r5B7NChg/hTg/q0adMGGzZskHGq90tPT8e2bds41wYOHCiehMMnenp6Eteqqqpw586deu8RwldUfBMiRTNmzICBgQHU1NTg6%2BuL4OBglJSUwNfXl3U0CVFRUQCAM2fOcK7z7SPdt2dTV1ZW4vnz53Bzc2OYqn5//PEH7O3tAfwzvtHCwgLz5s1jGUtuzZw5Ez4%2BPrw981u3jMrAwAAzZ85knObD6OnpISkpCaNGjRJfO3DgAO%2BmHAGvfzf5%2BfkhLy%2BPM9qvefPmuHHjBsNkhPw71HBJiAwUFBQgJycH2tranIUr5N97e9W0goICunTpwstPE4YNG4atW7eia9euMDMzQ0ZGBh49egQXFxccO3aMdTy5Y2RkxHktEAh4deY3KysL/fr1w6VLlxr8Hr59unDq1CnMmTMHvXv3hq6uLrKzs3Hnzh2EhoZCKBSyjsdhZ2eHwYMHo3Xr1vjjjz9gZ2eHrVu3wsHBQaIRmxA%2Bo%2BKbECkqKSmBt7e3%2BKyiQCDAwIEDsXHjRrRu3Zpxun/U1tZCJBKhQ4cO4muJiYkYNmwYmjVrxjCZfPvpp58QFRUFNzc3BAYGYvXq1di2bRvs7Owwbdo01vHeq6SkhFdj3XJychq8x4djB3VbDt9%2Bk1CHL28S3vbgwQMkJiYiPz8fOjo6GD16NAwMDFjHktCnTx9kZWUhOzsbvr6%2B2LNnD%2B7duwdPT0/Ex8ezjkfIB6PimxAp8vPzw8OHD%2BHr6wt9fX08fvwYK1euhIGBAQICAljHAwCUlZXhhx9%2BQNu2bcUztAsKCmBlZYWePXtix44dvDpPLU/j5mpraxEZGYm9e/ciNzcXOjo6cHR0xPTp03m12KTuqfzb%2Bvfvj8zMTAaJ3u3WrVvIzs6GpaUlXr58CS0tLdaR5N5ff/0FkUgEY2NjVFdX8/JsvZWVFU6dOoWqqipYWloiLS0NwOtPE971aQMhfENnvgmRopSUFMTFxYmLg%2B7duyM4OBhjxozhTfG9fft2KCoqws/PT3xNS0sLKSkpcHNzw48//ghPT0%2BGCbnkZdwc8PrJ99dff43JkyezjiLh8ePHWLp0KWpra1FSUoLvvvuOc7%2BkpIRXn84Ar98Uzpo1Czdv3oSioiJiY2Ph4OCAiIgIfP7556zjITc3973fw4ez6W8qLS3F0qVLkZCQABUVFRw4cABTpkzBrl270LlzZ9bxOD799FOEhIRg1qxZ0NLSQmpqKlRUVKCsrMw6GiH/ChXfhEjRq1evoKamxrnWunVriSe2LB07dgzh4eESTw%2B1tLTg5%2BeHuXPn8qr45vO4ubdt375doqjlC0NDQ9ja2qKoqAiXL1%2BGmZkZ576SkhKsra0ZpavfypUr0b17d%2BzatQtDhw5Fly5dMGPGDAQFBSEmJoZ1PIlmYOCfOdR1%2BHbsJCgoCGVlZUhKSoKTkxMMDAxgZWWFwMBA7Ny5k3U8Di8vL3h4eMDJyQkeHh6YOXMmampqxI2uhMgLKr4JkaI%2BffogJCQE8%2BfPFzeHhYSEoFevXqyjiRUUFDQ42cDY2BjPnj2TcaJ34/O4ubeZm5tj586dcHBw4OWbhUmTJgEA9PX1eTf6sD4XL17EyZMn0aJFC3FBO23aNN4srarr7Th8%2BDCysrLg5eWFDh064M8//8TatWvRt29fxgklpaSkID4%2BHurq6hAIBFBUVMTChQt5twgKALp06YKEhAQAr8/4p6SkoLS0FJ06dWKcjJB/h4pvQqRo/vz5cHZ2xpEjR6Cnp4ecnBwIBALs2rWLdTSxVq1aoaioCJqamhL3iouL0aJFCwapGsb3cXNvunr1KhITE7FhwwaJxtWbN28ySiXJxsYGP/30E77//nvxgpg2bdrA398fn3zyCet4YoqKiigvL0eLFi3Eo%2BZKS0vRsmVLxsleq2v6/Pnnn3HkyBGoq6sDeF00BgUFYfjw4XBxcWEZUUJNTY34zWzdz/TNa3x1%2B/ZtpKWloX///qyjEPKvUfFNiBR1794dx44dw6lTp1BQUAA9PT1YWFjwaoLEwIEDER0dDXd3d4l7e/fu5d3TOnlaMR0YGMg6wgcJCAjA7du38f3332P58uVo3749lJWVsXz5cvHWRj6wtraGl5cXlixZAoFAgIKCAqxYsQIWFhaso3GUlpZKHC0rKytDZWUlo0QNGzBgAPz9/bF06VLx/08bN26UOIbE0tOnT%2BHl5YWbN29i%2BPDhcHJygrOzM1q2bIn169djw4YNsLW1ZR2TkA9G004IkbGSkhKEhYXxZtHKw4cPYW9vD3t7e4wcORLa2trIz89HUlIS4uLiEBUVxasZ2nwfN/emmpoazor2Z8%2BeQVtbm2Gi%2BllbW%2BPAgQPiUZgpKSnQ0NCAubk5r6ZIlJaWwsfHB8ePHwfwenSfhYUFgoODJXorWPL29saTJ0/g4eEBXV1diEQihISEoHfv3li6dCnreBwFBQVwc3PDrVu3UF1dDRUVFXTs2BGhoaG8%2BdRj5syZqK2thZOTE44ePYpz587B1dUVP/zwA%2BLi4hATE4PY2FjWMQn5YFR8EyJjeXl5sLS05NVT2suXL2PZsmW4e/eu%2BGx69%2B7d4evry7ulIPJiw4YNePbsGVauXAkAKCoqwpAhQzB16lReNbACgFAoRHp6OpKTk7FhwwYcO3YMFRUVMDc3r3cEIWuFhYXIzs6Gjo4O2rVrxzqOhNLSUvj5%2BSE5ORkVFRVQVlbGV199hSVLlvDuOIdIJIK%2Bvj5u3LiBnJwc6OjooHfv3rya7y8UCnH69Gm0bNkSf/31F4RCIa5fvw4lJSVUV1dDKBTyciQmIQ2hYyeEEJiYmCA%2BPh4ikQiFhYXQ1tbm3fnpOunp6fDz88OjR4/w9rMDvryh2b9/Pw4cOCAuvAFAXV0d69evx7Jly9ChQweMHz%2BeYUKubt26Ydu2bTh79iysrKxQUlKCjRs3okePHqyjSbh48SIOHz6MZ8%2BeoX379nBwcEDv3r1Zx%2BJo2bIlgoKCsGLFChQXF0NTU5O3YzG//vprHD9%2BHL179%2Bbdz7FORUWF%2BFy/uro6WrVqJX4T06xZM4nfA4TwHRXfhBAxAwMDXm62e9Pq1avRp08fLFmyBM2b8/NXWExMDNauXctZz62goABbW1s0b94cW7du5VXxvXz5cvj5%2BaFVq1Zwd3fHrVu3kJ6ejk2bNrGOxvHLL78gICAAtra2MDY2RnZ2NpydnbF27VrY2Niwjsdx//59xMTE4OnTpwgICEBCQgK%2B/fZb1rEkaGhoIC8vj1d9KG97e3zjm0e5AFDxTeQOP/9yEUJIAx49eoR9%2B/bxerFGdnZ2gw1rQ4cOhbe3t4wTvVvXrl2xZ88e8WszMzNerusOCwtDaGgoBg8eLL6WmpqKoKAgXhXfv/76K2bPng0rKyukpaWhvLwcW7duRVlZGWbMmME6Hke3bt3g5OSEvn37ShzhWbVqFaNUXDU1NcjMzBQX2VVVVZzXfNqbQMiHoOKbECnw8fFp8F55ebkMkzQ%2BHTt2RH5%2BPq%2Bf0Ddr1gyVlZX1nu99uwmTDyoqKhAfH4%2B8vDxxIVNZWYk7d%2B7watpJQUEBBgwYwLk2ZMgQeHl5MUpUv7oJHBYWFjA1NYWuri7CwsIwd%2B5c3hXfqqqqvJ8UUl5eLvGpwZuv334yTgjfUfFNiIypqKjIxUITvhoxYgSmTZsGBwcHickhfPm59ujRAydPnsTIkSMl7p06dYp3S0EWLVqEc%2BfOQVNTE5WVlVBVVcXdu3d58/OsM2TIEERFRWHy5MniawkJCRg0aBDDVJIeP34sXlJTVxj26tULf/31F8tY9eLL0%2B13%2Bf3331lHIOSjouKbECmQhz9o8mrfvn0AILFOvKioiDfForOzMxYsWCBe0a6goICamhqcPn0a/v7%2BWLx4MeuIHOfOnUNMTAwKCwsRExODdevWISIiAtevX2cdjaO6uhqrV6/GwYMHYWhoiLy8PFy7dg3Gxsb47rvvxN8XGRnJMOXrZU%2BXL19Gv379xNdu3LgBXV1dhqkk3bx5E3fu3IG9vT2A1592uLm5Yc6cObzawktIY0PFNyFErpw%2BfZrz%2BsGDB/jpp59w5MgRRokkWVhYYPr06ZgzZw6UlJSgqamJoqIiVFZWYtasWbCzs2MdkaOmpgadO3eGhoaGeGLMpEmTeLO2vY6xsTGMjY3Fr7t16wZzc3OGiern4uICNzc3TJgwAZWVlQgPD8eePXt4M9sfAG7dugVnZ2dMnDhRfO3Vq1dQUVHB5MmTER0dzflZE0I%2BHprzTQiRS5mZmdi5cydSU1PRvXt3ODo6YtKkSaxjceTl5eHMmTPi8Y1DhgzhzeKSN40ePRrbtm2DgYEBhEIhUlJSoKCggIEDB%2BLKlSus48ml1NRUREdHi2dnOzk5YdiwYaxjic2aNQu9evWCq6urxL1169bh4cOH2LJlC4NkhDR%2BVHwTQuRGTU0NkpOTsWvXLty9exdVVVXYvn07hgwZwjqaXAsLC8OePXsQGxuL9evX4%2BnTp1BWVsarV684U1BYevXqFbZt24bk5GTk5%2BdDW1sbw4YNw8yZM8UzoPkiICAAnp6evB7fZ25ujhMnTqBFixYS94qLi2FnZ4fz588zSEZI48evlntCGplr167Ve/3s2bMyTiL/du/eDRsbGwQHB8PGxgZnzpxBq1at0L17d9bR5N6MGTOwaNEiqKmpwdfXFx07doSamhpnSRBLf//9NyZMmIDk5GSMHj0aPj4%2BGDZsGJKSkjBhwgTeTRCKj4%2BHiooK6xjvVF5eXm/hDbye/c23nykhjQk9%2BSZEikxMTHD58mXOtZKSEgwZMoQ%2Bzv%2BXjIyMMHHiRCxcuFA8wm/AgAE4fPgwL49ykI9n69atuHDhAnbs2MEpaktLSzF9%2BnQMGjQI7u7uDBNyrVmzBqWlpRg3bhzatWvHGYXHl82xY8aMQVBQEIyMjCTu/fHHH/Dw8MCxY8cYJCOk8aPim5CP7PHjxxg1ahSqq6tRW1tb7wxaExMTREdHM0gnv6Kjo7F3714UFhbCyckJEydOxNixY3Ho0CHeFd/3799Hly5dWMd4L2dn5/fOSGY9OQR4fSZ9zZo1%2BOyzzyTuXb9%2BHYsWLcLRo0cZJKvfmwVt3c%2B37ndBXUMraz/%2B%2BCPOnz%2BPsLAwzhPwsrIyuLm5oWfPnrybn05IY0HFNyFScPv2bbx48QIzZsxAeHg4556ysjK6d%2B/e4Ee%2B5N0uXLiAqKgonDt3DtXV1QgMDMTo0aPRrFkz1tHEhEIh0tPTMXXqVOzcuZN1nAZ9SEMdH54o9%2BvXD1lZWfXeq6qqgpmZmcQnTCzl5OQ0eE9PT0%2BGSRpWUVGBb7/9Frm5ubC0tETbtm3x7NkzpKamQltbG9HR0VBVVWUdk5BGiYpvQqRIJBLxehOjPMvJycHevXsRFxcHBQUFjBkzBgsXLmQdC8Dr9eweHh4IDg5GYGAg6vs1O3r0aAbJ5JOZmRmOHz8ODQ0NiXtFRUUYOXIkLly4wCBZ/V68eIHWrVuLX1%2B7dg19%2BvRhmKh%2BFRUViIyMREpKingij7W1NSZOnFjvdlZCyMdBxTchUlRaWoq9e/fi0aNH4rXddWgRz8dRUVGBI0eOYO/evThw4ADrOACAiIgIREdH488//5TYwgm8Popw5swZ2QeTU9OnT4e5uTlns2WdyMhIpKWlITQ0lEEyrurqasyfPx81NTUICQkBADx//hzm5uYYPnw41q1bx6tPaAghbFDxTYgUeXh44MqVKxAKhVBUVOTco%2BK78RswYAAuXrzIOobcu3DhAmbNmgXa5R9/AAAZtUlEQVR/f38MHz4czZs3R0VFBQ4ePIigoCD8%2BOOP6N%2B/P%2BuYCAsLQ3x8PNatW8eZwvP7779jzpw5cHJywtSpUxkmJITwARXfhEiRUChEbGwsHT1pwmpra3Hr1i3k5OSgXbt26NOnz3ubHImkmJgYrF69GgCgrq6OgoICKCoqwtfXF%2BPHj2ec7rVRo0Zh3bp19U4QyczMxPLly3nVGEoIYYPWyxMiRcrKyrybxEFkp7CwEK6urrhx4wZat26NFy9eoGvXrtixYwdv/7soLCxEmzZtWMeQMGHCBNjY2ODs2bN49uwZtLW1YWlpyauseXl59RbewOsJR3/%2B%2BaeMExFC%2BIiW7BAiRRMnTsTq1atRWFjIOgphYPXq1dDT00NGRgbS09Nx4cIFdOnSRfwEly%2BqqqqwYcMG9OvXD9bW1hCJRBg/fjzy8/NZR%2BNo27Yt7O3t4eLiAnt7e14V3sDrN9ulpaX13isvL%2BdlEyMtAiNE9qj4JkSKfvnlF%2BzduxeDBw%2BGsbEx54s0fmlpaQgICICamhqA15sD/f39kZaWxjgZ1%2BbNm3Hx4kWEhIRAUVERWlpa0NHRQWBgIOtocqVfv344dOhQvfcOHz5c75xy1qZMmSJxraSkBHPmzGGQhpCmgY6dECJFfHvCSWSrurpa4ny3goIC7yZexMfHIyYmBp988gkEAgFUVVWxatUq2NjYsI4mV6ZNm4bJkyfj77//xqhRo8SzsxMTE7F582Zs3bqVdUQAkovA6nsYYGJiwiAZIU0DFd%2BESJGZmRkA4K%2B//oJIJMJnn32GqqoqXn78TD4%2BMzMzBAQEYPny5VBRUcGrV68QEBAAU1NT1tE4ysrKxEc46nrwVVRUoKDAjw9HU1NTYWFhwTrGe/Xu3RurVq3C8uXLERwcLL6uoaGBgIAADBo0iGG6fxgaGmL//v3vXQRGCJEOmnZCiBSVlpZi6dKlSEhIgIqKCg4cOIApU6Zg165d6Ny5M%2Bt4RMqys7MxZcoUPH36FFpaWigoKEDHjh0RFhYGXV1d1vHEXF1d8emnn8LT0xNmZmbIyMjAzp07kZ6ejrCwMNbxYGpqikuXLsHW1hbHjx9nHee9KioqkJWVhaKiImhra6Nv374So0b5ghaBESJ7VHwTIkXLli1Dfn4%2BFixYACcnJ6SlpSEwMBAikYjXa8fJx1NRUYFLly7h%2BfPn0NPTQ9%2B%2BfdG8Ob8%2BdBSJRJg8eTKqqqpQUFAAQ0NDlJaW8uZN4qBBgzBq1CjExMTA1dW13u9xd3eXcarGgRaBESJ7/PoLQEgjk5KSgvj4eKirq0MgEEBRURELFy7E0KFDWUcjMqKkpITBgwezjvFOBgYGSEhIwJkzZ5CTkwMdHR1YWlqiVatWrKMBAHx9fbF//37U1tYiPT1d4j7NTf/vfHx8GlwERgiRDiq%2BCZGimpoa8fnuug%2BZ3rxGCB9UVFQgNDQUDg4OGDFiBHbv3o0dO3bAw8ODF%2Be%2BR4wYgREjRsDR0RF79uxhHadRSU9Pp0VghMgY%2B9%2BqhDRiAwYMgL%2B/P169eiV%2BOrdx40ZxIyYhfLBq1SqcPXtWPIWlR48eOH/%2BPNauXcs4Gdf%2B/ftRWlqKxMREhIeH4/Dhw3jx4gXrWGKpqamsI/xrtAiMENmjM9%2BESFFBQQHc3Nxw69YtVFdXQ0VFBR07dkRoaCj9wSO8MXjwYMTHx3OW1jx//hxjx47F%2BfPnGSbjevz4Mb7//ntUVlaiffv2yM3NRU1NDXbv3o1u3bqxjid3jaEAEBoaivz8fLi7u/NuaREhjRUV34RIkUgkgr6%2BPm7cuCE%2BS9u7d2/ezXkm0lFbW4uUlBRYW1sjLy8PQUFBaNOmDebOnYuWLVuyjifWv39/nD9/HioqKuJr5eXlsLS0xMWLFxkm43J1dUWnTp3g5eUFBQUF1NTUIDg4GHfu3OFFA7M8NoZaW1sjNze33nPzt2/fZpCIkMaPim9CpGjQoEE4fvw4bxrXiGytWbMGR48exblz5zBz5kwUFxejWbNm0NfX59UkCVdXV3zyySdYvHgxlJSU8Pfff2PNmjV4%2BvQptm3bxjqe2MCBA5GamsrpmSgvL4e5uTkyMzMZJnstKSkJ%2B/fvR3p6er1LagQCASIjIxkka1hGRkaD9%2Bh4HCHSQQ2XhEiRhoYG8vLyqPhuok6fPo2YmBiUlZXh7NmzOHr0KLS0tHi3OXLx4sWYNm0aTExMoKmpiaKiInTq1AmhoaGso3E0a9YMJSUlnOMRJSUlaNGiBcNU/5DHxlBaBEaI7FHxTYgUdevWDU5OTujbty/atWvHucenJ59EOoqKiqCvr4/U1FRoa2ujY8eOqKmpQVVVFetoHAYGBkhMTERWVhaeP38uPh7Ft3nkVlZW%2BN///gdfX1/o6%2BtDJBJhxYoVsLKyYh2No64xNDU1FTk5OWjXrh2srKzQunVr1tEk0CIwQmSPpp0QIkWqqqqwtbWVKLxJ06Cvr4/4%2BHjs27cP5ubmqK2txe7du9GlSxfW0SRUV1ejQ4cO6Nu3L3R0dJCfn4/c3FzWsTj%2B97//oaqqCiNHjkSfPn1gZ2cHZWVlzJ8/n3U0jsePH8POzg4rV67EiRMnEBwcjOHDh%2BPu3buso0kICgpCWVkZkpKSoKioCAMDA1hZWSEwMJB1NEIaLTrzTYgU7dixAxMmTOBVcx2RnfT0dHh5eaFFixaIjIzE/fv34enpie3bt9d7JpiVpKQkLF26FCUlJeJrtbW1EAgEvGy6E4lEKCgogJ6eHrS1tVnHkcD3xtA3DR06VLwIzMzMDBkZGSgvL8fQoUPfeR6cEPLf8eszRUIambCwMEyZMoV1DMJIYWEhTpw4AWVlZQCvewDOnj0rfs0XmzdvxqRJkzBu3DjeHTWpj4GBAa%2BXwly7dg2bNm0SLyhSUFDAnDlzYG5uzjiZJFoERojs0bETQqRoyJAhCA8PR35%2BPusohIFly5ZxNkQqKyvzrvAGgD///BPu7u4wNDSEnp4e54v8e3WNoW/iU2Pom2gRGCGyR8U3IVKUlZWFjRs3wsLCAsbGxpwv0vj16NFDLpat9OjRA/fu3WMdo9Goawx98OABKioqcP/%2BfXh5efGuMRQAfHx8cP/%2BfZiamuLly5f4/PPPcenSJXh7e7OORkijRWe%2BCZEimqHbtDk5OeHGjRtQUVGBtrY2Z5HJsWPHGCbjWr9%2BPX755RcMHz4cbdu25dzj01KYhIQE2NjY8P5IRHFxMWbPno1Lly6J/80tLCwQFBTEu4kntAiMENmj4psQQqRk//79Dd5zdHSUYZJ3c3Z2rvc635bCmJmZ4ddff4WioiLrKB%2BE742hAC0CI4QFKr4JkSJra%2Bt61zYDwKlTp2SchvBFdXU1PVn8D6ZOnYoxY8bgq6%2B%2BYh2l0Rg5ciQ2b97My/GXhDRWVHwTIkUHDx7kvC4sLERcXBwcHR1pCkoTIBKJsH37duTl5YknSVRWVuLBgwf49ddfGacDjh49Cjs7Oxw6dKjB7xk7dqwME73b%2BPHj8dtvv0FJSQlt27blvLGlN7P/zZw5c3D%2B/HlaBEaIDPF/phQhcmzcuHES12xsbDBv3jwqvpuAxYsXo7KyEm3atEFBQQGMjIwQHx%2BPyZMns44GAAgNDYWdnR02bdpU732BQMCr4vvbb79lHaHRqVsERgiRHXryTYiMVVdXQygUIjMzk3UUImWff/45UlJSkJubi02bNiE0NBSpqakIDw9HVFQU63hyrbCwEG3atGEdo17y0hgK0CIwQligUYOESNGlS5c4X2lpafDz80PHjh1ZRyMy0KJFC2hoaMDQ0BB37twB8Hqj4P379xkn46qpqcGJEycAAHl5eZg7dy78/f0lZlWzVlVVhQ0bNqBfv36wtraGSCTC%2BPHj8ezZM9bROPz8/Brs9eCbsLAwqKiosI5BSJNCxTchUuTs7Mz5mjZtGq5cuYKFCxeyjkZkoEOHDjh37hxatmyJqqoq5OTk4Pnz56iqqmIdjWP16tVYsWIFgNeLgZ4/f44HDx7A39%2BfcTKuzZs34%2BLFiwgJCYGioiK0tLSgo6Mjzs4XvXr1QmJiIusYH4QWgREie3TshBBCpOTkyZOYN28eEhIScPjwYezbtw/NmzeHmZkZgoKCWMcTGzZsGHbt2gV1dXUIhUIkJCRAS0sLX3zxBdLT01nHE7O2tkZMTAw%2B%2BeQTmJmZISMjAy9evICNjQ2vcspTY6ilpSWePn1a75P627dvM0hESONHDZeESEltbS1EIhE6dOggvpaYmIhhw4bRmLkm4ssvv0RycjLatWsHd3d3dOjQASUlJXBwcGAdjaOoqAjt27fHmTNn0K5dOxgaGqK6uhrV1dWso3GUlZWJz3nXPTdSUVGBggK/PsSVp8ZQPr0JJKSpoOKbECkoKyvDDz/8gLZt22LLli0AgIKCAixcuBBRUVHYsWMHVFVVGackstC%2BfXv88ccfyM7OxogRI/Dy5UveNeIZGBjg0KFDSE5Ohrm5OWpqahAREYGuXbuyjsbRt29fbNmyBZ6enuIntXv27EGvXr0YJ%2BN6c8oRnxtDAdq0SwgLdOyEEClYt24drl69io0bN0JLS0t8vaCgAG5ubhg4cCA8PT0ZJiSyUFhYCA8PD1y5cgVKSkqIjY2Fk5MTIiIi0KdPH9bxxC5dugRvb2%2BoqKjgp59%2Bwr179zBv3jyEhoaib9%2B%2BrOOJiUQiTJ48GVVVVSgoKIChoSFKS0uxa9cudO7cmXU8saqqKmzevBlRUVGorq5GfHw85s6di9DQUN5tuqRFYITIHhXfhEiBra0twsPDYWhoKHHv9u3bmDt3Lo4dO8YgGZGl%2BfPnQ0VFBQsXLoSVlRUuXbqELVu24MKFC4iOjmYdr0EVFRUAwLsn9ADw6tUrnDlzBjk5OdDR0YGlpSXvVqNv2LABFy9exOzZs%2BHp6YnU1FR4eXmhefPmCAkJYR2PgxaBESJ7dOyEECmoeypXH2NjY96NRiPSceHCBZw4cQKqqqrip4suLi7YvXs342Tvxseiu46ysjJ0dXWhoKAAPT093hXeABAfHy9uDBUIBFBVVcWqVatgY2PDOpoEWgRGiOxR8U2IFLRq1QpFRUXQ1NSUuFdcXIwWLVowSEVkrXnz5qioqICqqqq4QbCsrIzO%2B/9Hjx8/houLC7Kzs6GhoYGioiJ89tln2Lp1q8RqdJbkpTG0IXp6enj06BHrGIQ0WvLxm4AQOTNw4MAGjxXs3buXV%2BdoifRYWVnB29sbIpEIAoEAxcXF8Pf3x9ChQ1lHk0sBAQEYMGAAMjMzcf78eaSnp6Nr1668m0de1xgKgNeNoQAtAiOEBTrzTYgUPHz4EPb29rC3t8fIkSOhra2N/Px8JCUlIS4uDlFRUejZsyfrmETKSkpK4O3tLW5cEwgEMDc3x7p169C6dWvG6eSPUCjEuXPnOMdiXr16BUtLS17N%2BZaXxlAAMDIy4rxWUFBAly5dsGzZMvTv359RKkIaNyq%2BCZGSy5cvY9myZbh79y4EAgFqa2vRvXt3%2BPr6wtTUlHU8IkP5%2BfniBkFdXV3WcSQ8e/YM4eHhWLRoETIzMzF79my0adMGISEhvBo3aG9vj6CgIE6mhw8fwtXVlXcNzPLQGEoIYYOKb0KkTCQSobCwENra2mjfvj3rOEQGXF1dERwcDDU1NdZRPsjs2bNRVlaGHTt2YPz48TAxMUGLFi1w/fp1XjSHHjp0CABw8%2BZNnDp1ClOnToWenh7y8/MRERGBL7/8El5eXoxTctXU1OD69evIy8uDnp4eLz/pokVghLBBxTchhHxkTk5OKCgowKZNm9CjRw/Wcd7L0tISiYmJKCkpgYWFBdLS0qCmpgahUIisrCzW8WBtbf3O%2BwKBgFczqeWhMbShRWBWVlbo2bMnLQIjRIqo%2BCaEkI%2BsuroamzZtQmRkJLy9vfHNN9%2BwjvROQqEQFy5cQHx8PCIiInD48GGUlJTgiy%2B%2B4NVZankxbdo06OvrY%2BHChVBRUUFJSQkCAwPx8uVLcaHLGi0CI4QdKr4JIURKMjIy4OPjAxMTE8yZM4czao5PR5CmT58OXV1dZGVlYcSIEfjmm2/g7%2B%2BP2tpabN68mXU8jszMTOTk5ODtP11jx45llEiSPDSG0iIwQtihOd%2BEECIlZmZm2Lp1K7755hscPXoUwOtztgKBALdv32ac7h%2BBgYFYv349%2BvfvDxcXF9y6dQsVFRVYsWIF62gcy5YtQ2xsLNq1a8dZiS4QCHhVfOvp6eHJkyecxtCnT59CQ0ODYSouWgRGCDtUfBNCiJRER0dj7dq1GDZsGNzd3Xm7ZKVdu3ZYvXq1%2BHWfPn0QGhrKMFH9EhMT8fPPP/OyeRH4pzHUxMQE06dPr7cxlC9oERgh7NCxE0II%2BcgKCwuxaNEiZGRkYOnSpbx6Kluf0tJSREdHQyQSoaqqinNv1apVjFJJsra2RnJyMuc4B5/IU2PowoULoa%2BvD3d3d4l727Ztw2%2B//YatW7cySEZI40dPvgkh5CMbM2YMtLW1ERcXh06dOrGO814%2BPj64du0a%2Bvfvz9vCFgDc3NywePFiTJ06VWJJER/O0J8%2BfZp1hA/m4uICe3t7FBUVNbgIjBAiHVR8E0LIR2ZjYwMfHx9eF7JvOnfuHI4dO8abMXgN%2Bfvvv5GYmCg%2BPw/w8ww9wP/G0E6dOmHnzp1YtmwZoqOjOYvAwsPDeXu0h5DGgI6dEEJIE2dra4uEhAQoKiqyjvJOgwYNwuzZs2Fubi5xfl5PT49RKknvagzly7GTN9EiMEJki4pvQghp4iIiIpCbmwsPDw%2BJ4xx8IhQKeTOq711MTU2xa9cuenpMCKkXFd%2BEENJEGRkZiY8bAOA8pa3Dp%2BMca9asga6uLr777jvWUd6J742hhBC2qPgmhJAmKj09vd6C%2B01mZmYySvN%2BkyZNQlZWFlq2bAl1dXVOdj4d59i/fz8yMjJ42xhKCGGLGi4JIaSJEgqFAIAVK1ZgyZIlEvcXLFjAq%2BLbwcEBDg4OrGO8lzw1hhJCZI%2BKb0IIaYLy8vJw4cIFAK%2Bf1L59Pvnly5c4ceIEi2gNGjduHOsIH2Tbtm1YsmRJvY2hhBBCxTchhDRBmpqaiIqKQmFhISoqKrBp0ybOfWVl5XoXsLDk7Ozc4DGZyMhIGadpWHV1NSZMmMA6BiGEp6j4JoSQJkhJSQmxsbEAgKlTp2Lnzp2ME71f3TGZOkVFRUhOTsbXX3/NKFH97O3tERkZyfvGUEIIG9RwSQghRG799ttvCAoKwu7du1lHEZOXxlBCCBv05JsQQpq4jIwMLF%2B%2BHI8ePZLYyMj3BsEePXrg5s2brGNwyEtjKCGEDSq%2BCSGkiVu1ahX69OmDJUuWoHlz/v5ZyM3N5byurKxEQkICdHV1GSWqn7w0hhJC2ODvb1lCCCEy8ejRI%2Bzbtw/Kysqso7yTtbU15whHbW0t1NXVsWLFCoapJMlLYyghhA0qvgkhpInr2LEj8vPzYWBgwDrKO719XrpZs2bQ0tKCoqIio0T1k5fGUEIIG9RwSQghTVxYWBji4uLg4OAAbW1tzr2xY8cyStW48LExlBDCBhXfhBDSxFlbW9d7XSAQ8GI6x9vHTd4mEAhw8uRJGSb6b/r164esrCzWMQghjNGxE0IIaeJOnz7NOsI7zZ49u97rV69exc8//4zPPvtMxoneTV4aQwkhbNCTb0IIIbh58yZiY2ORk5MDbW1t2Nvbo3///qxjNSgiIgLr16%2BHo6MjfHx8oKSkxDqSmJGRUYONoTY2NgyTEUL4gIpvQghp4s6fP4%2BZM2fC2toa%2Bvr6ePLkCVJSUrBhwwZ8%2BeWXrONxvHjxAt7e3sjMzIS/vz9GjBjBOpKEnJwczmu%2BNoYSQtig4psQQpo4JycnTJkyhVPIJiUlITw8HAcOHGCYjOvq1avw9PSEpqYmQkJCeD%2BdhRBC6kPFNyGENHGmpqZIT0%2BHgoKC%2BFpNTQ369%2B%2BPy5cvM0z2jx07diAkJARff/01FixYwKtjJnUaS2MoIUS6qOGSEEKaOA0NDdy5cwdGRkbia7///rvE2EFWXF1dkZqaim%2B//Ra2tra4du2axPeYmpoySMYlb42hhBA26Mk3IYQ0cWFhYYiJiYGLi4v4zHd4eDgmTpyI6dOns47HeVNQH4FAgNu3b8sozb/D58ZQQggbVHwTQkgTV1tbiy1btuDAgQN4/vw59PT04OjoiClTpnCOopAPJw%2BNoYQQNqj4JoQQQj4iagwlhLwLnfkmhJAmasuWLe/9Hnd3dxkkaTzkoTGUEMIWPfkmhJAmysjICGpqajA2NkZ9fwoEAgEiIyMZJJNPbzeG1ocPjaGEELao%2BCaEkCZq165dOHDgACorK%2BHo6IixY8dCS0uLdSy5Jc%2BNoYQQ2aHimxBCmrjr168jLi4Ox48fh4mJCRwdHTF06FBqtiSEECmg4psQQggAoLy8HMnJyTh48CAePXqEr776CvPmzWMdixBCGhUqvgkhhIiVlpYiMTERu3fvxpMnT3D9%2BnXWkQghpFGhaSeEEEKQlpaGuLg4nD59Gp06dcI333wDOzs71rEIIaTRoSffhBDSRD169AgHDx7E4cOHUVlZCTs7O9jb2%2BPTTz9lHY0QQhotKr4JIaSJMjY2hqamJkaPHg1LS0s0by75YSiNxiOEkI%2BLim9CCGmiaDQeIYTIHhXfhBBCCCGEyAgNcSWEEEIIIURGqPgmhBBCCCFERqj4JoQQQgghREao%2BCaEEEIIIURGqPgmhBBCCCFERqj4JoQQQgghREao%2BCaEEEIIIURGqPgmhBBCCCFERv4P4uM2ORyBEY0AAAAASUVORK5CYII%3D" class="center-img">
</div>
    <div class="row headerrow highlight">
        <h1>Sample</h1>
    </div>
    <div class="row variablerow">
    <div class="col-md-12" style="overflow:scroll; width: 100%%; overflow-y: hidden;">
        <table border="1" class="dataframe sample">
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
      <th>0</th>
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
      <th>1</th>
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
      <th>2</th>
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
      <th>3</th>
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
      <th>4</th>
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
</div>
</div>




```python
df.corr()
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
      <th>Current Loan Amount</th>
      <th>Credit Score</th>
      <th>Annual Income</th>
      <th>Years of Credit History</th>
      <th>Months since last delinquent</th>
      <th>Number of Open Accounts</th>
      <th>Number of Credit Problems</th>
      <th>Current Credit Balance</th>
      <th>Bankruptcies</th>
      <th>Tax Liens</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Current Loan Amount</th>
      <td>1.000000</td>
      <td>-0.139743</td>
      <td>0.024069</td>
      <td>0.014725</td>
      <td>0.003488</td>
      <td>-0.003094</td>
      <td>-0.000062</td>
      <td>0.003138</td>
      <td>0.003576</td>
      <td>-0.003069</td>
    </tr>
    <tr>
      <th>Credit Score</th>
      <td>-0.139743</td>
      <td>1.000000</td>
      <td>-0.033221</td>
      <td>-0.011658</td>
      <td>-0.007994</td>
      <td>0.008124</td>
      <td>0.000777</td>
      <td>-0.003263</td>
      <td>-0.003426</td>
      <td>0.004381</td>
    </tr>
    <tr>
      <th>Annual Income</th>
      <td>0.024069</td>
      <td>-0.033221</td>
      <td>1.000000</td>
      <td>0.146859</td>
      <td>-0.059675</td>
      <td>0.140463</td>
      <td>-0.013672</td>
      <td>0.292165</td>
      <td>-0.044837</td>
      <td>0.038185</td>
    </tr>
    <tr>
      <th>Years of Credit History</th>
      <td>0.014725</td>
      <td>-0.011658</td>
      <td>0.146859</td>
      <td>1.000000</td>
      <td>-0.039695</td>
      <td>0.128033</td>
      <td>0.061251</td>
      <td>0.201001</td>
      <td>0.062049</td>
      <td>0.020915</td>
    </tr>
    <tr>
      <th>Months since last delinquent</th>
      <td>0.003488</td>
      <td>-0.007994</td>
      <td>-0.059675</td>
      <td>-0.039695</td>
      <td>1.000000</td>
      <td>-0.035803</td>
      <td>0.088612</td>
      <td>-0.024292</td>
      <td>0.112907</td>
      <td>0.002730</td>
    </tr>
    <tr>
      <th>Number of Open Accounts</th>
      <td>-0.003094</td>
      <td>0.008124</td>
      <td>0.140463</td>
      <td>0.128033</td>
      <td>-0.035803</td>
      <td>1.000000</td>
      <td>-0.013731</td>
      <td>0.222763</td>
      <td>-0.022805</td>
      <td>0.005754</td>
    </tr>
    <tr>
      <th>Number of Credit Problems</th>
      <td>-0.000062</td>
      <td>0.000777</td>
      <td>-0.013672</td>
      <td>0.061251</td>
      <td>0.088612</td>
      <td>-0.013731</td>
      <td>1.000000</td>
      <td>-0.103814</td>
      <td>0.755866</td>
      <td>0.584917</td>
    </tr>
    <tr>
      <th>Current Credit Balance</th>
      <td>0.003138</td>
      <td>-0.003263</td>
      <td>0.292165</td>
      <td>0.201001</td>
      <td>-0.024292</td>
      <td>0.222763</td>
      <td>-0.103814</td>
      <td>1.000000</td>
      <td>-0.117995</td>
      <td>-0.011118</td>
    </tr>
    <tr>
      <th>Bankruptcies</th>
      <td>0.003576</td>
      <td>-0.003426</td>
      <td>-0.044837</td>
      <td>0.062049</td>
      <td>0.112907</td>
      <td>-0.022805</td>
      <td>0.755866</td>
      <td>-0.117995</td>
      <td>1.000000</td>
      <td>0.046160</td>
    </tr>
    <tr>
      <th>Tax Liens</th>
      <td>-0.003069</td>
      <td>0.004381</td>
      <td>0.038185</td>
      <td>0.020915</td>
      <td>0.002730</td>
      <td>0.005754</td>
      <td>0.584917</td>
      <td>-0.011118</td>
      <td>0.046160</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
print(df.info())
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
    None



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





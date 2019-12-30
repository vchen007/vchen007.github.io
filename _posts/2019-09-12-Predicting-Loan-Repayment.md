---
layout: post
title: Predicting Loan Repayment
categories: 
 - Blog
 - Regression
permalink: /posts/1
nocomments: true  # Disable the comment box. This is EasyBook feature
---

# Business Objective 
A bank has given us a data set and would like us to find which potential customers will likely repay a bank loan and what questions to ask on future applications based off of previous loan data.
1. Clean the data set of Loans and verify if loan were paid or defaulted. 
2. Look for the Customers who have paid and predict if future customers will pay back or default loan.
3. Come up with questions for customer when they are applying for loan

# Taking a look at the data set
![pandas .info() function](/Users/vchen123/Desktop/Dev Masters Prework/PBL #1)


Looking at the data, multiple columns have missing information that need to be filled and object columns need to be convereted to numbers.

**Number|**Loan ID**|**Customer ID**|**Loan Status**|**Current Loan Amount**|**Term**|**Credit Score**|**Years in current job**|**Home Ownership**|**Annual Income**|**Purpose**|**Monthly Debt**|**Years of Credit History**|**Months since last delinquent**|**Number of Open Accounts**|**Number of Credit Problems**|**Current Credit Balance**|**Maximum Open Credit**|**Bankruptcies**|**Tax Liens**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
0|000025bb-5694-4cff-b17d-192b1a98ba44|5ebc8bb1-5eb9-4404-b11b-a6eebc401a19|Fully Paid|11520|Short Term|741.0|10+ years|Home Mortgage|33694.0|Debt Consolidation|$584.03|12.3|41.0|10|0|6760|16056|0.0
1|00002c49-3a29-4bd4-8f67-c8f8fbc1048c|927b388d-2e01-423f-a8dc-f7e42d668f46|Fully Paid|3441|Short Term|734.0|4 years|Home Mortgage|42269.0|other|$1,106.04|26.3|NaN|17|0|6262|19149|0.0
2|00002d89-27f3-409b-aa76-90834f359a65|defce609-c631-447d-aad6-1270615e89c4|Fully Paid|21029|Short Term|747.0|10+ years|Home Mortgage|90126.0|Debt Consolidation|$1,321.85|28.8|NaN|5|0|20967|28335|0.0
3|00005222-b4d8-45a4-ad8c-186057e24233|070bcecb-aae7-4485-a26a-e0403e7bb6c5|Fully Paid|18743|Short Term|747.0|10+ years|Own Home|38072.0|Debt Consolidation|$751.92|26.2|NaN|9|0|22529|43915|0.0
4|0000757f-a121-41ed-b17b-162e76647c1f|dde79588-12f0-4811-bab0-e2b07f633fcd|Fully Paid|11731|Short Term|746.0|4 years|Rent|50025.0|Debt Consolidation|$355.18|11.5|NaN|12|0|17391|37081|0.0
5|0000a149-b055-4a57-b762-280783ccc25e|62ddc017-7023-4ba7-af23-1a7cd16c1ce5|Fully Paid|10208|Short Term|716.0|10+ years|Rent|41853.0|Business Loan|$561.52|13.2|NaN|4|1|2289|4671|1.0
6|0000afa6-8902-4f8f-b870-25a8fdad0aeb|e49c1a82-a0f7-45e8-9f46-2f75c43f9fbc|Charged Off|24613|Long Term|6640.0|6 years|Rent|49225.0|Business Loan|$542.29|17.6|73.0|7|0|14123|16954|0.0
7|0000afa6-8902-4f8f-b870-25a8fdad0aeb|e49c1a82-a0f7-45e8-9f46-2f75c43f9fbc|Charged Off|24613|Long Term|NaN|6 years|Rent|NaN|Business Loan|$542.29|17.6|73.0|7|0|14123|16954|0.0
8|00011dfc-31c1-4178-932a-fbeb3f341efb|ef6e098c-6c83-4752-8d00-ff793e476b8c|Fully Paid|10036|Short Term|NaN|5 years|Rent|NaN|Debt Consolidation|$386.36|17.7|NaN|7|0|11970|16579|0.0
9|0001cb86-af28-4011-bb86-183786e473ae|4aae67bb-d54b-41ae-8bce-1d62022ed8dd|Fully Paid|2036|Short Term|733.0|NaN|Home Mortgage|55985.0|Debt Consolidation|$741.79|19.8|29.0|7|0|10926|15676|0.0


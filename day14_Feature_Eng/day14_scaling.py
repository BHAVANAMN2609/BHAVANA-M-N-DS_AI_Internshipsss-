Goal: Ensure features with large numbers (like Salary) don't drown out features with small numbers (like Age).
Instructions:
Create two versions of your numeric data:
Standardized: (Mean = 0, Std = 1) using StandardScaler.
Normalized: (Range 0 to 1) using MinMaxScaler.
Plot a histogram of a feature before and after scaling to see the change in the x-axis.Why: Distance-based algorithms (like KNN or SVM) will assume a difference of $1,000 in salary is 1,000 times more important than a difference of 1 year in age if you don't scale.
/5
/5
Excellent
5 pts
Effectively applies scaling; explains why Standard vs Min-Max was chosen for the specific algorithm used.
Good
3 pts
Scaling is applied, but student fails to observe or document the change in data distribution.
Developing
1 pt
Scaling is missing or applied after training the model (invalidating the process).
# Some background stuff for my lecture

# Generate the data:
import pandas as pd
import numpy as np
import os
os.chdir('C:/Users/johng/OneDrive - Johns Hopkins/TA/Polytechnic')
         
# set seed
np.random.seed(12122023)

# size of data set
num_women = 500


# Generating data for women who work
working_women = pd.DataFrame({
    'Age': np.round(np.random.normal(loc=35, scale=8, size=num_women // 2)),
    'Education': np.random.choice([10, 11, 12, 13, 14, 15, 16, 17, 18], size=num_women // 2, p=[0.1,0.02,0.30,0.05,0.03,0.02,0.36,0.02,0.1,]),
    'Kids'     : np.random.choice([0,1,2,3], size=num_women // 2, p=[0.5,0.3,0.15,0.05,])
})

# now rig up a wage equation
working_women['wages'] = working_women.Age*.25 + working_women.Education*.7 + working_women.Kids*(-0.15) + np.random.normal(loc=5, scale=4, size=num_women // 2)
working_women.to_csv('./workers.csv', index=False)
working_women['H'] = np.ones(num_women // 2)
# (arbitrary coefficient choiee)

# Generating data for women who do not work (with rounded ages)
non_working_women = pd.DataFrame({
    'Age': np.round(np.random.normal(loc=35, scale=8, size=num_women // 2)),
    'Education': np.random.choice([10, 11, 12, 13, 14, 15, 16, 17, 18], size=num_women // 2, p=[0.13,0.04,0.35,0.05,0.03,0.02,0.31,0.02,0.05,]),
    'Kids'     : np.random.choice([0,1,2,3], size=num_women // 2, p=[0.25,0.35,0.25,0.15,])
})

non_working_women['wages'] = working_women.Age*.25 + working_women.Education*.5 + working_women.Kids*(-0.15) + np.random.normal(loc=3, scale=4, size=num_women // 2)
non_working_women['H'] = np.zeros(num_women // 2)

np.mean(wages)
np.mean(shadow_wages)

women_data = pd.concat([working_women, non_working_women], ignore_index=True)

# Shuffle the dataset
women_data = women_data.sample(frac=1).reset_index(drop=True)

# Display the first few rows of the dataset
print(women_data.head())

women_data.to_csv('./full_data.csv', index=False)

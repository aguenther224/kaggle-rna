# Import necessary libraries/packages
import os
import re
import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns

# Check current working directory
os.getcwd()

# Import and rename dataframes to notebook

from os import listdir
def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]

filenames = find_csv_filenames("C:/Users/Alex/sr3fk")
for name in filenames:
  print (name)
dfs = [0,1,2,3,4,5]
for i in range(len(filenames)):
    dfs[i] = pd.read_csv(filenames[i])

sample_submission    = dfs[0]
test_sequences       = dfs[1]
train_labels         = dfs[2]
train_sequences      = dfs[3]
validation_labels    = dfs[4]
validation_sequences = dfs[5]





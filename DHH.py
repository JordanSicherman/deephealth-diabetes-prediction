import pandas as pd
import numpy as np
import statsmodels.formula.api as smf

d = pd.read_csv("diabetes-training.csv").replace({"?": np.nan, "None": np.nan, "Other": np.nan, "Up": 2, "AfricanAmerican": 2, ">30": 2,
                                                  "Male": 1, "Hispanic": 1, "<30": 1, "Steady": 1, "Ch": 1, "Yes": 1,
                                                  "No": 0, "NO": 0, "Caucasian": 0, "Female": 0, "Down": -1,
                                                  "[0-10)": 0, "[10-20)": 1, "[20-30)": 2, "[30-40)": 3, "[40-50)": 4, "[50-60)": 5, "[60-70)": 6, "[70-80)": 7, "[80-90)": 8, "[90-100)": 9})

msk = np.random.rand(len(data)) < 0.8

train = data[msk]
test = data[~msk]

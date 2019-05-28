import pandas as pd
from scipy.stats import zscore
import warnings
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')

foods_df = pd.read_csv("../data/nutrients.csv", header=0)
columns = foods_df.columns

foods_df['Calories'].plot.hist(
  bins = 50,
  title = "Histogram of the Calories variable"
)

foods_df["calories_zscore"] = zscore(foods_df["Calories"])
foods_df["calories_is_outlier"] = foods_df["calories_zscore"].apply(lambda x: x <= -2.5 or x >= 2.5)
outliers = foods_df["calories_is_outlier"]



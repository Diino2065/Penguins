import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

sns.set_theme(style="whitegrid")

df = sns.load_dataset("penguins")
df = df.dropna()
print(f"Oblik skupa: {df.shape}")

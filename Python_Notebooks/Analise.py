#%%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %%

df = pd.read_csv("..\\Data_Cleaned\\Daily_clean_dataset.csv")
df_2 = pd.read_csv("..\\Data_Cleaned\\bellabeat_clean_dataset.csv")

# %%

avg_steps = df.groupby('Id')['TotalSteps'].mean().reset_index()
avg_steps

# %%

activity_distribution = df['activity_level'].value_counts()

activity_distribution
# %%

plt.scatter(df['TotalSteps'], df['Calories'])
plt.xlabel("Steps")
plt.ylabel("Calories")
plt.title("Steps vs Calories")
plt.show()
# %%

df['SedentaryMinutes'].mean()
# %%

steps_by_day = df.groupby('Weekday')['TotalSteps'].mean()

steps_by_day.plot(kind='bar')
plt.show()
# %%

df_2.groupby('activity_level')['TotalMinutesAsleep'].mean()
# %%
df_2['TotalMinutesAsleep'].mean()
# %%

hourly = pd.read_csv("..\Data\\mturkfitbit_export_4.12.16-5.12.16\Fitabase Data 4.12.16-5.12.16\hourlySteps_merged.csv")

hourly['ActivityHour'] = pd.to_datetime(hourly['ActivityHour'])

hourly['hour'] = hourly['ActivityHour'].dt.hour

hourly.groupby('hour')['StepTotal'].mean().plot()
plt.show()
# %%

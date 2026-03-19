#%%

import pandas as pd

# %%

daily_3_12 = pd.read_csv("..\\Data\\mturkfitbit_export_3.12.16-4.11.16\\Fitabase Data 3.12.16-4.11.16\\dailyActivity_merged.csv")

daily_4_12 = pd.read_csv("..\\Data\\mturkfitbit_export_4.12.16-5.12.16\\Fitabase Data 4.12.16-5.12.16\\dailyActivity_merged.csv")

sleep = pd.read_csv("..\\Data\\mturkfitbit_export_4.12.16-5.12.16\\Fitabase Data 4.12.16-5.12.16\\sleepDay_merged.csv")



# %%
daily = pd.concat([daily_3_12, daily_4_12])

#%%

daily.info()

sleep.info()
# %%

daily['ActivityDate'] = pd.to_datetime(daily['ActivityDate']) 



sleep['SleepDay'] = pd.to_datetime(
    sleep['SleepDay'])


# %%

daily.duplicated().sum()


sleep.duplicated().sum()

# %%


sleep = sleep.drop_duplicates()


# %%

daily[daily['TotalSteps'] < 0]

#%%

daily[daily['Calories'] == 0]
#%%



#%%


# %%

daily["Weekday"] = daily['ActivityDate'].dt.day_name()

# %%

def classify_activity(steps):
    
    if steps < 5000:
        return "Sedentary"
    
    elif steps < 7500:
        return "Lightly Active"
    
    elif steps < 10000:
        return "Moderately Active"
    
    else:
        return "Very Active"

daily['activity_level'] = daily['TotalSteps'].apply(classify_activity)




#%%

daily = daily.dropna()
sleep = sleep.dropna()

# %%

merged = pd.merge(
    daily,
    sleep,
    left_on=['Id','ActivityDate'],
    right_on=['Id','SleepDay'],
    how='inner'
)

# %%
merged.columns

#%%
final = merged[[
    'Id',
    'ActivityDate',
    'TotalSteps',
    'Calories',
    'VeryActiveMinutes',
    'SedentaryMinutes',
    'TotalMinutesAsleep',
    'TotalTimeInBed',
    'Weekday',
    'activity_level'
]]

# %%

final.to_csv("..\\Data_Cleaned\\bellabeat_clean_dataset.csv", index=False)

# %%

daily.to_csv("..\\Data_Cleaned\\Daily_clean_dataset.csv", index=False)

# %%
sleep.to_csv("..\\Data_Cleaned\\Sleep_clean_dataset.csv", index=False)


# %%

import pandas as pd

df1 = pd.read_csv('avg_tmin_by_tract_2020-2024.csv')
df2 = pd.read_csv('avg_tmin_by_tract_2015-2019.csv')

# 1. Left join: all 2020-2024 tracts, bring in 2015-2019 data where matched
merged = df1.merge(
    df2,
    left_on='tract_fips20',
    right_on='tract_fips10',
    how='left'
).drop(columns='tract_fips10')  # drop redundant ID column

# 2. Append 2015-2019-only tracts (not matched to any 2020 tract)
only_2015 = df2[~df2['tract_fips10'].isin(df1['tract_fips20'])].rename(
    columns={'tract_fips10': 'tract_fips20'}
)
combined = pd.concat([merged, only_2015], ignore_index=True)

# 3. Sort columns chronologically and rows by tract ID
year_cols = [str(y) for y in range(2015, 2025) if str(y) in combined.columns]
combined = combined[['tract_fips20'] + year_cols].sort_values('tract_fips20').reset_index(drop=True)

combined.to_csv('avg_tmin_combined_2015-2024.csv', index=False)
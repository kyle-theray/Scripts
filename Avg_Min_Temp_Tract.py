import pandas as pd

# ── 1. Load the filtered data ─────────────────────────────────────────────────
df = pd.read_csv('2024_output.csv')

# ── 2. Convert tmin from tenths of a degree to actual degrees ─────────────────
# (Standard gridMET/Daymet encoding: values are scaled by 100)
df['tmin_actual'] = df['tmin'] / 100

# ── 3. Calculate average minimum temperature per census tract; use 'tract_fips10' for data from 2015 to 2019 ─────────────────
avg_tmin = (
    df.groupby('tract_fips20', as_index=False)['tmin_actual']
    .mean()
    .rename(columns={'tmin_actual': 'avg_tmin'})
    .round(2)
)

# ── 4. Save results ───────────────────────────────────────────────────────────
avg_tmin.to_csv('avg_tmin_by_tract_2024.csv', index=False)

print(f"Total census tracts: {len(avg_tmin)}")
print(f"\nAverage minimum temperature (°) by census tract:")
print(avg_tmin.to_string(index=False))

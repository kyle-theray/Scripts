import pandas as pd

# ── 1. Load the data ──────────────────────────────────────────────────────────
# Adjust the filename/path to match your actual file
df = pd.read_csv('nanda_PRISM_daily_Tract_2024_01P.csv')
# df = pd.read_csv('test.csv')


# ── 2. Filter ─────────────────────────────────────────────────────────────────
mask = (
    (df['month'] >= 6) &                                      # June–August
    (df['month'] <= 8) &
    (df['tract_fips20'].astype(str).str.startswith('13121'))  # Fulton Co., GA tracts, use 'tract_fips10' for data from 2015 to 2019
)

filtered_df = df[mask]

# ── 3. Save results ───────────────────────────────────────────────────────────
filtered_df.to_csv('2024_output.csv', index=False)

print(f"Original rows : {len(df):,}")
print(f"Filtered rows : {len(filtered_df):,}")
print(filtered_df.head())
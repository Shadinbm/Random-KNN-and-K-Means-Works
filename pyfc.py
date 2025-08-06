# import pandas as pd

# # Load the CSV file
# df = pd.read_csv("dat.csv")

# # Drop all columns whose names start with 'Unnamed'
# df = df.loc[:, ~df.columns.str.startswith('Unnamed')]

# # (Optional) Save cleaned data back to a new file
# df.to_csv("datfresh.csv", index=False)

# # Print result to verify
# print("Remaining columns:")
# print(df.columns.tolist())
import pandas as pd

df = pd.read_csv("datfresh.csv")

# Add serial number column starting from 1
df.insert(0, 'S.No', range(1, len(df) + 1))

# Save to new CSV
df.to_csv("datfresh.csv", index=False)

# Optional: print preview
# print(df.head())

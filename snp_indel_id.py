import pandas as pd

# Load the Excel file into a pandas DataFrame
df = pd.read_excel('88_snp_PASS.xlsx')

# Create a new column to specify SNP, Insertion, or Deletion
df['Type'] = df.apply(lambda row: 'SNP' if len(row['REF']) == len(row['ALT']) else ('Insertion' if len(row['REF']) < len(row['ALT']) else 'Deletion'), axis=1)

# Save the DataFrame back to the Excel file
df.to_excel('88_SNP_FILTER.xlsx', index=False)
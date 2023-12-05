
import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset
hawthorn_df = pd.read_csv('Hawthorn.csv')

# Print out the column names to check the correct column name for players
print(hawthorn_df.columns)

# The output will show you the actual column names. Let's assume the correct column name is found to be 'Hawthorn Player'
# Then, you would adjust the code to use this correct column name:

# Function to standardize player names from "Lastname, Firstname" to "Firstname Lastname"
def standardize_name(name):
    parts = name.split(', ')
    return ' '.join(parts[::-1]) if len(parts) == 2 else name 
supercoach_df = pd.read_csv('supercoach.csv')

# Correcting the column name in the DataFrame
hawthorn_df['Player'] = hawthorn_df['Player'].apply(standardize_name)

# Do the same for the Supercoach DataFrame
# Assuming that you have already loaded supercoach_df and the column name for player is 'Supercoach Player'
supercoach_df['Player'] = supercoach_df['Player'].apply(standardize_name)

# After correcting the column names, you can proceed with merging the DataFrames on the standardized player names
# Make sure to replace the 'Hawthorn Player' and 'Supercoach Player' with the actual column names from your DataFrames


# Merge the dataframes
merged_df = pd.merge(hawthorn_df, supercoach_df, on='Player')

# Save the merged dataframe
merged_df.to_csv('merged_hawthorn_supercoach.csv', index=False)
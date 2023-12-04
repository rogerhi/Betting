import pandas as pd
import matplotlib.pyplot as plt

""" from pip._internal import main as pipmain

pipmain(['install', "icecream"]) """
from icecream import ic
# Function to standardize player names from "Lastname, Firstname" to "Firstname Lastname"
def standardize_name(name):
    parts = name.split(', ')
    return ' '.join(parts[::-1]) if len(parts) == 2 else name

# Load the datasets
hawthorn_df = pd.read_csv('hawthorn.csv')
supercoach_df = pd.read_csv('supercoach.csv')

# Standardize the player names in both dataframes
# Remove leading and trailing spaces from column names
hawthorn_df.columns = hawthorn_df.columns.str.strip()

# Now apply the standardize_name function
hawthorn_df['Player'] = hawthorn_df['Player'].apply(standardize_name)

supercoach_df['Player'] = supercoach_df['Player'].apply(standardize_name)

# Merge the datasets on player names
combined_df = pd.merge(hawthorn_df, supercoach_df[['Player', 'Supercoach Value']], on='Player', how='left')

# Now you can perform analysis on the combined_df
# For example, to see the correlation between goals scored and Supercoach value
correlation = combined_df[['GL', 'Supercoach Value']].corr()

# Create a scatter plot
plt.scatter(combined_df['DI'], combined_df['Supercoach Value'])
plt.title('Goals vs Supercoach Value')
plt.xlabel('Goals Scored')
plt.ylabel('Supercoach Value')
plt.show()
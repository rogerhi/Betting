# Let's try loading the file again with this new information
import pandas as pd

supercoach_scores_path_latest_info = 'supercoach.csv'

try:
    # Reading the CSV file with the assumption that the first row is the header
    supercoach_df_latest_info = pd.read_csv(supercoach_scores_path_latest_info)
    load_success_latest_info = True
except Exception as e:
    load_success_latest_info = False
    error_message_latest_info = str(e)

# Checking if the file was loaded successfully
load_success_latest_info, supercoach_df_latest_info.head() if load_success_latest_info else error_message_latest_info

print(supercoach_df_latest_info.head())
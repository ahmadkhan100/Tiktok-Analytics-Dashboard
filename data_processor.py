# data_processor.py
import pandas as pd

def process_data(df):
    """
    Clean and process the TikTok data DataFrame.

    Parameters:
    - df: A pandas DataFrame with raw data from TikTok.

    Returns:
    - A processed pandas DataFrame with cleaned and organized data.
    """
    # Here you would include any cleaning steps such as removing duplicates,
    # handling missing values, or parsing dates. This is a placeholder.
    
    # Example: Convert duration from seconds to minutes
    df['duration'] = df['duration'].apply(lambda x: x / 60)
    
    # Sorting data by duration of the videos
    df = df.sort_values(by='duration')
    
    return df

# The process_data function can be imported and used in the main app.py to prepare the data
# before feeding it to the visualizations.


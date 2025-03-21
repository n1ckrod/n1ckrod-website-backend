import os
import pandas as pd
from datetime import datetime
from zoneinfo import ZoneInfo

def process_csv_files(folder_path):
    # Get list of CSV files in the folder, ignore case (.csv, .CSV, etc)
    csv_files = [f for f in os.listdir(folder_path) 
                 if f.lower().endswith('.csv') and os.path.isfile(os.path.join(folder_path, f))]
    
    if not csv_files:
        print(f"No CSV files found in {folder_path}")
        return
        
    for csv_file in csv_files:
        try:
            # Read CSV file
            file_path = os.path.join(folder_path, csv_file)
            df = pd.read_csv(file_path)
            
            # Convert first column (UTC seconds) to EST datetime
            first_col = df.columns[0]
            df[first_col] = pd.to_datetime(df[first_col], unit='s', utc=True)
            df[first_col] = df[first_col].dt.tz_convert(ZoneInfo('America/New_York'))
            
            # Group by minute and calculate mean for all columns
            df = df.set_index(first_col)
            df = df.resample('1T', closed='left', label='left').mean()
            
            # Save processed file
            output_path = os.path.join(folder_path, f'processed_{csv_file}')
            df.to_csv(output_path)
            print(f"Successfully processed: {csv_file}")
            
        except Exception as e:
            print(f"Error processing {csv_file}: {str(e)}")

# Example usage:
# folder_path = "path/to/your/csv/folder"
# process_csv_files(folder_path)

if __name__ == "__main__":
    folder_path = "YOUR_FOLDER_PATH_HERE"  # Replace with your actual folder path
    process_csv_files(folder_path)
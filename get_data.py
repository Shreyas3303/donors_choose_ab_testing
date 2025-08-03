import kagglehub
import os
import pandas as pd

# Step 1: Download the dataset
path = kagglehub.dataset_download("arunasivapragasam/donors-choose")
print("Path to dataset files:", path)

# Step 2: List all files in the dataset folder
files = os.listdir(path)
print("Downloaded files:", files)

# Step 3: Find the first CSV file and load it
csv_file = next((f for f in files if f.endswith(".csv")), None)
if csv_file is None:
    raise FileNotFoundError("No CSV file found in the dataset folder.")

csv_path = os.path.join(path, csv_file)
df = pd.read_csv(csv_path)
print("Preview of data:\n", df.head())

# Step 4: Save a copy of the CSV
output_path = "donors_choose_copy.csv"
df.to_csv(output_path, index=False)
print("File saved to:", output_path)

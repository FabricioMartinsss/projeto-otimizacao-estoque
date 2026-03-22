import sqlite3
import os
import pandas as pd

conn = sqlite3.connect("data/processed/olist.db")

raw_path = "data/raw"
csv_files = [f for f in os.listdir(raw_path) if f.endswith(".csv")]

for file in csv_files: 
    file_path = os.path.join(raw_path, file)
    df = pd.read_csv(file_path)
    table_name = file.replace(".csv", "")
    df.to_sql(table_name, conn, if_exists="replace", index=False)

conn.close()
import os
from dotenv import load_dotenv

from etl.extract   import extract
from etl.transform import transform
from etl.load      import load


#Load environment variables
load_dotenv()

DB_USER     = os.getenv("DB_USER",     "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_HOST     = os.getenv("DB_HOST",     "localhost")
DB_NAME     = os.getenv("DB_NAME",     "superstore_db")

DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

RAW_DATA_PATH = "data/raw_superstore.csv"

# Run ETL Pipeline 
if __name__ == "__main__":
    print("\n Starting Superstore ETL Pipeline\n")

    df_raw     = extract(RAW_DATA_PATH)       # E — Extract
    df_clean   = transform(df_raw)            # T — Transform
    load(df_clean, DB_URL)                    # L — Load

    

    print("\n Pipeline finished successfully!\n")

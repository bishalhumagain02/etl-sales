import pandas as pd
import sqlalchemy
from sqlalchemy import text

def load(df: pd.DataFrame, db_url: str) -> None:
    """
    LOAD: Push the cleaned DataFrame into MySQL.

    Uses SQLAlchemy + pymysql.
    if_exists='replace' drops and recreates the table each run (good for dev).
    Switch to if_exists='append' for incremental loads later.
    """
    print("\n" + "=" * 50)
    print(" LOAD PHASE")
    print("=" * 50)

    try:
        engine = sqlalchemy.create_engine(db_url)

        # Test connection
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print(" Connected to MySQL successfully")

        # Write to MySQL
        df.to_sql(
            name="sales",
            con=engine,
            if_exists="replace",   # Drop and recreate table each run
            index=False,
            chunksize=500,         # Write in batches of 500 rows
        )

        # Verify row count
        with engine.connect() as conn:
            result = conn.execute(text("SELECT COUNT(*) FROM sales"))
            count = result.scalar()

        print(f" {count} rows loaded into 'superstore_db.sales'")

    except Exception as e:
        print(f" Load failed: {e}")
        raise

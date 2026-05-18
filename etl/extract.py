import pandas as pd

def extract(filepath: str) -> pd.DataFrame:
    
    print("=" * 50)
    print(" EXTRACT PHASE")
    print("=" * 50)

    df = pd.read_csv(filepath, encoding="latin-1")  # Superstore CSV uses latin-1

    print(f" Loaded {len(df)} rows, {len(df.columns)} columns")
    print(f"   Columns: {list(df.columns)}")
    print(f"\n   Sample (3 rows):")
    print(df.head(3).to_string(index=False))

    return df

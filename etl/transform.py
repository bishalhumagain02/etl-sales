import pandas as pd

def transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    TRANSFORM: Clean, standardize, and enrich the raw Superstore data.

    Steps:
        1. Standardize column names
        2. Drop duplicates
        3. Handle missing values
        4. Fix data types
        5. Derive new columns (profit_margin, shipping_days)
        6. Filter bad records
        7. Sort
    """
    print("\n" + "=" * 50)
    print(" TRANSFORM PHASE")
    print("=" * 50)

    original_count = len(df)

    # Standardize column 
    df.columns = (
        df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")
    )
    

    # Drop exact duplicate rows
    df = df.drop_duplicates()
    

    # Handle missing values
  
    df["postal_code"] = df["postal_code"].fillna("Unknown").astype(str)

    # Drop rows where critical fields are missing
    critical_cols = ["order_id", "sales", "quantity", "profit", "product_name"]
    df = df.dropna(subset=critical_cols)

    # Fix data types 
    df["order_date"] = pd.to_datetime(df["order_date"], infer_datetime_format=True)
    df["ship_date"]  = pd.to_datetime(df["ship_date"],  infer_datetime_format=True)
    df["sales"]      = df["sales"].astype(float).round(2)
    df["profit"]     = df["profit"].astype(float).round(2)
    df["quantity"]   = df["quantity"].astype(int)
    df["discount"]   = df["discount"].astype(float).round(2)

    # Standardize text casing
    for col in ["segment", "region", "category", "sub_category", "ship_mode"]:
        df[col] = df[col].str.strip().str.title()

    

    #  Derive new columns 
    # Profit margin = profit / sales (avoid division by zero)
    df["profit_margin"] = (df["profit"] / df["sales"]).round(4)

    # Shipping days = difference between order_date and ship_date
    df["shipping_days"] = (df["ship_date"] - df["order_date"]).dt.days


    # Filter bad/invalid records 
    
    df = df[df["sales"]     > 0]          # No zero or negative sales
    df = df[df["quantity"]  > 0]          # No zero or negative quantity
    df = df[df["shipping_days"] >= 0]     # Ship date can't be before order date
    

    # Sort by order date 
    df = df.sort_values("order_date").reset_index(drop=True)
   

    # ── Summary ───────────────────────────────────────────
    print(f"\n Transform Summary:")
    print(f"   Rows before : {original_count}")
    print(f"   Rows after  : {len(df)}")
    print(f"   Rows removed: {original_count - len(df)}")
    print(f"\n   Cleaned sample:")
    print(df[["order_id", "category", "sales", "profit", "profit_margin", "shipping_days"]].head(5).to_string(index=False))

    return df

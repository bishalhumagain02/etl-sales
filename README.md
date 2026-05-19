

A data engineering project that builds a complete ETL pipeline
using Python, Pandas and MySQL on the Kaggle Superstore dataset.

# Setup

# 1. Install dependencies
```bash
pip install -r requirements.txt
```

# 2. Download dataset
Go to https://www.kaggle.com/datasets/vivek468/superstore-dataset-final
Download and place as `data/raw_superstore.csv`

# 3. Set up MySQL
```bash
mysql -u root -p < db_setup.sql
```

# 4. Configure credentials
```bash
cp .env.example .env
# Edit .env with your MySQL password
```

# 5. Run the pipeline
```bash
python main.py
```



#  ETL Steps

| Step | File | What it does |
|------|------|-------------|
| Extract | `etl/extract.py` | Reads CSV with latin-1 encoding |
| Transform | `etl/transform.py` | Cleans nulls, fixes types, derives new columns |
| Load | `etl/load.py` | Loads into MySQL via SQLAlchemy |
| Analysis | `analysis/queries.py` | Runs 6 SQL business insight queries |



##  Transformations Applied

- Standardized column names (lowercase, underscores)
- Removed duplicate rows
- Handled missing values (drop or fill)
- Fixed date formats with `pd.to_datetime()`
- Standardized text casing (Title Case)
- Derived `profit_margin = profit / sales`
- Derived `shipping_days = ship_date - order_date`
- Filtered invalid records (negative sales, negative shipping days)



#  Business Insights Generated

1. Sales, Profit & Orders by Category
2. Top 10 Most Profitable Products
3. Monthly Sales Trend
4. Region-wise Performance
5. Customer Segment Analysis
6. Loss-Making Sub-Categories


# Tech Stack

- Python 3.8+
- Pandas — data cleaning & transformation
- MySQL— data warehouse
- SQLAlchemy + PyMySQL — database connector
- python-dotenv— secure credentials management

# Importing Modules
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql import DataFrame
from functools import reduce

# Initializing the spark session
spark = (
    SparkSession
    .builder
    .appName('Pivoting Data')
    .getOrCreate()
)

# Previewing one file
apple_df = spark.read.csv(
    './01. Pivoting Data/data/AAPL.csv',
    header=True,
    inferSchema=True
)
apple_df.show(5, False)

# Selecting the columns
selected_columns = ['Date', 'Adj Close']
apple_df = apple_df.select(selected_columns)
apple_df.show(5, False)

# Renaming Column
apple_df = apple_df.withColumnRenamed('Adj Close', 'apple')
apple_df.show(5, False)

""" Let's combine all the above steps and apply to all the files """
# Let's read all the files in a list of DataFrames
file_path = [
    './01. Pivoting Data/data/AAPL.csv',
    './01. Pivoting Data/data/BMW.csv',
    './01. Pivoting Data/data/Other/Cars/TM.csv',
    './01. Pivoting Data/data/Other/Tech/GOOG.csv',
    './01. Pivoting Data/data/Other/Tech/MSFT.csv',
]

df_list = [
    spark.read.csv(csv_path, header=True, inferSchema=True)
    for csv_path in file_path
]

# Selecing the desired columns and renaming the 'Adj Close' column

def select_columns(df:DataFrame, alias:str) -> DataFrame:
    """ Selects the columns from the provided DataFrame """
    return df.select(F.col('Date'), F.col('Adj Close').alias(alias))

alias_name = [
    'apple',
    'bmw',
    'tm',
    'google',
    'microsoft',
]

df_selected = [
    select_columns(df, name) for df, name in zip(df_list, alias_name)
]

# Joining all the DataFrames
def join_df(df1:DataFrame, df2:DataFrame) -> DataFrame:
    """ Joins the two data frame on the provided column using inner function"""
    return df1.join(
        df2,
        on='Date',
    )

stock_df = reduce(join_df, df_selected)
stock_df.show(5, False)

# Unpivot our data
unpivot_expr = """
stack(
    5,
    'apple', apple, 
    'bmw', bmw, 
    'tm', tm, 
    'google', google, 
    'microsoft', microsoft
    )
    AS
    (Company, Price)
"""

stocks = stock_df.select(F.col('Date'), F.expr(unpivot_expr))
stocks.show(10, False)
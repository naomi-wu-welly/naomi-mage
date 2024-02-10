import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):

    # Define the months you're interested in
    months = [10, 11, 12]
    # Define dtype, parse method as course
    taxi_dtypes = {
        'VendorID': pd.Int64Dtype(),
        'passenger_count': pd.Int64Dtype(),
        'trip_distance': float,
        'RatecodeID':pd.Int64Dtype(),
        'store_and_fwd_flag':str,
        'PULocationID':pd.Int64Dtype(),
        'DOLocationID':pd.Int64Dtype(),
        'payment_type': pd.Int64Dtype(),
        'fare_amount': float,
        'extra':float,
        'mta_tax':float,
        'tip_amount':float,
        'tolls_amount':float,
        'improvement_surcharge':float,
        'total_amount':float,
        'congestion_surcharge':float
        }
    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

    df_merged = pd.DataFrame()

    # Load data for each month and append to the list
    for month in months:
        # Construct the URL for the file
        url = f"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-{month}.csv.gz"
    
        # Read the CSV file into a DataFrame
        df = pd.read_csv(url, sep=',', compression="gzip", dtype=taxi_dtypes, parse_dates=parse_dates)
        # Append the DataFrame to the list
        df_merged = pd.concat([df_merged, df], ignore_index=True, sort=False)
        
    return df_merged

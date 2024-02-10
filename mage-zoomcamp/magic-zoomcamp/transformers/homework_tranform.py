if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    # Remove rows where the passenger count is equal to 0 and the trip distance is equal to zero
    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]

    # Create a new column lpep_pickup_date by converting lpep_pickup_datetime to a date
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    # Rename columns in Camel Case to Snake Case, e.g. VendorID to vendor_id
    data = data.rename(columns=
        {'VendorID': 'vendor_id'
        ,'lpep_pickup_datetime': 'lpep_pickup_datetime'
        ,'lpep_dropoff_datetime': 'lpep_dropoff_datetime'
        ,'store_and_fwd_flag': 'store_and_fwd_flag'
        ,'RatecodeID': 'ratecode_id'
        ,'PULocationID': 'pickup_location_id'
        ,'DOLocationID': 'dropoff_location_id'
        ,'passenger_count': 'passenger_count'    
        ,'trip_distance': 'trip_distance'
        ,'fare_amount': 'fare_amount'
        ,'extra': 'extra'
        ,'mta_tax': 'mta_tax'
        ,'tip_amount': 'tip_amount'
        ,'tolls_amount': 'tolls_amount'
        ,'ehail_fee': 'ehail_fee'
        ,'improvement_surcharge': 'improvement_surcharge'
        ,'total_amount': 'total_amount'
        ,'payment_type': 'payment_type'
        ,'trip_type': 'trip_type'
        , 'congestion_surcharge': 'congestion_surcharge'})
    
    return data

@test
def test_output(output, *args) -> None:
    # Add three assertions:
    # vendor_id is one of the existing values in the column (currently)
    assert set(['vendor_id']).issubset(output.columns)
    # passenger_count is greater than 0
    assert (output['passenger_count'] > 0).all()
    # trip_distance is greater than 0
    assert (output['trip_distance'] > 0).all()

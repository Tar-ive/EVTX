import pandas as pd

def load_data():
    county_ev_df = pd.read_csv('county_ev.csv')
    total_ev_count_by_county_df = pd.read_csv('total_ev_count_by_county.csv')
    tx_zip_codes_data_df = pd.read_csv('tx-zip-codes-data.csv')

    # Handle NaN values in 'Grand Total' column
    county_ev_df['Grand Total'] = county_ev_df['Grand Total'].fillna(0)

    return county_ev_df, total_ev_count_by_county_df, tx_zip_codes_data_df

def calculate_ev_density(county_ev_df, tx_zip_codes_data_df):
    # Aggregate the total number of EVs in each county
    ev_counts_by_county = county_ev_df.groupby('County')['Grand Total'].sum().reset_index()
    ev_counts_by_county.columns = ['County', 'ev_count']

    # Merge this aggregated data with the population data
    merged_data = pd.merge(ev_counts_by_county, tx_zip_codes_data_df, left_on='County', right_on='county')

    return merged_data

def get_top_ev_models(county_ev_df):
    # Sum up the counts for each model
    model_sums = county_ev_df.drop(columns=['County', 'Latitude', 'Longitude', 'Grand Total']).sum().sort_values(ascending=False)
    top_ev_models = model_sums.reset_index()
    top_ev_models.columns = ['Model', 'Count']
    return top_ev_models

def get_top_tesla_counties(county_ev_df):
    # Sum up the counts for Tesla models
    tesla_models = ['Tesla Model 3', 'Tesla Model S', 'Tesla Model X', 'Tesla Model Y']
    county_ev_df['TeslaCount'] = county_ev_df[tesla_models].sum(axis=1)
    top_tesla_counties = county_ev_df.groupby('County')['TeslaCount'].sum().reset_index()
    top_tesla_counties = top_tesla_counties.sort_values(by='TeslaCount', ascending=False).head(20)
    return top_tesla_counties

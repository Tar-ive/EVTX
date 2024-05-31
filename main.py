import streamlit as st
import pandas as pd
import plotly.express as px
from calculations import load_data, calculate_ev_density, get_top_ev_models, get_top_tesla_counties

# Load the datasets
county_ev_df, total_ev_count_by_county_df, tx_zip_codes_data_df = load_data()
merged_data = calculate_ev_density(county_ev_df, tx_zip_codes_data_df)
top_ev_models = get_top_ev_models(county_ev_df)
top_tesla_counties = get_top_tesla_counties(county_ev_df)

# Create a sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["EV Registrations in Texas", "Tesla Registrations", "Download Data"])

# Add data source caption
data_source = "**Data source: Dallas-Fort Worth Clean Cities Coalition (DFWCC)**"

if page == "EV Registrations in Texas":
    st.title("EV Registrations in Texas")

    # Sidebar filter
    st.sidebar.header("Filter by Model")
    model = st.sidebar.selectbox("Model", county_ev_df.columns[2:-3])

    # Filter the data based on user selection
    filtered_data = county_ev_df[["County", "Latitude", "Longitude", model]]
    filtered_data["TotalCount"] = filtered_data[model]

    # Handle NaN values in 'TotalCount' column
    filtered_data['TotalCount'] = filtered_data['TotalCount'].fillna(0)

    # Map visualization
    st.header("EV Registrations Map")
    fig = px.scatter_mapbox(
        filtered_data,
        lat="Latitude",
        lon="Longitude",
        size="TotalCount",
        color="County",
        hover_name="County",
        mapbox_style="carto-positron",
        title="EV Registrations by County"
    )
    fig.update_layout(height=750)  # Increase height for a larger map
    st.plotly_chart(fig, use_container_width=True)
    st.caption("Zoom in or Zoom out to see the full data.")
    st.caption(data_source)

    # Top 20 counties by total EV registrations
    st.header("Top 20 Counties by EV Registrations")
    top_20_counties = total_ev_count_by_county_df.nlargest(20, 'Vehicle Count')

    # Bar chart for top 20 counties
    fig3 = px.bar(
        top_20_counties,
        x="county",
        y="Vehicle Count",
        title="Top 20 Counties by EV Registrations",
        labels={"county": "County", "Vehicle Count": "Total EV Registrations"},
        color="county",
        height=550  # Increase height for a larger chart
    )
    st.plotly_chart(fig3, use_container_width=True)
    st.caption(data_source)

    # Bottom 20 counties by total EV registrations
    st.header("Bottom 20 Counties by EV Registrations")
    bottom_20_counties = total_ev_count_by_county_df.nsmallest(20, 'Vehicle Count')

    # Bar chart for bottom 20 counties
    fig4 = px.bar(
        bottom_20_counties,
        x="county",
        y="Vehicle Count",
        title="Bottom 20 Counties by EV Registrations",
        labels={"county": "County", "Vehicle Count": "Total EV Registrations"},
        color="county",
        height=550  # Increase height for a larger chart
    )
    st.plotly_chart(fig4, use_container_width=True)
    st.caption(data_source)

    # Top EV models
    st.header("Top EV Models")

    fig5 = px.bar(
        top_ev_models.head(20),  # Show top 20 EV models
        x="Model",
        y="Count",
        title="Top EV Models",
        labels={"Model": "EV Model", "Count": "Number of Registrations"},
        color="Model",
        height=550  # Increase height for a larger chart
    )
    st.plotly_chart(fig5, use_container_width=True)
    st.caption(data_source)

elif page == "Tesla Registrations":
    st.title("Tesla Registrations in Texas")

    # Filter for Tesla registrations
    tesla_data = county_ev_df[["County", "Latitude", "Longitude", "Tesla Model 3", "Tesla Model S", "Tesla Model X", "Tesla Model Y"]]
    tesla_data["TeslaCount"] = tesla_data[["Tesla Model 3", "Tesla Model S", "Tesla Model X", "Tesla Model Y"]].sum(axis=1)

    # Handle NaN values in 'TeslaCount' column
    tesla_data['TeslaCount'] = tesla_data['TeslaCount'].fillna(0)

    # Map visualization for Tesla
    st.header("Tesla Registrations Map")
    fig2 = px.scatter_mapbox(
        tesla_data,
        lat="Latitude",
        lon="Longitude",
        size="TeslaCount",
        color="County",
        hover_name="County",
        mapbox_style="carto-positron",
        title="Tesla Registrations by County in Texas"
    )
    fig2.update_layout(height=750)  # Increase height for a larger map
    st.plotly_chart(fig2, use_container_width=True)
    st.caption("Zoom in or Zoom out to see the full data.")
    st.caption(data_source)

    # Top counties with highest number of Teslas
    st.header("Top Counties with Highest Number of Teslas")

    fig6 = px.bar(
        top_tesla_counties,
        x="County",
        y="TeslaCount",
        title="Top Counties with Highest Number of Teslas",
        labels={"County": "County", "TeslaCount": "Number of Teslas"},
        color="County",
        height=550  # Increase height for a larger chart
    )
    st.plotly_chart(fig6, use_container_width=True)
    st.caption(data_source)

elif page == "Download Data":
    st.title("Download EV Registration Data")

    # Download buttons for datasets
    st.markdown("### Download Data")
    st.download_button(
        label="Download county_ev.csv",
        data=county_ev_df.to_csv(index=False).encode('utf-8'),
        file_name='county_ev.csv',
        mime='text/csv',
    )
    st.download_button(
        label="Download total_ev_count_by_county.csv",
        data=total_ev_count_by_county_df.to_csv(index=False).encode('utf-8'),
        file_name='total_ev_count_by_county.csv',
        mime='text/csv',
    )
    st.download_button(
        label="Download tx-zip-codes-data.csv",
        data=tx_zip_codes_data_df.to_csv(index=False).encode('utf-8'),
        file_name='tx-zip-codes-data.csv',
        mime='text/csv',
    )
    st.caption(data_source)

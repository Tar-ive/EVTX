# EVTX

https://evs-texas.streamlit.app/

## Overview
**EVTX** is a visual representation project aimed at displaying the distribution and statistics of Electric Vehicles (EVs) across various counties in Texas. This project leverages geographical data visualization techniques to provide insights into the adoption and prevalence of EVs in the state.

## Features
- Interactive map displaying EV distribution by county.
- Visual charts and graphs representing statistical data.
- Data filtering options for detailed analysis.
- User-friendly interface for exploring the data.

## Installation

### Prerequisites
- Python 3.7+
- Virtual environment (recommended)

### Clone the Repository
```bash
git clone https://github.com/tar-ive/EVTX.git
cd EVTX
```

### Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Data Preparation
1. Ensure you have the necessary EV data for Texas counties in CSV or similar format.
2. Place the data file in the `data/` directory.

## Running the Application

### Start the Application
```bash
streamlit run main.py
```

### Access the Application
Open your web browser and go to `http://localhost:8501`.

## Usage
- **Map Visualization**: Explore the interactive map to see the distribution of EVs across different counties.
- **Charts and Graphs**: View various statistical representations of the data.
- **Filters**: Use the available filters to narrow down the data based on specific criteria like county, date range, etc.

## Project Structure
```
EVTX/
├── data/
│   └── ev_data.csv         # Placeholder for your data file
├── app.py                  # Main application script
├── requirements.txt        # List of dependencies
├── README.md               # Project documentation
└── .gitignore              # Git ignore file
```



## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or suggestions, please contact us at [adhsaksham27@gmail.com].

---


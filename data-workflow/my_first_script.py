# Code to curl data using Python
import requests
import pandas as pd
import time
import plotly.express as px


def perform_query(url):
    """
    This function performs a query on a REST API and returns a dataframe with the content 
    of the query
    
    Parameters
    ----------
        url (str) full URL containing the query
        
    Returns
    -------
        jsonResponse (JSON object) containing JSON response in JSON format
    """
    
    try:
        # Time query
        start_time = time.time()
        # Using GET command 
        response = requests.get(url)
        total_time = time.time() - start_time
        print(total_time)
        # Raise issues if response is different from 200
        response.raise_for_status()

        # access JSOn content
        jsonResponse = response.json()

        return jsonResponse
    
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    except JSONDecodeError:
        print("Error, please verify this is a valid API URL")
    except NameError:
        print("Entry point not well defined")
        
        
def download_intensity_by_date(start_d, end_d):
    
    """
    This function downloads actual and forecasted intensity during a given time range
    
    Parameters
    ----------
    start_d (str) date in format YYYY-MM-DD indicating start of observations
    end_d (str) date in format YYYY-MM-DD indicating end of observations
    
    Returns
    -------
    all_df (dataframe) master table with requested queries
    
    """
    try:
        # Create data range 
        date_range = pd.date_range(start=start_d, end=end_d, freq='D')
        dates = [date.date() for date in date_range]
        # Iterate over all dates 
        # Perform query
        # Store content into master dataframe
        all_df = []
        for item in dates:
            new_url = f'https://api.carbonintensity.org.uk/intensity/date/{item}'
            query = perform_query(new_url)
            df = pd.json_normalize(query, record_path="data")
            all_df.append(df)


        return all_df
    except:
        print("Error")
        
if __name__=="__main__":
    start="2019-12-01"
    end="2019-12-31"
    all_df = download_intensity_by_date(start, end)

    master_sheet = pd.concat(all_df)
    #display(master_sheet.head())
    master_sheet.head().to_csv("Master5rows.csv")
    print(master_sheet.info())
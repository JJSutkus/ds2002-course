#!/usr/bin/env python3

#imports
import sys
import os
import logging
import requests
import pandas as pd
from datetime import datetime

#initialize logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

#Extract
def extract():
    """
    Extracts ISS location data from API.

    Returns JSON response from API.
    """

    url = "http://api.open-notify.org/iss-now.json"

    try:
        logger.info("Starting data extraction.") 
        response = requests.get(url, timeout=20)
        response.raise_for_status()
        data = response.json()
        logger.info("Data extraction successful.")
        return data
    
    except requests.exceptions.RequestException as e:
        logger.error(f"Error during API request.")
        sys.exit(1)

#Transform
def transform(data):
    """
    Transfrom raw ISS data into single row pandas data frame.

    Returns pandas.DataFrame: ISS location record
    """

    try:
        logger.info("Starting data transformation.")

        timestamp = data["timestamp"]
        latitude = float(data["iss_position"]["latitude"])
        longitude = float(data["iss_position"]["longitude"])

        time = pd.to_datetime(timestamp, unit="s")

        df = pd.DataFrame([{
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "latitude": latitude,
            "longitude": longitude
        }])

        logger.info("Data transformation successful.")
        return df
    
    except (KeyError, ValueError) as e:
        logger.error(f"Error during transformation: {e}")
        sys.exit(1)

#Load
def load(df, output_file):
    """
    Changes ISS data to CSV and creates file.

    Args:
        df (pandas data frame): ISS data to append
        output: path to CSV output file
    """

    try:
        logger.info("Loading data into output file.")

        df.to_csv(output_file, mode='a', index=False, header=not os.path.exists(output_file))
        logger.info("Data successfully changed to CSV file.")

    except Exception as e:
        logger.error(f"Error during load process: {e}")
        sys.exit(1)

#Main  
def main():
    """
    Main ETL workflow
    """

    if len(sys.argv) != 2:
        logger.error("Usage: python iss.py <output_csv_file>")
        sys.exit(1)

    output_file = sys.argv[1]

    data = extract()
    df = transform(data)
    load(df, output_file)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

#imports
import sys
import os
import logging
import requests
import pandas as pd
from datetime import datetime
import mysql.connector

#initialize logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

#Database Configuration
DB_HOST = "ds2002.cgls84scuy1e.us-east-1.rds.amazonaws.com"
DB_USER = "ds2002"
DB_NAME = "iss"
DB_PASSWORD = "Xf3$fa57CwD!"

REPORTER_ID = "awj8sf"
REPORTER_NAME = "Jonathan Sutkus"

#Database Connection
def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

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
        message = data.get("message", "success")  # default to 'success' if missing

        time = pd.to_datetime(timestamp, unit="s")

        df = pd.DataFrame([{
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "latitude": latitude,
            "longitude": longitude,
            "message": message
        }])

        logger.info("Data transformation successful.")
        return df

    except (KeyError, ValueError) as e:
        logger.error(f"Error during transformation: {e}")
        sys.exit(1)

# Register reporter
def register_reporter(table, reporter_id, reporter_name):

    db = None
    cursor = None

    try:
        db = get_connection()
        cursor = db.cursor()

        check_query = f"SELECT reporter_id FROM {table} WHERE reporter_id = %s"
        cursor.execute(check_query, (reporter_id,))
        result = cursor.fetchone()

        if result is None:
            insert_query = f"""
            INSERT INTO {table} (reporter_id, reporter_name)
            VALUES (%s, %s)
            """
            cursor.execute(insert_query, (reporter_id, reporter_name))
            db.commit()
            logger.info("Reporter registered.")
        else:
            logger.info("Reporter already exists.")

    except Exception as e:
        logger.error(f"Database error: {e}")

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

# Load
def load(df):

    db = None
    cursor = None

    try:
        logger.info("Loading data into database.")

        db = get_connection()
        cursor = db.cursor()

        row = df.iloc[0]

        insert_query = """
        INSERT INTO locations
        (message, latitude, longitude, timestamp, reporter_id)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(insert_query, (
            row["message"],
            row["latitude"],
            row["longitude"],
            row["timestamp"],
            REPORTER_ID
        ))

        db.commit()

        logger.info("Location inserted into database.")

    except Exception as e:
        logger.error(f"Error during load process: {e}")
        sys.exit(1)

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()


# Main
def main():

    # register reporter once
    register_reporter("reporters", REPORTER_ID, REPORTER_NAME)

    data = extract()
    df = transform(data)
    load(df)


if __name__ == "__main__":
    main()
"""Download NYC Yellow Taxi trip data for 2023."""
import os
from pathlib import Path
from urllib.request import urlretrieve
from tqdm import tqdm

DATA_DIR = Path(__file__).parent.parent / "data" / "raw"
BASE_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data"
YEAR = 2023
TAXI_TYPE = "yellow"

def download_month(year: int, month: int, taxi_type: str = "yellow") -> Path:
    """Download a single month of a taxi trip data

    Args:
        year: Year (e.g., 2023).
        month: Month (1-12).
        taxi_type: 'yellow', 'green', or 'fhv'.

    Returns:
        Path to the download file.
    """
    filename = f"{taxi_type}_tripdata_{year}-{month:02d}.parquet"
    url = f"{BASE_URL}/{filename}"
    output_path = DATA_DIR / filename

    if output_path.exists():
        print(f"Already exists: {filename}")
        return output_path
    
    print(f"Downloading: {filename}")
    urlretrieve(url, output_path)
    return output_path

def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    for month in tqdm(range(1, 13), desc="Months"):
        try:
            download_month(YEAR, month, TAXI_TYPE)
        except Exception as e:
            print(f"x Failed for month {month}: {e}")

    print(f"\n Done. Files in: {DATA_DIR}")

if __name__ =="__main__":
    main() 
    
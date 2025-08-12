#!/usr/bin/env python3
import requests
from datetime import date

def getOppsFromSamApi():
    """
    Download content from the SAM.gov API and save it to a file.

    inputs: none
    outputs: JSON response saved locally in the working directory where this is run
    assumptions:
        - NAICS code of interest is: 541511
        - Procurement types of interest are: p, r, o, i
        - No more than 1000 results are expected
        - Dates of interest are 01/01/2025 to date (dynamically fetches today's date)
    """
    # base URL for calling the sam.gov API
    # lots hardcoded in here. If you disagree with assumptions above, make this dynamically populated
    url = f"https://api.sam.gov/prod/opportunities/v2/search?limit=1000&api_key={API_KEY_HERE}&postedFrom=01/01/2025&postedTo={date.today().strftime('%m/%d/%Y')}&ncode=541511&ptype=p&ptype=r&ptype=o&ptype=i"

    # Make the request
    response = requests.get(url)

    # Raise an error if it failed
    response.raise_for_status()

    # Save the raw content to a file
    with open("samapiresponse.json", "wb") as f:
        f.write(response.content)

    print("Saved API response to output_file")

if __name__ == "__main__":
    getOppsFromSamApi()

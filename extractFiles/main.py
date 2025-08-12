#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

def download_file(url, output_file):
    """Download a file using curl."""
    subprocess.run(
        ["curl", "-L", "-o", output_file, url],
        check=True
    )

def process_json(input_json):
    """Read JSON, extract resource links, and download them."""
    with open(input_json, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    opportunities = data.get("opportunitiesData", [])
    
    for opp in opportunities:
        notice_id = str(opp.get("noticeId", "unknown"))
        links = opp.get("resourceLinks") or []
        
        # Filter out null/None links
        valid_links = [link for link in links if link is not None]
        
        for idx, link in enumerate(valid_links, start=1):
            filename = f"{notice_id}_{idx}"
            print(f"Downloading: {link} → {filename}")
            try:
                download_file(link, filename)
            except subprocess.CalledProcessError:
                print(f"Failed to download {link}")

if __name__ == "__main__":
    # Path to your JSON file
    json_path = "../samapiresponse.json"
    
    process_json(json_path)

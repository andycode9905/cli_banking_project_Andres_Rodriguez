# storage.py
# Provides helper functions to load and save JSON data used across the application.
# Author: Andres Felipe Rodriguez Ortiz

import json
import os

def load_json(filepath):
    """
    Loads and returns data from a JSON file.
    If the file doesn't exist, returns an empty list.
    
    Parameters:
        filepath (str): Path to the JSON file.
    
    Returns:
        list or dict: Parsed JSON content.
    """
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r") as f:
        return json.load(f)

def save_json(filepath, data):
    """
    Saves data to a JSON file with indentation for readability.
    
    Parameters:
        filepath (str): Path to the JSON file.
        data (list or dict): Data to be saved.
    """
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)




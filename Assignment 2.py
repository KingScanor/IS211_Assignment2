# Assignment 2

import requests
import csv

def download_data(url):
    """
       Downloads the data from thr URL.

       Args:
           url (str): The URL to download data from.

       Returns:
           str: The downloaded content, or None if an error occurs.
       """
    try:
        response = requests.get(url)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while downloading data: {e}")
        return None
url = "https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv"
downloaded_content = download_data(url)

if downloaded_content:
    print (downloaded_content)
else:
    print ("Download Failed")

def processData (content):
    """
       builds a dictionary mapping IDs to (name, birthday) tuples after parsing the content of the CSV file.

        Args:
            content (str): The CSV content to process.

        Returns:
            dict: A dictionary mapping IDs to (name, birthday) tuples.
        """
    data_dict = {}
    reader = csv.reader(content.splitlines())
    next(reader) # Skip header

    for row in reader:
         id, name, birthday = row
         data_dict[int(id)] = (name, birthday)

    return data_dict

def displayPerson(id, data_dict):
    """
    prints the name and date of birth linked to the specified ID.

    Args:
        id (int): The ID to look up.
        data_dict (dict): The dictionary mapping IDs to (name, birthday) tuples.
    """
    if id in data_dict:
        name,birthday  = data_dict[id]
        print (f"Person ID {id}: Name - {name}, Birthday - {birthday}")
    else:
        print("No user found with that id")

url = "https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv"
csv_content = download_data(url)

if csv_content:
    data_dict = processData(csv_content)

    # Show information for a specific ID.
    displayPerson(50, data_dict)

else:
    print("Failed to download data.")
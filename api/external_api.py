import requests

from config import EXTERNAL_API_ENDPOINT

HEADERS = {'x-rapidapi-key': "4c1e1966admshbadb4f437ae744ep137974jsn8df6fec9d8c9",
           'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com"}


def fetch_data_from_external_api(term):
    """
    Fetches data from an external API based on the given search term.

    Args:
        term (str): The search term for the API request.

    Returns:
        dict: The JSON response from the API.
    """
    querystring = {"term": term}
    response = requests.get(EXTERNAL_API_ENDPOINT, headers=HEADERS, params=querystring)
    response.raise_for_status()
    return response.json()


def sort_by_attribute(data, key_containing_list="list", attribute="thumbs_up"):
    """
    Sorts a list inside a dictionary based on a specific attribute.

    Args:
        data (dict): The data containing the list.
        key_containing_list (str, optional): The key in the dictionary that points to the list. Defaults to "list".
        attribute (str, optional): The attribute based on which the list should be sorted. Defaults to "thumbs_up".

    Returns:
        list: The sorted list.

    Raises:
        ValueError: If the data isn't a dictionary or the specified key doesn't point to a list.
    """
    if not isinstance(data, dict):
        raise ValueError("Expected data to be a dictionary.")

    list_data = data.get(key_containing_list, [])

    if not isinstance(list_data, list):
        raise ValueError(f"The value associated with the key '{key_containing_list}' is not a list.")

    return sorted(list_data, key=lambda x: x.get(attribute, 0), reverse=True)


def get_first_entry_attribute(data, key_containing_list="list", attribute="definition"):
    """
    Retrieves a specific attribute from the first entry of a sorted list inside a dictionary.

    Args:
        data (dict): The data containing the list.
        key_containing_list (str, optional): The key in the dictionary that points to the list. Defaults to "list".
        attribute (str, optional): The attribute to be retrieved from the first entry. Defaults to "definition".

    Returns:
        Any: The value of the specified attribute from the first entry.

    Raises:
        ValueError: If there's no data or the specified attribute doesn't exist in the first entry.
    """
    sorted_data = sort_by_attribute(data, key_containing_list)

    if sorted_data:
        return sorted_data[0].get(attribute)
    else:
        raise ValueError(f"No data found or the attribute '{attribute}' does not exist in the first entry.")

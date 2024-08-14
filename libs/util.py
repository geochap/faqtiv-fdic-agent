def preserve_order(ids, data, key):
    """
    Preserves the order of items based on the list of IDs.

    Args:
        ids (list): The list of IDs.
        data (list): The list of data dictionaries.
        key (str): The key to match IDs in data.

    Returns:
        list: A list of data dictionaries in the order of the given IDs.
    """
    data_dict = {str(item[key]): item for item in data}
    return [data_dict[str(id)] for id in ids if str(id) in data_dict]

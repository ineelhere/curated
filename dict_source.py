from pymongo import MongoClient

def download_data(db_name, collection_name, connection_string):
    """
    Downloads data from MongoDB and returns it as a dictionary.

    :param db_name: Name of the database.
    :param collection_name: Name of the collection.
    :param connection_string: MongoDB connection string.
    :return: Dictionary containing the fetched data.
    """
    client = MongoClient(connection_string)
    db = client[db_name]
    collection = db[collection_name]
    
    # Fetch the data
    documents = collection.find()
    
    # Convert the fetched data into a dictionary
    data_dict = {doc['title']: doc['url'] for doc in documents}
    
    return data_dict

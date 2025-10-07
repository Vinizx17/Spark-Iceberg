from pymongo import MongoClient

def get_mongo_collection(uri: str, db_name: str, collection_name: str):
    """
    Conecta no MongoDB e retorna a coleção desejada.
    """
    client = MongoClient(uri)
    db = client[db_name]
    return db[collection_name]

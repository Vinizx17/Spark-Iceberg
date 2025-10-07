from mongo_client import get_mongo_collection
from exporter import export_sales_to_parquet_bytes
from minio_client import upload_bytes_to_minio

MONGO_URI = "mongodb://mongodb:27017/"
DB_NAME = "database"
COLLECTION_NAME = "sales"
MINIO_BUCKET = "raw"
MINIO_OBJECT = "sales.parquet"

def main():
    collection = get_mongo_collection(MONGO_URI, DB_NAME, COLLECTION_NAME)
    parquet_buffer = export_sales_to_parquet_bytes(collection)
    if parquet_buffer:
        upload_bytes_to_minio(parquet_buffer, MINIO_BUCKET, MINIO_OBJECT)
        print(f"Dados enviados para o bucket '{MINIO_BUCKET}' como '{MINIO_OBJECT}'.")

if __name__ == "__main__":
    main()

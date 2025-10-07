from minio import Minio

def get_minio_client():
    """
    Retorna cliente MinIO.
    """
    return Minio(
        endpoint="minio:9000",
        access_key="minioadmin",
        secret_key="minioadmin",
        secure=False
    )

def upload_bytes_to_minio(data_bytes, bucket: str, object_name: str):
    """
    Envia um buffer de bytes diretamente para o MinIO.
    """
    client = get_minio_client()
    if not client.bucket_exists(bucket):
        client.make_bucket(bucket)
    client.put_object(bucket, object_name, data_bytes, length=-1, part_size=10*1024*1024)
    print(f"{object_name} enviado para o bucket {bucket}")

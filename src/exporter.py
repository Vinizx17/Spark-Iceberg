# exporter.py
import pyarrow as pa
import pyarrow.parquet as pq
import io
from bson.decimal128 import Decimal128
from bson.objectid import ObjectId
from datetime import datetime, date

def convert_values(obj):
    """Converte tipos incompatíveis com PyArrow"""
    if isinstance(obj, Decimal128):
        return float(obj.to_decimal())
    elif isinstance(obj, ObjectId):
        return str(obj)
    elif isinstance(obj, (datetime, date)):
        return obj.isoformat()
    elif isinstance(obj, list):
        return [convert_values(x) for x in obj]
    elif isinstance(obj, dict):
        return {k: convert_values(v) for k, v in obj.items()}
    else:
        return obj

def export_sales_to_parquet_bytes(collection):
    """Extrai documentos do MongoDB, converte e retorna buffer Parquet em memória"""
    docs = list(collection.find({}))
    if not docs:
        print("Coleção vazia.")
        return None

    # Converte valores incompatíveis
    converted_docs = [convert_values(doc) for doc in docs]

    # Cria tabela PyArrow e escreve no buffer
    table = pa.Table.from_pylist(converted_docs)
    buffer = io.BytesIO()
    pq.write_table(table, buffer)
    buffer.seek(0)
    print("✅ Parquet gerado em memória.")
    return buffer

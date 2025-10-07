# Lakehouse Project

Este projeto demonstra um ambiente de **Lakehouse** usando **MongoDB**, **MinIO**, **Apache Spark**, e **Apache Iceberg**, orquestrado via **Docker Compose**.  
O objetivo é extrair dados da collection `sales` do MongoDB, transformar em Parquet e salvar no bucket `raw` do MinIO.  

## Tecnologias

- Python 3.11
- Apache Spark
- Apache Iceberg
- MongoDB
- MinIO
- Docker / Docker Compose


bash
docker-compose up --build -d
Acesse o container Python e execute o pipeline:

bash
docker exec -it mongodb bash
cd docker-entrypoint-initdb.d
sh script.sh
O script vai:

Abrir os arquivos JSON na pasta database

criar a collection sales no banco de dados database


bash
Copiar código
docker exec -it python-env bash
cd /app/src
python3 main.py
O script vai:

Conectar ao MongoDB

Ler a collection sales

Gerar arquivo Parquet em memória

Enviar para o bucket raw do MinIO

Observações
Não há persistência de dados no container Python, tudo é enviado diretamente para MinIO.

O ambiente já está configurado para trabalhar com Iceberg via Spark usando jupyter notebook.

****Ambiente de desenvolvimento, não replicar em produção*****
# Dockerfile
FROM jupyter/pyspark-notebook:spark-3.5.0

USER root

# Instala wget
RUN apt-get update && apt-get install -y wget && rm -rf /var/lib/apt/lists/*

# Cria pasta para JARs (caso não exista)
RUN mkdir -p $SPARK_HOME/jars

# Baixa JARs necessários
RUN wget -P $SPARK_HOME/jars https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-spark-runtime-3.5_2.12/1.4.3/iceberg-spark-runtime-3.5_2.12-1.4.3.jar && \
    wget -P $SPARK_HOME/jars https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar && \
    wget -P $SPARK_HOME/jars https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar

# Instala pacotes Python
RUN pip install --no-cache-dir pyspark python-dotenv

USER $NB_UID

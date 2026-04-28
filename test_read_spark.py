from pyspark.sql import SparkSession
import os

# =========================
# 0. FIX WINDOWS
# =========================
os.environ["HADOOP_HOME"] = "D:\\hadoop"
os.environ["PATH"] += ";D:\\hadoop\\bin"

# =========================
# 1. SPARK SESSION (CLEAN)
# =========================
spark = SparkSession.builder \
    .appName("TestReadMinIO") \
    .config(
        "spark.jars.packages",
        "org.apache.hadoop:hadoop-aws:3.3.4"
    ) \
    .config("spark.hadoop.fs.s3a.endpoint", "http://localhost:9000") \
    .config("spark.hadoop.fs.s3a.access.key", "admin") \
    .config("spark.hadoop.fs.s3a.secret.key", "password") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.io.native.lib.available", "false") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# =========================
# 2. PATH (CEK SESUAI MINIO)
# =========================
path = "s3a://data-lake/online_retail_clean.csv"
# atau:
# path = "s3a://data-lake/processed/online_retail/"

# =========================
# 3. READ DATA
# =========================
print("Membaca data dari MinIO...")

df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("mode", "DROPMALFORMED") \
    .csv(path)

# =========================
# 4. VALIDASI
# =========================
df.show(5)
print("Jumlah data:", df.count())
df.printSchema()

# =========================
# 5. STOP
# =========================
spark.stop()

print("=== TEST SELESAI ===")
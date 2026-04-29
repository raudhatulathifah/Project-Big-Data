import pandas as pd
from minio import Minio

# =========================
# 1. LOAD CSV (PANDAS)
# =========================
df = pd.read_csv("data/raw/online_retail.csv")

print("Jumlah data:", len(df))
print(df.head())

# =========================
# 2. KONEKSI MINIO
# =========================
client = Minio(
    "localhost:9000",
    access_key="admin",
    secret_key="password",
    secure=False
)

bucket = "data-lake"

if not client.bucket_exists(bucket):
    client.make_bucket(bucket)

# =========================
# 3. SIMPAN CSV KE MINIO
# =========================
file_path = "online_retail_clean.csv"
df.to_csv(file_path, index=False)

client.fput_object(
    bucket,
    "processed/hasil_cleansing.csv",
    file_path
)

print("✔ Data berhasil diupload ke MinIO")

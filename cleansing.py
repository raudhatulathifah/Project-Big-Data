from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim, lower

spark = SparkSession.builder \
    .appName("Cleansing Retail Data") \
    .getOrCreate()

# ======================
# LOAD DATA
# ======================
df_raw = spark.read.csv("online_retail.csv", header=True, inferSchema=True)

print("=== DATA SEBELUM CLEANING ===")
df_raw.show(5)
df_raw.printSchema()

# ======================
# CLEANING
# ======================
df_clean = df_raw

df_clean = df_clean.dropna(subset=["CustomerID"])
df_clean = df_clean.filter(col("Quantity") > 0)
df_clean = df_clean.filter(col("UnitPrice") > 0)
df_clean = df_clean.dropDuplicates()
df_clean = df_clean.withColumn("Description", trim(lower(col("Description"))))

print("=== DATA SETELAH CLEANING ===")
df_clean.show(5)

# ======================
# PERBANDINGAN
# ======================
print("=== PERBANDINGAN JUMLAH DATA ===")
print("Sebelum:", df_raw.count())
print("Sesudah:", df_clean.count())

# ======================
# ANALISIS
# ======================
print("=== GROUP BY COUNTRY ===")
df_clean.groupBy("Country").count().show()

print("=== DESCRIBE ===")
df_clean.describe().show()

# ======================
# SAVE
# ======================
df_clean.toPandas().to_csv("hasil_cleansing.csv", index=False)

print("=== SELESAI ===")

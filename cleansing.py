from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Cleansing Retail Data") \
    .getOrCreate()

df = spark.read.csv("online_retail.csv", header=True, inferSchema=True)

df.show(5)
df.printSchema()

from pyspark.sql.functions import col, trim, lower

# Hapus data tanpa CustomerID
df = df.dropna(subset=["CustomerID"])

# Hapus transaksi aneh
df = df.filter(col("Quantity") > 0)
df = df.filter(col("UnitPrice") > 0)

# Hapus duplikat
df = df.dropDuplicates()

# Rapihin text
df = df.withColumn("Description", trim(lower(col("Description"))))

df.show()

df.groupBy("Country").count().show()
df.describe().show()

print("=== MENYIMPAN KE CSV (PANDAS) ===")

df.toPandas().to_csv("hasil_cleansing.csv", index=False)

print("=== SELESAI ===")
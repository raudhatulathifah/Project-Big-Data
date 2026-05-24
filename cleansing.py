<<<<<<< HEAD
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim, lower

# ======================
# INIT SPARK
# ======================
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
# PROSES CLEANING
# ======================
df_clean = df_raw

# Hapus data tanpa CustomerID
df_clean = df_clean.dropna(subset=["CustomerID"])

# Hapus transaksi tidak valid
df_clean = df_clean.filter(col("Quantity") > 0)
df_clean = df_clean.filter(col("UnitPrice") > 0)

# Hapus duplikat
df_clean = df_clean.dropDuplicates()

# Rapihin teks Description
df_clean = df_clean.withColumn("Description", trim(lower(col("Description"))))

print("=== DATA SETELAH CLEANING ===")
df_clean.show(5)

# ======================
# PERBANDINGAN DATA
# ======================
print("=== PERBANDINGAN JUMLAH DATA ===")
print("Jumlah sebelum:", df_raw.count())
print("Jumlah sesudah:", df_clean.count())
print("Data yang dihapus:", df_raw.count() - df_clean.count())

# ======================
# ANALISIS DATA
# ======================
print("=== JUMLAH TRANSAKSI PER NEGARA ===")
df_clean.groupBy("Country").count().show()

print("=== STATISTIK DATA ===")
df_clean.describe().show()


# ======================
# HANDLE OUTLIER (TAMBAHAN)
# ======================
print("=== HANDLE OUTLIER ===")

# Hitung quantile (1% dan 99%)
quantiles = df_clean.approxQuantile(["Quantity", "UnitPrice"], [0.01, 0.99], 0)

q_low_quantity, q_high_quantity = quantiles[0]
q_low_price, q_high_price = quantiles[1]

# Filter data tanpa outlier
df_no_outlier = df_clean.filter(
    (col("Quantity") >= q_low_quantity) & (col("Quantity") <= q_high_quantity) &
    (col("UnitPrice") >= q_low_price) & (col("UnitPrice") <= q_high_price)
)

print("=== DATA SETELAH HAPUS OUTLIER ===")
df_no_outlier.show(5)

print("Jumlah setelah hapus outlier:", df_no_outlier.count())

# ======================
# SAVE HASIL (PANDAS)
# ======================
print("=== MENYIMPAN KE CSV (PANDAS) ===")

df_clean.toPandas().to_csv("hasil_cleansing.csv", index=False)

# Simpan versi TANPA OUTLIER (untuk ML)
df_no_outlier.toPandas().to_csv("hasil_no_outlier.csv", index=False)

=======
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim, lower

# ======================
# INIT SPARK
# ======================
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
# PROSES CLEANING
# ======================
df_clean = df_raw

# Hapus data tanpa CustomerID
df_clean = df_clean.dropna(subset=["CustomerID"])

# Hapus transaksi tidak valid
df_clean = df_clean.filter(col("Quantity") > 0)
df_clean = df_clean.filter(col("UnitPrice") > 0)

# Hapus duplikat
df_clean = df_clean.dropDuplicates()

# Rapihin teks Description
df_clean = df_clean.withColumn("Description", trim(lower(col("Description"))))

print("=== DATA SETELAH CLEANING ===")
df_clean.show(5)

# ======================
# PERBANDINGAN DATA
# ======================
print("=== PERBANDINGAN JUMLAH DATA ===")
print("Jumlah sebelum:", df_raw.count())
print("Jumlah sesudah:", df_clean.count())
print("Data yang dihapus:", df_raw.count() - df_clean.count())

# ======================
# ANALISIS DATA
# ======================
print("=== JUMLAH TRANSAKSI PER NEGARA ===")
df_clean.groupBy("Country").count().show()

print("=== STATISTIK DATA ===")
df_clean.describe().show()


# ======================
# HANDLE OUTLIER (TAMBAHAN)
# ======================
print("=== HANDLE OUTLIER ===")

# Hitung quantile (1% dan 99%)
quantiles = df_clean.approxQuantile(["Quantity", "UnitPrice"], [0.01, 0.99], 0)

q_low_quantity, q_high_quantity = quantiles[0]
q_low_price, q_high_price = quantiles[1]

# Filter data tanpa outlier
df_no_outlier = df_clean.filter(
    (col("Quantity") >= q_low_quantity) & (col("Quantity") <= q_high_quantity) &
    (col("UnitPrice") >= q_low_price) & (col("UnitPrice") <= q_high_price)
)

print("=== DATA SETELAH HAPUS OUTLIER ===")
df_no_outlier.show(5)

print("Jumlah setelah hapus outlier:", df_no_outlier.count())

# ======================
# SAVE HASIL (PANDAS)
# ======================
print("=== MENYIMPAN KE CSV (PANDAS) ===")

df_clean.toPandas().to_csv("hasil_cleansing.csv", index=False)

# Simpan versi TANPA OUTLIER (untuk ML)
df_no_outlier.toPandas().to_csv("hasil_no_outlier.csv", index=False)

>>>>>>> aaa9441499e0b7722427fbc35aaa89f236fdc7ce
print("=== SELESAI ===")
# Customer Segmentation in ERP Sales Module using K-Means Clustering with Apache Spark MLlib

## 📌 Project Overview

This project implements customer segmentation on the Sales ERP module using the **K-Means Clustering** algorithm based on the **RFM (Recency, Frequency, Monetary)** approach with **Apache Spark MLlib**.

This project was developed by Group 1 as part of the final project for the **Big Data and Analytics (CSD60707)** course in the Information Systems Study Program, Faculty of Computer Science, Universitas Brawijaya.

The analytical process follows the **Medallion Architecture** concept, to generate business-ready analytical data.

---

## 🎯 Objectives

- Perform customer segmentation using K-Means Clustering
- Apply RFM-based feature engineering
- Evaluate clustering quality using:
  - Elbow Method (SSE/WCSS)
  - Silhouette Score
- Generate business insights for:
  - targeted marketing
  - customer retention
  - customer engagement
- Visualize analytical results using Microsoft Power BI

---

## 🛠️ Technologies Used

- Apache Spark (PySpark)
- Spark MLlib
- Python
- MinIO (S3A Storage)
- Microsoft Power BI
- Docker Compose

---

## 🏗️ Architecture Overview

This project implements a simplified Medallion Architecture:

### Bronze Layer
Raw transactional data ingestion.

### Silver Layer
Cleaned and preprocessed transactional data.

### Gold Layer
Business-ready analytical data containing:
- RFM features
- customer segments
- clustering results

---

## ⚙️ Analytical Pipeline

1. Data Ingestion
2. Data Cleaning & Preprocessing
3. Outlier Handling
4. RFM Feature Engineering
5. Feature Scaling & Transformation
6. K-Means Clustering
7. Model Evaluation
8. Dashboard Visualization

---

## 📊 RFM Feature Engineering

The segmentation model uses three main features:

|  Feature  |              Description              |
|-----------|---------------------------------------|
| Recency   | Number of days since last transaction |
| Frequency | Total number of transactions          |
| Monetary  | Total customer spending               |

---

## 🧹 Data Preprocessing

Several preprocessing techniques were applied before clustering:

- Quantile-based outlier filtering (1%–99%)
- Winsorizing/Capping for Monetary feature
- Log Transformation
- StandardScaler normalization

Output datasets:
- `hasil_cleansing.csv`
- `hasil_no_outlier.csv`

---

## 🤖 K-Means Clustering

### Optimal Cluster Selection

The model was evaluated using:
- Elbow Method (SSE/WCSS)
- Silhouette Score

Testing range:
- `k = 2` to `k = 6`

### Final Result

| Metric | Value |
|---|---|
| Optimal Cluster | 3 |
| Silhouette Score | ~0.602 |

The best clustering performance was achieved using **k = 3**.

---

## 📈 Customer Segments

| Segment | Characteristics | Business Strategy |
|---|---|---|
| Loyal Customers | High frequency & monetary | Loyalty program, VIP service |
| Potential Customers | Moderate activity | Upselling & targeted marketing |
| At-Risk Customers | Low activity & high recency | Re-engagement campaign |

---

## 📊 Dashboard

Analytical results were visualized using Microsoft Power BI.

### Dashboard Components
- Total Customers
- Total Revenue
- Average Transactions
- Customer Recency
- Cluster Distribution
- Scatter Plot
- Elbow Method Analysis
- Silhouette Score Analysis
- Top Customers Analysis

### Dashboard Summary

| Metric | Value |
|---|---|
| Total Customers | 4.29K |
| Total Revenue | $31.7M |
| Average Transactions | 4.19 |
| Average Recency | 93.13 |
| Silhouette Score | 0.602 |

---

## 📂 Repository Structure

```bash
Project-Big-Data/
│
├── data_lake/
│   ├── bronze/
│   │   └── online_retail.csv
│   │
│   ├── silver/
│   │   ├── online_retail_clean.csv
│   │   └── hasil_no_outlier.csv
│   │
│   └── gold/
│       ├── clustering/
│       │   └── part-00000-....csv
│       │
│       ├── classification/
│       │   └── final_classification_results.csv
│       │
│       └── dashboard-online-retail-cluster.pbix
│
├── docker-compose.yml
├── ingestion.py
├── cleansing.py
├── ml_clustering.ipynb
├── ml_classification.ipynb
├── test_read_spark.py
├── hasil_no_outlier.zip
└── README.md
```

---

## 👥 Team Members

| Name | Role |
|---|---|
| Farida Choirun Nisa | Project Manager, Business Analyst, Dashboard Developer |
| Raudhatul Athifah | Data Engineer |
| Agatha Jeanetta Arimbi Putri | Data Scientist |
| Ni Kadek Alya Prishantiputri S. | ML Engineer |
| Muthia Khalisha | ML Engineer |

---

## 🚀 Future Improvements

- Implement DBSCAN / Hierarchical Clustering
- Add RFM-T (Tenure) feature
- Automate pipeline using Apache Airflow
- Improve interactive dashboard
- Periodic model retraining

---

## 📎 Documentation & Resources

### Documentation
- Google Docs Report:
  https://docs.google.com/document/d/1005KOwe1Uam4VQziWaEvtNe-bz2K70c1eArvELzN6C0/edit?usp=sharing

### Repository
- GitHub Repository:
  https://github.com/raudhatulathifah/Project-Big-Data.git

### Team Progress Monitoring
- Spreadsheet Monitoring:
  https://docs.google.com/spreadsheets/d/1hGVUVv0-i9ZWqeebGtCxeRPtwAO1RwHbQI7xKvao4O8/edit?usp=sharing

---

## 📌 Course Information

**Course:** Big Data and Analytics (CSD60707)  
**Class:** SI A  
**Group:** Group 1
**Institution:** Information Systems, Faculty of Computer Science, Universitas Brawijaya  
**Year:** 2026

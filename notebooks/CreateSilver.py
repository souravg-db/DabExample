# Databricks notebook source
# MAGIC %md
# MAGIC ### Define Variables

# COMMAND ----------

dbutils.widgets.text("source_table", "test_sg_0923.misc.customer_bronze")
dbutils.widgets.text("target_table", "test_sg_0923.misc.customer_silver")

# COMMAND ----------

source_table = dbutils.widgets.get("source_table")
target_table =  dbutils.widgets.get("target_table")

# COMMAND ----------

filter_clause = " c_mktsegment is not null"

# COMMAND ----------

# MAGIC %md
# MAGIC ### Read Bronze, filter and Write to Silver

# COMMAND ----------

(spark.read
 .table(f"{source_table}")
 .filter(f"{filter_clause}")
 .write
 .format("delta")
 .mode("overwrite")
 .saveAsTable(f"{target_table}")
 )

# COMMAND ----------



# Databricks notebook source
# MAGIC %md
# MAGIC ### Define Variables

# COMMAND ----------

dbutils.widgets.text("source_table", "samples.tpch.customer")
dbutils.widgets.text("target_table", "test_sg_0923.misc.customer_bronze")

# COMMAND ----------

source_table = dbutils.widgets.get("source_table")
target_table =  dbutils.widgets.get("target_table")

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC ### Read Source and write to bronze

# COMMAND ----------

(spark.read
 .table(f"{source_table}")
 .write
 .format("delta")
 .mode("overwrite")
 .saveAsTable(f"{target_table}")
 )

# COMMAND ----------



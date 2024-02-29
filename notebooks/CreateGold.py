# Databricks notebook source
# MAGIC %md
# MAGIC ### Define Variables

# COMMAND ----------

dbutils.widgets.text("source_table", "test_sg_0923.misc.customer_silver")
dbutils.widgets.text("target_table", "test_sg_0923.misc.customer_gold")

# COMMAND ----------

source_table = dbutils.widgets.get("source_table")
target_table =  dbutils.widgets.get("target_table")

# COMMAND ----------

group_by_key = "c_mktsegment"

# COMMAND ----------

# MAGIC %md
# MAGIC ### Read Bronze, filter and Write to Silver

# COMMAND ----------

(spark.read
 .table(f"{source_table}")
 .groupBy(f"{group_by_key}")
 .count()
 .write
 .format("delta")
 .mode("overwrite")
 .saveAsTable(f"{target_table}")
 )

# COMMAND ----------



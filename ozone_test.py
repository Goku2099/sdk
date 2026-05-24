""" Needed manual port-forward because initial Spark Connect
startup took longer than SDK readiness timeout due to
Hadoop AWS dependency downloads."""

from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .remote("sc://localhost:15002")
    .getOrCreate()
)

df = spark.createDataFrame(
    [
        ("sameer", 1),
        ("spark", 2),
    ],
    ["name", "id"]
)

df.show()

df.write.mode("overwrite").csv("s3a://spark-data/demo")

print("Write completed")

df2 = spark.read.csv("s3a://spark-data/demo")

df2.show()

print("Read completed")

from pyspark.sql import SparkSession

# 创建SparkSession
spark = SparkSession.builder.appName("JsonParsingApp").master("local[*]").getOrCreate()

# 读取本地文件
input_path = "file:///Users/tangqiliang/Documents/files/dept/csv/0215"
df = spark.read.option("header", True).csv(input_path)
df.createOrReplaceTempView("my_dept")

# 进行数据清洗和处理
cleaned_df = spark.sql("""
    select 
    company_id,staff_id,dept1,dept2,dept3,dept4,dept5
     from my_dept
""")

# cleaned_df.show()

# 将数据写回本地文件
output_path = "file:///Users/tangqiliang/Documents/files/dept/result/0215"
cleaned_df.repartition(3).write. \
    mode("overwrite"). \
    format("parquet"). \
    save(output_path)

# 停止SparkSession
spark.stop()

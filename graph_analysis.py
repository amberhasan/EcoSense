from pyspark.sql import SparkSession
from graphframes import GraphFrame
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Initialize Spark session
spark = SparkSession.builder.appName("Energy Efficiency Graph Analysis").getOrCreate()

# Sample DataFrames for vertices (buildings) and edges (relationships)
vertices = spark.createDataFrame([
    ("building1", "Building A"),
    ("building2", "Building B"),
    ("building3", "Building C"),
    ("building4", "Building D")
], ["id", "name"])

edges = spark.createDataFrame([
    ("building1", "building2", 0.5),
    ("building2", "building3", 0.8),
    ("building3", "building4", 0.7),
    ("building4", "building1", 0.9)
], ["src", "dst", "weight"])

# Create a GraphFrame
graph = GraphFrame(vertices, edges)

# Perform graph analysis - PageRank
pagerank = graph.pageRank(resetProbability=0.15, maxIter=10)
pagerank_df = pagerank.vertices.select("id", "pagerank").toPandas()

# Initialize FastAPI
app = FastAPI()

# Enable CORS so your frontend can access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint to get PageRank results
@app.get("/graphx-insights")
def get_graph_insights():
    return pagerank_df.to_dict(orient="records")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

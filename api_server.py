from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import energy_graph_analysis
import logging

# Initialize the FastAPI app
app = FastAPI()

# Set up logging for better debugging and monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Enable CORS for cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint to fetch graph insights
@app.get("/graphx-insights")
async def get_graphx_insights():
    """
    Endpoint to retrieve the energy insights from the graph analysis.
    """
    try:
        # Call the analyze_graph function to get the data
        data = energy_graph_analysis.analyze_graph()
        logging.info("Graph insights retrieved successfully")
        return data
    except Exception as e:
        logging.error(f"Error fetching graph insights: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Health check endpoint to confirm that the server is running
@app.get("/health")
async def health_check():
    """
    Health check endpoint to ensure the server is running.
    """
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    # Run the FastAPI server with reload for development
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

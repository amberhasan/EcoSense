from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import energy_graph_analysis

app = FastAPI()

# Enable CORS for cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/graphx-insights")
async def get_graphx_insights():
    try:
        data = energy_graph_analysis.analyze_graph()
        return data
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

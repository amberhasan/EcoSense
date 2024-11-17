from datetime import datetime

def analyze_graph():
    # Example enriched data
    buildings = [
        {
            "building_id": "1",
            "pagerank": 2.5,
            "energy_consumption": 1500,
            "building_type": "Commercial",
            "efficiency_score": 85,
            "recommendations": "Install smart HVAC systems, optimize lighting schedules.",
            "last_updated": datetime.utcnow().isoformat()
        },
        {
            "building_id": "2",
            "pagerank": 3.2,
            "energy_consumption": 1200,
            "building_type": "Residential",
            "efficiency_score": 92,
            "recommendations": "Upgrade insulation, switch to LED lighting.",
            "last_updated": datetime.utcnow().isoformat()
        },
        {
            "building_id": "3",
            "pagerank": 1.8,
            "energy_consumption": 2500,
            "building_type": "Industrial",
            "efficiency_score": 70,
            "recommendations": "Reduce machinery idle time, implement energy monitoring.",
            "last_updated": datetime.utcnow().isoformat()
        }
    ]
    return buildings

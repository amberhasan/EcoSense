from datetime import datetime

def analyze_graph():
    # Example enriched data
    buildings = [
        {
            "building_id": "1",
            "pagerank": 4.5,
            "energy_consumption": 1200,
            "building_type": "Commercial",
            "efficiency_score": 88,
            "recommendations": "Install smart HVAC systems, optimize lighting schedules.",
            "last_updated": datetime.utcnow().isoformat()
        },
        {
            "building_id": "2",
            "pagerank": 3.8,
            "energy_consumption": 950,
            "building_type": "Residential",
            "efficiency_score": 95,
            "recommendations": "Upgrade insulation, switch to LED lighting.",
            "last_updated": datetime.utcnow().isoformat()
        },
        {
            "building_id": "3",
            "pagerank": 2.1,
            "energy_consumption": 1600,
            "building_type": "Industrial",
            "efficiency_score": 73,
            "recommendations": "Reduce machinery idle time, implement energy monitoring.",
            "last_updated": datetime.utcnow().isoformat()
        },
        {
            "building_id": "4",
            "pagerank": 5.0,
            "energy_consumption": 800,
            "building_type": "Educational",
            "efficiency_score": 97,
            "recommendations": "Optimize classroom lighting, use smart thermostats.",
            "last_updated": datetime.utcnow().isoformat()
        },
        {
            "building_id": "5",
            "pagerank": 2.8,
            "energy_consumption": 2000,
            "building_type": "Industrial",
            "efficiency_score": 65,
            "recommendations": "Install energy-efficient motors, improve ventilation.",
            "last_updated": datetime.utcnow().isoformat()
        }
    ]
    return buildings

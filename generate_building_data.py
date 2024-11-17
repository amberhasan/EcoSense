from datetime import datetime, timedelta
import random

def generate_recommendations(building_type, efficiency_score):
    """Generate recommendations based on building type and efficiency score."""
    recommendations = []
    
    if building_type == "Commercial":
        if efficiency_score < 70:
            recommendations.append("Upgrade to energy-efficient lighting systems.")
            recommendations.append("Implement smart HVAC controls.")
        elif efficiency_score < 90:
            recommendations.append("Optimize heating and cooling schedules.")
        else:
            recommendations.append("Conduct regular energy audits.")

    elif building_type == "Residential":
        if efficiency_score < 70:
            recommendations.append("Improve insulation to reduce heat loss.")
            recommendations.append("Switch to LED bulbs and energy-efficient appliances.")
        elif efficiency_score < 90:
            recommendations.append("Seal air leaks around windows and doors.")
        else:
            recommendations.append("Install solar panels to further reduce energy bills.")

    elif building_type == "Industrial":
        if efficiency_score < 70:
            recommendations.append("Reduce machinery idle time and improve maintenance schedules.")
        elif efficiency_score < 90:
            recommendations.append("Implement energy monitoring systems.")
        else:
            recommendations.append("Optimize manufacturing processes for energy efficiency.")

    return ", ".join(recommendations)

def generate_building_data(num_buildings=5):
    """Generate dynamic building data."""
    building_types = ["Commercial", "Residential", "Industrial"]
    buildings = []

    for i in range(1, num_buildings + 1):
        building_type = random.choice(building_types)
        pagerank = round(random.uniform(1, 5), 2)
        energy_consumption = random.randint(1000, 3000)  # in kWh
        efficiency_score = random.randint(50, 100)  # Percentage

        recommendations = generate_recommendations(building_type, efficiency_score)
        
        buildings.append({
            "building_id": str(i),
            "pagerank": pagerank,
            "energy_consumption": energy_consumption,
            "building_type": building_type,
            "efficiency_score": efficiency_score,
            "recommendations": recommendations,
            "last_updated": datetime.utcnow().isoformat()
        })
    
    return buildings

# Function to analyze the graph data
def analyze_graph():
    """Analyze the graph and return enriched building data."""
    return generate_building_data(10)

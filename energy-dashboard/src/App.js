import React, { useEffect, useState } from "react";
import axios from "axios";

// Main App component
function App() {
  const [data, setData] = useState(null); // State to store fetched data
  const [loading, setLoading] = useState(true); // State to indicate loading status
  const [error, setError] = useState(null); // State to store error messages

  // Function to fetch data from FastAPI endpoint
  const fetchData = async () => {
    try {
      const response = await axios.get("http://localhost:8000/energy");
      setData(response.data);
      setLoading(false);
      setError(null); // Clear any previous errors
    } catch (err) {
      console.error("Error fetching data:", err);
      setError("Failed to fetch data. Please try again later.");
      setLoading(false);
    }
  };

  // useEffect to periodically fetch data every 2 seconds
  useEffect(() => {
    fetchData(); // Initial fetch on component mount
    const interval = setInterval(fetchData, 2000); // Fetch every 2 seconds
    return () => clearInterval(interval); // Cleanup interval on component unmount
  }, []);

  return (
    <div
      style={{
        fontFamily: "Arial, sans-serif",
        textAlign: "center",
        padding: "20px",
      }}
    >
      <h1 style={{ color: "#007bff", marginBottom: "20px" }}>
        Real-Time Energy Data Dashboard
      </h1>

      {/* Loading State */}
      {loading && <p>Loading data, please wait...</p>}

      {/* Error State */}
      {error && <p style={{ color: "red" }}>{error}</p>}

      {/* Displaying Data */}
      {data && !loading && (
        <div
          style={{
            border: "2px solid #007bff",
            borderRadius: "10px",
            padding: "20px",
            display: "inline-block",
            textAlign: "left",
            backgroundColor: "#f8f9fa",
            boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
          }}
        >
          <p>
            <strong>Building ID:</strong> {data.building_id || "N/A"}
          </p>
          <p>
            <strong>Timestamp:</strong>{" "}
            {data.timestamp
              ? new Date(data.timestamp * 1000).toLocaleString()
              : "N/A"}
          </p>
          <p>
            <strong>Energy Usage:</strong> {data.energy_usage || "N/A"} kWh
          </p>
          <p>
            <strong>Temperature:</strong> {data.temperature || "N/A"} °C
          </p>
          <p>
            <strong>HVAC Status:</strong> {data.hvac_status || "N/A"}
          </p>
        </div>
      )}

      {/* No Data State */}
      {!loading && !data && !error && (
        <p style={{ color: "orange" }}>
          No new data available. Please check back later.
        </p>
      )}
    </div>
  );
}

export default App;

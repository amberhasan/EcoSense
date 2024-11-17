import React, { useEffect, useState } from "react";
import axios from "axios";
import "./styles.css"; // Import your CSS file

// Main App Component
function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Function to fetch data from FastAPI endpoint
  const fetchData = async () => {
    try {
      const response = await axios.get("http://localhost:8000/energy");
      setData(response.data);
      setLoading(false);
      setError(null);
    } catch (err) {
      console.error("Error fetching data:", err);
      setError("Failed to fetch data. Please try again later.");
      setLoading(false);
    }
  };

  // useEffect to periodically fetch data every 2 seconds
  useEffect(() => {
    fetchData();
    const interval = setInterval(fetchData, 2000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="app-container">
      {/* Header Section */}
      <Header />

      {/* Overview Section */}
      <Overview />

      {/* Real-Time Data Dashboard */}
      <div className="container_fluid">
        {loading && <p>Loading data, please wait...</p>}
        {error && <p className="error-message">{error}</p>}
        {data && <DataDashboard data={data} />}
      </div>

      {/* Footer Section */}
      <Footer />
    </div>
  );
}

function Header() {
  return (
    <div className="container_fluid title">
      <img className="logo" src="images/EcoSense.png" alt="EcoSense Logo" />
      <h1>EcoSense</h1>
    </div>
  );
}

function Overview() {
  return (
    <div className="container_fluid content">
      <div className="bubble">
        <h2>Overview</h2>
        <h3>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed mauris
          sapien, convallis in lectus in, porta elementum risus. Aenean eget est
          vel augue vehicula volutpat. Phasellus sit amet dui molestie, sagittis
          turpis a, convallis neque.
        </h3>
      </div>
      <button type="button" className="btn btn-success btn-lg">
        Get Started
      </button>
    </div>
  );
}

function DataDashboard({ data }) {
  return (
    <div className="data-container">
      <h2>Real-Time Energy Data Dashboard</h2>
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
  );
}

function Footer() {
  return (
    <div className="container_fluid bottom-container">
      <a className="footer-link" href="/about">
        About Us
      </a>
      <p className="copyright">© 2024 EcoSense.</p>
    </div>
  );
}

export default App;

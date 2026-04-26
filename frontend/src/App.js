import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [jobs, setJobs] = useState([]);
  const [search, setSearch] = useState("");
  const [filter, setFilter] = useState("");

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/jobs")
      .then(res => setJobs(res.data))
      .catch(err => console.error(err));
  }, []);

  // 🔍 Filter logic
  const filteredJobs = jobs.filter(job =>
    job.title.toLowerCase().includes(search.toLowerCase()) &&
    (filter === "" || job.category === filter)
  );

  return (
    <div style={{ fontFamily: "Arial", background: "#f5f7fa", minHeight: "100vh" }}>
      
      {/* HEADER */}
      <div style={{
        background: "#0d6efd",
        color: "white",
        padding: "20px",
        textAlign: "center",
        fontSize: "24px",
        fontWeight: "bold"
      }}>
        AcadTrack AI 🚀
      </div>

      {/* 🔍 SEARCH + FILTER */}
      <div style={{
        display: "flex",
        gap: "10px",
        padding: "20px",
        justifyContent: "center"
      }}>
        
        <input
          type="text"
          placeholder="Search jobs..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          style={{
            padding: "10px",
            width: "250px",
            borderRadius: "6px",
            border: "1px solid #ccc"
          }}
        />

        <select
          value={filter}
          onChange={(e) => setFilter(e.target.value)}
          style={{
            padding: "10px",
            borderRadius: "6px"
          }}
        >
          <option value="">All</option>
          <option value="Internship">Internship</option>
          <option value="Faculty">Faculty</option>
          <option value="Research">Research</option>
          <option value="Tender">Tender</option>
        </select>

      </div>

      {/* JOB LIST */}
      <div style={{
        display: "grid",
        gridTemplateColumns: "repeat(auto-fill, minmax(300px, 1fr))",
        gap: "20px",
        padding: "20px"
      }}>
        
        {filteredJobs.map((job, index) => (
          <div key={index} style={{
            background: "white",
            padding: "15px",
            borderRadius: "12px",
            boxShadow: "0 4px 10px rgba(0,0,0,0.1)"
          }}>
            
            <h3>{job.title}</h3>

            <p><b>🏫 {job.institute}</b></p>
            <p><b>📌 {job.category}</b></p>

            <a 
              href={job.link} 
              target="_blank" 
              rel="noreferrer"
              style={{
                display: "inline-block",
                marginTop: "10px",
                padding: "8px 12px",
                background: "#0d6efd",
                color: "white",
                borderRadius: "6px",
                textDecoration: "none"
              }}
            >
              Apply →
            </a>

          </div>
        ))}

      </div>
    </div>
  );
}

export default App;
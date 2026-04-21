import { useEffect, useState } from "react";
import axios from "axios";
import { motion } from "framer-motion";
import { PieChart, Pie, Cell } from "recharts";

function App() {
  const [packets, setPackets] = useState([]);
  const [logs, setLogs] = useState([]);
  const [stats, setStats] = useState({
    normal: 0,
    attack: 0,
  });

  const DURATION = 5;

  useEffect(() => {
    runSimulation();
  }, []);

  const runSimulation = async () => {
    while (true) {
      try {
        const res = await axios.get("http://127.0.0.1:8000/simulate");

        const pkt = {
          id: Date.now(),
          prediction: res.data.prediction,
          actual: res.data.actual,
          confidence: res.data.confidence,
        };

        // UPDATE STATS
        if (pkt.prediction === "Normal") {
          setStats((prev) => ({ ...prev, normal: prev.normal + 1 }));
        } else {
          setStats((prev) => ({ ...prev, attack: prev.attack + 1 }));
        }

        // SHOW PACKET
        setPackets([pkt]);

        // WAIT till reaches server
        await sleep(DURATION * 1000);

        // LOG AFTER DETECTION
        setLogs((prev) => [
          {
            time: new Date().toLocaleTimeString(),
            ...pkt,
          },
          ...prev.slice(0, 9),
        ]);

        await sleep(800);
      } catch (err) {
        console.log("Backend error");
      }
    }
  };

  const sleep = (ms) => new Promise((res) => setTimeout(res, ms));

  return (
    <div style={container}>
      <h1>🚨 NIDS Live Monitoring</h1>

      {/* NETWORK */}
      <div style={networkStyle}>
        
        {/* INTERNET */}
        <div style={internetStyle}>🌐</div>

        {/* SERVER */}
        <div style={serverStyle}>🖥</div>

        {/* PIE CHART */}
        <div style={pieContainer}>
          <h4 style={{ textAlign: "center", marginBottom: "5px" }}>Traffic</h4>

          <PieChart width={180} height={180}>
            <Pie
              data={[
                { name: "Normal", value: stats.normal },
                { name: "Attack", value: stats.attack },
              ]}
              cx="50%"
              cy="50%"
              outerRadius={60}
              dataKey="value"
            >
              <Cell fill="#22c55e" />
              <Cell fill="#ef4444" />
            </Pie>
          </PieChart>
        </div>

        {/* PACKET */}
        {packets.map((pkt) => (
          <motion.div
            key={pkt.id}
            initial={{ x: 120 }}
            animate={{ x: 720 }} // adjusted for new layout
            transition={{ duration: DURATION }}
            style={packetStyle}
          >
            <motion.div
              initial={{ opacity: 0 }}
              animate={{
                opacity: 1,
                background:
                  pkt.prediction === "Normal" ? "#22c55e" : "#ef4444",
              }}
              transition={{ delay: DURATION - 0.2 }}
              style={innerPacket}
            />
          </motion.div>
        ))}
      </div>

      {/* LOGS */}
      <h2 style={{ marginTop: "40px" }}>📊 Detection Logs</h2>

      <table style={table}>
        <thead>
          <tr>
            <th>Time</th>
            <th>Prediction</th>
            <th>Actual</th>
            <th>Confidence</th>
          </tr>
        </thead>

        <tbody>
          {logs.map((log, i) => (
            <tr key={i}>
              <td>{log.time}</td>
              <td style={{ color: log.prediction === "Normal" ? "lime" : "red" }}>
                {log.prediction}
              </td>
              <td>{log.actual}</td>
              <td>{(log.confidence * 100).toFixed(2)}%</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

/* STYLES */

const container = {
  background: "linear-gradient(135deg, #020617, #000000)",
  minHeight: "100vh",
  color: "white",
  padding: "30px",
};

const networkStyle = {
  position: "relative",
  height: "300px",
  borderRadius: "20px",
  background: "rgba(255,255,255,0.05)",
  backdropFilter: "blur(20px)",
  border: "1px solid rgba(255,255,255,0.1)",
  overflow: "hidden",
};

const internetStyle = {
  position: "absolute",
  left: "40px",
  top: "100px",
  width: "100px",
  height: "100px",
  borderRadius: "50%",
  background: "rgba(59,130,246,0.2)",
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  fontSize: "40px",
  boxShadow: "0 0 25px #3b82f6",
};

const serverStyle = {
  position: "absolute",
  right: "300px", // ✅ shifted left (fix overlap)
  top: "100px",
  width: "100px",
  height: "100px",
  borderRadius: "50%",
  background: "rgba(34,197,94,0.2)",
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  fontSize: "40px",
  boxShadow: "0 0 25px #22c55e",
};

const pieContainer = {
  position: "absolute",
  right: "40px", // ✅ stays right
  top: "60px",
  width: "200px",
  height: "200px",
  background: "rgba(255,255,255,0.05)",
  borderRadius: "20px",
  padding: "10px",
  backdropFilter: "blur(10px)",
  boxShadow: "0 0 20px rgba(255,255,255,0.1)",
};

const packetStyle = {
  position: "absolute",
  top: "140px",
  width: "14px",
  height: "14px",
  borderRadius: "50%",
  background: "white",
};

const innerPacket = {
  width: "100%",
  height: "100%",
  borderRadius: "50%",
};

const table = {
  width: "100%",
  textAlign: "center",
  marginTop: "10px",
};

export default App;
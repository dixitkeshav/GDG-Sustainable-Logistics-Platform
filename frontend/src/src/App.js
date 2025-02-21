import React, { useState } from "react";
import { login, trackShipment } from "./api";

function App() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [loginMessage, setLoginMessage] = useState("");
    const [shipmentStatus, setShipmentStatus] = useState("");

    const handleLogin = async () => {
        const response = await login(username, password);
        setLoginMessage(response.message || response.error);
    };

    const handleTrackShipment = async () => {
        const response = await trackShipment();
        setShipmentStatus(response.shipment_status || "Error fetching shipment");
    };

    return (
        <div>
            <h2>Login</h2>
            <input type="text" placeholder="Username" onChange={(e) => setUsername(e.target.value)} />
            <input type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} />
            <button onClick={handleLogin}>Login</button>
            <p>{loginMessage}</p>

            <h2>Track Shipment</h2>
            <button onClick={handleTrackShipment}>Track</button>
            <p>{shipmentStatus}</p>
        </div>
    );
}

export default App;

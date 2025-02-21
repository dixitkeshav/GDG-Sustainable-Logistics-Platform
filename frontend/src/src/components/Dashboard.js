import React, { useState, useEffect } from "react";
import { getShipments } from "../api";

const Dashboard = () => {
    const [shipments, setShipments] = useState([]);
    const [message, setMessage] = useState("");

    useEffect(() => {
        const fetchShipments = async () => {
            const token = localStorage.getItem("token");
            if (!token) {
                setMessage("You must log in first");
                return;
            }
            const result = await getShipments(token);
            if (result.error) {
                setMessage(result.error);
            } else {
                setShipments(result.shipments);
            }
        };

        fetchShipments();
    }, []);

    return (
        <div className="container mt-5">
            <h2>Dashboard</h2>
            {message && <p className="text-danger">{message}</p>}
            <ul className="list-group">
                {shipments.map((shipment, index) => (
                    <li key={index} className="list-group-item">
                        {shipment.tracking_id} - {shipment.status}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Dashboard;

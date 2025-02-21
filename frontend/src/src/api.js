const BASE_URL = "http://127.0.0.1:5000"; // Make sure Flask runs on this

// LOGIN API
export const login = async (username, password) => {
    const response = await fetch("http://127.0.0.1:5000/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
    });

    console.log(response); // Log response to check if request is sent correctly
    return response.json();
};

// SHIPMENT TRACKING API
export const trackShipment = async () => {
    const response = await fetch(`${BASE_URL}/shipment/track`, { // Matches Flask shipment_bp
        method: "GET",
        headers: { "Content-Type": "application/json" },
    });

    return response.json();
};


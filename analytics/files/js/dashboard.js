// Fetch AQI data
async function fetchData(url) {
    const response = await fetch(url);
    return await response.json();
}

async function renderAqiChart() {
    const data = await fetchData('/api/aqi-data/');
    
    // Extract labels and values for AQI chart
    const labels = data.map(entry => new Date(entry.timestamp).toLocaleString());
    const aqiValues = data.map(entry => entry.aqi);
    const locations = data.map(entry => entry.location);  // Get location names

    const ctx = document.getElementById('aqiChart').getContext('2d');
    
    // Create datasets for each location
    const datasets = [];

    // Group data by location
    const locationsSet = new Set(locations);
    locationsSet.forEach(location => {
        const locationData = data.filter(entry => entry.location === location);
        const locationAqiValues = locationData.map(entry => entry.aqi);

        datasets.push({
            label: location,  // Set the label for the location
            data: locationAqiValues,
            borderColor: getRandomColor(), // Get a random color for each location
            backgroundColor: 'rgba(75, 192, 192, 0.2)',  // Customize the background color
            borderWidth: 1
        });
    });

    // Create chart
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: datasets // Use the dynamically created datasets
        },
        options: {
            scales: {
                x: { 
                    title: { 
                        display: true, 
                        text: 'Time' 
                    } 
                },
                y: { 
                    title: { 
                        display: true, 
                        text: 'AQI Level' 
                    } 
                }
            },
            plugins: {
                tooltip: {
                    callbacks: {
                        // Customize tooltips to display location along with AQI value
                        label: function(tooltipItem) {
                            const label = tooltipItem.dataset.label || '';
                            const value = tooltipItem.raw;
                            const time = tooltipItem.label;
                            return `${label} - AQI: ${value} at ${time}`;
                        }
                    }
                }
            }
        }
    });
}

// Utility function to get random color for each location
function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

// Render Vehicle Chart
async function renderVehicleChart() {
    const data = await fetchData('/api/vehicle-data/');
    const labels = data.map(entry => new Date(entry.timestamp).toLocaleString());
    const vehicleCounts = data.map(entry => entry.vehicle_count);

    const ctx = document.getElementById('vehicleChart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Vehicle Count',
                data: vehicleCounts,
                backgroundColor: 'rgba(153, 102, 255, 0.2)',
                borderColor: 'rgba(153, 102, 255, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                x: { title: { display: true, text: 'Time' } },
                y: { title: { display: true, text: 'Vehicles' } }
            }
        }
    });
}

// Render the Map with markers
async function renderMap() {
    const data = await fetchData('/api/aqi-data/');

    // Initialize the map
    const map = L.map('map').setView([20.5937, 78.9629], 5); // Center on India (adjust zoom if needed)

    // Add OpenStreetMap tile layer
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // Loop through the AQI data and place markers
    data.forEach(entry => {
        const { location, aqi, lat, lon } = entry; // Assuming lat and lon are present in your data

        // Create a marker
        const marker = L.marker([lat, lon]).addTo(map);

        // Create a popup to show the AQI data
        const popupContent = `
            <strong>Location:</strong> ${location} <br>
            <strong>AQI:</strong> ${aqi} <br>
            <strong>Timestamp:</strong> ${new Date(entry.timestamp).toLocaleString()}
        `;
        marker.bindPopup(popupContent);
    });
}

document.addEventListener('DOMContentLoaded', () => {
    renderAqiChart();
    renderVehicleChart();
    renderMap(); // Call renderMap to initialize the map and markers
});

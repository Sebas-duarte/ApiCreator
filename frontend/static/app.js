// API Configuration
const API_URL = 'http://localhost:5000';
let authToken = localStorage.getItem('authToken');

// Utility Functions
function showAlert(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type}`;
    alertDiv.textContent = message;
    
    const container = document.querySelector('.container') || document.querySelector('.main-container');
    if (container) {
        container.insertBefore(alertDiv, container.firstChild);
        setTimeout(() => alertDiv.remove(), 3000);
    }
}

function clearAlerts() {
    document.querySelectorAll('.alert').forEach(alert => alert.remove());
}

async function makeRequest(endpoint, method = 'GET', data = null) {
    const options = {
        method,
        headers: {
            'Content-Type': 'application/json',
        }
    };

    if (authToken) {
        options.headers['Authorization'] = `Bearer ${authToken}`;
    }

    if (data) {
        options.body = JSON.stringify(data);
    }

    try {
        const response = await fetch(`${API_URL}${endpoint}`, options);
        const jsonData = await response.json();

        if (!response.ok) {
            throw new Error(jsonData.error || `Error ${response.status}`);
        }

        return jsonData;
    } catch (error) {
        console.error('Request error:', error);
        throw error;
    }
}

function isLoggedIn() {
    return !!authToken;
}

function logout() {
    localStorage.removeItem('authToken');
    authToken = null;
    window.location.href = '/';
}

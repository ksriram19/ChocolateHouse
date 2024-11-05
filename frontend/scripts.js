const apiUrl = "http://127.0.0.1:8000/docs";

// Function to add an item to the specified endpoint
async function addItem(event, endpoint) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());

    // Convert numeric fields to numbers
    for (const key in data) {
        if (!isNaN(data[key])) data[key] = Number(data[key]);
    }

    try {
        const response = await fetch(`${apiUrl}/${endpoint}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data),
        });
        const result = await response.json();
        alert(result.message || "Item added successfully!");
    } catch (error) {
        console.error("Error adding item:", error);
    }
    event.target.reset();
}

// Function to display items from the specified endpoint
async function displayItems(endpoint) {
    try {
        const response = await fetch(`${apiUrl}/${endpoint}`, {
            method: "GET",
        });
        const items = await response.json();
        const displayDiv = document.getElementById(`${endpoint}-display`);
        displayDiv.innerHTML = `<h3>${endpoint.charAt(0).toUpperCase() + endpoint.slice(1)} List</h3>`;
        
        items.forEach(item => {
            displayDiv.innerHTML += `<p>${JSON.stringify(item)}</p>`;
        });
    } catch (error) {
        console.error("Error displaying items:", error);
    }
}

// Function to delete an item by ID for a specified endpoint
async function deleteItem(endpoint, id) {
    try {
        const response = await fetch(`${apiUrl}/${endpoint}?id=${id}`, {
            method: "DELETE",
        });
        const result = await response.json();
        alert(result.message || "Item deleted successfully!");
    } catch (error) {
        console.error("Error deleting item:", error);
    }
}

// Function to update an item by ID for specific endpoints
async function updateItem(endpoint, id, updateData) {
    try {
        const response = await fetch(`${apiUrl}/${endpoint}?id=${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(updateData),
        });
        const result = await response.json();
        alert(result.message || "Item updated successfully!");
    } catch (error) {
        console.error("Error updating item:", error);
    }
}

// Function for Major Category
function callAddMajorCategory() {
    const input = document.getElementById('input1').value;
    fetch(`/AddMajorCategory?input=${input}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('result1').innerText = JSON.stringify(data);
        });
}

// Function for Sub Category
function callAddSubCategory() {
    const input = document.getElementById('input2').value;
    fetch(`/AddSubCategory?input=${input}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('result2').innerText = JSON.stringify(data);
        });
}

// Function for Ingredient
function callAddIngredient() {
    const input = document.getElementById('input3').value;
    fetch(`/AddIngredient?input=${input}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('result3').innerText = JSON.stringify(data);
        });
}

// Function for Allergy
function callAddAllergy() {
    const input = document.getElementById('input4').value;
    fetch(`/AddAllergy?input=${input}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('result4').innerText = JSON.stringify(data);
        });
}

// Function for Customer
function callAddCustomer() {
    const name = document.getElementById('input5').value;
    const phone = document.getElementById('input51').value;
    fetch(`/AddCustomer?name=${name}&phone=${phone}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('result5').innerText = JSON.stringify(data);
        });
}

// Function for Variant
function callAddVariant() {
    const input = document.getElementById('input6').value;
    fetch(`/AddVariant?input=${input}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('result6').innerText = JSON.stringify(data);
        });
}

// Function for Composition
function callAddComposition() {
    const input = document.getElementById('input7').value;
    fetch(`/AddComposition?input=${input}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('result7').innerText = JSON.stringify(data);
        });
}

// Function for Offering
function callAddOffering() {
    const input = document.getElementById('input8').value;
    fetch(`/AddOffering?input=${input}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('result8').innerText = JSON.stringify(data);
        });
}

// Function for Customer Preference
function callAddCustomerPreference() {
    const input = document.getElementById('input9').value;
    fetch(`/AddCustomerPreference?input=${input}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('result9').innerText = JSON.stringify(data);
        });
}

// Function for Customer Allergy
function callAddCustomerAllergy() {
    const input = document.getElementById('input10').value;
    fetch(`/AddCustomerAllergy?input=${input}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('result10').innerText = JSON.stringify(data);
        });
}

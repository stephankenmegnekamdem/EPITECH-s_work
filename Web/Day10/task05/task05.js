const typeInput = document.getElementById("type");
const typeMessage = document.getElementById("typeMessage");
const brandInput = document.getElementById("brand");
const brandMessage = document.getElementById("brandMessage");
const priceInput = document.getElementById("price");
const priceMessage = document.getElementById("priceMessage");
const numberInput = document.getElementById("number");
const numberMessage = document.getElementById("numberMessage");
const resultBody = document.getElementById("resultBody");

function showMessage(element, text, isValid) {
    element.textContent = text;
    element.classList.remove("text-danger", "text-success");
    element.classList.add(isValid ? "text-success" : "text-danger");
}

function clearMessages() {
    [typeMessage, brandMessage, priceMessage, numberMessage].forEach(el => {
        el.textContent = "";
        el.classList.remove("text-danger", "text-success");
    });
}

function fillTable(products) {
    resultBody.innerHTML = "";
    products.forEach(product => {
        const row = document.createElement("tr");
        ["type", "brand", "price", "number", "stock"].forEach(key => {
            const cell = document.createElement("td");
            cell.textContent = product[key];
            row.appendChild(cell);
        });
        resultBody.appendChild(row);
    });
}

document.getElementById("send").addEventListener("click", () => {
    const type = typeInput.value;
    const brand = brandInput.value;
    const price = priceInput.value;
    const number = numberInput.value;

    clearMessages();
    resultBody.innerHTML = "";

    const query = "task06.php?type=" + encodeURIComponent(type)
        + "&brand=" + encodeURIComponent(brand)
        + "&price=" + encodeURIComponent(price)
        + "&number=" + encodeURIComponent(number);

    fetch(query)
        .then(response => response.json())
        .then(data => {
            const errors = data.errors;
            if (errors.type) showMessage(typeMessage, errors.type, false);
            if (errors.brand) showMessage(brandMessage, errors.brand, false);
            if (errors.price) showMessage(priceMessage, errors.price, false);
            if (errors.number) showMessage(numberMessage, errors.number, false);

            if (data.success) {
                fillTable(data.products);
            }
        })
        .catch(() => {
            showMessage(typeMessage, "Error: the request did not succeed.", false);
        });
});
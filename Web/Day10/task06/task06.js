const typeInput = document.getElementById("type");
const typeMessage = document.getElementById("typeMessage");
const brandInput = document.getElementById("brand");
const brandMessage = document.getElementById("brandMessage");
const priceInput = document.getElementById("price");
const priceMessage = document.getElementById("priceMessage");
const numberInput = document.getElementById("number");
const numberMessage = document.getElementById("numberMessage");

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

document.getElementById("send").addEventListener("click", () => {
    const query = "task06.php?type=" + encodeURIComponent(typeInput.value)
        + "&brand=" + encodeURIComponent(brandInput.value)
        + "&price=" + encodeURIComponent(priceInput.value)
        + "&number=" + encodeURIComponent(numberInput.value);

    clearMessages();

    fetch(query)
        .then(response => response.json())
        .then(data => {
            if (!data.success) {
                const errors = data.errors;
                if (errors.type) showMessage(typeMessage, errors.type, false);
                if (errors.brand) showMessage(brandMessage, errors.brand, false);
                if (errors.price) showMessage(priceMessage, errors.price, false);
                if (errors.number) showMessage(numberMessage, errors.number, false);
            } else {
                showMessage(typeMessage, data.message, true);
            }
        })
        .catch(() => {
            showMessage(typeMessage, "Error: the request did not succeed.", false);
        });
});
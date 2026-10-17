
    const typeInput = document.getElementById("type");
    const typeMessage = document.getElementById("typeMessage");
    const brandInput = document.getElementById("brand");
    const brandMessage = document.getElementById("brandMessage");

    function showMessage(element, text, isValid) {
        element.textContent = text;
        element.classList.remove("text-danger", "text-success");
        element.classList.add(isValid ? "text-success" : "text-danger");
    }

    typeInput.addEventListener("input", () => {
        const value = typeInput.value;
        if (value === "") {
            showMessage(typeMessage, "No type sent yet!", false);
            return;
        }
        if (value.length < 3) {
            showMessage(typeMessage, "type: this type does not have enough characters.", false);
            return;
        }
        if (value.length > 10) {
            showMessage(typeMessage, "type: this type has too many characters.", false);
            return;
        }
        if (!/^[A-Za-z-]+$/.test(value)) {
            showMessage(typeMessage, "type: this type has non-alphabetical characters (different from '-').", false);
            return;
        }
        showMessage(typeMessage, "type: this type is valid.", true);
    });

    brandInput.addEventListener("input", () => {
        const value = brandInput.value;
        if (value === "") {
            showMessage(brandMessage, "No brand sent yet!", false);
            return;
        }
        if (value.length < 2) {
            showMessage(brandMessage, "brand: this brand does not have enough characters.", false);
            return;
        }
        if (value.length > 20) {
            showMessage(brandMessage, "brand: this brand has too many characters.", false);
            return;
        }
        if (!/^[A-Za-z0-9&-]+$/.test(value)) {
            showMessage(brandMessage, "brand: this brand has invalid characters.", false);
            return;
        }
        showMessage(brandMessage, "brand: this brand is valid.", true);
    });

    document.getElementById("send").addEventListener("click", () => {
        const type = typeInput.value;
        const brand = brandInput.value;

        fetch("task04.php?type=" + encodeURIComponent(type) + "&brand=" + encodeURIComponent(brand))
            .then(response => response.json())
            .then(data => {
                showMessage(typeMessage, data.type, data.typeValid);
                showMessage(brandMessage, data.brand, data.brandValid);
            })
            .catch(() => {
                showMessage(typeMessage, "An error has occurred.", false);
            });
    });
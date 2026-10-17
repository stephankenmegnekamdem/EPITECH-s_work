const nameInput = document.getElementById("name");
const messageInput = document.getElementById("message");
const chat = document.getElementById("chat");

function loadMessages() {
    fetch("task07.php")
        .then(response => response.json())
        .then(messages => {
            chat.innerHTML = "";
            messages.forEach(msg => {
                const line = document.createElement("p");
                const author = document.createElement("strong");
                author.textContent = msg.name + ": ";
                const text = document.createElement("span");
                text.textContent = msg.message;
                line.appendChild(author);
                line.appendChild(text);
                chat.appendChild(line);
            });
        })
        .catch(() => {
            chat.textContent = "Could not load messages.";
        });
}

document.getElementById("send").addEventListener("click", () => {
    const body = new URLSearchParams({
        name: nameInput.value,
        message: messageInput.value
    });

    fetch("task07.php", { method: "POST", body: body })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                messageInput.value = "";
                loadMessages();
            }
        });
});

loadMessages();
setInterval(loadMessages, 4000);
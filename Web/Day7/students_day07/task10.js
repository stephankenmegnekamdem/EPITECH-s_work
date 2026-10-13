const input = document.querySelector("#listItem");
const addButton = document.querySelector("#addButton");

addButton.addEventListener("click", () => {
  const newDiv = document.createElement("div");
  newDiv.textContent = input.value;
  input.after(newDiv);
  input.value = "";
});
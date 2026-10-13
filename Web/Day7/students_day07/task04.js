const buttons = document.querySelectorAll(".exercice footer div button");
const plusButton = buttons[0];
const minusButton = buttons[1];
const colorSelect = document.querySelector(".exercice footer div select");

plusButton.addEventListener("click", () => {
  const size = parseFloat(getComputedStyle(document.body).fontSize);
  document.body.style.fontSize = (size + 1) + "px";
});

minusButton.addEventListener("click", () => {
  const size = parseFloat(getComputedStyle(document.body).fontSize);
  document.body.style.fontSize = (size - 1) + "px";
});

colorSelect.addEventListener("change", () => {
    if(colorSelect.value){
        document.body.style.backgroundColor = colorSelect.value;
    }


});
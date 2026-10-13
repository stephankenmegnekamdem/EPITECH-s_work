const square = document.querySelector(".exercice footer div canvas");
const info = document.querySelector(".exercice footer div + div");
const zone = square.parentElement;

zone.style.position = "relative";
zone.style.height = "150px";
square.style.position = "absolute";

let x = 100;
let y = 40;
let drag = false;

function show() {
  square.style.left = x + "px";
  square.style.top = y + "px";
  info.textContent = `New coordinates = {x:${x}, y:${150 - y - 20}}`;
}

square.addEventListener("mousedown", () => {
  drag = true;
});

document.addEventListener("mouseup", () => {
  drag = false;
});

document.addEventListener("mousemove", (event) => {
  if (drag) {
    const box = zone.getBoundingClientRect();
    x = event.clientX - box.left - 10;
    y = event.clientY - box.top - 10;
    show();
  }
});

show();
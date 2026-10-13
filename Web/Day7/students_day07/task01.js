// 1. Find the white box: the empty div inside the footer of the exercise
const box = document.querySelector(".exercice footer div");

// 2. The counter. It is declared outside the listener so it keeps its value between clicks
let clicks = 0;

// 3. This function runs every time the box is clicked
box.addEventListener("click", () => {
  clicks = clicks + 1;       // add 1 to the counter (clicks++ does the same)
  box.textContent = clicks;  // replace the box's text with the new number
});
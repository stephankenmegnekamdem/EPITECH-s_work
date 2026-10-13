const paragraphs = document.querySelectorAll("p");

paragraphs.forEach((paragraph) => {
  // Hover: add "blue" when the mouse enters, remove it when the mouse leaves
  paragraph.addEventListener("mouseenter", () => {
    paragraph.classList.add("blue");
  });
  paragraph.addEventListener("mouseleave", () => {
    paragraph.classList.remove("blue");
  });

  // Click: switch "highlighted" on and off
  paragraph.addEventListener("click", () => {
    paragraph.classList.toggle("highlighted");
  });
});
const hideButton = document.querySelector('button')
const paragraphs= document.querySelectorAll("p")
hideButton.addEventListener("click", () =>{
   paragraphs.forEach((paragraph) =>{
       paragraph.style.display = "none";
    });
});
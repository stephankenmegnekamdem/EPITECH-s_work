const box = document.querySelector(".exercice footer div");

box.addEventListener("click", () =>{
    let name="";
    while (!name){
         name = prompt("What's your name?");

    }
    if( confirm(`Are you sure that ${name} is your name?`)){
        const greeting = `Hello ${name}!`;
        alert(greeting);
        box.textContent = greeting;
    }


});
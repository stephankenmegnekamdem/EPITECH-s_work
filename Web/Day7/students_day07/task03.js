const box = document.querySelector(".exercice footer div");
let arr="";

document.addEventListener("keydown", (event)=> {
    if(event.key.length===1){
        arr=arr + event.key
    }

    if (arr.length>42){
        arr=arr.slice(-42)
    }
    box.textContent=arr;
});
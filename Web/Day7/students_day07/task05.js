const canvas = document.querySelector('.exercice footer div canvas');
const buttons= document.querySelectorAll('.exercice footer div button');
const pauseButton = buttons[0];
const stopButton = buttons[1];
const audio = document.querySelector(".exercice footer div audio");
const playButton = document.createElement("button");
playButton.textContent = "Play";
document.querySelector(".exercice footer div audio").after(playButton);
audio.src = "https://www.soundboard.com/track/download/156453";
playButton.addEventListener( "click", () =>{
audio.play()
});
pauseButton.addEventListener( "click", () =>{
audio.pause();
});
stopButton.addEventListener("click", () =>{
audio.pause();
audio.currentTime = 0;
});
const ctx = canvas.getContext("2d");

ctx.beginPath();
ctx.moveTo(6, 6);
ctx.lineTo(14, 10);
ctx.lineTo(6, 14);
ctx.closePath();

ctx.strokeStyle = "white";
ctx.lineWidth = 1;
ctx.stroke();

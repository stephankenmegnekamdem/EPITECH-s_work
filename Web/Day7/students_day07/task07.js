const message = document.querySelector(".exercice footer div");

// Is the cookie there?
function cookieExists() {
  return document.cookie.includes("acceptsCookies=true");
}

// Create the cookie, valid for one day
function createCookie() {
  const date = new Date();
  date.setTime(date.getTime() + 24 * 60 * 60 * 1000);
  document.cookie = "acceptsCookies=true; expires=" + date.toUTCString() + "; path=/";
}

// Delete the cookie by setting an expiry date in the past
function deleteCookie() {
  document.cookie = "acceptsCookies=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/";
}

// Create the second white box with its "Delete the cookie" button
function showDeleteBox() {
  const deleteBox = document.createElement("div");
  const button = document.createElement("button");
  button.textContent = "Delete the cookie";
  deleteBox.appendChild(button);
  message.after(deleteBox);

  button.addEventListener("click", () => {
    deleteCookie();
    deleteBox.remove();
    message.style.display = "";  // show the first message again
  });
}

// On page load: if the cookie exists, hide the message and show the delete box
if (cookieExists()) {
  message.style.display = "none";
  showDeleteBox();
}

// On click: create the cookie, hide the message, show the delete box
message.addEventListener("click", () => {
  createCookie();
  message.style.display = "none";
  showDeleteBox();
});
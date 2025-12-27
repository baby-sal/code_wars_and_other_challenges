const newHeader = document.createElement("h2");

newHeader.textContent = "This is header 2";

document.body.appendChild(newHeader);


const elementToRemove = document.getElementById("remove-this-element");

elementToRemove.remove();


const elementToChange = document.getElementsById("change-text");
const elementToHide = document.getElementsById("hide-text");

elementToChange.textContent = "Changed text";

elementToHide.remove();
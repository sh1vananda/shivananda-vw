let car = document.getElementById("car");
let leftBtn = document.getElementById("left");
let rightBtn = document.getElementById("right");

let position = 0;
const dist = 20;
const maxLeft = 560;
leftBtn.addEventListener("click", function () {
    if (position < maxLeft) {
        position += dist;
        car.style.right = position + "px";
    }
});

rightBtn.addEventListener("click", function () {
    if (position > 0) {
        position -= dist;
        car.style.right = position + "px";
    }
});
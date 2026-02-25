const redCar = document.getElementById("red");
const blueCar = document.getElementById("blue");
const blast = document.getElementById("blast");
const playBtn = document.getElementById("play");

const main = document.querySelector("main");

const message = document.getElementById("message");

const screenWidth = window.innerWidth;

let blueStart = screenWidth -120;
let blueX = blueStart;

let collisionPoint = screenWidth / 2;

blueCar.style.left = blueX + "px";
redCar.style.left = (collisionPoint - 120) + "px";

redCar.style.transform = "scale(0.2)";
blast.style.left = (collisionPoint - 70) + "px";

playBtn.addEventListener("click", () => {
    playBtn.style.display = "none";
    animate();
});

function animate() {
    const interval = setInterval(() => {

        blueX -= 5;
        blueCar.style.left = blueX + "px";

        let totalDistance = blueStart - collisionPoint;
        let coveredDistance = blueStart - blueX;
        let progress = coveredDistance / totalDistance;

        let scale = 0.2 + (0.8 * progress);
        if (scale > 1) scale = 1;

        redCar.style.transform = `scale(${scale})`;

        if (blueX <= collisionPoint) {
            clearInterval(interval);
            redCar.style.transform = "scale(1)";
            blast.style.display = "block";

            setTimeout(() => {
                main.style.transform = "translateY(200px)";
            }, 500);

            setTimeout(() => {
                message.style.display = "block";
            }, 1000);
        }

    }, 20);
}
let cn = document.querySelector("div");
let btn1 = document.querySelector("#cycle")
let btn2 = document.querySelector("#on")
let btn3 = document.querySelector("#off")

let clicks = 0;

btn1.addEventListener("click", function () {
    clicks += 1;
    displayMoon(clicks);
})

btn2.addEventListener("click", function () {
    cn.textContent = "🌕";
    clicks = 0;
})

btn3.addEventListener("click", function () {
    cn.textContent = "🌑";
    clicks = 0;
})

function displayMoon(num) {
    const moons = ["🌑", "🌒", "🌓", "🌔", "🌕", "🌖", "🌗", "🌘"];
    cn.textContent = moons[num % moons.length]
}
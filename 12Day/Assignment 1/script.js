let pr = document.getElementById("message");
let bt = document.querySelector("button");
let hd = document.querySelector("h4")


let clicks = 0
let gif = document.createElement("img")
gif.src = "https://media1.tenor.com/m/gDZEurgsII0AAAAd/black-cat-birthday-hat.gif";
gif.style.width = "250px";

bt.addEventListener("click", function () {
    clicks += 1
    console.log(`clicks: ${clicks}`)
    pr.style.fontSize = (15 + clicks * 20) + "px";
    changeHeadingColor(clicks);
    if (clicks < 4) {
        waitForMessage(clicks);
    }
    if (clicks === 4) {
        pr.innerHTML = `
            <h1 style="color:purple; font-size: 36px; animation: bounce 0.5s infinite;">Happy Birthday!</h1>
        `;
        pr.appendChild(gif)
        bt.style.display = "none";
        hd.style.display = "none";
    }
})

function changeHeadingColor(num) {
    const colors = ["red", "blue", "green"];
    hd.style.color = colors[num - 1 % colors.length]
}

function waitForMessage(num) {
    pr.textContent = "Wait" + ".".repeat(num);
}
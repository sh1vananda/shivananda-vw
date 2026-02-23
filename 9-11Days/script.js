const countEl = document.getElementById("count");
const incBtn = document.getElementById("increment");
const decBtn = document.getElementById("decrement");
const resetBtn = document.getElementById("reset");

window.addEventListener("scroll", function () {
  console.log("Scroll Y:", window.scrollY);
});

function goToTop() {
  window.scrollTo({
    top: 0,
  });
}

function showAlert() {
  window.alert("Window alert!!!");
}

function openSite() {
  window.open("https://www.example.com", "_blank");
}

let count = 0;

function updateDisplay() {
  countEl.textContent = count;
}

incBtn.addEventListener("click", function () {
  count++;
  updateDisplay();
});

decBtn.addEventListener("click", function () {
  count--;
  updateDisplay();
});

resetBtn.addEventListener("click", function () {
  count = 0;
  updateDisplay();
});

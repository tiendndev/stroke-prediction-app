const headerMenu = document.querySelector(".menu");

const html = document.documentElement;

window.onload = () => {
  const storedTheme = localStorage.getItem("theme");
  const gptLayoutBg = document.querySelector(".app.gpt-layout");
  const contentsBg = document.querySelector(".contents");
  const formContainerBg = document.querySelector(".form-container");
  const gptHideButtonBg = document.querySelector('.gpt-hide-button i');
  const textChartMode = document.querySelectorAll('.text-chart-mode text textPath');


  if (storedTheme == "light") {
    html.setAttribute("data-bs-theme", storedTheme);
    localStorage.setItem("theme", "light");
    gptLayoutBg.classList.add("light-mode");
    contentsBg.classList.add("light-mode");
    formContainerBg.classList.add("light-mode");
    gptHideButtonBg.style.color = "#000"
    textChartMode.forEach((t) => {
      t.setAttribute('fill', '#fff');
    });
  } else {
    html.setAttribute("data-bs-theme", "dark");
    localStorage.setItem("theme", "dark");
    gptLayoutBg.classList.remove("light-mode");
    contentsBg.classList.remove("light-mode");
    formContainerBg.classList.remove("light-mode");
    gptHideButtonBg.style.color = "#fff"
    textChartMode.forEach((t) => {
      t.setAttribute('fill', '#fff');
    });
  }
};

const gptShowBtn = document.querySelector(".gpt-show-button");
const gptHideBtn = document.querySelector(".gpt-hide-button");
const gptLayOut = document.querySelector(".gpt-layout");
const appFirstChild = document.querySelector(".app:first-child");
gptShowBtn.addEventListener("click", () => {
  gptLayOut.style.display = "none";
  appFirstChild.style.display = "block";
});

gptHideBtn.addEventListener("click", () => {
  gptLayOut.style.display = "flex";
  gptLayOut.style.width = "100% !important";
  appFirstChild.style.display = "none";
});

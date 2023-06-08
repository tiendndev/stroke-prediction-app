const headerImg = document.querySelector('.header_img')
const headerMenu = document.querySelector('.menu')

headerImg.onclick = () => {
   headerMenu.classList.toggle('menu-active')
}

const darkMode = document.querySelector('.dark-mode')
const lightMode = document.querySelector('.light-mode')
const html = document.documentElement

darkMode.onclick = () => {
   html.setAttribute('data-bs-theme', 'dark')
   localStorage.setItem('theme', 'dark');
}

lightMode.onclick = () => {
   html.setAttribute('data-bs-theme', 'light')
   localStorage.setItem('theme', 'light');
}

window.onload = () => {
   const storedTheme = localStorage.getItem('theme');
   if (storedTheme) {
     html.setAttribute('data-bs-theme', storedTheme);
   }
 };
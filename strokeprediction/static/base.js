const headerMenu = document.querySelector('.menu')

const html = document.documentElement

window.onload = () => {
   const storedTheme = localStorage.getItem('theme');
   if (storedTheme) {
     html.setAttribute('data-bs-theme', storedTheme);
   }
 };
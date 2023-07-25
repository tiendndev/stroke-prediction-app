document.addEventListener("DOMContentLoaded", function (event) {
  const showNavbar = (toggleId, navId, bodyId, headerId) => {
    const toggle = document.getElementById(toggleId),
      nav = document.getElementById(navId),
      bodypd = document.getElementById(bodyId),
      headerpd = document.getElementById(headerId);

    nav.classList.remove("show");

    // Validate that all variables exist
    if (toggle && nav && bodypd && headerpd) {
      toggle.addEventListener("click", () => {
        // show navbar
        nav.classList.toggle("show");
        // change icon
        toggle.classList.toggle("bx-menu");
        toggle.classList.toggle("bx-x");
        // add padding to body
        bodypd.classList.toggle("body-pd");
        // add padding to header
        headerpd.classList.toggle("body-pd");
      });
    }
  };


  showNavbar("header-toggle", "nav-bar", "body-pd", "header");

  /*===== LINK ACTIVE =====*/
  const linkColor = document.querySelectorAll(".nav_link");
  let local_route = window.location.href.slice(21);
  let ngrok_route = window.location.href.slice(39);
  let render_route = window.location.href.slice(40);

  linkColor.forEach((l) => {
    switch (local_route) {
      case "/form":
        l.classList.remove("active");
        linkColor[0].classList.add("active");
        break;
      case "/image":
        l.classList.remove("active");
        linkColor[1].classList.add("active");
        break;
        case "/bmi":
          l.classList.remove("active");
          linkColor[2].classList.add("active");
          break;
        case "/calendar":
          l.classList.remove("active");
          linkColor[3].classList.add("active");
          break;
      default:
        l.classList.remove("active");
        linkColor[0].classList.add("active");
        break;
    }
  });
});

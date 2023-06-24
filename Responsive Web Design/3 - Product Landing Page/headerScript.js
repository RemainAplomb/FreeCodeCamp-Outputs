document.addEventListener("DOMContentLoaded", () => {
    const hamburgerMenu = document.getElementById("hamburg-button");
    const navMenu = document.getElementById("header");
    const navContent = document.getElementById("nav-bar");
  
    hamburgerMenu.addEventListener("click", () => {
      hamburgerMenu.classList.toggle("active");
      navMenu.classList.toggle("active");
    //   navContent.classList.toggle("active");
    });
  });
  

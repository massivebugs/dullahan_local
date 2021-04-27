;(function () {
  const navbarBurger = document.querySelector(".navbar-burger")
  const toggleTarget = document.getElementById(navbarBurger.dataset.target)

  if (navbarBurger && toggleTarget) {
    navbarBurger.addEventListener("click", () => {
      toggleTarget.classList.toggle("is-active")
    })
  }
})()

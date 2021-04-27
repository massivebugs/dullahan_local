window.addEventListener("load", () => {
  const settingsBtn = document.querySelector(".settings-button")
  const btnGroup = document.querySelector(".button-group")
  const deleteBtn = document.querySelector(".delete-device-button")
  const deviceBtn = document.querySelectorAll(".device-button")

  settingsBtn.addEventListener("click", (e) => {
    e.target.textContent = e.target.classList.contains("toggled")
      ? "Settings"
      : "X"
    e.target.classList.toggle("toggled")
    btnGroup.classList.toggle("hidden")
  })

  deleteBtn.addEventListener("click", () => {
    deviceBtn.forEach((b) => {
      document.body.classList.toggle("delete-device")
      b.setAttribute("href", b.getAttribute('href').replace('control', 'delete'))
      console.log("set!")
    })
  })
})

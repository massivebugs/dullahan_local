// TODO: prettify!!

window.addEventListener("load", () => {
  // The current device ID is collected from DOM (TODO: Implement something better)
  const deviceID = document.getElementById("device-id").textContent

  const socket = new WebSocket(
    "ws://" + window.location.host + window.location.pathname
  )

  socket.onmessage = e => {
    // Parses the json data and updates the command history DOM
    const commandHistory = document.querySelector(".command-history")
    const data = JSON.parse(JSON.parse(e.data).message)
    let output = ""
	  console.log(data)
    for (key in data) {
      let valueList = data[key].split("\n")
      valueList.pop()
      valueList.forEach((value) => {
        output += key + ": " + value + "\n"
      })
    }
    commandHistory.textContent = output
    outputBox = document.querySelector(".output")
    outputBox.scrollTop = outputBox.scrollHeight
  }

  socket.onclose = e => {
    console.error("Chat socket closed unexpectedly")
  }
  
  // Listens for command submit, and sends it via socket
  commandForm = document.querySelector(".command-form")
  commandForm.addEventListener('submit', e => {
    e.preventDefault()
    const message = commandForm.command.value
    if (message.length > 0) {
	    socket.send(
	      JSON.stringify({
		message: message,
		device: deviceID,
	      })
	    )
    commandForm.reset()
    }
  })
})

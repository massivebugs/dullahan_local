window.addEventListener('load', () => {
	document.querySelector('.change-device-form')
	.addEventListener('submit', e => {
		e.preventDefault()
		window.location.assign(window.location.pathname.slice(0, -1).concat(e.target.device.value))
	})
})

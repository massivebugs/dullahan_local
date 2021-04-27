window.addEventListener('load', () => {
	const deviceListDOM = document.querySelector('.device-list')
	const scanningDOM = document.querySelector('.device-list-scanning')
	fetch(window.location.origin + '/devices/search/')
	.then(res => res.json())
	.then(data => JSON.parse(data.nearby_devices))
	.then(parsed_data => { 
		deviceListDOM.removeChild(scanningDOM)
		if (Object.keys(parsed_data).length > 0){
			for (let device in parsed_data){
				const device_btn = document.createElement('button')
				device_btn.classList.add('device-button', 'button')
				device_btn.textContent = `${device} : ${parsed_data[device]}`
				device_btn.setAttribute('data-hostname', device)
				device_btn.setAttribute('data-uuid', parsed_data[device])
				deviceListDOM.appendChild(device_btn)
			}
		deviceListDOM.addEventListener('click', e => {
			if (e.target.tagName == "BUTTON"){
				const form = document.querySelector('form')
				let hostname = e.target.dataset['hostname']
				let uuid = e.target.dataset['uuid']
				form['hostname'].value = hostname
				form['uuid'].value = uuid
				console.log(form)
			}
		})
		}
		else {
			alert('No devices were found')
		}
	})
})

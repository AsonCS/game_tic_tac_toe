
const KEY_MOVE_PARAM = 'move'
const KEY_REFRESH_PARAM = 'refresh'

function refreshScreen() {
	document.location.search = KEY_REFRESH_PARAM + '=1'
}

function onClickButton(button) {
	const search = document.location.search.slice(1)
	const value = button.textContent
	let params = ''
	let findParam = false
	search.split('&').forEach(param => {
		if (param.trim().length > 0) {
			let idx = param.indexOf(KEY_MOVE_PARAM)
			if (idx > -1) {
				params += KEY_MOVE_PARAM + '=' + value
				findParam = true
			} else {
				idx = param.indexOf(KEY_REFRESH_PARAM)
				if (idx == -1) {
					params += param
				}
			}
			params += '&'
		}
	})
	if (!findParam) {
		params += KEY_MOVE_PARAM + '=' + value + '&'
	}
	// alert(params.slice(0,-1))
	document.location.search = params.slice(0,-1)
}

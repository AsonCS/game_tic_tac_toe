
const KEY_MOVE_PARAM = 'move'
const KEY_REFRESH_PARAM = 'refresh'

const PLAYER_ONE = 'X'
const PLAYER_TWO = 'O'

board = []
has_game_ended = false
player = "O"

function loadScene() {
	const hidden_player_win_msg = document.getElementById('hidden_player_win_msg')
	const hidden_time_player_win_msg = document.getElementById('hidden_time_player_win_msg')
	hidden_player_win_msg.getElementsByTagName('label')[0].textContent = player
	hidden_time_player_win_msg.getElementsByTagName('label')[0].textContent = player
	if (has_game_ended) {
		hidden_player_win_msg.removeAttribute('hidden')
		hidden_time_player_win_msg.setAttribute('hidden', true)
	} else {
		hidden_time_player_win_msg.removeAttribute('hidden')
		hidden_player_win_msg.setAttribute('hidden', true)
	}
	
	for (i = 0; i < 9; i++) {
		let button = document.getElementById('button_' + (i + 1))
		button.textContent = board[i]
		const isAvailable = board[i] !== PLAYER_ONE && board[i] !== PLAYER_TWO
		if (!has_game_ended && isAvailable) {
			button.removeAttribute('disabled')
		} else {
			button.setAttribute('disabled', true)
		}
		button.onclick = () => {
			onClickButton(button)
		}
	}
}

function refreshScreen() {
	document.location.search = KEY_REFRESH_PARAM + '=1'
}

function onClickButton(button) {
	doFetch(button.textContent)
}

function doFetch(move) {
	fetch(`/api/game?${KEY_MOVE_PARAM}=${move}`)
		.then(it => it.json()).then(value => {
			board = value.board
			has_game_ended = value.has_game_ended
			player = value.player
			loadScene()
		})
		.catch(error => {
			console.error(error)
		})
}

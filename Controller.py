from game import TicTacToe
from HtmlGenerate import HtmlGenerate


class Controller:

	PATH_TO_STATIC = 'static/'
	PATH_TO_API_GAME = 'api/game'
	PATH_DEFAULT = ''

	__WORD_TO_STOP = 'stop'
	__KEY_ROOM_PARAM = 'room'
	__KEY_MOVE_PARAM = 'move'
	__KEY_REFRESH_PARAM = 'refresh'
	__DEAFULT_HTML_ERROR_RESPONSE = (500, '<h1>Internal Error</h1>')
	__DEAFULT_JSON_ERROR_RESPONSE = (500, '{ }')
	__DEFAULT_SUCCESS_CODE = 200

	def __init__(self, path: 'str') -> None:
		path = path.lower()
		if (Controller.__WORD_TO_STOP in path):
			raise KeyboardInterrupt()
		
		query = ''
		path = path.split('?')[:2]
		if (len(path) == 2):
			query = path[1]
		self.path: 'str' = path[0]
		if (Controller.PATH_TO_STATIC in self.path):
			self.type = Controller.PATH_TO_STATIC
			return
		elif (Controller.PATH_TO_API_GAME in self.path):
			self.type = Controller.PATH_TO_API_GAME
		else:
			self.type = Controller.PATH_DEFAULT
		
		self.__params: 'dict[str,str]' = {}
		for param in query.split('&'):
			# print('param', param)
			key_value = param.split('=')[:2]
			# print('key_value', key_value)
			key_value = key_value[:2]
			if (len(key_value) == 2):
				self.__params[key_value[0]] = key_value[1]


	def load_game_html(self) -> 'tuple[int,str]':
		"""code, html = Controller().load_game()"""
		try:
			player, has_game_ended, board = self.__do_move()
			
			html = HtmlGenerate().get_scene(player, has_game_ended, board)
			return (Controller.__DEFAULT_SUCCESS_CODE, html)
		except Exception as e:
			e.with_traceback()
			return Controller.__DEAFULT_HTML_ERROR_RESPONSE


	def load_game_json(self) -> 'tuple[int,str]':
		"""code, html = Controller().load_game()"""
		try:
			player, has_game_ended, board = self.__do_move()
			
			json = '{'
			json += f'"player": "{player}",'
			json += '"has_game_ended": ' + ('true,' if has_game_ended else 'false,')
			json += f'"board": {board}'
			json += '}'
			json = json.replace("'", '"')

			return (Controller.__DEFAULT_SUCCESS_CODE, json)
		except Exception as e:
			print('load_game_json', e)
			return Controller.__DEAFULT_JSON_ERROR_RESPONSE
	

	def __do_move(self) -> 'tuple[str, bool, list[str]]':
		"""player, has_game_ended, board = Controller().do_move()"""
		room = self.__params.get(Controller.__KEY_ROOM_PARAM)
		move = self.__params.get(Controller.__KEY_MOVE_PARAM)
		refresh = self.__params.get(Controller.__KEY_REFRESH_PARAM)
		game = TicTacToe(room)

		if not refresh:
			return game.do_move(move)
		else:
			return game.refresh_game()

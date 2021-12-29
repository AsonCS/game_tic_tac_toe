from game import TicTacToe

class HtmlGenerate:

	def get_scene(self, player: 'str', has_game_ended: 'bool', board: 'list[str]'):
		with open('src/index.html') as f:
			html = f.read()

			params: 'dict[str,str]' = {}
			params['throw Error()'] = ''
			params['$player'] = f'"{player}"'
			board = str(board).replace("'", '"')
			params['$board'] = board
			params['$has_game_ended'] = 'true' if has_game_ended else 'false'

			html = self.__replace_html_variables(html, params)
			f.close()
			return html
	

	def __replace_html_variables(self, html: 'str', params: 'dict[str,str]'):
		for key, value in params.items():
			# print(key, value)
			html = html.replace(key, value)
		return html

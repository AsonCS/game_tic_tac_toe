from game import TicTacToe


class HtmlGenerate:

    @staticmethod
    def __replace_html_variables(html: 'str', params: 'dict[str,str]'):
        for key, value in params.items():
            html = html.replace(key, value)
        return html

    def __init__(self, directory: 'str'):
        self.__directory = directory

    def get_scene(self, player: 'str', has_game_ended: 'bool', board: 'list[str]'):
        with open(f'{self.__directory}/src/index.html') as f:
            html = f.read()

            params: 'dict[str,str]' = {
                '$player_win_msg': player,
                '$hidden_player_win_msg': '' if has_game_ended else 'hidden',
                '$hidden_time_player_win_msg': 'hidden' if has_game_ended else ''
            }
            index = 1
            for field in board:
                value_disabled = '' if TicTacToe.is_available(field) else 'disabled'
                key_button_value = f'$b{index}'
                button_disabled = f'$button_disabled_{index}'
                params[key_button_value] = field
                params[button_disabled] = value_disabled
                index += 1

            html = self.__replace_html_variables(html, params)
            f.close()
            return html

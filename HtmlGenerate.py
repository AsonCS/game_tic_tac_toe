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
                'throw Error()': '', '$player': f'"{player}"'
            }
            board = str(board).replace("'", '"')
            params['$board'] = board
            params['$has_game_ended'] = 'true' if has_game_ended else 'false'

            html = self.__replace_html_variables(html, params)
            f.close()
            return html

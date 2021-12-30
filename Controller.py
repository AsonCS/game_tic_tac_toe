from HtmlGenerate import HtmlGenerate
from game import TicTacToe


class Controller:
    PATH_TO_STATIC = 'static/'
    PATH_TO_GAME = 'game'

    __WORD_TO_STOP = 'stop'
    __KEY_ROOM_PARAM = 'room'
    __KEY_MOVE_PARAM = 'move'
    __KEY_REFRESH_PARAM = 'refresh'
    __DEFAULT_ERROR_RESPONSE = (500, '<h1>Internal Error</h1>')
    __DEFAULT_SUCCESS_CODE = 200

    def __init__(self, path: 'str', directory: 'str') -> None:
        self.__directory = directory

        path = path.lower()
        if Controller.__WORD_TO_STOP in path:
            raise KeyboardInterrupt()

        query = ''
        path = path.split('?')[:2]
        if len(path) == 2:
            query = path[1]
        self.path: 'str' = path[0]
        if Controller.PATH_TO_STATIC in self.path:
            self.type = Controller.PATH_TO_STATIC
            return
        else:
            self.type = Controller.PATH_TO_GAME

        self.__params: 'dict[str,str]' = {}
        for param in query.split('&'):
            # print('param', param)
            key_value = param.split('=')[:2]
            # print('key_value', key_value)
            key_value = key_value[:2]
            if len(key_value) == 2:
                self.__params[key_value[0]] = key_value[1]

    def load_game(self) -> 'tuple[int,str]':
        """code, html = Controller().load_game()"""
        try:
            room = self.__params.get(Controller.__KEY_ROOM_PARAM)
            move = self.__params.get(Controller.__KEY_MOVE_PARAM)
            refresh = self.__params.get(Controller.__KEY_REFRESH_PARAM)
            game = TicTacToe(room)

            if not refresh:
                player, has_game_ended, board = game.do_move(move)
            else:
                player, has_game_ended, board = game.refresh_game()

            html = HtmlGenerate(self.__directory).get_scene(player, has_game_ended, board)
            return Controller.__DEFAULT_SUCCESS_CODE, html
        except Exception as e:
            print('load_game', e)
            return Controller.__DEFAULT_ERROR_RESPONSE

_PLAYER_ONE = 'X'
_PLAYER_TWO = 'O'

_KEY_BOARD = 'KEY_BOARD'
_KEY_PLAYER = 'KEY_PLAYER'

_SESSION = {
    '1': {
        _KEY_PLAYER: _PLAYER_ONE
    },
    '2': {
        _KEY_PLAYER: _PLAYER_ONE
    },
    '3': {
        _KEY_PLAYER: _PLAYER_ONE
    }
}


class TicTacToe:

    def __init__(self, room: 'str') -> None:
        self.__room = '1'
        if room in _SESSION.keys():
            self.__room = room
        self.__board: 'str' = self.__get_from_session(_KEY_BOARD)
        if not self.__board:
            self.__board = self.__new_board

    @staticmethod
    def is_available(field: 'str') -> 'bool':
        return not (field == _PLAYER_ONE or field == _PLAYER_TWO)

    def do_move(self, move: 'str') -> 'tuple[str,bool,list[str]]':
        """player, has_game_ended, board = TicTacToe().do_move('1')"""
        player = self.__get_from_session(_KEY_PLAYER)

        try:
            move = int(move) - 1
            if not (-1 < move < 9):
                raise ValueError()
            if self.is_available(self.__board[move]):
                self.__board[move] = player
                player = self.__invert_player()
                self.__set_on_session(_KEY_BOARD, self.__board)
        except TypeError as e:
            pass
        except Exception as e:
            print('do_move', type(e))

        has_game_ended = self.__validate_game_end()

        if has_game_ended:
            player = self.__invert_player()
            self.refresh_game()

        return player, has_game_ended, self.__board

    def refresh_game(self) -> 'tuple[str,bool,list[str]]':
        board = self.__new_board
        self.__set_on_session(_KEY_BOARD, board)
        self.__set_on_session(_KEY_PLAYER, _PLAYER_ONE)
        return _PLAYER_ONE, False, board

    def __set_on_session(self, key: 'str', value):
        _SESSION[self.__room][key] = value

    def __get_from_session(self, key: 'str') -> 'str':
        return _SESSION[self.__room].get(key)

    def __invert_player(self):
        if self.__get_from_session(_KEY_PLAYER) == _PLAYER_ONE:
            self.__set_on_session(_KEY_PLAYER, _PLAYER_TWO)
            return _PLAYER_TWO
        else:
            self.__set_on_session(_KEY_PLAYER, _PLAYER_ONE)
            return _PLAYER_ONE

    def __validate_game_end(self) -> 'bool':
        first_line = self.__board[0] == self.__board[1] == self.__board[2]
        second_line = self.__board[3] == self.__board[4] == self.__board[5]
        third_line = self.__board[6] == self.__board[7] == self.__board[8]
        line = first_line or second_line or third_line

        first_column = self.__board[0] == self.__board[3] == self.__board[6]
        second_column = self.__board[1] == self.__board[4] == self.__board[7]
        third_column = self.__board[2] == self.__board[5] == self.__board[8]
        column = first_column or second_column or third_column

        first_diagonal = self.__board[0] == self.__board[4] == self.__board[8]
        second_diagonal = self.__board[6] == self.__board[4] == self.__board[2]
        diagonal = first_diagonal or second_diagonal

        return line or column or diagonal

    @property
    def __new_board(self):
        return [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9'
        ]

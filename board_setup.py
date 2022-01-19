class Board:

    def __init__(self):
        self.aa = {"x": "x", "o": "0", "hor": '===', "ver": "|"}
        self.board = self.refresh_board()
        self.remaining_choices = self.remaining_choices()
        self.o_place = []
        self.x_place = []
        self.winner = ""
        self.game_is_on = True
        self.player = {'O': self.o_place, "X": self.x_place}
        self.placement = {"T": 0, "M": 2, "R": 4, "L": 0, "B": 4,}

        self.winning_sets = [["BL", "BM", "BR"], ["ML", "MR", "MM"], ["TL", "TM", "TR"],
                             ["TL", "ML", "BL"], ["TM", "MM", "BM"], ["TR", "MR", "BR"],
                             ["TL", "MM", "BR"], ["TR", "MM", "BL"]]

        self.computer_picks = ["BL", "BM", "BR", "ML", "MM", "MR", "TL", "TM", "TR"]

    def refresh_board(self):
        return [["   ", self.aa["ver"], "   ", self.aa["ver"], "   ", "\n"],
                [self.aa["hor"], self.aa["ver"], self.aa["hor"], self.aa["ver"], self.aa["hor"], "\n"],
                ["   ", self.aa["ver"], "   ", self.aa["ver"], "   ", "\n"],
                [self.aa["hor"], self.aa["ver"], self.aa["hor"], self.aa["ver"], self.aa["hor"], "\n"],
                ["   ", self.aa["ver"], "   ", self.aa["ver"], "   ", "\n"]]

    def remaining_choices(self):
        return "TL TM TR \n " \
               "ML MM MR \n " \
               "BL BM BR \n "

    def print_board(self):
        top = f" {''.join(self.board[0])}"
        line1 = ''.join(self.board[1])
        mid = ''.join(self.board[2])
        line2 = ''.join(self.board[3])
        bot = ''.join(self.board[4])
        print(top, line1, mid, line2, bot)

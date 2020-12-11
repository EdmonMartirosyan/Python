#1
class User:
    def __init__(self, name):
        self.name = name
    def send_message(self, user, message):
        return f"{message} sent to {user.name}"
    def post(self, message):
        return f"The {message} has been posted"
    def info(self):
        return ""
    def describe(self):
        return self.name


class Person(User):
    def __init__(self, name, birthday):
        super().__init__(name)
        self.birthday = birthday
    def info(self):
        return f"{self.name} was born on {self.birthday}"
    def subscribe(self, user):
        return f"You have subscribed to {user.name}"


class Community(User):
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description
    def info(self):
        return self.description



#2
class TicTacToe:
    def __init__(self):
        self.new_game()
    def new_game(self):
        self.matrix = []
        for i in range(3):
            self.matrix.append([])
            for j in range(3):
                self.matrix[i].append("-")
    def get_field(self):
        print(self.matrix)
    def check_field(self):
        x1_cord = 0
        x2_cord = 0
        o1_cord = 0
        o2_cord = 0
        x_y_cord = []
        o_y_cord = []
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] == "x":
                    x_y_cord.append(j)
                    if self.matrix[i].count("x") == 3 or x_y_cord.count(j) == 3:
                        return "x"
                    if i == j:
                        x1_cord += 1
                    if i + j == 2:
                        x2_cord += 1
                    if x1_cord == 3 or x2_cord == 3:
                        return "x"
                elif self.matrix[i][j] == "o":
                    o_y_cord.append(j)
                    if self.matrix[i].count("o") == 3 or o_y_cord.count(j) == 3:
                        return "o"
                    if i == j:
                        o1_cord += 1
                    if i + j == 2:
                        o2_cord += 1
                    if o1_cord == 3 or o2_cord == 3:
                        return "o"
        if "-" not in self.matrix[0] and "-" not in self.matrix[1] and "-" not in self.matrix[2]:
            return "D"
        return "Continue playing"
    moves_count = 0
    def make_move(self, row, col):
        global moves_count
        if self.matrix[row-1][col-1] == "-":
            if TicTacToe.moves_count % 2 == 0:
                self.matrix[row-1][col-1] = "x"
                TicTacToe.moves_count += 1
            else:
                self.matrix[row-1][col-1] = "o"
                TicTacToe.moves_count += 1
            if self.check_field() == "x":
                print("X-player won!\nGame over")
            elif self.check_field() == "o":
                print("O-player won!\nGame over")
            elif self.check_field() == "D":
                print("Draw\nGame over")
            elif self.check_field() is None:
                print("Continue playing")
        else:
            print(f"Cell {row}, {col} is already filled")


d = TicTacToe()
d.make_move(1, 1)
d.make_move(1, 2)
d.make_move(2, 2)
d.make_move(3, 3)
d.make_move(2, 1)
d.make_move(2, 3)
d.make_move(3, 1)
d.get_field()




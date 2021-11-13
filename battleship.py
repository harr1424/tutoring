import random

class Board():
    def __init__(self):
        self.matrix = self.get_matrix(10, 10)

    def get_matrix(self, n, m):
        matrix = [[None for j in range(m)] for i in range(n)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = "_"
        return matrix

    def to_string(self, matrix):
        strings = []
        for row in matrix:
            strings.append(str(row))
        return '\n'.join(strings)

    def __str__(self):
        return self.to_string(self.matrix)

    def set_element(self, i, j, element):
        self.matrix[i - 1][j - 1] = element

    def set_carrier_vertically(self, i, j):
        row = i
        col = j
        for element in range(5):
            self.set_element(row, col, "C")
            row += 1

    def set_carrier_horizontally(self, i, j):
        row = i
        col = j
        for element in range(5):
            self.set_element(row, col, "C")
            col += 1

    def set_battleship_vertically(self, i, j):
        row = i
        col = j
        for element in range(4):
            self.set_element(row, col, "B")
            row += 1

    def set_battleship_horizontally(self, i, j):
        row = i
        col = j
        for element in range(4):
            self.set_element(row, col, "B")
            col += 1

    def set_cruiser_vertically(self, i, j):
        row = i
        col = j
        for element in range(3):
            self.set_element(row, col, "c")
            row += 1

    def set_cruiser_horizontally(self, i, j):
        row = i
        col = j
        for element in range(3):
            self.set_element(row, col, "c")
            col += 1

    def set_submarine_vertically(self, i, j):
        row = i
        col = j
        for element in range(3):
            self.set_element(row, col, "S")
            row += 1

    def set_submarine_horizontally(self, i, j):
        row = i
        col = j
        for element in range(3):
            self.set_element(row, col, "S")
            col += 1

    def set_destroyer_vertically(self, i, j):
        row = i
        col = j
        for element in range(2):
            self.set_element(row, col, "D")
            row += 1

    def set_destroyer_horizontally(self, i, j):
        row = i
        col = j
        for element in range(2):
            self.set_element(row, col, "D")
            col += 1

    def reset(self):
        self.matrix = self.get_matrix(10, 10)

    def player_turn(self, choice_string):
        player_choice = choice_string.split()
        if player_choice[0] == "CARRIER":
            if player_choice[-1] == "VERTICAL":
                self.set_carrier_vertically(int(player_choice[1]), int(player_choice[2]))
            elif player_choice[-1] == "HORIZONTAL":
                self.set_carrier_horizontally(int(player_choice[1]), int(player_choice[2]))
            else:
                print("You did not enter horizontal or vertical")
        elif player_choice[0] == "BATTLESHIP":
            if player_choice[-1] == "VERTICAL":
                self.set_battleship_vertically(int(player_choice[1]), int(player_choice[2]))
            elif player_choice[-1] == "HORIZONTAL":
                self.set_battleship_horizontally(int(player_choice[1]), int(player_choice[2]))
            else:
                print("You did not enter horizontal or vertical")
        elif player_choice[0] == "CRUISER":
            if player_choice[-1] == "VERTICAL":
                self.set_cruiser_vertically(int(player_choice[1]), int(player_choice[2]))
            elif player_choice[-1] == "HORIZONTAL":
                self.set_cruiser_horizontally(int(player_choice[1]), int(player_choice[2]))
            else:
                print("You did not enter horizontal or vertical")
        elif player_choice[0] == "SUBMARINE":
            if player_choice[-1] == "VERTICAL":
                self.set_submarine_vertically(int(player_choice[1]), int(player_choice[2]))
            elif player_choice[-1] == "HORIZONTAL":
                self.set_submarine_horizontally(int(player_choice[1]), int(player_choice[2]))
            else:
                print("You did not enter horizontal or vertical")
        elif player_choice[0] == "DESTROYER":
            if player_choice[-1] == "VERTICAL":
                self.set_destroyer_vertically(int(player_choice[1]), int(player_choice[2]))
            elif player_choice[-1] == "HORIZONTAL":
                self.set_destroyer_horizontally(int(player_choice[1]), int(player_choice[2]))
            else:
                print("You did not enter horizontal or vertical")
        else:
            print("The ship name you entered does not exist")

    def comp_turn(self):
        ships = ["CARRIER", "BATTLESHIP", "CRUISER", "SUBMARINE", "DESTROYER"]
        orientation = ["VERTICAL", "HORIZONTAL"]
        ship_selection = ships[random.randint(0,4)]
        row = random.randint(0,9)
        col = random.randint(0,9)
        ship_orientation = orientation[random.randint(0,1)]

        comp_choice = [ship_selection, row, col, ship_orientation]

        if comp_choice[0] == "CARRIER":
            if comp_choice[-1] == "VERTICAL":
                self.set_carrier_vertically(int(comp_choice[1]), int(comp_choice[2]))
            elif comp_choice[-1] == "HORIZONTAL":
                self.set_carrier_horizontally(int(comp_choice[1]), int(comp_choice[2]))
            else:
                print("You did not enter horizontal or vertical")
        elif comp_choice[0] == "BATTLESHIP":
            if comp_choice[-1] == "VERTICAL":
                self.set_battleship_vertically(int(comp_choice[1]), int(comp_choice[2]))
            elif comp_choice[-1] == "HORIZONTAL":
                self.set_battleship_horizontally(int(comp_choice[1]), int(comp_choice[2]))
            else:
                print("You did not enter horizontal or vertical")
        elif comp_choice[0] == "CRUISER":
            if comp_choice[-1] == "VERTICAL":
                self.set_cruiser_vertically(int(comp_choice[1]), int(comp_choice[2]))
            elif comp_choice[-1] == "HORIZONTAL":
                self.set_cruiser_horizontally(int(comp_choice[1]), int(comp_choice[2]))
            else:
                print("You did not enter horizontal or vertical")
        elif comp_choice[0] == "SUBMARINE":
            if comp_choice[-1] == "VERTICAL":
                self.set_submarine_vertically(int(comp_choice[1]), int(comp_choice[2]))
            elif comp_choice[-1] == "HORIZONTAL":
                self.set_submarine_horizontally(int(comp_choice[1]), int(comp_choice[2]))
            else:
                print("You did not enter horizontal or vertical")
        elif comp_choice[0] == "DESTROYER":
            if comp_choice[-1] == "VERTICAL":
                self.set_destroyer_vertically(int(comp_choice[1]), int(comp_choice[2]))
            elif comp_choice[-1] == "HORIZONTAL":
                self.set_destroyer_horizontally(int(comp_choice[1]), int(comp_choice[2]))
            else:
                print("You did not enter horizontal or vertical")
        else:
            print("The ship name you entered does not exist")


print("Initializing....")
player_board = Board()
comp_board = Board()
print("Initializing complete")
print("Welcome to Battleship! Enter Q to quit at any time.")
print("You have an empty 10 x 10 grid upon which to place your ships")
print("Carrier (C) = 5 spaces")
print("Battleship (B) = 4 spaces")
print("Cruiser (c) = 3 spaces")
print("Submarine (S) = 3 spaces")
print("Destroyer (D) = 2 spaces")
print("To play, enter the name of a ship followed by a row, column, and either horizontal or vertical")
print("The row and column you enter will be the starting position for the ship, which will then extend to the right or downwards")
print("For example: Cruiser 3 5 vertical")
player_board.set_carrier_vertically(3, 5)
print(player_board)
player_board.reset()
print("And: Cruiser 3 5 horizontal")
player_board.set_carrier_horizontally(3, 5)
print(player_board)
player_board.reset()
print("Player Board loos like:")
print(player_board)
user_choice = str(input("Enter your first ship placement, or q to quit:")).upper()
while user_choice != "Q":
    Board.player_turn(player_board, user_choice)
    print("Player Board loos like:")
    print(player_board)
    Board.comp_turn(comp_board)

    # for testing only
    # print("Computer board looks like:")
    # print(comp_board)

    user_choice = str(input("Enter your next ship placement, or q to quit:")).upper()


# TODO corner cases: overlaid ships, index out of bounds, missing arguments, computer placement not perfect
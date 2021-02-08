class Lamp:
    def __init__(self, color):
        self.color = color


class LampFactory:
    lamps = {}

    @staticmethod
    def get_lamp(color):
        return LampFactory.lamps.setdefault(color, Lamp(color))


class TreeBranch:
    def __init__(self, branch_number):
        self.branch_number = branch_number

    def hang(self, lamp):
        print(f"Hang {lamp.color} [{id(lamp)}] lamp on "
              f"branch {self.branch_number} [{id(self)}]")


class ChristmasTree:
    def __init__(self):
        self.lamps_hung = 0
        self.branches = {}

    def get_branch(self, number):
        return self.branches.setdefault(number, TreeBranch(number))

    def dress_up_the_tree(self):
        for i in range(3):
            self.hang_lamp('red', i)
            self.hang_lamp('blue', i)
            self.hang_lamp('yellow', i)

    def hang_lamp(self, color, branch_number):
        self.get_branch(branch_number).hang(LampFactory.get_lamp(color))
        self.lamps_hung += 1


if __name__ == '__main__':
    ChristmasTree().dress_up_the_tree()

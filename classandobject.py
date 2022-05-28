class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)

    def change_name(self, newname):
        self.name = str(newname)
        print("the student new name is ", newname)

    def change_age(self, newage):
        self.age = int(newage)
        print("the student new age is ", newage)

    def add_track(self, newtrack):
        self.tracks = str(newtrack)
        print("the student new track is ", newtrack)

    def get_score(self):
        self.get_score = self.score
        print("the student score is ", self.score)
        return (self.score)


Bob = Student("Bob", 26, ["FE", "BE"], 20.90)


# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("BE")
Bob.get_score()

#https://www.reddit.com/r/dailyprogrammer/comments/2rfae0/20150105_challenge_196_practical_exercise_ready/

class Set:
    def __init__(self, ints):
        ints = sorted(ints)
        self.contents = []
        self.contents = [num for num in ints if num not in self.contents]

    def __str__(self):
        return self.contents

    def contains(self, int):
        return int in self.contents

    def union(self, set2):
        return list(set(self.contents + set2.contents))

    def intersection(self, set2):
        return list(set([num for num in self.contents if set2.contains(num)]))

    def isEqual(self, set2):
        return self.contents == set2.contents

first_set = Set([483, 843, 239, 520])
second_set = Set([483, 829, 224, 520])

print(first_set.__str__())
print(first_set.contains(483))
print(first_set.union(second_set))
print(first_set.intersection(second_set))
print(first_set.isEqual(second_set))
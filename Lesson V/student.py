"""Task 2"""


from random import randint


class Student:
    """Students"""
    def __init__(self, name, course_info):
        self.name = name
        self.info = course_info
        self.results = {}
        self.last_done = max(self.results.keys()) if self.results else None

    def make_lab(self, points, number=-1):
        """Add labs results"""
        if number <= self.info['lab_num'] - 1:
            if number <= -1:
                number = min([i for i in range(0, self.info['lab_num']) if i not in self.results])
            if points > self.info['lab_max']:
                points = self.info['lab_max']
            if number not in self.results:
                self.results[number] = [points, 1]
            elif self.results[number][1] < 5:
                self.results[number][0] = points
                self.results[number][1] += 1
        return self

    def make_exam(self, points):
        """Add exam result"""
        if points > self.info['exam_max']:
            points = self.info['exam_max']
        self.results['exam'] = [points, 1]
        return self

    def is_certified(self):
        """Certification"""
        max_possible = self.info['exam_max'] + self.info['lab_max'] * self.info['lab_num']
        enough = self.info['k'] * max_possible
        scores = [result[0] for result in self.results.values()]
        got = sum(scores)
        if got >= enough:
            return got, True
        return got, False


LERA = Student('Valeria', {"exam_max": 30, "lab_max": 7, "lab_num": 10, "k": 0.61})
for i in range(LERA.info['lab_num'] + 3):
    LERA.make_lab(randint(0, LERA.info['lab_max'] + 3), i)
LERA.make_exam(randint(0, LERA.info["exam_max"]))
print(LERA.is_certified())

# check whether the limit of attempts (5) works
TIMUR = Student('Timur', {"exam_max": 20, "lab_max": 10, "lab_num": 4, "k": 0.6})
for i in range(7):
    TIMUR.make_lab(randint(0, 11), 1)
    print(TIMUR.results)

# check whether make_lab works correctly if n is not given or larger than possible
TIMUR.make_lab(8, 3)
print(TIMUR.results)
TIMUR.make_lab(5, 9)
print(TIMUR.results)
TIMUR.make_lab(9)
print(TIMUR.results)
TIMUR.make_lab(10)
print(TIMUR.results)

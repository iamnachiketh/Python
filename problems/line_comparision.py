import math

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


    def calculate_length(self):
        length = math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
        return round(length, 2)


    def compare_lines(self, other_line):
        length1 = self.calculate_length()
        length2 = other_line.calculate_length()

        print(f"Length of Line 1: {length1}")
        print(f"Length of Line 2: {length2}")

        if length1 == length2:
            print("Both lines are equal.")
        elif length1 > length2:
            print("Line 1 is longer than Line 2.")
        else:
            print("Line 1 is shorter than Line 2.")



line1 = Line(1, 2, 4, 6)
line2 = Line(2, 3, 5, 7)


print("\nLine Comparison:")
line1.compare_lines(line2)

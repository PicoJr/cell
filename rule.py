RULE_LEN = 8


class Rule:

    @staticmethod
    def pattern_of_int(n):
        return format(n, 'b').zfill(3)

    def __init__(self, rule_id):
        self.id = rule_id

    def to_bin(self):
        return format(self.id, 'b').zfill(RULE_LEN)  # 'xxxxxxxx'

    def apply_to_pattern(self, pattern):
        p = int(pattern, 2)  # '100' -> 4
        return list(reversed(self.to_bin()))[p]

    def apply_to_line(self, line):
        padded_line = '0' + line + '0'
        new_line = ""
        for i, c in enumerate(line):
            pattern = padded_line[i:i + 3]  # 'xxx'
            new_line += self.apply_to_pattern(pattern)
        return new_line

    def display(self):
        for i in range(RULE_LEN):
            pattern = Rule.pattern_of_int(i)
            print("{} {}".format(pattern, self.apply_to_pattern(pattern)))

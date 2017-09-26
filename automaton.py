import re

from rule import Rule


class Automaton:
    @staticmethod
    def prettify_line(line):
        sub_0 = re.sub('0', '_', line)
        return re.sub('1', '#', sub_0)

    @staticmethod
    def seed_of_line(line):
        flag = ''
        for i in range(0, len(line), 8):
            flag += chr(int(line[i:i + 8], 2))
        return flag

    @staticmethod
    def line_of_seed(seed):
        line = ''
        for c in seed:
            line += "{:08b}".format(ord(c))
        return line

    def __init__(self, rule_id, seed):
        self.rule = Rule(rule_id)
        self.seed = seed

    def print_steps(self, steps, raw_display=False):
        line = Automaton.line_of_seed(self.seed)
        for step in range(steps):
            if raw_display:
                print("{:<3} {}".format(step, line))
            else:
                print("{:<3} {}".format(step, Automaton.prettify_line(line)))
            next_line = self.rule.apply_to_line(line)
            line = next_line

    def display(self):
        self.rule.display()

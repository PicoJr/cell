#!/usr/bin/env python3

import argparse
import logging
from automaton import Automaton


def main():
    parser = argparse.ArgumentParser(description='display 1-D cellular automaton')
    parser.add_argument('rule', type=int, help='wolframe rule (0-255)')
    parser.add_argument('steps', type=int, help='number of steps')
    parser.add_argument('seed', help='bin(seed) -> first line')
    parser.add_argument('--debug', action='store_true', help='for debug purpose')
    parser.add_argument('--raw', action='store_true', help='display with 0,1')
    args = parser.parse_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    automaton = Automaton(args.rule, args.seed)
    automaton.display()
    automaton.print_steps(args.steps, args.raw)


if __name__ == '__main__':
    main()

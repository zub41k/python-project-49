#!/usr/bin/env python3

from brain_games.logic import game_engine
from brain_games.games import gcd


def main():
    game_engine(gcd)


if __name__ == '__main__':
    main()

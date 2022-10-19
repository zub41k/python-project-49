#!/usr/bin/env python3

from brain_games.logic import greeting
from brain_games.games.even import play_round

def main():
    greeting(play_round())


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

if __name__ == "__main__":
    matches = 756
    times_batted = 1054
    times_not_out = 162
    runs_scored = 48426

    batting_average = runs_scored / (times_batted - times_not_out)

    print(f"Sir Geoffrey Boycott's Batting Average is {batting_average:.2f}.")
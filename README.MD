# One line of Wordle
## How to run
Wordle can be ran on repl.it [here](https://replit.com/@Stegg2020/1LineWordle#main.py)


Alternatively, clone the repo and run `python3 wordle.py` (Python 3.8+ required)

The files `answers.txt` and `valid.txt` are required to run.

Your terminal must support ANSI escape sequences aswell

## Features
This clone of wordle contains:
 - Dark/High Contrast mode (can be set inside wordle.py)
 - Full wordle corpus (answer + valid list)
 - Smart character matching (handles duplicates)
 - Emoji output

## File Info
This repo contains 3 python files, all of which contain the exact same code

`wordle.py` contains one line of python

`wordle_source.py` contains a better formated version of `wordle.py`

`wordle_annotated.py` contains comments that explain the process behind each bit of code

## Challenge Info
If you'd like to know the rules I set for myself, it's:
 1. All code must be on one line in one file
 2. Data can be read externally (via `open`) or hard-coded (though the first one is preferred)
 3. Semicolons, lambdas, and evals aren't allowed
 4. Only imports from Python's standard library is allowed
 5. Any version of Python 3 can be used, but latest is preferable

### List of Tricks
 - `['', print(1), print(2), ...][0]` can be used to run functions, and returns an empty string
 - `while (0 if 'i' in vars() else i:=0) + somebound > i: ...` declares both a `while` loop and `i`
 - Variables can be set inline with `:=`, lists can be set inline with `somelist.__setitem__(idx, val)`
 - In the case of `X or Y`, `Y` will never be evaluated if `X` is `True`.
 - In the case of `X and Y`, `Y` will never be evaluated if `X` is `False`
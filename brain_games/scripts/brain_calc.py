#!/usr/bin/env python3
import prompt
import random


GAME_CONFIG = {
    "win_target": 3,
    "range": [1, 10]
}


def main(config=GAME_CONFIG):
    print("Welcome to the Brain Games!")

    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")

    print("What is the result of the expression?")
    correct_answers_counter = 0
    (range_start, range_end) = config["range"]

    while correct_answers_counter != config["win_target"]:

        x = random.randint(range_start, range_end)
        y = random.randint(range_start, range_end)
        operator = random.choice(["-", "+", "*"])

        print(f"Question: {x} {operator} {y}")

        foo = {
            "-": lambda x, y: str(x - y),
            "+": lambda x, y: str(x + y),
            "*": lambda x, y: str(x * y)
        }
        result = foo[operator](x, y)
        answer = prompt.string("Your answer: ")

        if result == answer:
            print("Correct!")
            correct_answers_counter += 1
        else:
            print(
                f"{answer} is wrong answer ;(. "
                + f"Correct answer was {result}.\n"
                + f"Let's try again, {name}!"
            )
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()

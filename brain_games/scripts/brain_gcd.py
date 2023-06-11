#!/usr/bin/env python3
import random
import prompt


GAME_CONFIG = {
    "win_target": 3,
    "range": [1, 100]
}


def main(config=GAME_CONFIG):
    print("Welcome to the Brain Games!")

    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")

    print("Find the greatest common divisor of given numbers.")
    correct_answers_counter = 0
    (range_start, range_end) = config["range"]

    while correct_answers_counter != config["win_target"]:
        x = random.randint(range_start, range_end)
        y = random.randint(range_start, range_end)
        print(f"Question: {x} {y}")

        answer = prompt.string("Your answer: ")

        while y:
            x, y = y, x % y

        correct_answer = str(x)

        if answer == correct_answer:
            print("Correct!")
            correct_answers_counter += 1
        else:
            print(
                f"{answer} is wrong answer ;(. "
                + f"Correct answer was {correct_answer}.\n"
                + f"Let's try again, {name}!"
            )
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()

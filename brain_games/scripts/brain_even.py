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

    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers_counter = 0
    (range_start, range_end) = config["range"]

    while correct_answers_counter != config["win_target"]:
        number = random.randint(range_start, range_end)
        is_even = True if number % 2 == 0 else False

        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")

        if any([
            (answer == "yes" and is_even),
            (answer == "no" and not is_even),
        ]):
            print("Correct!")
            correct_answers_counter += 1
        else:
            correct_answer = "yes" if answer == "no" else "no"
            print(
                f"{answer} is wrong answer ;(. "
                + f"Correct answer was {correct_answer}.\n"
                + f"Let's try again, {name}!"
            )
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()

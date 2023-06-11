#!/usr/bin/env python3
import random
import prompt


GAME_CONFIG = {
    "win_target": 3,
    "range": [1, 100]
}


def check_if_number_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def main(config=GAME_CONFIG):
    print("Welcome to the Brain Games!")

    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")

    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    correct_answers_counter = 0
    (range_start, range_end) = config["range"]

    while correct_answers_counter != config["win_target"]:
        number = random.randint(range_start, range_end)

        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")

        is_prime = check_if_number_prime(number)

        if any([
            (answer == "yes" and is_prime),
            (answer == "no" and not is_prime),
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

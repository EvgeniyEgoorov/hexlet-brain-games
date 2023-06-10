#!/usr/bin/env python3
import random
import prompt


def main():
    print("Welcome to the Brain Games!")

    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")

    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers_counter = 0

    while correct_answers_counter != 3:
        number = random.randint(1, 100)
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
                f"{answer} is wrong answer ;(.\
                    Correct answer was {correct_answer}.\
                    \nLet's try again, {name}!"
            )
            correct_answers_counter = 0

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()

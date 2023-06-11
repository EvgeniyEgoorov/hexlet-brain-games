#!/usr/bin/env python3
import prompt
import random


def main():
    print("Welcome to the Brain Games!")

    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")

    print("What is the result of the expression?")
    correct_answers_counter = 0

    while correct_answers_counter != 3:

        x = random.randint(1, 10)
        y = random.randint(1, 10)
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

#!/usr/bin/env python3
import random
import prompt


def check_if_number_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def main():
    print("Welcome to the Brain Games!")

    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")

    print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")
    correct_answers_counter = 0

    while correct_answers_counter != 3:
        number = random.randint(1, 100)

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
                f"{answer} is wrong answer ;(." +
                f"Correct answer was {correct_answer}.\n" +
                f"nLet's try again, {name}!"
            )
            correct_answers_counter = 0

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
